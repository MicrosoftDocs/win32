---
description: The MediaDisks property enumerates all the media disks for this product instance. This property calls the MsiSourceListEnumMediaDisks. Returns the disk information as an array of Record objects.
ms.assetid: 9ea7c9a8-4ff1-4b26-a8d5-c23510650566
title: Product.MediaDisks property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Product.MediaDisks
api_type: 
- COM
api_location: 
- Msi.dll
---

# Product.MediaDisks property

The **MediaDisks** property enumerates all the media disks for this product instance. This property calls the [**MsiSourceListEnumMediaDisks**](/windows/desktop/api/Msi/nf-msi-msisourcelistenummediadisksa). Returns the disk information as an array of [**Record**](record-object.md) objects.

This property is read-only.

## Syntax


```JScript
propVal = Product.MediaDisks
```



## Property value

## Remarks

In each record, the first field contains the disk Id, the second field contains the volume label and the third field contains the disk prompt registered for the disk.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IProduct is defined as 000C10A0-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                          |



## See also

<dl> <dt>

[**Product**](product-object.md)
</dt> <dt>

[**MsiSourceListEnumMediaDisks**](/windows/desktop/api/Msi/nf-msi-msisourcelistenummediadisksa)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




