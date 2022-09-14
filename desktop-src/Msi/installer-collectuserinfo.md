---
description: The CollectUserInfo method of the Installer object invokes a user interface wizard sequence which collects and stores both user information and the product code.
ms.assetid: 2faacf38-1af1-4e8a-a3f6-87733104614e
title: Installer.CollectUserInfo method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.CollectUserInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.CollectUserInfo method

The **CollectUserInfo** method of the [**Installer**](installer-object.md) object invokes a user interface wizard sequence which collects and stores both user information and the product code.

## Syntax


```JScript
Installer.CollectUserInfo(
  Product
)
```



## Parameters

<dl> <dt>

*Product* 
</dt> <dd>

Specifies the [**product code**](productcode.md) of the product.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

An application should call the **CollectUserInfo** method the first time it is run. The **CollectUserInfo** method opens the product's installation package and invokes an authored user interface wizard sequence which collects user information. Upon completion of the wizard sequence, the collected user information is registered. The [**UILevel**](installer-uilevel.md) property should be set to msiUILevelFull because this API requires an authored user interface.

The **CollectUserInfo** method invokes the [FirstRun Dialog](firstrun-dialog.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiCollectUserInfo**](/windows/desktop/api/Msi/nf-msi-msicollectuserinfoa)
</dt> </dl>

 

 




