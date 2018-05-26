---
title: Data Syntax
description: The Syntax member of a data structure describes the type of data stored in the value member.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d615d9fd-0498-4d45-915d-1a53e08cf8fc
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- data Failover Cluster ,structures,syntax member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Data Syntax

The **Syntax** member of a data structure describes the type of data stored in the value member. The **Syntax** member is a [**CLUSPROP\_SYNTAX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_syntax?branch=master) union that describes data in one of two ways:

-   As two WORD values with one value describing the format of the data and the other describing the data type. When **Syntax** is specified this way, the values are combined into a single **DWORD** at run time.
-   As a single **DWORD** value combining the format and type at compile time.

If there is no single **DWORD** value defined that describes the data, you must use a combination of format and type. For example, user-defined types must be described as a combination of format and type. Otherwise you can use either method of describing the data.

 

 




