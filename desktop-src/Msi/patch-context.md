---
description: The Context property returns the context of this patch.
ms.assetid: 09c92b0b-44f3-4355-8171-03da8ba32757
title: Patch.Context property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Patch.Context
api_type: 
- COM
api_location: 
- Msi.dll
---

# Patch.Context property

The **Context** property returns the context of this patch.

This property is read-only.

## Syntax


```JScript
propVal = Patch.Context
```



## Property value

## Remarks

This property returns one of the following values.



| Context                        | Value | Meaning                        |
|--------------------------------|-------|--------------------------------|
| MSIINSTALLCONTEXT\_USERMANAGED | 1     | Patch under managed context.   |
| MSIINSTALLCONTEXT\_USER        | 2     | Patch under unmanaged context. |
| MSIINSTALLCONTEXT\_MACHINE     | 4     | Patch under machine context.   |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IPatch is defined as 000C10A1-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                            |



## See also

<dl> <dt>

[**Patch Object**](patch-object.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




