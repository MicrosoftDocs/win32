---
title: CanAccessLicenseServer method of the Win32_TerminalServiceSetting class
description: CanAccessLicenseServer is no longer available.
ms.assetid: b09fa901-8ae1-431e-8d97-27ee84a84779
ms.tgt_platform: multiple
keywords:
- CanAccessLicenseServer method Remote Desktop Services
- CanAccessLicenseServer method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , CanAccessLicenseServer method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.CanAccessLicenseServer
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CanAccessLicenseServer method of the Win32\_TerminalServiceSetting class

\[**CanAccessLicenseServer** is no longer available for use as of Windows Server 2008 R2.\]

**Windows Server 2008:  **

Determines whether the Remote Desktop Session Host (RD Session Host) server is allowed to request Remote Desktop Services client access licenses (RDS CALs) from a Remote Desktop license server based on the following:

-   The "license server security group" group policy setting on the Remote Desktop license server.
-   Membership in the Terminal Server Computers local group on the license server.

## Syntax


```mof
uint32 CanAccessLicenseServer(
  [in]  string ServerName,
  [out] uint32 AccessAllowed
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

The name of the Remote Desktop license server.

</dd> <dt>

*AccessAllowed* \[out\]
</dt> <dd>

Whether the RD Session Host server is allowed to request RDS CALs from the license server.

<dt>

0
</dt> <dd>

The request is allowed.

</dd> <dt>

1
</dt> <dd>

The request is not allowed.

</dd> </dl> </dd> </dl>

## Return value

Returns **S\_OK** if the RD Session Host server has access to the license server. Returns **S\_FALSE** if the RD Session Host server does not have access to the license server.

## Remarks

The "license server security group" policy setting allows you to specify the RD Session Host servers that are permitted to contact the license server to obtain RDS CALs. If the policy setting is enabled on the license server, the license server will only respond to RDS CAL requests from RD Session Host servers whose computer accounts are members of the Terminal Server Computers local group on the license server.

To connect to the \\root\\CIMV2\\TerminalServices namespace, the authentication level must include packet privacy. For C/C++ calls, this is an authentication level of **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**. For Visual Basic and scripting calls, this is an authentication level of **WbemAuthenticationLevelPktPrivacy** or "pktPrivacy", with a value of 6. The following Visual Basic Scripting Edition (VBScript) example shows how to connect to a remote computer with packet privacy.


```VB
strComputer = "RemoteServer1" 
Set objServices = GetObject( _
    "winmgmts:{authenticationLevel=pktPrivacy}!Root/CIMv2/TerminalServices")
```



Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| End of client support<br/>    | None supported<br/>                                                               |
| End of server support<br/>    | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md)
</dt> </dl>

 

