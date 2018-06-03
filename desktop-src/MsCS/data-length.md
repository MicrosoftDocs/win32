---
title: Data Length
description: The Length member of a data structure describes the actual byte size of the data stored in the value member.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ee1ddf12-26b7-474c-89c3-64dc5727a3e7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- data Failover Cluster ,structures,Length member Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Data Length

The **Length** member of a data structure describes the actual byte size of the data stored in the value member. For strings, the byte size must always include the terminating **NULL**. The byte size does not include the size of the **Syntax** member and does not include extra bytes used as padding between entries in a value list.

 

 




