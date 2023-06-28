---
title: Compiling a Full Catalog from TSV Files
description: Compiling a Full Catalog from TSV Files
ms.assetid: fba80b32-dc78-4c4a-a351-e8786f9a7131
keywords:
- Windows Media Player online stores,compiling catalogs
- online stores,compiling catalogs
- type 1 online stores,compiling catalogs
- Windows Media Player online stores,TSV files
- online stores,TSV files
- type 1 online stores,TSV files
- Windows Media Player online stores,catcomp.exe
- online stores,catcomp.exe
- type 1 online stores,catcomp.exe
- catcomp.exe
- compiling catalogs
- tab-separated-value (TSV) files
- TSV (tab-separated-value) files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Compiling a Full Catalog from TSV Files

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

New catalogs are created from a set of tab-separated-value (TSV) files. The files must be in Unicode format. Place the required TSV files listed below into a folder (the input path argument to catcomp.exe), and call catcomp.exe using the following syntax:


```C++
catcomp <input path> [version number] [locale ID] [debug]
```



If a version number is not provided, the version number will be set to 0. If no locale ID is provided, the system locale is used. If only one numeric optional argument is provided, it is assumed to be the version number. If debug is specified, the output to the screen will provide more detailed diagnostic information.

For example, the following will compile a catalog from the files in C:\\CatalogData\\210 and give the catalog a version number of 210:


```C++
catcomp C:\CatalogData\210 210
```



To display more detailed error messages, the optional debug argument can be added, as follows:


```C++
catcomp C:\CatalogData\210 210 debug
```



## Required TSV Files

Each of the following files must be present, but an empty file can be used if there is no data for a file. For instance, if your catalog contains no radio channels, radio.csv can be empty. The files must be named exactly as listed.

[track.csv](track-csv.md)

[album.csv](album-csv.md)

[artist.csv](artist-csv.md)

[genre.csv](genre-csv.md)

[subgenre.csv](subgenre-csv.md)

[list.csv](list-csv.md)

[listitem.csv](listitem-csv.md)

[radio.csv](radio-csv.md)

> [!Note]  
> Although the file names must have .csv extensions, the files are not in Comma Separated Values (CSV) format. The files must be in Tab Separated Values (TSV) format.

 

If compilation is successful, catcomp.exe creates three output files.



| File name                   | Description                                                                                                                                                                         |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| catalog.wmdb                | Uncompressed compiled catalog.                                                                                                                                                      |
| catalog.wmdb.lz             | Catalog in compressed format. Your plug-in can give the location of this file to Windows Media Player in [IWMPContentPartner::GetCatalogURL](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getcatalogurl). |
| compiled\_unique\_words.txt | An intermediate output file. Not used by Windows Media Player.                                                                                                                      |



 

 

 




