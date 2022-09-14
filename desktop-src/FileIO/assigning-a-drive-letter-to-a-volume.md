---
description: You can assign a drive letter (for example, X:\) to a local volume by using the SetVolumeMountPoint function, provided there is no volume already assigned to that drive letter.
ms.assetid: 8c78b2e8-199a-4934-a9c4-6f3913f44efe
title: Assigning a Drive Letter to a Volume
ms.topic: article
ms.date: 05/31/2018
---

# Assigning a Drive Letter to a Volume

You can assign a drive letter (for example, X:\) to a local volume by using the [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa) function, provided there is no volume already assigned to that drive letter. If the local volume already has a drive letter. then [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa) will fail. To handle this, first delete the drive letter by using the [**DeleteVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-deletevolumemountpointw) function. For example code, see [Editing Drive Letter Assignments](editing-drive-letter-assignments.md).

The system supports at most one drive letter per volume. Therefore, you cannot have C:\\ and F:\\ represent the same volume.

> [!Caution]
>
> Deleting an existing drive letter and assigning a new one may break existing paths, such as those in desktop shortcuts. It may also break the path to the program making the drive letter changes. With Windows virtual memory management, this may break the application, leaving the system in an unstable and possibly unusable state. It is the program designer's responsibility to avoid such potential catastrophes.

 

 

 



