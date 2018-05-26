---
Description: Functions used to manage mounted folders.
ms.assetid: 2624500b-11d6-4892-97d7-22efa450f681
title: Mounted Folder Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Mounted Folder Functions

The mounted folder functions can be divided into three groups: general-purpose functions, functions used to scan for volumes, and functions used to scan a volume for mounted folders.

## General-Purpose Mounted Folder Functions



| Function                                                                     | Description                                                                                                                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DeleteVolumeMountPoint**](/windows/win32/FileAPI/nf-fileapi-deletevolumemountpointw?branch=master)                     | Deletes a drive letter or mounted folder.                                                                                                                   |
| [**GetVolumeNameForVolumeMountPoint**](/windows/win32/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw?branch=master) | Retrieves the volume GUID path for the volume that is associated with the specified volume mount point (drive letter, volume GUID path, or mounted folder). |
| [**GetVolumePathName**](/windows/win32/FileAPI/nf-fileapi-getvolumepathnamew?branch=master)                               | Retrieves the mounted folder that is associated with the specified volume.                                                                                  |
| [**SetVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-setvolumemountpointa?branch=master)                           | Associates a volume with a drive letter or a directory on another volume.                                                                                   |



 

## Volume-Scanning Functions



| Function                                   | Description                                                                                                                                    |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindFirstVolume**](/windows/win32/FileAPI/nf-fileapi-findfirstvolumew?branch=master) | Returns the name of a volume on a computer. [**FindFirstVolume**](/windows/win32/FileAPI/nf-fileapi-findfirstvolumew?branch=master) is used to begin enumerating the volumes of a computer. |
| [**FindNextVolume**](/windows/win32/FileAPI/nf-fileapi-findnextvolumew?branch=master)   | Continues a volume search started by a call to [**FindFirstVolume**](/windows/win32/FileAPI/nf-fileapi-findfirstvolumew?branch=master).                                                     |
| [**FindVolumeClose**](/windows/win32/FileAPI/nf-fileapi-findvolumeclose?branch=master) | Closes a search for volumes.                                                                                                                   |



 

## Mounted Folder Scanning Functions



| Function                                                       | Description                                                                                                                                                                               |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindFirstVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findfirstvolumemountpointa?branch=master) | Retrieves the name of a mounted folder on the specified volume. [**FindFirstVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findfirstvolumemountpointa?branch=master) is used to begin scanning the mounted folders on a volume. |
| [**FindNextVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findnextvolumemountpointa?branch=master)   | Continues a mounted folder search started by a call to [**FindFirstVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findfirstvolumemountpointa?branch=master).                                                                    |
| [**FindVolumeMountPointClose**](/windows/win32/WinBase/nf-winbase-findvolumemountpointclose?branch=master) | Closes a search for mounted folders.                                                                                                                                                      |



 

 

 



