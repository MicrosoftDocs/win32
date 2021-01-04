---
title: ActivateServerAutomatic method of the Win32_TSLicenseServer class
description: Activates the Remote Desktop license server automatically over the Internet.
ms.assetid: a33ba72f-3403-4bd2-94a9-0c5ef1cbb03e
ms.tgt_platform: multiple
keywords:
- ActivateServerAutomatic method Remote Desktop Services
- ActivateServerAutomatic method Remote Desktop Services , Win32_TSLicenseServer class
- Win32_TSLicenseServer class Remote Desktop Services , ActivateServerAutomatic method
topic_type:
- apiref
api_name:
- Win32_TSLicenseServer.ActivateServerAutomatic
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActivateServerAutomatic method of the Win32\_TSLicenseServer class

Activates the Remote Desktop license server automatically over the Internet.

## Syntax


```mof
uint32 ActivateServerAutomatic(
  [out] uint32 ActivationStatus
);
```



## Parameters

<dl> <dt>

*ActivationStatus* \[out\]
</dt> <dd>

The activation status returned can be one of the following.

<dt>

0
</dt> <dd>

The Remote Desktop license server is activated.

</dd> <dt>

1
</dt> <dd>

The Remote Desktop license server is not activated.

</dd> <dt>

2
</dt> <dd>

An unknown error occurred. It is not known whether the Remote Desktop license server is activated.

</dd> </dl> </dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

This method fails unless the **FirstName**, **LastName**, **Company**, and **CountryRegion** properties are set.

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

[**Win32\_TSLicenseServer**](win32-tslicenseserver.md)
</dt> </dl>

 

