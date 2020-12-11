---
title: ReinstallLicenseKeyPackOffline method of the Win32_TSLicenseKeyPack class
description: Reinstalls a Remote Desktop Services license key pack that uses the license identifier that was received over the Internet or the phone.
ms.assetid: CFDB4C3B-C7C1-4670-BC87-92727057A500
ms.tgt_platform: multiple
keywords:
- ReinstallLicenseKeyPackOffline method Remote Desktop Services
- ReinstallLicenseKeyPackOffline method Remote Desktop Services , Win32_TSLicenseKeyPack class
- Win32_TSLicenseKeyPack class Remote Desktop Services , ReinstallLicenseKeyPackOffline method
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack.ReinstallLicenseKeyPackOffline
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ReinstallLicenseKeyPackOffline method of the Win32\_TSLicenseKeyPack class

Reinstalls a Remote Desktop Services license key pack that uses the license identifier that was received over the Internet or the phone.

## Syntax


```mof
uint32 ReinstallLicenseKeyPackOffline(
  [in]  string sLicenseKeyPackId,
  [out] uint32 KeyPackId
);
```



## Parameters

<dl> <dt>

*sLicenseKeyPackId* \[in\]
</dt> <dd>

Contains the 35-character license code. Only the 35-character alphanumeric character string should be given as input. No hyphens should be added.

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

 

 





