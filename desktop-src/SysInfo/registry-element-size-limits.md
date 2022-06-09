---
description: The following table identifies the size limits for the various registry elements.
ms.assetid: a6d3a884-f181-46a5-b655-226c68792e08
title: Registry Element Size Limits
ms.topic: article
ms.date: 05/31/2018
---

# Registry Element Size Limits

The following table identifies the size limits for the various registry elements.



| Registry Element | Size Limit                                                                                                                                            |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key name         | 255 characters. The key name includes the absolute path of the key in the registry, always starting at a base key, for example, HKEY\_LOCAL\_MACHINE. |
| Value name       | 16,383 characters. **Windows 2000:** 260 ANSI characters or 16,383 Unicode characters.<br/>                                                      |
| Value            | Available memory (latest format)1 MB (standard format)<br/>                                                                                     |
| Tree             | A registry tree can be 512 levels deep. You can create up to 32 levels at a time through a single registry API call.                                  |



 

Long values (more than 2,048 bytes) should be stored in a file, and the location of the file should be stored in the registry. This helps the registry perform efficiently.

The file location can be the name of a value or the data of a value. Each backslash in the location string must be preceded by another backslash as an escape character. For example, specify "C:\\\\mydir\\\\myfile" to store the string "C:\\mydir\\myfile". A file location can also be the name of a key if it is within the 255-character limit for key names and does not contain backslashes, which are not allowed in key names.

 

 




