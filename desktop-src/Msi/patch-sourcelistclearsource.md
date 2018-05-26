---
Description: Removes a network or URL source.
ms.assetid: 76c7cc6c-740f-40e0-8385-024dcc82b79e
title: Patch.SourceListClearSource method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Patch.SourceListClearSource method

The **SourceListClearSource** method removes a network or URL source. This method calls [**MsiSourceListClearSource**](/windows/win32/Msi/nf-msi-msisourcelistclearsourcea?branch=master).

## Syntax


```JScript
Patch.SourceListClearSource(
  Type,
  SourcePath
)
```



## Parameters

<dl> <dt>

*Type* 
</dt> <dd>

Type of source to be removed.

<dl><span id="MSISOURCETYPE_NETWORK"></span><span id="msisourcetype_network"></span><dt>

**MSISOURCETYPE\_NETWORK**
</dt><span id="MSISOURCETYPE_URL"></span><span id="msisourcetype_url"></span><dt>

**MSISOURCETYPE\_URL**
</dt> </dl> </dd> <dt>

*SourcePath* 
</dt> <dd>

Path to the source to be removed.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                    |                                                                                                                                                                                                                                                                                      |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IPatch is defined as 000C10A1-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                            |



## See also

<dl> <dt>

[**Patch**](patch-object.md)
</dt> <dt>

[**MsiSourceListClearSource**](/windows/win32/Msi/nf-msi-msisourcelistclearsourcea?branch=master)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




