---
title: InstallAgreementLicenseKeyPack method of the Win32_TSLicenseKeyPack class
description: Installs a Remote Desktop Services license key pack that was purchased through a license agreement, and automatically connects over the Internet to validate the key pack license.
ms.assetid: 70a0aac3-2709-47ba-bf6a-549393c4c115
ms.tgt_platform: multiple
keywords:
- InstallAgreementLicenseKeyPack method Remote Desktop Services
- InstallAgreementLicenseKeyPack method Remote Desktop Services , Win32_TSLicenseKeyPack class
- Win32_TSLicenseKeyPack class Remote Desktop Services , InstallAgreementLicenseKeyPack method
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack.InstallAgreementLicenseKeyPack
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# InstallAgreementLicenseKeyPack method of the Win32\_TSLicenseKeyPack class

Installs a Remote Desktop Services license key pack that was purchased through a license agreement, and automatically connects over the Internet to validate the key pack license.

## Syntax


```mof
uint32 InstallAgreementLicenseKeyPack(
  [in]  uint32 AgreementType,
  [in]  string sAgreementNumber,
  [in]  uint32 ProductVersion,
  [in]  uint32 ProductType,
  [in]  uint32 LicenseCount,
  [out] uint32 KeyPackId
);
```

## Parameters

*AgreementType* \[in\]

Agreement type.

| Value | Description |
|-------|-------------|
| 0 | The license key pack is from a Select volume license agreement (for customers with 250 or more computers). The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form. |
| 1 | The license key pack is from an Enterprise volume license agreement for customers with 250 or more computers. The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form. |
| 2 | The license key pack is from a Campus volume license agreement for a higher education institution. The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form. |
| 3 | The license key pack is from a School volume license agreement for primary and secondary institutions. The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form. |
| 4 | The license key pack is from a Service Provider license agreement for service providers to license Microsoft software on a monthly basis. The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form. |
| 5 | The license key pack is from another license agreement, such as Open Value, Multi-Year Open License, and Open Subscription License. The *sAgreementNumber* parameter is the agreement number provided with your program information. |

*sAgreementNumber* \[in\]

Agreement number or enrollment number. The *sAgreementNumber* parameter is a seven digit numeric string without hyphens.

*ProductVersion* \[in\]

Product version.

| Value | Description |
|-------|-------------|
| 0 | Not supported |
| 1 | Not supported |
| 2 | Windows Server 2008/Windows Server 2008 R2 |
| 4 | Windows Server 2012/Windows Server 2012 R2 |
| 5 | Windows Server 2016 |
| 6 | Windows Server 2019 |

*ProductType* \[in\]

Product type.

| Value | Description |
|-------|-------------|
| 0 | The Remote Desktop Services license key pack product type is per device. Therefore, each device that connects to the RD Session Host server must have a license. |
| 1 | The Remote Desktop Services license key pack product type is per user. Therefore, each user who connects to the RD Session Host server must have a license. |
| 2 | This product type is not valid. |

*LicenseCount* \[in\]

Number of licenses to install.

*KeyPackId* \[out\]

Receives the key pack identifier.

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

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

[**Win32\_TSLicenseKeyPack**](win32-tslicensekeypack.md)
</dt> </dl>

 

