0x02. Redis Basic


Redis is an open-source, in-memory data structure store that serves as a
key-value database. It excels in performance and flexibility, making it
popular for various use cases. Some key concepts include:

In-Memory Storage: Redis stores data in RAM, enabling high-speed data access.

Key-Value Store: Data is stored as key-value pairs, where each key is unique.

Data Structures: Redis supports various data structures like strings,
hashes, lists, sets, and sorted sets, allowing for versatile data modeling.

Persistence: While Redis primarily relies on in-memory storage, it offers
persistence options to save data to disk for durability.

Atomic Operations: Redis ensures atomicity for operations, making it suitable
for scenarios requiring consistency.

Pub/Sub Messaging: Redis supports publish/subscribe messaging, enabling
real-time communication between different parts of an application.

Replication: Redis allows for data replication, providing high availability
and fault tolerance.

Partitioning: Horizontal scaling is achieved through partitioning,
distributing data across multiple Redis instances.

Lua Scripting: Redis supports Lua scripting, allowing users to execute
custom scripts on the server side.

TTL (Time-to-Live): Keys in Redis can be set with an expiration time,
providing automatic data eviction.
