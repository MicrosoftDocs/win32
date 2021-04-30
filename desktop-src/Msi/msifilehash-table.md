---
description: The MsiFileHash table is used to store a 128-bit hash of a source file provided by the Windows Installer package. The hash is split into four 32-bit values and stored in separate columns of the table.
ms.assetid: 972a2784-418d-4cb3-b13c-df89b079e94c
title: MsiFileHash Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiFileHash Table

The **MsiFileHash** table is used to store a 128-bit hash of a source file provided by the Windows Installer package. The hash is split into four 32-bit values and stored in separate columns of the table.

Windows Installer can use file hashing as a means to detect and eliminate unnecessary file copying. A file hash stored in the **MsiFileHash** table may be compared to a hash of an existing file on the user's computer obtained by calling [**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha). The **MsiFileHash** table can only be used with unversioned files.

The **MsiFileHash** table has the following columns.



| Column    | Type                               | Key | Nullable |
|-----------|------------------------------------|-----|----------|
| File\_    | [Identifier](identifier.md)       | Y   | N        |
| Options   | [Integer](integer.md)             | N   | N        |
| HashPart1 | [DoubleInteger](doubleinteger.md) | N   | N        |
| HashPart2 | [DoubleInteger](doubleinteger.md) | N   | N        |
| HashPart3 | [DoubleInteger](doubleinteger.md) | N   | N        |
| Hashpart4 | [DoubleInteger](doubleinteger.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

Foreign key to [File table](file-table.md). 72 char string.

</dd> <dt>

<span id="Options"></span><span id="options"></span><span id="OPTIONS"></span>Options
</dt> <dd>

This column must be 0 and is reserved for future use.

</dd> <dt>

<span id="HashPart1"></span><span id="hashpart1"></span><span id="HASHPART1"></span>HashPart1
</dt> <dd>

First 32 bits of hash. The file hash entered in this field must be obtained by calling [**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha) or the [**FileHash method**](installer-filehash.md). Do not use other methods.

</dd> <dt>

<span id="HashPart2"></span><span id="hashpart2"></span><span id="HASHPART2"></span>HashPart2
</dt> <dd>

Second 32 bits of hash. The file hash entered in this field must be obtained by calling [**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha) or the [**FileHash method**](installer-filehash.md). Do not use other hashing methods.

</dd> <dt>

<span id="HashPart3"></span><span id="hashpart3"></span><span id="HASHPART3"></span>HashPart3
</dt> <dd>

Third 32 bits of hash. The file hash entered in this field must be obtained by calling [**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha) or the [**FileHash method**](installer-filehash.md). Do not use other methods.

</dd> <dt>

<span id="HashPart4"></span><span id="hashpart4"></span><span id="HASHPART4"></span>HashPart4
</dt> <dd>

Fourth 32 bits of hash. The file hash entered in this field must be obtained by calling [**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha) or the [**FileHash method**](installer-filehash.md). Do not use other methods.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE60](ice60.md)  
[ICE66](ice66.md)  
</dl>

## Related topics

<dl> <dt>

[**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha)
</dt> <dt>

[Default File Versioning](default-file-versioning.md)
</dt> </dl>

 

 



