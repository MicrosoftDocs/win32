---
description: At the core of any installer is the actual installation of files.
ms.assetid: e6f6d6a5-bdb0-4866-8d2c-56313d92c94c
title: File Versioning Rules
ms.topic: article
ms.date: 05/31/2018
---

# File Versioning Rules

At the core of any installer is the actual installation of files. Determining whether to install a file is a complex process. At the highest level, this determination depends on whether the component to which a file belongs is marked for installation. Once determined that a file should be copied, the process is complicated if another file with the same name exists in the target folder. In such situations, making the determination requires a set of rules involving the following properties:

-   Version
-   Date
-   Language

The installer only uses these rules when trying to install a file to a location that already contains a file with the same name. In this case, the Windows Installer uses the following rules, all other things being equal, to determine whether to install.

Highest Version Wins—All other things being equal, the file with the highest version wins, even if the file on the computer has the highest version.

Versioned Files Win—A versioned file gets installed over a nonversioned file.

Favor Product Language—If the file being installed has a different language than the file on the computer, favor the file with the language that matches the product being installed. Language-neutral files are treated as just another language so the product being installed is favored again.

Mismatched Multiple Languages—After factoring out any common languages between the file being installed and the file on the computer, any remaining languages are favored according to what is needed by the product being installed.

Preserve Superset Languages—Preserve the file that supports multiple languages regardless of whether it is already on the computer or is being installed.

Nonversioned Files are User Data—If the Modified date is later than the Create date for the file on the computer, do not install the file because user customizations would be deleted. If the Modified and Create dates are the same, install the file. If the Create date is later than the Modified date, the file is considered unmodified, install the file.

The installation of a [Companion File](companion-files.md) depends not on its own file versioning information, but on the versioning of its companion parent. In the case of Companion Files, the installation is skipped only if the parent file has a higher version. Note that a file that is the key path for its component must not be a companion file because this results in the versioning logic of the key path file being determined by the companion parent file.

Nonversioned Files Using [Companion Files](companion-files.md)-A nonversioned file that is associated with a versioned file using the companion mechanism abides by the rules for the versioned file. The only exception is if the versioned file on the computer and the versioned file being installed have the same version and language but the companion file is missing on the computer. In this case the companion file being installed is used even though the versioned file on the computer is used. Additionally, a nonversioned file using a companion file is installed if the [**REINSTALLMODE**](reinstallmode.md) property includes the overwrite older versions options ("o" or "e") and the companion file's version is equal to a file already on the machine.

Rules are Global—The rules for determining when to install a file reside in one place within the installer and are global, meaning they apply to all files equally.

For examples of the format used for file versions, see the [Version](version.md) data type. For more specific information, see [Replacing Existing Files](replacing-existing-files.md) or [Default File Versioning](default-file-versioning.md).

 

 



