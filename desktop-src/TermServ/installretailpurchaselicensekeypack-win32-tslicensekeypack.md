---
title: InstallRetailPurchaseLicenseKeyPack method of the Win32_TSLicenseKeyPack class
description: Installs a Remote Desktop Services license key pack that was purchased through a retail channel.
ms.assetid: cd33c785-7aa1-4e30-8155-4176b6f4c037
ms.tgt_platform: multiple
keywords:
- InstallRetailPurchaseLicenseKeyPack method Remote Desktop Services
- InstallRetailPurchaseLicenseKeyPack method Remote Desktop Services , Win32_TSLicenseKeyPack class
- Win32_TSLicenseKeyPack class Remote Desktop Services , InstallRetailPurchaseLicenseKeyPack method
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack.InstallRetailPurchaseLicenseKeyPack
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# InstallRetailPurchaseLicenseKeyPack method of the Win32\_TSLicenseKeyPack class

Installs a Remote Desktop Services license key pack that was purchased through a retail channel.

## Syntax


```mof
uint32 InstallRetailPurchaseLicenseKeyPack(
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

 

