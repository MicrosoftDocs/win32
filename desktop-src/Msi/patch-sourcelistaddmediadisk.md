---
description: The SourceListAddMediaDisk method adds a disk to the set of registered disks. Accepts Diskid, VolumeLabel and DiskPrompt as parameters. This method calls on MsiSourceListAddMediaDisk.
ms.assetid: 6feaf2d3-7e39-4e22-9e74-9a2f98369eac
title: Patch.SourceListAddMediaDisk method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Patch.SourceListAddMediaDisk
api_type: 
- COM
api_location: 
- Msi.dll
---

# Patch.SourceListAddMediaDisk method

The **SourceListAddMediaDisk** method adds a disk to the set of registered disks. Accepts *Diskid*, *VolumeLabel* and *DiskPrompt* as parameters. This method calls on [**MsiSourceListAddMediaDisk**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddmediadiska).

## Syntax


```JScript
Patch.SourceListAddMediaDisk(
  Diskid,
  VolumeLabel,
  DiskPrompt
)
```



## Parameters

<dl> <dt>

*Diskid* 
</dt> <dd>

This parameter provides the ID of the disk being added or updated.

</dd> <dt>

*VolumeLabel* 
</dt> <dd>

This parameter provides the label of the disk being added or updated. An update, overwrites the existing volume label in the registry. To change the disk prompt only, get the existing registered volume label and provide it along with the new disk prompt. A NULL or empty string registers an empty string (0 bytes in length) as the volume label.

</dd> <dt>

*DiskPrompt* 
</dt> <dd>

This parameter provides the disk prompt of the disk being added or updated. An update overwrites the existing disk prompt in the registry. To change the volume label only, get the existing disk prompt from the registry and provide it with the new volume label. A NULL or empty string registers an empty string (0 bytes in length) as the disk prompt.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IPatch is defined as 000C10A1-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                            |



## See also

<dl> <dt>

[**Patch**](patch-object.md)
</dt> <dt>

[**MsiSourceListAddMediaDisk**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddmediadiska)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




