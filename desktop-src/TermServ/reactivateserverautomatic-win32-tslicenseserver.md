---
title: ReactivateServerAutomatic method of the Win32_TSLicenseServer class
description: Reactivates the Remote Desktop license server by using an automatic connection to the Internet.
ms.assetid: 98b9b8e5-4de4-418c-9175-58e8b84784d5
ms.tgt_platform: multiple
keywords:
- ReactivateServerAutomatic method Remote Desktop Services
- ReactivateServerAutomatic method Remote Desktop Services , Win32_TSLicenseServer class
- Win32_TSLicenseServer class Remote Desktop Services , ReactivateServerAutomatic method
topic_type:
- apiref
api_name:
- Win32_TSLicenseServer.ReactivateServerAutomatic
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ReactivateServerAutomatic method of the Win32\_TSLicenseServer class

Reactivates the Remote Desktop license server by using an automatic connection to the Internet.

## Syntax


```mof
uint32 ReactivateServerAutomatic(
  [in]  uint32 Reason,
  [out] uint32 ActivationStatus
);
```



## Parameters

<dl> <dt>

*Reason* \[in\]
</dt> <dd>

Reason for the activation. It can be one of the following values.

<dt>

0
</dt> <dd>

The server was redeployed.

</dd> <dt>

1
</dt> <dd>

The certificate was corrupt.

</dd> <dt>

2
</dt> <dd>

The private key was compromised.

</dd> <dt>

3
</dt> <dd>

The activation key expired.

</dd> <dt>

4
</dt> <dd>

The server was upgraded.

</dd> </dl> </dd> <dt>

*ActivationStatus* \[out\]
</dt> <dd>

The activation status returned can be one of the following values.

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

 

