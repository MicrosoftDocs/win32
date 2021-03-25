---
description: The SourceListInfo property of the Patch object gets and sets the source information properties for a patch. This property call MsiSourceListGetInfo or MsiSourceListSetInfo. This is a read or write property.
ms.assetid: a07f2cc8-fee2-4703-89ea-769921713268
title: Patch.SourceListInfo property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Patch.SourceListInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# Patch.SourceListInfo property

The **SourceListInfo** property of the [**Patch**](patch-object.md) object gets and sets the source information properties for a patch. This property call [**MsiSourceListGetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistgetinfoa) or [**MsiSourceListSetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistsetinfoa). This is a read or write property.

This property is read-only.

## Syntax


```JScript
propVal = Patch.SourceListInfo
```



## Property value

The name of the source information properties for a patch to query or set. For possible values, see the Remarks section of this topic.

## Remarks

Not all properties that can be retrieved can be set. The *szProperty* parameter can be one of the following values.



| Property         | Can set? | Meaning                                                                                                                                                                                                                                                           |
|------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MediaPackagePath | Y        | The path relative to the root of the installation media.                                                                                                                                                                                                          |
| DiskPrompt       | Y        | The prompt template used when prompting the user for installation media.                                                                                                                                                                                          |
| LastUsedSource   | Y        | The most recently used source location for the patch. When you set this property, prefix the source location with "n;" for a network source or "u;" for URL type. For example, use "n;\\\\scratch\\scratch\\test" or "u;https://microsoft.com/Patches/Office/SP1". |
| LastUsedType     | N        | "n" if the last-used source is a network location. "u" if the last used source was a URL location. "m" if the last used source was media. Empty string ("") if there is no last used source.                                                                      |
| PackageName      | Y        | The name of the Windows Installer package or patch package on the source.                                                                                                                                                                                         |



 

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

[**MsiSourceListGetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistgetinfoa)
</dt> <dt>

[**MsiSourceListSetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistsetinfoa)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




