---
description: The FileHash method of the Installer Object takes the path to a file and returns a 128-bit hash of that file. The file hash information is returned as a Record Object. The entire 128-bit file hash is returned as four 32-bit IntegerData property fields.
ms.assetid: 065ffde1-4d7c-4e71-9315-7926d4cd38ed
title: Installer.FileHash method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.FileHash
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.FileHash method

The **FileHash** method of the [**Installer Object**](installer-object.md) takes the path to a file and returns a 128-bit hash of that file. The file hash information is returned as a [**Record Object**](record-object.md). The entire 128-bit file hash is returned as four 32-bit [**IntegerData**](record-integerdata.md) property fields.

The values returned in the [**Record Object**](record-object.md) correspond to the four fields of the [**MSIFILEHASHINFO**](/windows/desktop/api/Msi/ns-msi-msifilehashinfo) structure returned by [**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha). The numbering of four fields is 1-based in the [MsiFileHash Table](msifilehash-table.md).

-   Field 1 corresponds to the HashPart1 column.
-   Field 2 corresponds to the HashPart2 column.
-   Field 3 corresponds to the HashPart3 column.
-   Field 4 corresponds to the HashPart4 column.

## Syntax


```JScript
Installer.FileHash(
  FilePath,
  Options
)
```



## Parameters

<dl> <dt>

*FilePath* 
</dt> <dd>

Path to the file that is to be hashed.

</dd> <dt>

*Options* 
</dt> <dd>

Reserved for future use.

The value of this parameter must be 0 (zero).

</dd> </dl>

## Return value

If successful, this method returns a [**Record Object**](record-object.md) that contains the hash of the file.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[Default File Versioning](default-file-versioning.md)
</dt> <dt>

[Manage File Sizes and Versions](manage-file-sizes-and-versions.md)
</dt> <dt>

[MsiFileHash Table](msifilehash-table.md)
</dt> <dt>

[**MsiGetFileHash**](/windows/desktop/api/Msi/nf-msi-msigetfilehasha)
</dt> </dl>

 

 




