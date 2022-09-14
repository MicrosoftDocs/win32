---
description: The InstallProperty property is the value of the property for the instance of this product. This property calls the MsiGetProductInfoEx function, with the ProductCode, UserSid and Context of the Product object and the requested property as a parameter.
ms.assetid: 945c11fe-39da-43b7-a19f-e6364d5e715c
title: Product.InstallProperty method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Product.InstallProperty
api_type: 
- COM
api_location: 
- Msi.dll
---

# Product.InstallProperty method

The **InstallProperty** property is the value of the property for the instance of this product.

This property calls the [**MsiGetProductInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetproductinfoexa) function, with the *ProductCode*, *UserSid* and *Context* of the [**Product**](product-object.md) object and the requested property as a parameter.

## Syntax


```JScript
Product.InstallProperty(
  property
)
```



## Parameters

<dl> <dt>

*property* 
</dt> <dd>

Specifies the property to be retrieved. The properties in the following list can only be retrieved from applications that are already installed. Note that [required](required-properties.md) properties are guaranteed to be available, but other properties are available only if that property has been set. See the indicated links to the installer [properties](properties.md) for information about how each property is set.



| Installed properties                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="INSTALLPROPERTY_PRODUCTSTATE"></span><span id="installproperty_productstate"></span><dl> <dt>**INSTALLPROPERTY\_PRODUCTSTATE**</dt> </dl>                         | State of the product returned in string form as "1" for Advertised and "5" for installed.<br/>                                                                                                                                                                                                                                                                            |
| <span id="INSTALLPROPERTY_HELPLINK"></span><span id="installproperty_helplink"></span><dl> <dt>**INSTALLPROPERTY\_HELPLINK**</dt> </dl>                                     | Support link. For more information, see the [**ARPHELPLINK**](arphelplink.md) property.<br/>                                                                                                                                                                                                                                                                             |
| <span id="INSTALLPROPERTY_HELPTELEPHONE"></span><span id="installproperty_helptelephone"></span><dl> <dt>**INSTALLPROPERTY\_HELPTELEPHONE**</dt> </dl>                      | Support telephone. For more information, see the [**ARPHELPTELEPHONE**](arphelptelephone.md) property.<br/>                                                                                                                                                                                                                                                              |
| <span id="INSTALLPROPERTY_INSTALLDATE"></span><span id="installproperty_installdate"></span><dl> <dt>**INSTALLPROPERTY\_INSTALLDATE**</dt> </dl>                            | The last time this product received service. The value of this property is replaced each time a patch is applied or removed from the product or the /v [Command-Line Option](command-line-options.md) is used to repair the product. If the product has received no repairs or patches this property contains the time this product was installed on this computer.<br/> |
| <span id="INSTALLPROPERTY_INSTALLEDPRODUCTNAME"></span><span id="installproperty_installedproductname"></span><dl> <dt>**INSTALLPROPERTY\_INSTALLEDPRODUCTNAME**</dt> </dl> | Installed product name. For more information, see the [**ProductName**](productname.md) property.<br/>                                                                                                                                                                                                                                                                   |
| <span id="INSTALLPROPERTY_INSTALLLOCATION"></span><span id="installproperty_installlocation"></span><dl> <dt>**INSTALLPROPERTY\_INSTALLLOCATION**</dt> </dl>                | Installation location. For more information, see the [**ARPINSTALLLOCATION**](arpinstalllocation.md) property.<br/>                                                                                                                                                                                                                                                      |
| <span id="INSTALLPROPERTY_INSTALLSOURCE"></span><span id="installproperty_installsource"></span><dl> <dt>**INSTALLPROPERTY\_INSTALLSOURCE**</dt> </dl>                      | Installation source. For more information, see the [**SourceDir**](sourcedir.md) property.<br/>                                                                                                                                                                                                                                                                          |
| <span id="INSTALLPROPERTY_LOCALPACKAGE"></span><span id="installproperty_localpackage"></span><dl> <dt>**INSTALLPROPERTY\_LOCALPACKAGE**</dt> </dl>                         | Local cached package.<br/>                                                                                                                                                                                                                                                                                                                                                |
| <span id="INSTALLPROPERTY_PUBLISHER"></span><span id="installproperty_publisher"></span><dl> <dt>**INSTALLPROPERTY\_PUBLISHER**</dt> </dl>                                  | Publisher. For more information, see the [**Manufacturer**](manufacturer.md) property.<br/>                                                                                                                                                                                                                                                                              |
| <span id="INSTALLPROPERTY_URLINFOABOUT"></span><span id="installproperty_urlinfoabout"></span><dl> <dt>**INSTALLPROPERTY\_URLINFOABOUT**</dt> </dl>                         | URL information. For more information, see the [**ARPURLINFOABOUT**](arpurlinfoabout.md) property.<br/>                                                                                                                                                                                                                                                                  |
| <span id="INSTALLPROPERTY_URLUPDATEINFO"></span><span id="installproperty_urlupdateinfo"></span><dl> <dt>**INSTALLPROPERTY\_URLUPDATEINFO**</dt> </dl>                      | URL update information. For more information, see the [**ARPURLUPDATEINFO**](arpurlupdateinfo.md) property.<br/>                                                                                                                                                                                                                                                         |
| <span id="INSTALLPROPERTY_VERSIONMINOR"></span><span id="installproperty_versionminor"></span><dl> <dt>**INSTALLPROPERTY\_VERSIONMINOR**</dt> </dl>                         | Minor product version derived from the [**ProductVersion**](productversion.md) property.<br/>                                                                                                                                                                                                                                                                            |
| <span id="INSTALLPROPERTY_VERSIONMAJOR"></span><span id="installproperty_versionmajor"></span><dl> <dt>**INSTALLPROPERTY\_VERSIONMAJOR**</dt> </dl>                         | Major product version derived from the [**ProductVersion**](productversion.md) property.<br/>                                                                                                                                                                                                                                                                            |
| <span id="INSTALLPROPERTY_VERSIONSTRING"></span><span id="installproperty_versionstring"></span><dl> <dt>**INSTALLPROPERTY\_VERSIONSTRING**</dt> </dl>                      | Product version. For more information, see the [**ProductVersion**](productversion.md) property.<br/>                                                                                                                                                                                                                                                                    |



 

