---
description: A label is a user-friendly name that is assigned to a volume, usually by an end user, to make it easier to recognize. A volume can have a label, a drive letter, both, or neither. To set the label for a volume, use the SetVolumeLabel function.
ms.assetid: f640f42d-a703-4e2e-a6d3-09cbe989cd11
title: Naming a Volume
ms.topic: article
ms.date: 05/31/2018
---

# Naming a Volume

A label is a user-friendly name that is assigned to a volume, usually by an end user, to make it easier to recognize. A volume can have a label, a drive letter, both, or neither. To set the label for a volume, use the [**SetVolumeLabel**](/windows/desktop/api/WinBase/nf-winbase-setvolumelabela) function.

Several factors can make it difficult to identify specific volumes using only drive letters and labels. One is that a volume is not required to have a drive letter or a label. Another is that two different volumes can have the same label, which makes them indistinguishable except by drive letter. A third factor is that drive letter assignments can change as volumes are added to and removed from the computer.

To solve this problem, the operating system uses *volume GUID paths* to identify volumes. These are strings of this form:

"\\\\?\\Volume{*GUID*}\\"

where *GUID* is a globally unique identifier (GUID) that identifies the volume.

A volume GUID path is sometimes referred to as a *unique volume name*, because a volume GUID path can refer only to one volume. However, this term is misleading, because a volume can have more than one volume GUID path.

The "\\\\?\\" prefix disables path parsing and is not considered to be part of the path. For more information about the "\\\\?\\" prefix, see [Naming a File or Directory](naming-a-file.md).

You must specify full paths when using volume GUID paths with the "\\\\?\\" prefix.

A *mounted folder* is an association between a folder on one volume and another volume, so that the folder path can be used to access the volume. For example, if you use the [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa) function to create a mounted folder that associates the volume "D:\\" with the folder "C:\\MountD\\", you can then use either path ("D:\\" or "C:\\MountD\\") to access the volume "D:\\".

A *volume mount point* is any user-mode path that can be used to access a volume. There are three types of volume mount points:

-   A drive letter, for example, "C:\\".
-   A volume GUID path, for example, "\\\\?\\Volume{26a21bda-a627-11d7-9931-806e6f6e6963}\\".
-   A mounted folder, for example, "C:\\MountD\\".

All volume and mounted folder functions that take a volume GUID path as an input parameter require the trailing backslash. All volume and mounted folder functions that return a volume GUID path provide the trailing backslash, but this is not the case with the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function. You can open a volume by calling **CreateFile** and omit the trailing backslash from the volume name you specify. **CreateFile** processes a volume GUID path with an appended backslash as the root directory of the volume.

The operating system assigns a volume GUID path to a volume when the volume is first installed and when the volume is formatted. The volume and mounted folder functions use volume GUID paths to access volumes. To obtain the volume GUID path for a volume, use the [**GetVolumeNameForVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw) function.

Path lengths may be a concern when a mounted folder is created that associates a volume that has a deep directory tree with a directory on another volume. This is because the path of the volume is concatenated to the path of the directory. The globally defined constant **MAX\_PATH** defines the maximum number of characters a path can have. (For more information about **MAX\_PATH**, see [Naming a File or Directory](naming-a-file.md).) You can avoid this constraint by doing either of the following:

-   Refer to volumes by their volume GUID paths.
-   Use the Unicode (W) versions of file functions, which support the \\\\?\\ prefix.

 

 



