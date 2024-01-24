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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Retrieving Catalog Information

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



 

 




