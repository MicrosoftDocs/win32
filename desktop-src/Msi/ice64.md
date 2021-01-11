---
description: ICE64 checks that new directories in the user profile are removed correctly in roaming scenarios.
ms.assetid: d878bf4a-33c4-4c68-bd74-b7884d6680a5
title: ICE64
ms.topic: article
ms.date: 05/31/2018
---

# ICE64

ICE64 checks that new directories in the user profile are removed correctly in roaming scenarios.

Failure to fix a warning or error reported by ICE64 generally leads to problems in completely cleaning the computer during an uninstallation. When a roaming user who has installed the application logs on to a computer for the first time, all of the profile is copied down onto the computer. On advertisement (which takes place after the roaming profile download), the Installer verifies that the directory is already there and therefore does not delete it on uninstallation. This leaves the directory on the user's computer permanently.

## Result

ICE64 posts a warning or an error in a roaming situation if a new directory in the user profile that should be removed is not removed.

## Example

ICE64 reports the following error for the example shown.

``` syntax
The directory 'MyOtherFolder' is in the user profile but is not listed in the RemoveFile table.
```

The folder 'MyOtherFolder' is a custom profile folder. Because it is not listed in the RemoveFile table, it is not removed in some scenarios.

To fix this error, create a row for the folder in the RemoveFile table.

[Directory Table](directory-table.md)



| Directory     | Directory\_Parent | DefaultDir  |
|---------------|-------------------|-------------|
| AppDataFolder | TARGETDIR         |             |
| MyFolder      | AppDataFolder     | DataFolder  |
| MyOtherFolder | AppDataFolder     | DataFolder2 |



 

[RemoveFile Table](removefile-table.md)



| FileKey | Component\_ | FileName | DirProperty | InstallMode |
|---------|-------------|----------|-------------|-------------|
| Key1    | Component1  |          | MyFolder    | 2           |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



