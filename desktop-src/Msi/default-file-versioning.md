---
description: The flow diagrams in the following sections illustrate the default file versioning rules used when the key file of a component being installed has the same name as a file already installed in the target location.
ms.assetid: a09e091c-ee82-4951-b129-d1d4c8948883
title: Default File Versioning
ms.topic: article
ms.date: 05/31/2018
---

# Default File Versioning

The flow diagrams in the following sections illustrate the default file versioning rules used when the key file of a component being installed has the same name as a file already installed in the target location. Default file versioning is also illustrated in [Replacing Existing Files](replacing-existing-files.md).

Note that with Windows Installer, file hashing is available to optimize the copying of files. For details, see [**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha) and the [MsiFileHash table](msifilehash-table.md). The MsiFileHash table can only be used with unversioned files.

-   [Both Files Have a Version](both-files-have-a-version.md)
-   [Neither File Has a Version](neither-file-has-a-version.md)
-   [Neither File Has a Version with File Hash Check](neither-file-has-a-version-with-file-hash-check.md)
-   [One File Has a Version](one-file-has-a-version.md)

 

 



