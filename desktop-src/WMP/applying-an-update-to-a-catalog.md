---
title: Applying an Update To a Catalog
description: Applying an Update To a Catalog
ms.assetid: 4aedb0d6-36c7-425c-b6d3-e16161cf6828
keywords:
- Windows Media Player online stores,applying updates to catalogs
- online stores,applying updates to catalogs
- type 1 online stores,applying updates to catalogs
- Windows Media Player online stores,updating catalogs
- online stores,updating catalogs
- type 1 online stores,updating catalogs
- Windows Media Player online stores,catalog updates
- online stores,catalog updates
- type 1 online stores,catalog updates
- catalog updates
- updating catalogs
- applying updates to catalogs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Applying an Update To a Catalog

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This is not normally done except for diagnostic purposes—for instance, to help verify that a difference file is valid. The catalog generated in this way is not in compressed form and should not be passed to Windows Media Player.

 

A new catalog file can be created by using the syntax below, where *inputcatalog* is the location of the original catalog, and *inputdiff* is the location of the difference file to apply. The catalog files must be in uncompressed form.


```C++
catcomp applydiff <inputcatalog> <inputdiff>
```



For example, the following creates a new catalog from C:\\Catalog210\\catalog.wmdb and C:\\Catalog210\\catalog.diff.


```C++
catcomp applydiff C:\Catalog210\catalog.wmdb C:\Catalog210\catalog.diff
```



If compilation is successful, catcomp.exe creates the follow output files.



| File name        | Description       |
|------------------|-------------------|
| catalog.wmdb.new | New catalog file. |



 

 

 




