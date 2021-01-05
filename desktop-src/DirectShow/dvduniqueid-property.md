---
description: The DVDUniqueID property retrieves a system-generated number that uniquely identifies the current disc.
ms.assetid: 8ea6dd4d-6998-4212-8874-9c6cd93a1db3
title: DVDUniqueID Property
ms.topic: reference
ms.date: 05/31/2018
---

# DVDUniqueID Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDUniqueID` property retrieves a system-generated number that uniquely identifies the current disc.

``` syntax
[ iDiscID = ] MSWebDVD.DVDUniqueID
```

## Return Value

Returns an integer value that uniquely identifies the current disc.

## Remarks

This property is read-only with no default value. The identifier (ID) number is not absolutely unique, but it is unique for all practical purposes. The ID applies to all replicated copies of a disc. In other words, all copies of a specific movie have the same ID. The ID is based on file sizes, dates, and other information, and not the BCA value.

 

 



