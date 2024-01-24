---
description: If the SP\_COPY\_NEWER flag is specified during a file copy operation, the setup functions check for an existing copy of the file in the target directory.
ms.assetid: fd493b5d-7bab-4450-a749-745c536902dc
title: File Version Comparisons
ms.topic: article
ms.date: 05/31/2018
---

# File Version Comparisons

If the SP\_COPY\_NEWER flag is specified during a file copy operation, the setup functions check for an existing copy of the file in the target directory. If an existing copy is found, the functions compare the versions of the target and source file to determine which is newer.

The file version information used during version checks is that specified in the **dwFileVersionMS** and **dwFileVersionLS** members of a [**VS\_FIXEDFILEINFO**](/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo) structure, used by the version functions. If one of the files does not have version resources specified or if they have the same version information, the source file is treated as the newer file.

 

 
