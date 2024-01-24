---
title: ActivateServer method of the Win32_TSLicenseServer class
description: Activates the Remote Desktop license server by using a Remote Desktop license server identifier that is obtained over the phone or the Internet.
ms.assetid: 628e87f0-600e-404d-a0b4-35f1570b4fc0
ms.tgt_platform: multiple
keywords:
- ActivateServer method Remote Desktop Services
- ActivateServer method Remote Desktop Services , Win32_TSLicenseServer class
- Win32_TSLicenseServer class Remote Desktop Services , ActivateServer method
topic_type:
- apiref
api_name:
- Win32_TSLicenseServer.ActivateServer
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActivateServer method of the Win32\_TSLicenseServer class

Activates the Remote Desktop license server by using a Remote Desktop license server identifier that is obtained over the phone or the Internet.

## Syntax


```mof
uint32 ActivateServer(
  [in]  string sLicenseServerId,
  [out] uint32 ActivationStatus
);
```



## Parameters

<dl> <dt>

*sLicenseServerId* \[in\]
</dt> <dd>

Remote Desktop license server ID that was obtained over the phone or the Internet. The *sLicenseServerId* parameter is a 35-character alphanumeric string that cannot include hyphens.

</dd> <dt>

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

 

