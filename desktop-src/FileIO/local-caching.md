---
description: Local caching of data is a technique used to speed network access to data files. It involves caching data on clients rather than on servers when possible.
ms.assetid: a7eb24b3-7e23-4798-8584-30a171fa4f04
title: Local Caching
ms.topic: article
ms.date: 05/31/2018
---

# Local Caching

*Local caching* of data is a technique used to speed network access to data files. It involves caching data on clients rather than on servers when possible.

The effect of local caching is that it allows multiple write operations on the same region of a file to be combined into one write operation across the network. Local caching reduces network traffic because the data is written once. Such caching improves the apparent response time of applications because the applications do not wait for the data to be sent across the network to the server.

Local caching of data to be read can appear to speed things up by means of reading ahead. A simple example is an application accessing data sequentially, such as a compiler's preprocessor. In such cases, the network layer of the operating system reads data across the network before the application requests the data. Ideally, the network delivers the data before the application requests it from the file system, resulting in near-instantaneous response. In practice, this rarely happens, but often reading ahead speeds applications by anticipating the next request.

Local caching can also help reduce network traffic by reading a portion of a file across the network once and then keeping it in the local cache. Subsequent read operations on that portion by the application read from the local cache.

One type of application that can benefit from local caching is batch files. Command processors read and execute a batch file one line at a time. For each line, the command processor opens the file, searches to the beginning of the line, reads as much as it needs, closes the file, then executes the line. Each line results in a lot of network traffic. Network traffic can be reduced considerably by caching the entire batch file on a client.

Local caching also helps with another problem associated with networks, especially networks that perform work over modems and other thin pipes: slow response time. Users do not want to wait while data is retrieved over the network, modified, and then written back. With reading ahead and write caching, it often appears that these functions operate much faster than they actually do.

A hazard of local caching is that written data only has as much integrity as the client itself for as long as the data is cached on the client. In general, locally cached data should be flushed to the server as soon as possible. With modern operating systems and hardware support such as uninterruptible power supplies, the risk of losing locally cached data is reduced. But the risk still exists, and you should consider both the trade-off between data integrity and apparent response speed and the trade-off between data integrity and reduced network traffic.

 

 



