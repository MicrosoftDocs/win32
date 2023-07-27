---
description: The DVDDirectory property sets or retrieves the current directory of the current DVD volume.
ms.assetid: 0dbfdf28-cda5-41b2-82ce-114d9b940d91
title: DVDDirectory Property
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVDDirectory Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDDirectory` property sets or retrieves the current directory of the current DVD volume.

``` syntax
[ sDirPath = ] MSWebDVD.DVDDirectory
```

## Return Value

Returns a string value indicating the path to the DVD root directory.

## Remarks

This property is read/write with no default value. Use this method to set the root path when there is more than one DVD drive on a system. When there is only one drive on the system and its drive letter is higher than "C", the MSWebDVD object finds it automatically. For a standard DVD-Video disc, the root path should include the ts\_video directory:


```VB
MSWebDVD.DVDDirectory = "e:\\video_ts"
```



Some DVD volumes may have their video in a directory named something other than "video\_ts." The general idea is that an additional "DVD volume" (the set of .IFO. VOB, and .BUP files that would normally be stored in the VIDEO\_TS directory) can be placed in a subdirectory on the disc. By changing the root to point to this directory, MSWebDVD will operate on this separate DVD volume. A new set of menus, titles, and so on will be available, independent of the titles in the VIDEO\_TS root, which will no longer be accessible. Such directories are called "hidden directories." The following example shows how to set a hidden directory as the root, where "hidden" is a placeholder for whatever name the disc authors have given to the directory.


```VB
MSWebDVD.DVDDirectory = "d:\\webdvd\\hidden"
```



 

 



