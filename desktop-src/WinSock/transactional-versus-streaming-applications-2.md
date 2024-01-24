---
description: 'There are two fundamental types of network applications: transactional and streaming. These application types are also called interactive and batch processing application types, respectively.'
ms.assetid: 85795cdd-5a4f-4199-98bd-b5ce2299338b
title: Transactional versus Streaming Applications
ms.topic: article
ms.date: 05/31/2018
---

# Transactional versus Streaming Applications

There are two fundamental types of network applications: *transactional* and *streaming*. These application types are also called *interactive* and *batch processing* application types, respectively.

Transactional applications are stop-and-go applications. They usually perform request/reply operations, often ordered. Examples of transactional applications include synchronous remote procedure call (RPC), as well as some HTTP and Domain Name System (DNS) implementations.

Streaming applications move data. To describe streaming applications with a parallel term, streaming applications adhere to a pedal-to-the-metal data transmission philosophy, usually with little concern for data ordering. Examples of streaming applications include network backup and file transfer protocol (FTP).

Once the application type is determined, its network and protocol characteristics are determined as well.

## Related topics

<dl> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> <dt>

[Performance Dimensions](performance-dimensions-2.md)
</dt> </dl>

 

 



