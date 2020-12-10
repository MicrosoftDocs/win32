---
title: ReinstallRetailPurchaseLicenseKeyPack method of the Win32_TSLicenseKeyPack class
description: Reinstalls a Remote Desktop Services license key pack that was purchased through a retail channel.
ms.assetid: 19528726-8DEB-4D03-BFA6-647C8A612FA2
ms.tgt_platform: multiple
keywords:
- ReinstallRetailPurchaseLicenseKeyPack method Remote Desktop Services
- ReinstallRetailPurchaseLicenseKeyPack method Remote Desktop Services , Win32_TSLicenseKeyPack class
- Win32_TSLicenseKeyPack class Remote Desktop Services , ReinstallRetailPurchaseLicenseKeyPack method
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack.ReinstallRetailPurchaseLicenseKeyPack
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ReinstallRetailPurchaseLicenseKeyPack method of the Win32\_TSLicenseKeyPack class

Reinstalls a Remote Desktop Services license key pack that was purchased through a retail channel.

## Syntax


```mof
uint32 ReinstallRetailPurchaseLicenseKeyPack(
  [in]  string sLicenseCode,
  [out] uint32 KeyPackId
);
```



## Parameters

<dl> <dt>

*sLicenseCode* \[in\]
</dt> <dd>

Contains the 25-character license code. Only the 25-character alphanumeric character string should be given as input. No hyphens should be added.

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

 

 





