---
description: The DVDAdm.BookmarkOnStop property sets or retrieves a value that tells the MSWebDVD object whether to automatically save a bookmark of the current location and settings when the user clicks the Stop button.
ms.assetid: bcadaa3c-23b7-4408-8199-058103a92a34
title: BookmarkOnStop Property
ms.topic: reference
ms.date: 05/31/2018
---

# BookmarkOnStop Property

The `DVDAdm.BookmarkOnStop` property sets or retrieves a value that tells the MSWebDVD object whether to automatically save a bookmark of the current location and settings when the user clicks the **Stop** button.

``` syntax
[ bBookmarkOnStop = ] DVD.DVDAdm.BookmarkOnStop
```

## Return Value

Returns a Boolean value indicating whether the MSDVDAdm object will save a bookmark of all DVD settings including position on disc, parental level and parental country/region.

## Remarks

This property is read/write with a default value of false.

Bookmarks are valid only for a particular machine. A user cannot save a bookmark and then send it to someone else to read on a different machine.

## See also

<dl> <dt>

[**BookmarkOnClose**](bookmarkonclose-property.md)
</dt> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



