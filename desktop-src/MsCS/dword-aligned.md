---
title: DWORD-aligned
description: Each data structure in a value list must begin on a DWORD boundary. This means that the distance (in bytes) between the start of the value list buffer and the start of any data structure is always an even multiple of sizeof(DWORD).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '515640ca-44e5-46ef-9f90-74a086344c2f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DWORD alignment of values lists Failover Cluster", "value lists Failover Cluster ,DWORD alignment", "data Failover Cluster ,value lists,DWORD alignment"]
---

# DWORD-aligned

Each [data structure](data-structures.md) in a [value list](value-lists.md) must begin on a **DWORD** boundary. This means that the distance (in bytes) between the start of the value list buffer and the start of any data structure is always an even multiple of `sizeof(DWORD)`.

If a data structure contains variable length data, you might have to advance a few extra bytes before adding the next data structure in order to ensure **DWORD**-alignment (see the diagram in [Value Lists](value-lists.md)). Use the [**ALIGN\_CLUSPROP**](align-clusprop.md) macro to calculate the correct alignment size.

The extra bytes lying between data structures in a value list are referred to as "padding."

Note that the **Length** member of the data structure should specify the actual size of the data, not the size returned by [**ALIGN\_CLUSPROP**](align-clusprop.md). For more information and examples of using **ALIGN\_CLUSPROP**, see [Using Lists and Tables](using-lists-and-tables.md).

 

 




