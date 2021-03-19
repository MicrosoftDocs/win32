---
description: The ProductState property is a read-only property that returns the install state information for a product.
ms.assetid: 9ae3bc86-aa13-41b3-b058-4037607f7dd5
title: Installer.ProductState Property method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ProductState
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ProductState Property method

The **ProductState property** is a read-only property that returns the install state information for a product.

## Syntax


```JScript
Installer.ProductState Property(
  Product
)
```



## Parameters

<dl> <dt>

*Product* 
</dt> <dd>

Specifies the product code of the product.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Returns one of the values shown in the following table.



| Installation state        | Description                                      |
|---------------------------|--------------------------------------------------|
| msiInstallStateAbsent     | The product is installed for a different user.   |
| msiInstallStateDefault    | The product is installed for the current user.   |
| msiInstallStateAdvertised | The product is advertised but not installed.     |
| msiInstallStateInvalidArg | An invalid parameter was passed to the function. |
| msiInstallStateUnknown    | The product is neither advertised nor installed. |
| msiInstallStateBadConfig  | The configuration data is corrupt.               |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiQueryProductState**](/windows/desktop/api/Msi/nf-msi-msiqueryproductstatea)
</dt> </dl>

 

 




