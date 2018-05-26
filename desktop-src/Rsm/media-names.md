---
Description: When new physical media are placed into a library, Removable Storage Manager assigns an initial display name to the media that an administrator can use to visually identify the media.
ms.assetid: 2ccc60e1-88e6-496d-8627-4301d6957d50
title: Media Names
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Media Names

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

When new physical media are placed into a library, Removable Storage Manager assigns an initial display name to the media that an administrator can use to visually identify the media. This name is derived from several sources, including the on-media label and the bar code. The rules include the following:

1.  If the media has a bar code label, its alphanumeric value is used as the display name.
2.  If the media is single-sided and has a recognized label type on its single side, the name is taken from the label. If the format is MTF, the label is taken from information in the MTF header. If the format is a file system, the name is taken from the volume name.
3.  The sequence number is used.

 

 



