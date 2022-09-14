---
title: ImportAgreementLicenseKeyPack method of the Win32_TSLicenseKeyPack class
description: Imports, from another Remote Desktop license server, a Remote Desktop Services license key pack that was purchased through a license agreement, and automatically connects over the Internet to validate the key pack license.
ms.assetid: 3C29E691-3734-4D39-A89F-F381F285DC9E
ms.tgt_platform: multiple
keywords:
- ImportAgreementLicenseKeyPack method Remote Desktop Services
- ImportAgreementLicenseKeyPack method Remote Desktop Services , Win32_TSLicenseKeyPack class
- Win32_TSLicenseKeyPack class Remote Desktop Services , ImportAgreementLicenseKeyPack method
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack.ImportAgreementLicenseKeyPack
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ImportAgreementLicenseKeyPack method of the Win32\_TSLicenseKeyPack class

Imports, from another Remote Desktop license server, a Remote Desktop Services license key pack that was purchased through a license agreement, and automatically connects over the Internet to validate the key pack license.

## Syntax


```mof
uint32 ImportAgreementLicenseKeyPack(
  [in]  uint32 AgreementType,
  [in]  string sAgreementNumber,
  [in]  uint32 ProductVersion,
  [in]  uint32 ProductType,
  [in]  uint32 LicenseCount,
  [in]  string sSourceLSName,
  [in]  string sSourceLSProductId,
  [out] uint32 KeyPackId
);
```



## Parameters

<dl> <dt>

*AgreementType* \[in\]
</dt> <dd>

Agreement type.

<dt>

0
</dt> <dd>

The license key pack is from a Select volume license agreement (for customers with 250 or more computers). The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form.

</dd> <dt>

1
</dt> <dd>

The license key pack is from an Enterprise volume license agreement for customers with 250 or more computers. The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form.

</dd> <dt>

2
</dt> <dd>

The license key pack is from a Campus volume license agreement for a higher education institution. The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form.

</dd> <dt>

3
</dt> <dd>

The license key pack is from a School volume license agreement for primary and secondary institutions. The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form.

</dd> <dt>

4
</dt> <dd>

The license key pack is from a Service Provider license agreement for service providers to license Microsoft software on a monthly basis. The *sAgreementNumber* parameter is the enrollment number (seven numeric digits) found on the signed agreement form.

</dd> <dt>

5
</dt> <dd>

The license key pack is from another license agreement, such as Open Value, Multi-Year Open License, and Open Subscription License. The *sAgreementNumber* parameter is the agreement number provided with your program information.

</dd> </dl> </dd> <dt>

*sAgreementNumber* \[in\]
</dt> <dd>

Agreement number or enrollment number. The *sAgreementNumber* parameter is a seven digit numeric string without hyphens.

</dd> <dt>

*ProductVersion* \[in\]
</dt> <dd>

Product version.

<dt>

0
</dt> <dd>

Not supported.

</dd> <dt>

1
</dt> <dd>

Not supported.

</dd> <dt>

2
</dt> <dd>

Windows Server 2008

</dd> </dl> </dd> <dt>

*ProductType* \[in\]
</dt> <dd>

Product type.

<dt>

0
</dt> <dd>

The Remote Desktop Services license key pack product type is per device. Therefore, each device that connects to the RD Session Host server must have a license.

</dd> <dt>

1
</dt> <dd>

The Remote Desktop Services license key pack product type is per user. Therefore, each user who connects to the RD Session Host server must have a license.

</dd> <dt>

2
</dt> <dd>

This product type is not valid.

</dd> </dl> </dd> <dt>

*LicenseCount* \[in\]
</dt> <dd>

Number of licenses to import.

</dd> <dt>

*sSourceLSName* \[in\]
</dt> <dd>

The name of the source Remote Desktop license server. This is either the fully qualified distinguished name or the IP address of the server.

</dd> <dt>

*sSourceLSProductId* \[in\]
</dt> <dd>

The Remote Desktop license server identifier. The is a 35-character alphanumeric string that cannot include hyphens.

</dd> <dt>

*KeyPackId* \[out\]
</dt> <dd>

Receives the key pack identifier.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

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

 

 





