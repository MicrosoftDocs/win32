---
description: The Cabinet data type must be used in the Cabinet column of the Media table.
ms.assetid: 149c74ea-4342-45dd-8da4-4dfa7f4317a0
title: Cabinet
ms.topic: article
ms.date: 05/31/2018
---

# Cabinet

The Cabinet data type must be used in the Cabinet column of the [Media table](media-table.md).

If the cabinet name is preceded by the number sign, the cabinet is stored as a data stream inside the package. The character string which follows the \# is an [Identifier](identifier.md) for this data stream. Note that if the cabinet is stored as a data stream, the name of a cabinet is case-sensitive.

If the cabinet name is not preceded by the number sign \#, the cabinet is stored in a separate file located at the root of the source tree specified by the [Directory Table](directory-table.md). The cabinet file must use the short file name syntax consisting of an eight character name, a period, and a three character extension. The Cabinet data type cannot use the short\|longname syntax for file names. If the cabinet file is stored as a separate file, the name of the cabinet file is not case-sensitive.

To conserve disk space, the installer removes any cabinets embedded in the .msi file before caching the installation package on the user's computer.

See [Including a Cabinet File in an Installation](including-a-cabinet-file-in-an-installation.md).

 

 



