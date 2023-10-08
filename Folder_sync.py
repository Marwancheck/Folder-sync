import os
import shutil
import time
import argparse




def sync_folders (source, replica, log_file, time):
    if not os.path.isdir(source):
        os.mkdir(source)


    if not os.path.isdir(replica):
        os.mkdir(replica)


    source_files = set(os.listdir(source))


    replica_files = set(os.listdir(replica))

    for file in source_files - replica_files:
        source_location = os.path.join(source, file)
        replica_location = os.path.join(replica, file)
        shutil.copy2(source_location, replica_location)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Folder Synchronization Program")
    parser.add_argument("source", help="Source folder path")
    parser.add_argument("replica", help="Replica folder path")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log", help="Log file path")
    args = parser.parse_args()

    sync_folders(args.source, args.replica, args.log_file, args.time)

