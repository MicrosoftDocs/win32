---
title: ImportOpenPurchaseLicenseKeyPack method of the Win32_TSLicenseKeyPack class
description: Imports, from another Remote Desktop license server, an Open License Remote Desktop Services license key pack.
ms.assetid: FE1923FF-5292-4080-AB51-88B8A6B2322C
ms.tgt_platform: multiple
keywords:
- ImportOpenPurchaseLicenseKeyPack method Remote Desktop Services
- ImportOpenPurchaseLicenseKeyPack method Remote Desktop Services , Win32_TSLicenseKeyPack class
- Win32_TSLicenseKeyPack class Remote Desktop Services , ImportOpenPurchaseLicenseKeyPack method
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack.ImportOpenPurchaseLicenseKeyPack
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ImportOpenPurchaseLicenseKeyPack method of the Win32\_TSLicenseKeyPack class

Imports, from another Remote Desktop license server, an Open License Remote Desktop Services license key pack.

## Syntax


```mof
uint32 ImportOpenPurchaseLicenseKeyPack(
  [in]  string sLicenseNumber,
  [in]  string sAuthorizationNumber,
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

*sLicenseNumber* \[in\]
</dt> <dd>

8-character numeric string that is provided with the license key pack. The *sLicenseNumber* parameter cannot contain hyphens.

</dd> <dt>

*sAuthorizationNumber* \[in\]
</dt> <dd>

15-character alphanumeric string that is provided with the license key. The *sAuthorizationNumber* parameter cannot contain hyphens.

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

The number of licenses to import

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

 

 





