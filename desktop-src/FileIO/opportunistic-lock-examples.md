---
description: Diagrams of network-traffic views for a level 1 opportunistic lock, a batch opportunistic lock, and a filter opportunistic lock.
ms.assetid: 78830113-b18e-40c7-8ec4-8896dbc58030
title: Opportunistic Lock Examples
ms.topic: article
ms.date: 05/31/2018
---

# Opportunistic Lock Examples

The following examples show data and SMB message movements as opportunistic locks are made and broken. Note that clients can cache file attribute data as well as file data.

Also note that these examples are based on situations where client applications are requesting opportunistic locks from remote servers. These processes are automatically initiated by the network redirector and the remote server—there is no direct involvement by the client application or applications. The processes described by these examples can be generalized into situations where local client applications are directly requesting opportunistic locks from the local file system, with the exception that no exchange of data over the network is involved.

## Level 1 Opportunistic Lock

The following diagram shows a network-traffic view of a level 1 opportunistic lock on a file. The arrows indicate the direction of data movement, if any.



| Event | Client X                                          | Server                                   | Client Y                                          |
|-------|---------------------------------------------------|------------------------------------------|---------------------------------------------------|
| 1     | Opens file, requests level 1 lock ==>          |                                          |                                                   |
| 2     |                                                   | <== Grants level 1 opportunistic lock |                                                   |
| 3     | Performs read, write, and other operations ==> |                                          |                                                   |
| 4     |                                                   |                                          | <== Requests to open file                      |
| 5     |                                                   | <== Breaks opportunistic lock         |                                                   |
| 6     | Discards read-ahead data                          |                                          |                                                   |
| 7     | Writes data ==>                                |                                          |                                                   |
| 8     | Sends "close" or "done" message ==>            |                                          |                                                   |
| 9     |                                                   | Okays open operation ==>              |                                                   |
| 10    | Performs read, write, and other operations ==> |                                          | <== Performs read, write, and other operations |



 

In event 1, client X opens a file and as part of the open operation requests a level 1 opportunistic lock on the file. In event 2, the server grants the level 1 lock because no other client has the file open. The client proceeds to access the file in the usual manner in event 3.

In event 4, client Y attempts to open the file and requests an opportunistic lock. The server sees that client X has the file open. The server ignores Y's request while client X flushes any write data and abandons its read cache for the file.

The server forces X to clean up by sending to X an SMB message breaking the opportunistic lock, event 5. Client X "silently" discards any read-ahead data; in other words, this process generates no network traffic. In event 7, client X writes any cached write data to the server. When client X is done writing cached data to the server, client X sends either a "close" or a "done" message to the server, event 8.

After the server has been notified that client X is done flushing its write cache to the server or has closed the file, then the server can open the file for client Y, in event 9. Because the server now has two clients with the same file open, it grants an opportunistic lock to neither. Both clients proceed to read from the file, and one or neither writes to the file.

## Batch Opportunistic Lock

The following diagram shows a network-traffic view of a batch opportunistic lock. The arrows indicate the direction of data movement, if any.



| Event | Client X                               | Server                                 | Client Y                                          |
|-------|----------------------------------------|----------------------------------------|---------------------------------------------------|
| 1     | Opens file, requests batch lock ==> |                                        |                                                   |
| 2     |                                        | <== Grants batch opportunistic lock |                                                   |
| 3     | Reads file ==>                      |                                        |                                                   |
| 4     |                                        | <== Sends data                      |                                                   |
| 5     | Closes file                            |                                        |                                                   |
| 6     | Opens file                             |                                        |                                                   |
| 7     | Searches for data                      |                                        |                                                   |
| 8     | Reads data ==>                      |                                        |                                                   |
| 9     |                                        | <== Sends data                      |                                                   |
| 10    | Closes file                            |                                        |                                                   |
| 11    |                                        |                                        | <== Opens file                                 |
| 12    |                                        | <== Breaks opportunistic lock       |                                                   |
| 13    | Closes file ==>                     |                                        |                                                   |
| 14    |                                        | Okays open operation ==>            |                                                   |
| 15    |                                        |                                        | <== Performs read, write, and other operations |



 

