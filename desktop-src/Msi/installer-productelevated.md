---
description: The ProductElevated property of the Installer object returns True if the product is managed or False if the product is not managed.
ms.assetid: 8126f5a0-751f-46c3-9014-208e9c2db34c
title: Installer::ProductElevated property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ProductElevated
- Installer.get_ProductElevated
- Installer.ProductElevated
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer::ProductElevated property

The **ProductElevated** property of the [**Installer**](installer-object.md) object returns True if the product is managed or False if the product is not managed.

This property is read-only.

## Syntax


```JScript
propVal = Installer.ProductElevated
```



## Property value

The full product code GUID of the product. This parameter is required.

## Remarks

The **ProductElevated** property uses the [**MsiIsProductElevated**](/windows/desktop/api/Msi/nf-msi-msiisproductelevateda) function. The return of the property does not take into account the [AlwaysInstallElevated](alwaysinstallelevated.md) policy.

## Examples

The following sample script demonstrates the use of the **ProductElevated** property .


```VB
Dim installer
Set installer = CreateObject("WindowsInstaller.Installer")

' 
' Install Orca tool per-machine
'
installer.InstallProduct "\\products\public\orca\orca.msi", "ALLUSERS=1"

'
' Verify Orca is managed
'

Dim bManaged
bManaged = installer.ProductElevated("{85F4CBCB-9BBC-4B50-A7D8-E1106771498D}")

If bManaged Then
    MsgBox "Success - Product Is Managed"
Else
    MsgBox "Failure - Product Is Not Managed"
End If
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

 

 




