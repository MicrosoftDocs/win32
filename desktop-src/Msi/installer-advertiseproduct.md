---
description: The AdvertiseProduct method of the Installer object advertises an installation package.
ms.assetid: a060ccb5-353f-439b-8d48-709c81da5f2c
title: Installer::AdvertiseProduct method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.AdvertiseProduct
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer::AdvertiseProduct method

The **AdvertiseProduct** method of the [**Installer**](installer-object.md) object advertises an installation package.

## Syntax


```JScript
.AdvertiseProduct(
  packagePath,
  context,
  transforms,
  language,
  options
)
```



## Parameters

<dl> <dt>

*packagePath* 
</dt> <dd>

The full path to the Windows Installer package (.msi) to be advertised.

</dd> <dt>

*context* 
</dt> <dd>

The context of the advertisement. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="msiAdvertiseProductMachine"></span><span id="msiadvertiseproductmachine"></span><span id="MSIADVERTISEPRODUCTMACHINE"></span><dl> <dt>**msiAdvertiseProductMachine**</dt> <dt>0</dt> </dl> | Advertises the application for an instalation in the per-machine [installation context](installation-context.md). This makes the package available for installation by all users of the computer.<br/> |
| <span id="msiAdvertiseProductUser"></span><span id="msiadvertiseproductuser"></span><span id="MSIADVERTISEPRODUCTUSER"></span><dl> <dt>**msiAdvertiseProductUser**</dt> <dt>1</dt> </dl>             | Advertises the application for an installation in the per-user [installation context](installation-context.md).<br/>                                                                                   |



 

</dd> <dt>

*transforms* 
</dt> <dd>

The list of transforms to apply to the product. Transforms in the list are delimited by semicolons. This parameter is optional.

</dd> <dt>

*language* 
</dt> <dd>

The language of the installation package to use. This parameter is optional.

</dd> <dt>

*options* 
</dt> <dd>

The advertisement options. This parameter is optional. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="msiAdvertiseDefault"></span><span id="msiadvertisedefault"></span><span id="MSIADVERTISEDEFAULT"></span><dl> <dt>**msiAdvertiseDefault**</dt> <dt>0</dt> </dl>                             | Standard advertisement<br/>                                                                                                                                                                                                                                                                                                                 |
| <span id="msiAdvertiseSingleInstance"></span><span id="msiadvertisesingleinstance"></span><span id="MSIADVERTISESINGLEINSTANCE"></span><dl> <dt>**msiAdvertiseSingleInstance**</dt> <dt>1</dt> </dl> | Advertises a new instance of the product. Requires that the first transform in the transform list of the *transforms* parameter be the instance transform that changes the product code. For more information, see [Installing Multiple Instances of Products and Patches](installing-multiple-instances-of-products-and-patches.md).<br/> |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **AdvertiseProduct** method uses the [**MsiAdvertiseProductEx**](/windows/desktop/api/Msi/nf-msi-msiadvertiseproductexa) function.

## Examples

The following example demonstrates the use of the **AdvertiseProduct** method.


```VB
Dim installer
Set installer = CreateObject("WindowsInstaller.Installer")

'
' Perform machine advertisement of package, use transform
'

Installer.AdvertiseProduct "c:\scratch\simpletst\rtm\simple.msi", 0, "c:\scratch\simpletst\rtm\transform.mst"

'
' Verify advertised product state and registration
'
 
MsgBox Installer.ProductState("{BAE98781-CF88-4309-8E2D-3D8B347F5B53}")
MsgBox Installer.ProductInfo("{BAE98781-CF88-4309-8E2D-3D8B347F5B53}", "Transforms")

'
' Remove Product
'
Installer.InstallProduct "c:\scratch\simpletst\rtm\simple.msi", "REMOVE=ALL"
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

 

 




