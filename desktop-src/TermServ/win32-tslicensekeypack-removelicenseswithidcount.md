---
title: RemoveLicensesWithIdCount method of the Win32_TSLicenseKeyPack class
description: Removes the specified number of Remote Desktop Services licenses from the specified key pack.
ms.assetid: 36228659-7BE7-490A-A00C-A99FA66BFEB8
ms.tgt_platform: multiple
keywords:
- RemoveLicensesWithIdCount method Remote Desktop Services
- RemoveLicensesWithIdCount method Remote Desktop Services , Win32_TSLicenseKeyPack class
- Win32_TSLicenseKeyPack class Remote Desktop Services , RemoveLicensesWithIdCount method
topic_type:
- apiref
api_name:
- Win32_TSLicenseKeyPack.RemoveLicensesWithIdCount
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RemoveLicensesWithIdCount method of the Win32\_TSLicenseKeyPack class

Removes the specified number of Remote Desktop Services licenses from the specified key pack.

## Syntax


```mof
uint32 RemoveLicensesWithIdCount(
  [in] uint32 KeyPackId,
  [in] uint32 LicenseCount
);
```



## Parameters

<dl> <dt>

*KeyPackId* \[in\]
</dt> <dd>

The identifier of the key pack that contains the licenses to remove.

</dd> <dt>

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

 

 





