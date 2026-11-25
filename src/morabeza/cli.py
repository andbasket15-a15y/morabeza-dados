"""Linha de comandos do projeto Morabeza (Sessão 3).

Uso:  python -m morabeza.cli --ilha Sal
"""
import argparse
import logging
import sys

from morabeza.apoio import faturacao_por_ilha, ler_vendas, total_venda
from morabeza.config import carregar_config

logger = logging.getLogger(__name__)


def criar_parser() -> argparse.ArgumentParser:
    # TODO 5: cria um argparse.ArgumentParser com dois argumentos opcionais:
    #         --config (por defeito "config.yaml") e --ilha (sem valor por defeito).
    parser = argparse.ArgumentParser(description="Resumo de vendas da Morabeza.")
    parser.add_argument("--config", default="config.yaml", help="Ficheiro de configuração YAML.")
    parser.add_argument("--ilha", help="Mostrar só a faturação desta ilha.")
    return parser


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    args = criar_parser().parse_args(argv)
    # TODO 6: carrega a configuração (args.config) e lê as vendas do ficheiro indicado nela.
    config = carregar_config(args.config)
    vendas = ler_vendas(config["ficheiro_vendas"])
    # TODO 7: regista no log: logger.info("Li %d vendas de %s", ...). Não uses print para isto.
    logger.info("Li %d vendas de %s", len(vendas), config["ficheiro_vendas"])
    # TODO 8: calcula a faturação por ilha. Sem --ilha, imprime "Faturação total: <valor> <moeda>".
    #         Com --ilha, imprime "Faturação em <ilha>: <valor> <moeda>".
    #         Se a ilha não existir, logger.error(...) e devolve 1. No fim, devolve 0.
    por_ilhas = faturacao_por_ilha(vendas)
    moeda = config["moeda"]
    if args.ilha in None:
        print(f"Faturação total: {sum(por_ilhas.values())} {moeda}")
        return 0
    else:
        logger.error("Ilha desconhecida: %s", args.ilha)
        print(f"Faturação em {args.ilha}: {por_ilhas[args.ilha]} {moeda}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
