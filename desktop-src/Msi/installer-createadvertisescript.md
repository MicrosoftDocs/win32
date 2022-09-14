---
description: The CreateAdvertiseScript method of the Installer object generates an advertise script.
ms.assetid: 32a331e5-d291-49cd-ab0e-7d0e4d72a95b
title: Installer::CreateAdvertiseScript method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.CreateAdvertiseScript
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer::CreateAdvertiseScript method

The **CreateAdvertiseScript** method of the [**Installer**](installer-object.md) object generates an advertise script.

## Syntax


```JScript
.CreateAdvertiseScript(
  packagePath,
  scriptFilePath,
  transforms,
  language,
  platform,
  options
)
```



## Parameters

<dl> <dt>

*packagePath* 
</dt> <dd>

The full path to the Windows Installer package (.msi) to be advertised.

</dd> <dt>

*scriptFilePath* 
</dt> <dd>

The full path to the script file to be created with the advertised information.

</dd> <dt>

*transforms* 
</dt> <dd>

The list of transforms to apply to the product. Transforms in the list are delimited by semicolons. This parameter is optional.

</dd> <dt>

*language* 
</dt> <dd>

The language of the installation package to use. This parameter is optional.

</dd> <dt>

*platform* 
</dt> <dd>

This parameter specifies for which platform the installer should create the script. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                                       | Meaning                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <span id="msiAdvertiseCurrentPlatform"></span><span id="msiadvertisecurrentplatform"></span><span id="MSIADVERTISECURRENTPLATFORM"></span><dl> <dt>**msiAdvertiseCurrentPlatform**</dt> <dt>0</dt> </dl> | Creates a script for the current platform.<br/>  |
| <span id="msiAdvertiseX86Platform"></span><span id="msiadvertisex86platform"></span><span id="MSIADVERTISEX86PLATFORM"></span><dl> <dt>**msiAdvertiseX86Platform**</dt> <dt>1</dt> </dl>                 | Creates a script for the x86 platform.<br/>      |
| <span id="msiAdvertiseIA64Platform"></span><span id="msiadvertiseia64platform"></span><span id="MSIADVERTISEIA64PLATFORM"></span><dl> <dt>**msiAdvertiseIA64Platform**</dt> <dt>2</dt> </dl>             | Creates a script for Itanium-based systems.<br/> |
| <span id="msiAdvertiseX64Platform"></span><span id="msiadvertisex64platform"></span><span id="MSIADVERTISEX64PLATFORM"></span><dl> <dt>**msiAdvertiseX64Platform**</dt> <dt>4</dt> </dl>                 | Creates a script for the x64 platform.<br/>      |



 

</dd> <dt>

*options* 
</dt> <dd>

Advertisement options. This parameter is optional. This parameter can be one of the following values. This parameter is optional.



| Value                                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="msiAdvertiseDefault"></span><span id="msiadvertisedefault"></span><span id="MSIADVERTISEDEFAULT"></span><dl> <dt>**msiAdvertiseDefault**</dt> <dt>0</dt> </dl>                             | Standard advertisement<br/>                                                                                                                                                                                                                                                                                                                 |
| <span id="msiAdvertiseSingleInstance"></span><span id="msiadvertisesingleinstance"></span><span id="MSIADVERTISESINGLEINSTANCE"></span><dl> <dt>**msiAdvertiseSingleInstance**</dt> <dt>1</dt> </dl> | Advertises a new instance of the product. Requires that the first transform in the transform list of the *transforms* parameter be the instance transform that changes the product code. For more information, see [Installing Multiple Instances of Products and Patches](installing-multiple-instances-of-products-and-patches.md).<br/> |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The [**AdvertiseProduct**](installer-advertiseproduct.md) method uses the [**MsiAdvertiseProductEx**](/windows/desktop/api/Msi/nf-msi-msiadvertiseproductexa) function.

## Examples

The following example demonstrates the use of the **CreateAdvertiseScript** method.


```VB
Dim installer
Set installer = CreateObject("WindowsInstaller.Installer")

'
' Create an advertise script for Orca
'

Installer.CreateAdvertiseScript "\\products\public\orca\orca.msi", "c:\scripts\orca.aas"
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

 

 




