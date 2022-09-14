---
title: Retrieving Catalog Information
description: Retrieving Catalog Information
ms.assetid: f2ec795f-6e6f-4c0c-9332-f1e96524221a
keywords:
- Windows Media Player online stores,retrieving catalog information
- online stores,retrieving catalog information
- type 1 online stores,retrieving catalog information
- Windows Media Player online stores,diagnostic information on catalogs
- online stores,diagnostic information on catalogs
- type 1 online stores,diagnostic information on catalogs
- Windows Media Player online stores,catcomp.exe
- online stores,catcomp.exe
- type 1 online stores,catcomp.exe
- catcomp.exe
- diagnostic information on catalogs
- retrieving catalog information
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Catalog Information

You can display diagnostic information on a catalog by running catcomp with the following syntax:


```C++
catcomp info <catalogpath> [track|artist|album] [ID]
```



For example, the following command displays information on an entire catalog, including the version, locale, and internal information on catalog items:


```C++
catcomp info C:\Catalog210\catalog.wmdb
```



The following displays information for the track with ID 3256:


```C++
catcomp info C:\Catalog210\catalog.wmdb track 3256
```



 

 




