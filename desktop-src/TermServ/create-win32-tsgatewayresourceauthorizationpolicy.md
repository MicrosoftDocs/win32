---
title: Create method of the Win32_TSGatewayResourceAuthorizationPolicy class
description: Creates a Remote Desktop resource authorization policy (RD \ 160;RAP).
ms.assetid: 3301a543-cdf9-4528-a29e-691054ef81c9
ms.tgt_platform: multiple
keywords:
- Create method Remote Desktop Services
- Create method Remote Desktop Services , Win32_TSGatewayResourceAuthorizationPolicy class
- Win32_TSGatewayResourceAuthorizationPolicy class Remote Desktop Services , Create method
topic_type:
- apiref
api_name:
- Win32_TSGatewayResourceAuthorizationPolicy.Create
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Create method of the Win32\_TSGatewayResourceAuthorizationPolicy class

Creates a Remote Desktop resource authorization policy (RD RAP).

## Syntax


```mof
uint32 Create(
  [in] string  Name,
  [in] string  Description,
  [in] boolean Enabled,
  [in] string  ResourceGroupType,
  [in] string  ResourceGroupName,
  [in] string  UserGroupNames,
  [in] string  ProtocolNames,
  [in] string  PortNumbers
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the RD RAP.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description of the RD RAP.

</dd> <dt>

*Enabled* \[in\]
</dt> <dd>

Indicates whether the RD RAP is to be enabled.

</dd> <dt>

*ResourceGroupType* \[in\]
</dt> <dd>

Resource group type.

<dt>

"RG"
</dt> <dd>

Resource group.

</dd> <dt>

"CG"
</dt> <dd>

Computer group, as stored in Active Directory Domain Services.

</dd> <dt>

"ALL"
</dt> <dd>

All resources.

</dd> </dl> </dd> <dt>

*ResourceGroupName* \[in\]
</dt> <dd>

Resource group name.

</dd> <dt>

*UserGroupNames* \[in\]
</dt> <dd>

Semicolon-separated list of user group names. If the user belongs to any of these user groups, access will be permitted. User group names should be of the format *Domain\\UserGroupName*.

</dd> <dt>

*ProtocolNames* \[in\]
</dt> <dd>

Semicolon-separated list of protocol names that are enabled for this policy. Names must match the return of the [**GetProtocolName**](getprotocolname-win32-tsgatewayserversettings.md) method of the [**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md) class.

</dd> <dt>

*PortNumbers* \[in\]
</dt> <dd>

Semicolon-separated list of port numbers that are enabled for this policy. To allow any port number, set "\*".

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayResourceAuthorizationPolicy**](win32-tsgatewayresourceauthorizationpolicy.md)
</dt> </dl>

 

