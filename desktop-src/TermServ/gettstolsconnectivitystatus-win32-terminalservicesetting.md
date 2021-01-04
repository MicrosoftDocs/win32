---
title: GetTStoLSConnectivityStatus method of the Win32_TerminalServiceSetting class
description: Determines the connectivity status between Remote Desktop Services and a license server.
ms.assetid: 11fc5865-47e8-4be8-a526-53e29f72d0a4
ms.tgt_platform: multiple
keywords:
- GetTStoLSConnectivityStatus method Remote Desktop Services
- GetTStoLSConnectivityStatus method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , GetTStoLSConnectivityStatus method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.GetTStoLSConnectivityStatus
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetTStoLSConnectivityStatus method of the Win32\_TerminalServiceSetting class

Determines the connectivity status between Remote Desktop Services and a license server.

## Syntax


```mof
uint32 GetTStoLSConnectivityStatus(
  [in]  string ServerName,
  [out] uint32 TStoLSConnectivityStatus
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

The name of the license server to check the connectivity status of.

</dd> <dt>

*TStoLSConnectivityStatus* \[out\]
</dt> <dd>

A value that indicates the connectivity status of the license server. This can be one of the following values.

<dt>

<span id="LS_CONNECTABLE_UNKNOWN"></span><span id="ls_connectable_unknown"></span>

<span id="LS_CONNECTABLE_UNKNOWN"></span><span id="ls_connectable_unknown"></span>**LS\_CONNECTABLE\_UNKNOWN** (0)


</dt> <dd>

The connectivity status cannot be determined.

</dd> <dt>

<span id="LS_CONNECTABLE_VALID_WS08R2"></span><span id="ls_connectable_valid_ws08r2"></span>

<span id="LS_CONNECTABLE_VALID_WS08R2"></span><span id="ls_connectable_valid_ws08r2"></span>**LS\_CONNECTABLE\_VALID\_WS08R2** (1)


</dt> <dd>

Remote Desktop Services can connect to the Windows Server 2008 R2 license server.

</dd> <dt>

<span id="LS_CONNECTABLE_VALID_WS08"></span><span id="ls_connectable_valid_ws08"></span>

<span id="LS_CONNECTABLE_VALID_WS08"></span><span id="ls_connectable_valid_ws08"></span>**LS\_CONNECTABLE\_VALID\_WS08** (2)


</dt> <dd>

Remote Desktop Services can connect to the Windows Server 2008 license server.

</dd> <dt>

<span id="LS_CONNECTABLE_BETA_RTM_MISMATCH"></span><span id="ls_connectable_beta_rtm_mismatch"></span>

<span id="LS_CONNECTABLE_BETA_RTM_MISMATCH"></span><span id="ls_connectable_beta_rtm_mismatch"></span>**LS\_CONNECTABLE\_BETA\_RTM\_MISMATCH** (3)


</dt> <dd>

Remote Desktop Services can connect to the license server, but one of the servers is running a beta version of the operating system.

</dd> <dt>

<span id="LS_CONNECTABLE_LOWER_VERSION"></span><span id="ls_connectable_lower_version"></span>

<span id="LS_CONNECTABLE_LOWER_VERSION"></span><span id="ls_connectable_lower_version"></span>**LS\_CONNECTABLE\_LOWER\_VERSION** (4)


</dt> <dd>

Remote Desktop Services can connect to the license server, but there is an incompatibility between the license server and the Remote Desktop Services host server.

</dd> <dt>

<span id="LS_CONNECTABLE_NOT_IN_TSCGROUP"></span><span id="ls_connectable_not_in_tscgroup"></span>

<span id="LS_CONNECTABLE_NOT_IN_TSCGROUP"></span><span id="ls_connectable_not_in_tscgroup"></span>**LS\_CONNECTABLE\_NOT\_IN\_TSCGROUP** (5)


</dt> <dd>

Security group policy is enabled in license server, but Remote Desktop Services is not a part of the group policy.

</dd> <dt>

<span id="LS_NOT_CONNECTABLE"></span><span id="ls_not_connectable"></span>

<span id="LS_NOT_CONNECTABLE"></span><span id="ls_not_connectable"></span>**LS\_NOT\_CONNECTABLE** (6)


</dt> <dd>

Remote Desktop Services cannot connect to the license server.

</dd> <dt>

<span id="LS_CONNECTABLE_UNKNOWN_VALIDITY"></span><span id="ls_connectable_unknown_validity"></span>

<span id="LS_CONNECTABLE_UNKNOWN_VALIDITY"></span><span id="ls_connectable_unknown_validity"></span>**LS\_CONNECTABLE\_UNKNOWN\_VALIDITY** (7)


</dt> <dd>

The license server can be connected to, but the validity of the connection cannot be determined.

</dd> <dt>

<span id="LS_CONNECTABLE_BUT_ACCESS_DENIED"></span><span id="ls_connectable_but_access_denied"></span>

<span id="LS_CONNECTABLE_BUT_ACCESS_DENIED"></span><span id="ls_connectable_but_access_denied"></span>**LS\_CONNECTABLE\_BUT\_ACCESS\_DENIED** (8)


</dt> <dd>

Remote Desktop Services can connect to the license server, but the user account does not have administrator privileges on the license server.

</dd> <dt>

<span id="LS_CONNECTABLE_VALID_WS08R2_VDI"></span><span id="ls_connectable_valid_ws08r2_vdi"></span>

<span id="LS_CONNECTABLE_VALID_WS08R2_VDI"></span><span id="ls_connectable_valid_ws08r2_vdi"></span>**LS\_CONNECTABLE\_VALID\_WS08R2\_VDI** (9)


</dt> <dd>

Remote Desktop Services can connect to the Windows Server 2008 R2 Virtual Desktop Infrastructure (VDI) server.

**Windows Server 2008 R2:** This value is not supported before Windows Server 2012.

</dd> <dt>

<span id="LS_CONNECTABLE_FEATURE_NOT_SUPPORTED"></span><span id="ls_connectable_feature_not_supported"></span>

<span id="LS_CONNECTABLE_FEATURE_NOT_SUPPORTED"></span><span id="ls_connectable_feature_not_supported"></span>**LS\_CONNECTABLE\_FEATURE\_NOT\_SUPPORTED** (10)


</dt> <dd>

The feature is not supported.

**Windows Server 2008 R2 and Windows Server 2008 R2 with SP1:** This value is not supported before Windows Server 2012.

</dd> <dt>

<span id="LS_CONNECTABLE_VALID_LS"></span><span id="ls_connectable_valid_ls"></span>

<span id="LS_CONNECTABLE_VALID_LS"></span><span id="ls_connectable_valid_ls"></span>**LS\_CONNECTABLE\_VALID\_LS** (11)


</dt> <dd>

The license server is valid.

**Windows Server 2008 R2 and Windows Server 2008 R2 with SP1:** This value is not supported before Windows Server 2012.

</dd> </dl> </dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md)
</dt> </dl>

 

 





