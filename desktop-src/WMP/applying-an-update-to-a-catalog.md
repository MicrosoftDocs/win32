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
ms.date: 05/31/2018
---

# Applying an Update To a Catalog

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



 

 

 




