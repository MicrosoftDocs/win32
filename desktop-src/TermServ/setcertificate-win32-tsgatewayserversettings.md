---
title: SetCertificate method of the Win32_TSGatewayServerSettings class
description: Sets the certificate hash for HTTPS binding on port 443 in IIS.
ms.assetid: b5f794bc-17b1-401a-92d8-c9bbe5d0d05f
ms.tgt_platform: multiple
keywords:
- SetCertificate method Remote Desktop Services
- SetCertificate method Remote Desktop Services , Win32_TSGatewayServerSettings class
- Win32_TSGatewayServerSettings class Remote Desktop Services , SetCertificate method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings.SetCertificate
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetCertificate method of the Win32\_TSGatewayServerSettings class

Sets the certificate hash for HTTPS binding on port 443 in IIS.

## Syntax


```mof
uint32 SetCertificate(
  [in] uint8 CertHash[]
);
```



## Parameters

<dl> <dt>

*CertHash* \[in\]
</dt> <dd>

Type: **uint8\[\]**

The new certificate hash.

</dd> </dl>

## Return value

Type: **uint32**

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

After the certificate hash has been set with this method, you must call the [**Configure**](configure-win32-tsgatewayserversettings.md) method to complete the configuration process.

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                        |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> </dl>

 

