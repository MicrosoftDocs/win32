---
description: The State property returns the installation state of this instance of the patch.
ms.assetid: b01b2839-d867-4353-99d0-8c612cd1eb0c
title: Patch.State property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Patch.State
api_type: 
- COM
api_location: 
- Msi.dll
---

# Patch.State property

The **State** property returns the installation state of this instance of the patch.

This property is read-only.

## Syntax


```JScript
propVal = Patch.State
```



## Property value

## Remarks

This property returns one of the following values.



| Installation State        | Meaning                                                      |
|---------------------------|--------------------------------------------------------------|
| MSIPATCHSTATE\_APPLIED    | Patch is applied to this product instance.                   |
| MSIPATCHSTATE\_SUPERSEDED | Patch is applied to this product instance but is superseded. |
| MSIPATCHSTATE\_OBSOLETED  | Patch is applied in this product instance but obsolete.      |



 

This method can return ERROR\_UNKNOWN\_PATCH, if the [**Patch**](patch-object.md) object is initialized with an empty string for *ProductCode*.

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

[**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




