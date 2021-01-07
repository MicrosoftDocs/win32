---
description: To make a complete list of the volumes on a computer, or to manipulate each volume in turn, you can enumerate volumes.
ms.assetid: 5adcd59a-48b7-4373-a10b-c352962f715a
title: Enumerating Volumes
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Volumes

To make a complete list of the volumes on a computer, or to manipulate each volume in turn, you can enumerate volumes. Within a volume, you can [scan for mounted folders](enumerating-volume-mount-points.md) or other objects on the volume.

Three functions allow an application to enumerate volumes on a computer:

-   [**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew)
-   [**FindNextVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findnextvolumew)
-   [**FindVolumeClose**](/windows/desktop/api/FileAPI/nf-fileapi-findvolumeclose)

These three functions operate in a manner very similar to the [**FindFirstFile**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfilea), [**FindNextFile**](/windows/desktop/api/FileAPI/nf-fileapi-findnextfilea), and [**FindClose**](/windows/desktop/api/FileAPI/nf-fileapi-findclose) functions.

Begin a search for volumes with [**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew). If the search is successful, process the results according to the design of your application. Then use [**FindNextVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findnextvolumew) in a loop to locate and process each subsequent volume. When the supply of volumes is exhausted, close the search with [**FindVolumeClose**](/windows/desktop/api/FileAPI/nf-fileapi-findvolumeclose).

You should not assume any correlation between the order of the volumes that are returned by these functions and the order of the volumes that are returned by other functions or tools. In particular, do not assume any correlation between volume order and drive letters as assigned by the BIOS (if any) or the Disk Administrator.

See [Mounted Folder Examples](volume-mount-point-examples.md) for an example of how to enumerate the volumes on a computer.

 

 



