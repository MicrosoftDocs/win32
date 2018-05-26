---
title: Parameter Blocks
description: A parameter block is a user-defined structure that stores the data, or pointers to the data, for one or more property values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fd77397b-36dd-4a20-b3f4-7dbbee1fd787
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- parameter blocks Failover Cluster
- data Failover Cluster ,parameter blocks
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Parameter Blocks

A parameter block is a user-defined structure that stores the data, or pointers to the data, for one or more property values. Property tables use parameter blocks for data storage. Each [property table](property-tables.md) entry specifies an offset to a member of a parameter block.

Because property tables use offsets to access parameter block data, there are no design constraints on parameter blocks. They can list their members in any order and can include any data, not just property data as members.

For a code example, see [Using Parameter Blocks](using-parameter-blocks.md).

 

 




