---
description: "Learn more about: Extensible Storage Engine"
title: Extensible Storage Engine
TOCTitle: Extensible Storage Engine
ms:assetid: 5c485eff-4329-4dc1-aa45-fb66e6554792
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269259(v=EXCHG.10)
ms:contentKeyID: 32765561
ms.date: 04/11/2016
ms.topic: article
---

# Extensible Storage Engine


_**Applies to:** Windows | Windows Server_

## Extensible Storage Engine

The Extensible Storage Engine (ESE) is an advanced indexed and sequential access method (ISAM) storage technology. ESE enables applications to store and retrieve data from tables using indexed or sequential cursor navigation. It supports denormalized schemas including wide tables with numerous sparse columns, multi-valued columns, and sparse and rich indexes. It enables applications to enjoy a consistent data state using transacted data update and retrieval. A crash recovery mechanism is provided so that data consistency is maintained even in the event of a system crash. It provides ACID (Atomic Consistent Isolated Durable) transactions over data and schema by way of a write-ahead log and a snapshot isolation model. Transactions in ESE are highly concurrent, making ESE useful for server applications. It caches data to maximize high performance access to data. In addition, it is lightweight, making it useful for applications that serve in auxiliary roles.

ESE is for use in applications that require fast and/or light structured data storage, where raw file access or the registry does not support the application's indexing or data size requirements.

It is used by applications that never store more than 1 megabyte of data, and has been used in applications with databases in extreme cases in excess of 1 terabyte, and commonly over 50 gigabytes.

This documentation is intended for developers who are familiar with C and C++, and basic database concepts such as tables, columns, indexes, recovery, and transactions. The only access method for ESE is the C API that is described in this documentation.

The Extensible Storage Engine is a Windows component that was introduced in Windows 2000. Not all features or APIs are available in all versions of the Windows operating systems.

ESE provides a user-mode storage engine that manages data inside of flat, binary files that are accessible through the Windows APIs. ESE is accessed through a DLL that is loaded directly into the application's process; no remote access methods are required of or provided by the database engine itself. Though ESE has no remote or inter-process access method, the data files it uses can be provided remotely by using server message block (SMB) through the Windows APIs, but this is not recommended.

**Note**  Windows XP 64-Bit Edition is the same as Windows Server 2003 for the purpose of determining the ESE feature set that is supported.

### Notes

ESE was formerly known as Joint Engine Technology (JET) Blue, and so frequently the term "JET Blue" or "JET" is used interchangeably with the term ESE outside this documentation. However, there are in fact two completely separate implementations of the JET API, called JET Blue and JET Red. The term "JET" is frequently also used to refer to JET Red, which is the database engine that is used with Microsoft Office Access. The two JET implementations are completely different, are separately maintained, have a vastly different feature set, and are not interchangeable. Within the ESE documentation, "JET" refers to the ESE or the JET API as ESE implements it. Any references to the JET Red will always explicitly be labeled "JET Red".

### In This Section

[Extensible Storage Engine Reference](./extensible-storage-engine-reference.md)
