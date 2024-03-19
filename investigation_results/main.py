from util.init_vertica import init_vertica
from util.init_clickhouse import init_clickhouse
from util.create_data import generate_random_data
from writer.vertica_writer import write_to_vertica
from writer.clickhouse_writer import write_to_ch
from reader.clickhouser_reader import read_from_ch
from reader.vertica_reader import read_from_vertica


def main():
    init_vertica()
    init_clickhouse()

    batch_sizes = [100, 500, 1000, 3000]

    for batch_size in batch_sizes:
        data_batch = generate_random_data(batch_size)
        # write
        write_to_ch(data_batch)
        write_to_vertica(data_batch)
        # read
        read_from_ch(batch_size)
        read_from_vertica(batch_size)


if __name__ == "__main__":
    main()
