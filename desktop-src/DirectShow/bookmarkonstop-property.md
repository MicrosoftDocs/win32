---
description: The DVDAdm.BookmarkOnStop property sets or retrieves a value that tells the MSWebDVD object whether to automatically save a bookmark of the current location and settings when the user clicks the Stop button.
ms.assetid: bcadaa3c-23b7-4408-8199-058103a92a34
title: BookmarkOnStop Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BookmarkOnStop Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 