In the batch opportunistic lock, client X opens a file, event 1, and the server grants client X a batch lock in event 2. Client X attempts to read data, event 3, to which the server responds with data, event 4.

Event 5 shows the batch opportunistic lock at work. The application on Client X closes the file. However, the network redirector filters out the close operation and does not transmit a close message, thus performing a "silent" close. The network redirector can do this because client X has sole ownership of the file. Later on, in event 6, the application reopens the file. Again, no data flows across the network. As far as the server is concerned, this client has had the file open since event 2.

Events 7, 8, and 9 show the usual course of network traffic. In event 10, another silent close occurs.

In event 11, client Y attempts to open the file. The server's view of the file is that client X has it open, even though the application on client X has closed it. Therefore, the server sends an a message breaking the opportunistic lock to client X. Client X now sends the close message across the network, event 13. Event 14 follows as the server opens the file for client Y. The application on client X has closed the file, so it does no more transfers to or from the server for that file. Client Y begins data transfers as usual in event 15.

Between the time client X is granted the lock on the file in event 2 and the final close at event 13, any file data that the client has cached is valid, in spite of the intervening application open and close operations. However, after the opportunistic lock is broken, cached data cannot be considered valid.

## Filter Opportunistic Lock

The following diagram shows a network-traffic view of a filter opportunistic lock. The arrows indicate the direction of data movement, if any.



| Event | Client X                                | Server                   | Client Y                    |
|-------|-----------------------------------------|--------------------------|-----------------------------|
| 1     | Opens file with no access rights ==> |                          |                             |
| 2     |                                         | <== Opens the file    |                             |
| 3     | Requests filter lock==>              |                          |                             |
| 4     |                                         | <== Grants lock       |                             |
| 5     | Opens file for reading ==>           |                          |                             |
| 6     |                                         | <== Reopens the file  |                             |
| 7     | Reads data using the read handle ==> |                          |                             |
| 8     |                                         | <== Sends data        |                             |
| 9     |                                         | <== Sends data        |                             |
| 10    |                                         | <== Sends data        |                             |
| 11    |                                         |                          | <== Opens the file       |
| 12    |                                         | Opens the file ==>    |                             |
| 13    |                                         |                          | <== Requests filter lock |
| 14    |                                         | Denies filter lock==> |                             |
| 15    |                                         |                          | <== Reads data           |
| 16    |                                         | Sends data ==>        |                             |
| 17    | Reads (cached) data                     |                          |                             |
| 18    | Closes file ==>                      |                          |                             |
| 19    |                                         |                          | <== Closes file          |



 

In the filter opportunistic lock, client X opens a file, event 1, and the server responds in event 2. The client then requests a filter opportunistic lock in event 3, followed by the server granting the opportunistic lock in event 4. Client X then opens the file again for reading in event 5, to which the server responds in event 6. The client then attempts to read data, to which the server responds with data, event 8.

Event 9 shows the filter opportunistic lock at work. The server reads ahead of the client and sends the data over the network even though the client has not requested it. The client caches the data. In event 10, the server also anticipates a future request for data and sends another portion of the file for the client to cache.

In event 11 and 12, another client, Y, opens the file. Client Y also requests a filter opportunistic lock. In event 14, the server denies it. In event 15, client Y requests data, which the server sends in event 16. None of this affects client X. At any time, another client can open this file for read access. No other client affects client X's filter lock.

Event 17 shows client X reading data. However, because the server has already sent the data and the client has cached it, no traffic crosses the network.

In this example, client X never tries to read all the data in the file, so the read-ahead indicated by events 9 and 10 is "wasted"; that is, the data is never actually used. This is an acceptable loss because the read-ahead has sped up the application.

In event 18, client X closes the file. The client's network redirector abandons the cached data. The server closes the file.

 

 



