---
Description: The SourceListAddMediaDisk method adds a disk to the set of registered disks. Accepts Diskid, VolumeLabel and DiskPrompt as parameters. This method calls on MsiSourceListAddMediaDisk.
ms.assetid: 19cb6884-2191-4da3-a6d2-8874564be67d
title: Product.SourceListAddMediaDisk method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Product.SourceListAddMediaDisk method

The **SourceListAddMediaDisk** method adds a disk to the set of registered disks. Accepts *Diskid*, *VolumeLabel* and *DiskPrompt* as parameters. This method calls on [**MsiSourceListAddMediaDisk**](/windows/win32/Msi/nf-msi-msisourcelistaddmediadiska?branch=master).

## Syntax


```JScript
Product.SourceListAddMediaDisk(
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

This parameter provides the label of the disk being added or updated. An update overwrites the existing volume label in the registry. To change the disk prompt only, get the existing registered volume label and provide it along with the new disk prompt. An empty string for this parameter registers an empty string (0 bytes in length) as the volume label.

</dd> <dt>

*DiskPrompt* 
</dt> <dd>

This parameter provides the disk prompt of the disk being added or updated. An update overwrites the existing disk prompt in the registry. To change the volume label only, get the existing disk prompt from the registry and provide it with the new volume label. An empty string for this parameter registers an empty string (0 bytes in length) as the disk prompt.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                    |                                                                                                                                                                                                                                                                                      |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IProduct is defined as 000C10A0-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                          |



## See also

<dl> <dt>

[**Product**](product-object.md)
</dt> <dt>

[**MsiSourceListAddMediaDisk**](/windows/win32/Msi/nf-msi-msisourcelistaddmediadiska?branch=master)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




