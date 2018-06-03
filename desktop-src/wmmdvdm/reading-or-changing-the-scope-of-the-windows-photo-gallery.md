---
title: Reading or Changing the Scope of the Windows Photo Gallery
description: Reading or Changing the Scope of the Windows Photo Gallery
ms.assetid: 2765b44b-203c-49c5-a345-e46e2a2b8dbc
keywords:
- Windows Movie Maker,Windows Photo Gallery
- Movie Maker,Windows Photo Gallery
- Windows DVD Maker,Windows Photo Gallery
- DVD Maker,Windows Photo Gallery
- programming guide,Windows Photo Gallery
- Windows Vista,Windows Photo Gallery
- Windows Photo Gallery
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reading or Changing the Scope of the Windows Photo Gallery

Windows Photo Gallery is the feature included in Windows Vista for browsing and viewing your photos and video files. This feature works closely with Windows Movie Maker and Windows DVD Maker to provide an easy way to create a movie from selected media files in the gallery (by using the **Make a Movie** button) or to burn a DVD of selected files (by using the Burn button).

The media files that are displayed in Windows Photo Gallery are those that are contained within any of the folders that make up its "scope". The scope is published in the **GalleryScopedFolders** registry entry under the following subkey:

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\Windows Photo Gallery**

The **GalleryScopedFolders** registry entry has the form shown in the following table.



| Name                 | Type               | Data                                                                                                                                                       |
|----------------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GalleryScopedFolders | **REG\_MULTI\_SZ** | A multi-line list of folder paths, with one path on each line; for example:"C:\\Users\\Public\\Videos"<br/> "C:\\Users\\Public\\Pictures"<br/> |



 

This registry key is used primarily for informational purposes; it's the way that Windows Photo Gallery publishes its scope so that other applications can determine what is in or out of the gallery's library of photos and video files without having to start Windows Photo Gallery.

An example of how this registry key is read and acted upon can be seen in the picture viewer that is built into the Windows Vista shell. If you open an image that is within the scope of the gallery, you see a **Go To Gallery** button in the upper-left corner of the viewer. If you open an image that is not within the scope of the gallery, the button in the upper-left corner is named **Add Folder To Gallery**.

Whenever the scope is written to, typically when a new folder is added to the gallery, the **GalleryScopedFolders** registry entry is updated immediately.

The Windows Photo Gallery has additional registry entries that affect the way that its library of visual media files is sorted, grouped, and displayed under the following registry key:

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\Windows Photo Gallery\\Library**

## Related topics

<dl> <dt>

[**Getting Information from Windows Vista About Windows Movie Maker and Windows DVD Maker**](getting-information-from-windows-vista-about-windows-movie-maker-and-windows-dvd-maker.md)
</dt> </dl>

 

 





