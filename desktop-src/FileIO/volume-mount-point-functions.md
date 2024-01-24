---
description: Functions used to manage mounted folders.
ms.assetid: 2624500b-11d6-4892-97d7-22efa450f681
title: Mounted Folder Functions
ms.topic: article
ms.date: 05/31/2018
---

# Mounted Folder Functions

The mounted folder functions can be divided into three groups: general-purpose functions, functions used to scan for volumes, and functions used to scan a volume for mounted folders.

## General-Purpose Mounted Folder Functions



| Function                                                                     | Description                                                                                                                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DeleteVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-deletevolumemountpointw)                     | Deletes a drive letter or mounted folder.                                                                                                                   |
| [**GetVolumeNameForVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw) | Retrieves the volume GUID path for the volume that is associated with the specified volume mount point (drive letter, volume GUID path, or mounted folder). |
| [**GetVolumePathName**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumepathnamew)                               | Retrieves the mounted folder that is associated with the specified volume.                                                                                  |
| [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa)                           | Associates a volume with a drive letter or a directory on another volume.                                                                                   |



 

## Volume-Scanning Functions



| Function                                   | Description                                                                                                                                    |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew) | Returns the name of a volume on a computer. [**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew) is used to begin enumerating the volumes of a computer. |
| [**FindNextVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findnextvolumew)   | Continues a volume search started by a call to [**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew).                                                     |
| [**FindVolumeClose**](/windows/desktop/api/FileAPI/nf-fileapi-findvolumeclose) | Closes a search for volumes.                                                                                                                   |



 

## Mounted Folder Scanning Functions



| Function                                                       | Description                                                                                                                                                                               |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindFirstVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findfirstvolumemountpointa) | Retrieves the name of a mounted folder on the specified volume. [**FindFirstVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findfirstvolumemountpointa) is used to begin scanning the mounted folders on a volume. |
| [**FindNextVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findnextvolumemountpointa)   | Continues a mounted folder search started by a call to [**FindFirstVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findfirstvolumemountpointa).                                                                    |
| [**FindVolumeMountPointClose**](/windows/desktop/api/WinBase/nf-winbase-findvolumemountpointclose) | Closes a search for mounted folders.                                                                                                                                                      |



 

 

 



