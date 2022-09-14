---
description: The SourceListClearAll method of the Patch object clears the complete source list of all sources of the specified type for a patch. Accepts Type as a parameter. This method calls MsiSourceListClearAllEx.
ms.assetid: 9458a3db-8eaa-4067-875f-8fac68bdf1f8
title: Patch.SourceListClearAll method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Patch.SourceListClearAll
api_type: 
- COM
api_location: 
- Msi.dll
---

# Patch.SourceListClearAll method

The **SourceListClearAll** method of the [**Patch**](patch-object.md) object clears the complete source list of all sources of the specified type for a patch. Accepts *Type* as a parameter. This method calls [**MsiSourceListClearAllEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearallexa).

## Syntax


```JScript
Patch.SourceListClearAll(
  Type
)
```



## Parameters

<dl> <dt>

*Type* 
</dt> <dd>

The type of source type, such as network, URL or media.

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

[**MsiSourceListClearAllEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearallexa)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




