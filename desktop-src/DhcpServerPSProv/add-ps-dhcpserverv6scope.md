---
title: Add method of the PS\_DhcpServerv6Scope class
description: Adds an IPv6 scope to the DHCP server with the specified parameters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 958c0021-5b1c-49b1-9128-2453d4888a8c
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerv6Scope class
- PS_DhcpServerv6Scope class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Scope.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_DhcpServerv6Scope class

Adds an IPv6 scope to the DHCP server with the specified parameters.

## Syntax


```mof
uint32 Add(
  [in]  datetime          ValidLifeTime,
  [in]  string            ComputerName,
  [in]  string            Prefix,
  [in]  string            Name,
  [in]  string            Description,
  [in]  string            State,
  [in]  uint16            Preference = 0,
  [in]  datetime          PreferredLifetime,
  [in]  datetime          T1,
  [in]  datetime          T2,
  [in]  boolean           PassThru,
  [out] DhcpServerv6Scope cmdletOutput
);
```



## Parameters

<dl> <dt>

*ValidLifeTime* \[in\]
</dt> <dd>

The valid life time of the IPv6 address leased by the DHCP server. The default value for the *ValidLifeTime* is 12 days. The *ValidLifeTime* value should be equal to or greater than the *PreferredLifetime* parameter.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

The IPv6 prefix of the scope being added.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name associated with the scope.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description associated with scope.

</dd> <dt>

*State* \[in\]
</dt> <dd>

The state of the scope. Possible values are Enabled and Disabled

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="InActive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**InActive** ("InActive")


</dt> <dd></dd> </dl> </dd> <dt>

*Preference* \[in\]
</dt> <dd>

The value for the preference field to be used by the DHCP server while responding to clients in this subnet.

Range: 0 255

</dd> <dt>

*PreferredLifetime* \[in\]
</dt> <dd>

The preferred life time of the IPv6 address leased by the DHCP server. The default value for the preferred lifetime is 8 days. The *PreferredLifetime* should be less than or equal to the *ValidLifeTime* parameter.

</dd> <dt>

*T1* \[in\]
</dt> <dd>

Lease renewal time. Default value is 4 days. The *T1* value should be less than the *T2* and *PreferredLifetime* parameters.

</dd> <dt>

*T2* \[in\]
</dt> <dd>

Lease rebind time. Default value is 6.4 days. The *T2* value should be greater than the *T1* parameter and less than the *PreferredLifetime* parameter.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is added.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Scope**](dhcpserverv6scope.md) class.

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

[**PS\_DhcpServerv6Scope**](ps-dhcpserverv6scope.md)
</dt> </dl>

 

 





