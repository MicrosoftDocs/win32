---
title: Set method of the PS\_DhcpServerSetting class
description: Sets a server level configuration parameter for the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ac901c84-ca58-4af1-9b75-08355d046cba
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerSetting class
- PS_DhcpServerSetting class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerSetting.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DhcpServerSetting class

Sets a server level configuration parameter for the DHCP server.

## Syntax


```mof
uint32 Set(
  [in]  uint32            ConflictDetectionAttempts,
  [in]  string            NpsUnreachableAction,
  [in]  boolean           NapEnabled,
  [in]  string            ComputerName,
  [in]  boolean           ActivatePolicies,
  [in]  boolean           PassThru,
  [out] DhcpServerSetting cmdletOutput
);
```



## Parameters

<dl> <dt>

*ConflictDetectionAttempts* \[in\]
</dt> <dd>

Number of time DHCP server should attempt conflict detection before leasing an IP address. Default value is 0. Valid values are 0-5.

</dd> <dt>

*NpsUnreachableAction* \[in\]
</dt> <dd>

When NAP enabled, the default action that the DHCP server should perform if the NPS server is unreachable. Valid values are Full, Restricted, NoAccess.

<dt>

<span id="Full"></span><span id="full"></span><span id="FULL"></span>

**Full** ("Full")


</dt> <dd></dd> <dt>

<span id="Restricted"></span><span id="restricted"></span><span id="RESTRICTED"></span>

**Restricted** ("Restricted")


</dt> <dd></dd> <dt>

<span id="NoAccess"></span><span id="noaccess"></span><span id="NOACCESS"></span>

**NoAccess** ("NoAccess")


</dt> <dd></dd> </dl> </dd> <dt>

*NapEnabled* \[in\]
</dt> <dd>

Enable/Disable NAP (Network Access Policy) check on the server. If NAP is enabled, DHCP server uses the NPS server to perform a NAP check before leasing an IP address.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ActivatePolicies* \[in\]
</dt> <dd>

Enable/Disable enforcement of policies. Valid values are True, False.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerSetting**](dhcpserversetting.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerSetting**](ps-dhcpserversetting.md)
</dt> </dl>

 

 





