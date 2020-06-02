import logging as log


def main():
    log.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=log.INFO)
    log.info("Starting etl")


if __name__ == "__main__":
    main()
