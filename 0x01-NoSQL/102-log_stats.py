#!/usr/bin/env python3
"""This script gets the top 10 Nginx stats with their IPs"""
from pymongo import MongoClient
main = __import__("12-log_stats").main


def printing_top_ips(logs_collection):
    """Printing top 10 IPs"""
    print("IPs:")
    logs = logs_collection.aggregate(
        [
            {
                "$group": {"_id": "$ip", "totalRequests": {"$sum": 1}}
            },
            {
                "$sort": {"totalRequests": -1}
            },
            {
                "$limit": 10
            },
        ]
    )
    for log in logs:
        ip = log["_id"]
        ip_request_count = log["totalRequests"]
        print(f"\t{ip}: {ip_request_count}")


def run():
    """Printing Nginx stats and top IPs from log file"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    main()
    printing_top_ips(client.logs.nginx)


if __name__ == "__main__":
    run()
