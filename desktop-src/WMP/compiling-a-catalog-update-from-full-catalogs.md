---
title: Compiling a Catalog Update from Full Catalogs
description: Compiling a Catalog Update from Full Catalogs
ms.assetid: 046c0a01-0ad7-41b6-bad5-dcab953a3980
keywords:
- Windows Media Player online stores,compiling catalogs
- online stores,compiling catalogs
- type 1 online stores,compiling catalogs
- Windows Media Player online stores,catalog updates
- online stores,catalog updates
- type 1 online stores,catalog updates
- Windows Media Player online stores,full catalogs
- online stores,full catalogs
- type 1 online stores,full catalogs
- compiling catalogs
- catalog updates
- full catalogs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Compiling a Catalog Update from Full Catalogs

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A catalog update containing the changes between two versions of a compiled catalog can be created by using the syntax below, where *path1* is the directory containing the first catalog, *path2* is the directory containing the second catalog, and debug can be optionally included to display detailed error information on the screen. The catalog files must be in uncompressed form—the file name of the compiled catalog would be catalog.wmdb, rather than catalog.wmdb.lz.


```C++
catcomp diff <path1> <path2> [debug]
```



For example, if the C:\\Catalog210\\ directory contains version 210 of a full compiled catalog and C:\\Catalog211\\ contains version 211, the following command creates a difference file that contains the changes between the two versions:


```C++
catcomp diff C:\Catalog210\ C:\Catalog211\
```



To display detailed error information, you can add the optional debug parameter as follows:


```C++
catcomp diff C:\Catalog210\ C:\Catalog211\ debug
```



If compilation is successful, catcomp.exe creates the output files listed below and saves them in the directory that contains the first catalog.



| File name             | Description                                                                                                                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| catalog.diff          | Uncompressed compiled difference file.                                                                                                                                                           |
| catalog.diff.lz       | Compressed version of catalog update file. Your plug-in can give the location of this file to Windows Media Player in [IWMPContentPartner::GetCatalogURL](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getcatalogurl). |
| catalog.wmdb.delta    | Intermediate output file. Not used by Windows Media Player                                                                                                                                       |
| catalog.wmdb.modified | Intermediate output file. Not used by Windows Media Player                                                                                                                                       |



 

 

 




