---
title: UninstallLicenseKeyPackWithId method of the Win32_TSLicenseKeyPack class
description: Uninstalls the Remote Desktop Services license key pack with the specified key pack identifier.
ms.assetid: ECB622AB-FAB4-4C5D-A007-E3ABA8E1D3E7
ms.tgt_platform: multiple
keywords:
- UninstallLicenseKeyPackWithId method Remote Desktop Services
- UninstallLicenseKeyPackWithId method Remote Desktop Services , Win32_TSLicenseKeyPack class
- Win32_TSLicenseKeyPack class Remote Desktop Services , UninstallLicenseKeyPackWithId method
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack.UninstallLicenseKeyPackWithId
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# UninstallLicenseKeyPackWithId method of the Win32\_TSLicenseKeyPack class

Uninstalls the Remote Desktop Services license key pack with the specified key pack identifier.

## Syntax


```mof
uint32 UninstallLicenseKeyPackWithId(
  [in] uint32 KeyPackId
);
```



## Parameters

<dl> <dt>

*KeyPackId* \[in\]
</dt> <dd>

The identifier of the key pack to uninstall.

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

 

 





