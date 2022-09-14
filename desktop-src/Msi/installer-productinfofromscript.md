---
description: The ProductInfoFromScript property of the Installer object returns the value of the specified attribute that is stored in an advertise script.
ms.assetid: 92aa479b-2b4c-482c-a186-a290461bc6d8
title: Installer::ProductInfoFromScript property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ProductInfoFromScript
- Installer.put_ProductInfoFromScript
- Installer.ProductInfoFromScript
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer::ProductInfoFromScript property

The **ProductInfoFromScript** property of the [**Installer**](installer-object.md) object returns the value of the specified attribute that is stored in an advertise script.

This property is write-only.

## Syntax


```JScript
Installer.ProductInfoFromScript = propVal 
```



## Property value

## Error codes

A string or integer value depending upon requested attribute.

## Remarks

The **ProductInfoFromScript** property uses the [**MsiGetProductInfoFromScript**](/windows/desktop/api/Msi/nf-msi-msigetproductinfofromscripta) function.

## Examples

The following sample script demonstrates the use of the **ProductInfoFromScript** property .


```VB
Dim installer
Set installer = CreateObject("WindowsInstaller.Installer")

' 
' Create an advertise script for Orca
'

installer.CreateAdvertiseScript "\\products\public\orca\orca.msi", "c:\scratch\orca.aas"

' 
' Output ProductName Information From Script
'

MsgBox  installer.ProductInfoFromScript("c:\scratch\orca.aas", 3)
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 4.5 on Windows Server 2003 and Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                           |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                                |



## See also

<dl> <dt>

[**Installer**](installer-object.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 




