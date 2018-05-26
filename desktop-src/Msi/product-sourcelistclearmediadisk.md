---
Description: The SourceListClearMediaDisk method of the Product object removes a specified disk from the set of registered disks for a product. Accepts Diskid as a parameter. This method calls MsiSourceListClearMediaDisk.
ms.assetid: 7eec644e-5127-4c17-a8bd-6b0eb091c8aa
title: Product.SourceListClearMediaDisk method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Product.SourceListClearMediaDisk method

The **SourceListClearMediaDisk** method of the [**Product**](product-object.md) object removes a specified disk from the set of registered disks for a product. Accepts *Diskid* as a parameter. This method calls [**MsiSourceListClearMediaDisk**](/windows/win32/Msi/nf-msi-msisourcelistclearmediadiska?branch=master).

## Syntax


```JScript
Product.SourceListClearMediaDisk(
  Diskid
)
```



## Parameters

<dl> <dt>

*Diskid* 
</dt> <dd>

This parameter provides the ID of the disk to remove.

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

[**MsiSourceListClearMediaDisk**](/windows/win32/Msi/nf-msi-msisourcelistclearmediadiska?branch=master)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




