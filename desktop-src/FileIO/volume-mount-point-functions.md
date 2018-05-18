---
Description: 'Functions used to manage mounted folders.'
ms.assetid: '2624500b-11d6-4892-97d7-22efa450f681'
title: Mounted Folder Functions
---

# Mounted Folder Functions

The mounted folder functions can be divided into three groups: general-purpose functions, functions used to scan for volumes, and functions used to scan a volume for mounted folders.

## General-Purpose Mounted Folder Functions



| Function                                                                     | Description                                                                                                                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DeleteVolumeMountPoint**](deletevolumemountpoint.md)                     | Deletes a drive letter or mounted folder.                                                                                                                   |
| [**GetVolumeNameForVolumeMountPoint**](getvolumenameforvolumemountpoint.md) | Retrieves the volume GUID path for the volume that is associated with the specified volume mount point (drive letter, volume GUID path, or mounted folder). |
| [**GetVolumePathName**](getvolumepathname.md)                               | Retrieves the mounted folder that is associated with the specified volume.                                                                                  |
| [**SetVolumeMountPoint**](setvolumemountpoint.md)                           | Associates a volume with a drive letter or a directory on another volume.                                                                                   |



 

## Volume-Scanning Functions



| Function                                   | Description                                                                                                                                    |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindFirstVolume**](findfirstvolume.md) | Returns the name of a volume on a computer. [**FindFirstVolume**](findfirstvolume.md) is used to begin enumerating the volumes of a computer. |
| [**FindNextVolume**](findnextvolume.md)   | Continues a volume search started by a call to [**FindFirstVolume**](findfirstvolume.md).                                                     |
| [**FindVolumeClose**](findvolumeclose.md) | Closes a search for volumes.                                                                                                                   |



 

## Mounted Folder Scanning Functions



| Function                                                       | Description                                                                                                                                                                               |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindFirstVolumeMountPoint**](findfirstvolumemountpoint.md) | Retrieves the name of a mounted folder on the specified volume. [**FindFirstVolumeMountPoint**](findfirstvolumemountpoint.md) is used to begin scanning the mounted folders on a volume. |
| [**FindNextVolumeMountPoint**](findnextvolumemountpoint.md)   | Continues a mounted folder search started by a call to [**FindFirstVolumeMountPoint**](findfirstvolumemountpoint.md).                                                                    |
| [**FindVolumeMountPointClose**](findvolumemountpointclose.md) | Closes a search for mounted folders.                                                                                                                                                      |



 

 

 



