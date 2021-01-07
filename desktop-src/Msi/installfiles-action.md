---
description: The InstallFiles action copies files specified in the File table from the source directory to the destination directory.
ms.assetid: 187ad82f-13f5-4ea3-913c-2ae7561a6ee6
title: InstallFiles Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallFiles Action

The InstallFiles action copies files specified in the File table from the source directory to the destination directory.

## Sequence Restrictions

The InstallFiles action must come after the [InstallValidate](installvalidate-action.md) action and before any file-dependent actions.

## ActionData Messages



| Field | Description of action data                      |
|-------|-------------------------------------------------|
| \[1\] | Identifier of installed file.                   |
| \[6\] | Size of installed file in bytes.                |
| \[9\] | Identifier of directory holding installed file. |



 

## Remarks

The InstallFiles action operates on files specified in the [File table](file-table.md). Each file is installed based on the installation state of the file's associated component in the [Component table](component-table.md). Only those files whose components are resolved to the **msiInstallStatelocal** state are eligible for copying.

The InstallFiles action implements the following columns of the File table.

-   The FileName column specifies the target file name.
-   The Version column specifies the file version.
-   The Attributes column specifies the file and installation attribute flag bits.
-   The File column specifies the unique file token.
-   The FileSize column specifies the uncompressed file size in bytes.
-   The Language column specifies the file language identifier.
-   The Sequence column specifies the sequence number on media.

The InstallFiles action implements the following columns of the Component table.

-   The Directory\_ column specifies a reference to a [Directory table](directory-table.md) item.
-   The Component column specifies a unique name for the component item.

The specified file is copied only if one of the following is true:

-   The file is not currently installed on the local computer.
-   The file is on the local computer but has a lower version number than the file in the [File table](file-table.md).
-   The file is on the local computer, but there is no associated version number.

The source directory for each file to be copied is determined by the sourceMode, which in turn depends on the value in the Cabinet column of the Media table. For a full discussion of the source mode, see the [Media table](media-table.md).

If the source directory for a file to be copied resides on removable media such as a floppy disk or CD-ROM, the InstallFiles action verifies that the proper source media is inserted before attempting to copy the file. The InstallFiles searches for media of the same removable type with a [*volume*](v-gly.md) label that matches the value given in the VolumeLabel column of the Media table. If a matching mounted volume is found, the file copying process proceeds. If no match is found, a dialog box requests that the user to insert the proper media. In this case, the dialog box uses the media name found in the DiskPrompt column of the Media table as part of the prompt.

Caution must be exercised because the InstallFiles action can delete an original file and not replace it. This occurs when the InstallFiles action experiences an error while replacing an older file and the user chooses to ignore the error. The default behavior of installer is to delete an old file before ensuring the new file is copied correctly.

For the file versioning rules used by the installer, see [File Versioning Rules](file-versioning-rules.md).

 

 