To retrieve the product ID, registered owner, or registered company from applications that are already installed, set *property* to one of the following text string values.



| Value      | Description                                                                                    |
|------------|------------------------------------------------------------------------------------------------|
| ProductID  | The product identifier. For more information, see the [**ProductID**](productid.md) property. |
| RegCompany | The company registered to use this product.                                                    |
| RegOwner   | The owner registered to use this product.                                                      |



 

To retrieve the instance type of the product, set *property* to the following value. This property is available for advertised or installed products.



| Value        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InstanceType | A missing value or a value of 0 indicates a normal product installation. A value of 1 indicates a product installed using a multiple instance transform and the [**MSINEWINSTANCE**](msinewinstance.md) property. Available with the installer running Windows Server 2003 or Windows XP with SP1. For more information, see [Installing Multiple Instances of Products and Patches](installing-multiple-instances-of-products-and-patches.md). |



 

The properties in the following list can also be retrieved from applications that are advertised. These properties cannot be retrieved for product instances that are installed under a per-user-unmanaged context for user accounts other than current user account.



| Advertised properties                 | Description                                                                                                                                                                                                                                                                                          |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INSTALLPROPERTY\_TRANSFORMS           | Transforms.                                                                                                                                                                                                                                                                                          |
| INSTALLPROPERTY\_LANGUAGE             | Product language.                                                                                                                                                                                                                                                                                    |
| INSTALLPROPERTY\_PRODUCTNAME          | Human readable–product name. For more information, see the [**ProductName**](productname.md) property.                                                                                                                                                                                              |
| INSTALLPROPERTY\_ASSIGNMENTTYPE       | Equals zero (0) if the product is advertised or installed per-user. Equals one (1) if the product is advertised or installed per-computer for all users.<br/>                                                                                                                                  |
| INSTALLPROPERTY\_PACKAGECODE          | Identifier of the package this product was installed from. For details, see [Package Codes](package-codes.md).                                                                                                                                                                                      |
| INSTALLPROPERTY\_VERSION              | Product version derived from the [**ProductVersion**](productversion.md) property.                                                                                                                                                                                                                  |
| INSTALLPROPERTY\_PRODUCTICON          | Primary icon for the package. For more information, see the [**ARPPRODUCTICON**](arpproducticon.md) property.                                                                                                                                                                                       |
| INSTALLPROPERTY\_PACKAGENAME          | Name of the original installation package.                                                                                                                                                                                                                                                           |
| INSTALLPROPERTY\_AUTHORIZED\_LUA\_APP | A value of 1 indicates a product that can be serviced by non-administrators using [User Account Control (UAC) Patching](user-account-control--uac--patching.md). A missing value or a value of 0 indicates least-privilege patching is not enabled. Available with Windows Installer 3.0 and later. |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the call succeeds, the property contains the value as a string.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IProduct is defined as 000C10A0-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                          |



## See also

<dl> <dt>

[**Product**](product-object.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




