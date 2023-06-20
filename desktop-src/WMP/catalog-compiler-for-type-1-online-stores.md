---
title: Catalog Compiler for Type 1 Online Stores
description: Catalog Compiler for Type 1 Online Stores
ms.assetid: 49c03d3b-3381-4663-83c8-5bc8fa70f7c3
keywords:
- Windows Media Player online stores,catalog compiler
- online stores,catalog compiler
- type 1 online stores,catalog compiler
- Windows Media Player online stores,catcomp.exe
- online stores,catcomp.exe
- type 1 online stores,catcomp.exe
- catalog compiler
- catcomp.exe
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Catalog Compiler for Type 1 Online Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The catalog compiler (catcomp.exe) is a command-line tool used by Type 1 online stores to compile the set of tab-separated-value (TSV) files containing the online store's catalog data into a compressed catalog that can be downloaded by Windows Media Player. The catalog compiler also compiles catalog update files containing only the catalog information that has changed since the last catalog update.

The compressed catalog files or catalog update files should be provided to Windows Media Player for download in the online store plug-in's implementation of [IWMPContentPartner::GetCatalogURL](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getcatalogurl).

Common Tasks

-   [Compiling a Full Catalog from TSV Files](compiling-a-full-catalog-from-tsv-files.md)
-   [Compiling a Catalog Update from Full Catalogs](compiling-a-catalog-update-from-full-catalogs.md)

Diagnostic Tasks

-   [Displaying Help](displaying-help.md)
-   [Retrieving Catalog Information](retrieving-catalog-information.md)
-   [Applying an Update To a Catalog](applying-an-update-to-a-catalog.md)

 

 




