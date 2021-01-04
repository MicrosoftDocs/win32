---
title: UninstallLicenseKeyPack method of the Win32_TSLicenseKeyPack class
description: Uninstalls a Remote Desktop Services license key pack.
ms.assetid: AF429AD7-C0DB-40AC-A4C6-591699FBF7E7
ms.tgt_platform: multiple
keywords:
- UninstallLicenseKeyPack method Remote Desktop Services
- UninstallLicenseKeyPack method Remote Desktop Services , Win32_TSLicenseKeyPack class
- Win32_TSLicenseKeyPack class Remote Desktop Services , UninstallLicenseKeyPack method
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack.UninstallLicenseKeyPack
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# UninstallLicenseKeyPack method of the Win32\_TSLicenseKeyPack class

Uninstalls a Remote Desktop Services license key pack.

## Syntax


```mof
uint32 UninstallLicenseKeyPack(
  [in] unit32 ProductVersion,
  [in] unit32 ProductType,
  [in] uint32 LicenseCount
);
```



## Parameters

<dl> <dt>

*ProductVersion* \[in\]
</dt> <dd>

Product version identifier for the Remote Desktop Services license key pack.

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

Product type of the Remote Desktop Services license key pack.

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

The number of licenses to uninstall.

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

 

 





