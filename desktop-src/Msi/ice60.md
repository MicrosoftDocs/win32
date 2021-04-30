---
description: ICE60 validates the File table of a Windows Installer database.
ms.assetid: 95d9b8b4-0b65-451a-8629-f0b276d6e35d
title: ICE60
ms.topic: article
ms.date: 05/31/2018
---

# ICE60

ICE60 checks that files in the [File table](file-table.md) meet the following condition:

-   If the file is not a font and has a version, then it must have a language.
-   ICE60 checks that no versioned files are listed in the [MsiFileHash table](msifilehash-table.md).

Failure to fix a warning reported by ICE60 generally leads to a file being needlessly reinstalled when a product repair is done. This happens because the file to be installed in the repair and the existing file on disk have the same version (they are the same file) but different languages. The file table lists the language as null, but the file itself has a language value in the resource. Based on the [file versioning rules](file-versioning-rules.md), the installer favors the file to be installed, so it is recopied needlessly.

## Result

ICE60 posts a warning or an error if a file in the [File table](file-table.md) that is not a font and has a version, does not have a language.

ICE60 posts the following error if a file listed in the MsiFileHash table is versioned.

``` syntax
ERROR: "The file [1] is Versioned. It cannot be hashed"
```

## Example

ICE60 reports the following error and warning for the example shown. (File B is a font; the other files are not.)

``` syntax
WARNING: The file FileE is not a Font, and its version is not a companion file reference. It should have a language specified in the Language column.
```

FileA has both a version and a language; therefore no warning or error is generated.

FileB has a version but no language. No warning or error is generated, however, because it is a font.

FileC is a companion reference, so it does not have to have a language. No warning or error is generated.

FileD has no version, so it does not need to have a language. No warning or error is generated.

FileE has a version but no language. Therefore a warning is generated.

To fix this warning, add a language to FileE.

Files should have language values stored in the version resource whenever possible. If a file is language neutral, use the [LANGID](column-data-types.md) 0.

[File Table](file-table.md) (FileB is a font; the other files are not.)



| File  | Version | Language |
|-------|---------|----------|
| FileA | 1.0     | 1033     |
| FileB | 1.0     |          |
| FileC | FileA   |          |
| FileD |         |          |
| FileE | 1.0     |          |



 

[Font Table](font-table.md)



| File  | FontTitle  |
|-------|------------|
| FileB | Font Title |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



