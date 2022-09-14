---
description: The DVDAdm.BookmarkOnClose property sets or retrieves a value that tells the MSDVDAdm object whether to automatically save a bookmark of the current location and settings when the user closes the application.
ms.assetid: 54901ad6-7989-4fb3-bb28-f54c7a2bca44
title: BookmarkOnClose Property
ms.topic: reference
ms.date: 05/31/2018
---

# BookmarkOnClose Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.BookmarkOnClose` property sets or retrieves a value that tells the MSDVDAdm object whether to automatically save a bookmark of the current location and settings when the user closes the application.

``` syntax
[ bBookmarkOnClose = ] DVD.DVDAdm.BookmarkOnClose
```

## Return Value

Returns a Boolean value, which if true, indicates that the MSDVDAdm control will save a bookmark of all DVD settings, including position on disc, parental level, and parental country/region when the user closes the DVD player application.

## Remarks

This property is read/write with a default value of true.

## See also

<dl> <dt>

[**BookmarkOnStop**](bookmarkonstop-property.md)
</dt> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



