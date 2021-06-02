---
title: Win32_TSLicenseKeyPack class
description: Provides methods and properties for viewing and installing Remote Desktop Services license key packs.
ms.assetid: 27450646-c51f-4911-bb42-410794e32003
ms.tgt_platform: multiple
keywords:
- Win32_TSLicenseKeyPack class Remote Desktop Services
- Win32_TSLicenseKeyPack class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack
- Win32_TSLicenseKeyPack.KeyPackId
- Win32_TSLicenseKeyPack.Description
- Win32_TSLicenseKeyPack.KeyPackType
- Win32_TSLicenseKeyPack.ProductType
- Win32_TSLicenseKeyPack.ProductVersion
- Win32_TSLicenseKeyPack.ProductVersionID
- Win32_TSLicenseKeyPack.TotalLicenses
- Win32_TSLicenseKeyPack.IssuedLicenses
- Win32_TSLicenseKeyPack.AvailableLicenses
- Win32_TSLicenseKeyPack.ExpirationDate
- Win32_TSLicenseKeyPack.AccessRights
- Win32_TSLicenseKeyPack.TypeAndModel
api_location:
- TlsWmiProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSLicenseKeyPack class

Provides methods and properties for viewing and installing Remote Desktop Services license key packs.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_TERMSERVLICENSING_Prov"), AMENDMENT]
class Win32_TSLicenseKeyPack
{
  uint32   KeyPackId;
  string   Description;
  uint32   KeyPackType;
  uint32   ProductType;
  string   ProductVersion;
  uint32   ProductVersionID;
  uint32   TotalLicenses;
  uint32   IssuedLicenses;
  uint32   AvailableLicenses;
  DATETIME ExpirationDate;
  uint32   AccessRights;
  string   TypeAndModel;
};
```

## Members

The **Win32\_TSLicenseKeyPack** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSLicenseKeyPack** class has these methods.



| Method                                                                                                        | Description                                                                                                                                                                                                                               |
|:--------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ConvertLicenses**](convertlicenses-win32-tslicensekeypack.md)                                             | Converts the licenses in the current key pack.<br/>                                                                                                                                                                                 |
| [**ImportAgreementLicenseKeyPack**](win32-tslicensekeypack-importagreementlicensekeypack.md)                 | Imports, from another Remote Desktop license server, a Remote Desktop Services license key pack that was purchased through a license agreement, and automatically connects over the Internet to validate the key pack license.<br/> |
| [**ImportLicenseKeyPackOffline**](win32-tslicensekeypack-importlicensekeypackoffline.md)                     | Imports, from another Remote Desktop license server, a Remote Desktop Services license key pack that uses a license identifier that was received over the Internet or the phone.<br/>                                               |
| [**ImportOpenPurchaseLicenseKeyPack**](win32-tslicensekeypack-importopenpurchaselicensekeypack.md)           | Imports, from another Remote Desktop license server, an Open License Remote Desktop Services license key pack.<br/>                                                                                                                 |
| [**ImportRetailPurchaseLicenseKeyPack**](win32-tslicensekeypack-importretailpurchaselicensekeypack.md)       | Imports, from another Remote Desktop license server, a Remote Desktop Services license key pack that was purchased through a retail channel.<br/>                                                                                   |
| [**InstallAgreementLicenseKeyPack**](installagreementlicensekeypack-win32-tslicensekeypack.md)               | Installs a Remote Desktop Services license key pack that was purchased through an agreement license.<br/>                                                                                                                           |
| [**InstallLicenseKeyPack**](installlicensekeypack-win32-tslicensekeypack.md)                                 | Installs a Remote Desktop Services license key pack that uses a license key pack ID that was received over the Internet or the phone.<br/>                                                                                          |
| [**InstallOpenLicenseKeyPack**](installopenlicensekeypack-win32-tslicensekeypack.md)                         | Installs a Remote Desktop Services license key pack that was purchased through an open license agreement.<br/>                                                                                                                      |
| [**InstallRetailPurchaseLicenseKeyPack**](installretailpurchaselicensekeypack-win32-tslicensekeypack.md)     | Installs a Remote Desktop Services license key pack that was purchased through a retail store.<br/>                                                                                                                                 |
| [**ReinstallAgreementLicenseKeyPack**](win32-tslicensekeypack-reinstallagreementlicensekeypack.md)           | Reinstalls a Remote Desktop Services license key pack that was purchased through a license agreement, and automatically connects over the Internet to validate the key pack license.<br/>                                           |
| [**ReinstallLicenseKeyPackOffline**](win32-tslicensekeypack-reinstalllicensekeypackoffline.md)               | Reinstalls a Remote Desktop Services license key pack that uses the license identifier that was received over the Internet or the phone.<br/>                                                                                       |
| [**ReinstallOpenPurchaseLicenseKeyPack**](win32-tslicensekeypack-reinstallopenpurchaselicensekeypack.md)     | Reinstalls an Open License Remote Desktop Services license key pack.<br/>                                                                                                                                                           |
| [**ReinstallRetailPurchaseLicenseKeyPack**](win32-tslicensekeypack-reinstallretailpurchaselicensekeypack.md) | Reinstalls a Remote Desktop Services license key pack that was purchased through a retail channel.<br/>                                                                                                                             |
| [**RemoveLicensesWithIdCount**](win32-tslicensekeypack-removelicenseswithidcount.md)                         | Removes the specified number of Remote Desktop Services licenses from the specified key pack.<br/>                                                                                                                                  |
| [**UninstallLicenseKeyPack**](win32-tslicensekeypack-uninstalllicensekeypack.md)                             | Uninstalls a Remote Desktop Services license key pack.<br/>                                                                                                                                                                         |
| [**UninstallLicenseKeyPackWithId**](win32-tslicensekeypack-uninstalllicensekeypackwithid.md)                 | Uninstalls the Remote Desktop Services license key pack with the specified key pack identifier.<br/>                                                                                                                                |



 

### Properties

The **Win32\_TSLicenseKeyPack** class has these properties.

<dl> <dt>

**AccessRights**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**BitMap**](/windows/desktop/WmiSdk/standard-qualifiers) ("0", "1", "2", "3"), [**BitValues**](/windows/desktop/WmiSdk/standard-qualifiers) ("RD Session", "VDI Session", "Calista", "VDI Partners")
</dt> </dl>

Qualifier for TS Licensing key pack access rights

</dd> <dt>

**AvailableLicenses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of available licenses in the Remote Desktop Services license key pack.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the Remote Desktop Services license key pack.

</dd> <dt>

**ExpirationDate**
</dt> <dd> <dl> <dt>

Data type: **[DATETIME](/windows/desktop/WmiSdk/datetime)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The expiration date of the Remote Desktop Services license key pack.

</dd> <dt>

**IssuedLicenses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of issued licenses in the Remote Desktop Services license key pack.

</dd> <dt>

**KeyPackId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifier for the Remote Desktop Services license key pack.

</dd> <dt>

**KeyPackType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of key pack for the Remote Desktop license server.

| Value | Description |
|-------|-------------|
| 0 | The Remote Desktop Services license key pack type is unknown. |
| 1 | The Remote Desktop Services license key pack type is a retail purchase. |
| 2 | The Remote Desktop Services license key pack type is a volume purchase. |
| 3 | The Remote Desktop Services license key pack type is a concurrent license. |
| 4 | The Remote Desktop Services license key pack type is temporary. |
| 5 | The Remote Desktop Services license key pack type is an open license. |
| 6 | Not supported. |

**ProductType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product type of the Remote Desktop Services license key pack.

| Value | Description |
|-------|-------------|
| 0 | The Remote Desktop Services license key pack product type is per device. Therefore, each device that connects to the RD Session Host server must have a license. |
| 1 | The Remote Desktop Services license key pack product type is per user. Therefore, each user who connects to the RD Session Host server must have a license. |
| 2 | This product type is not valid. |

**ProductVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product version for the Remote Desktop Services license key pack.

| Value | Description |
|-------|-------------|
| "Windows Server 2012" | Only servers running Windows Server 2012, Windows Server 2008 R2, or Windows Server 2008 are supported with this license. |
| "Windows Server 7" | Only servers running Windows Server 2008 R2, or Windows Server 2008 are supported with this license. |
| "Windows Server 2008" | Only servers running Windows Server 2008 are supported by this key pack. |

**ProductVersionID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product version identifier for the Remote Desktop Services license key pack.

| Value | Description |
|-------|-------------|
| 0 | Not supported |
| 1 | Not supported |
| 2 | Windows Server 2008 |
| 3 | Windows Server 2008 R2 |
| 4 | Windows Server 2012/Windows Server 2012 R2 |
| 5 | Windows Server 2016 |
| 6 | Windows Server 2019 |

**TotalLicenses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of licenses in the Remote Desktop Services license key pack.

</dd> <dt>

**TypeAndModel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Qualifier for TS Licensing key pack type and model. Examples: VDI Per Device subscription license, TS Per User CAL

</dd> </dl>

## Remarks

You must be a member of the Administrators group to use this class.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>TlsWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TlsWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSIssuedLicense**](win32-tsissuedlicense.md)
</dt> <dt>

[**Win32\_TSLicenseReport**](win32-tslicensereport.md)
</dt> <dt>

[**Win32\_TSLicenseReportEntry**](win32-tslicensereportentry.md)
</dt> <dt>

[**Win32\_TSLicenseServer**](win32-tslicenseserver.md)
</dt> </dl>

 

