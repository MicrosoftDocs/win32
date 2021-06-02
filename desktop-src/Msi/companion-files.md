---
description: The installation state of a companion file depends not on its own file versioning information, but on the versioning of its companion parent.
ms.assetid: 3c1e3507-8ed9-4ce8-8d38-6c8248a9e883
title: Companion Files
ms.topic: article
ms.date: 05/31/2018
---

# Companion Files

The installation state of a companion file depends not on its own file versioning information, but on the versioning of its companion parent. See the [File Versioning Rules](file-versioning-rules.md). To specify a companion file, the primary key of the companion parent in the [File table](file-table.md) must be authored into the Version column of the record for the companion.

In the following example, FileA is the companion parent and FileB is the companion file.

[File Table](file-table.md) (partial)



| File  | Version |
|-------|---------|
| FileA | 1.0.0.0 |
| FileB | FileA   |



 

In this example, the installation state of FileB depends on the [File Versioning Rules](file-versioning-rules.md) and the versioning information for FileA. If the installer determines that the version of FileA in the package should be installed over an older version of FileA that already exists on the user's computer, it will also install FileB from the package regardless of the version of any installed FileB.

Note that a file that is the key path for its component must not be a companion file. This would result in the versioning logic of the key path file being determined by the companion parent file.

 

 



