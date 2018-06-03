---
title: Set method of the PS\_DhcpServerv4DnsSetting class
description: Sets how the DNS server should be updated by the DHCP server with client-related information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2388170b-9616-458d-97f9-2a365f1db9ac
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerv4DnsSetting class
- PS_DhcpServerv4DnsSetting class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4DnsSetting.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DhcpServerv4DnsSetting class

Sets how the DNS server should be updated by the DHCP server with client-related information.

## Syntax


```mof
uint32 Set(
  [in]  string                 ComputerName,
  [in]  boolean                NameProtection,
  [in]  boolean                UpdateDnsRRForOlderClients,
  [in]  boolean                DeleteDnsRROnLeaseExpiry,
  [in]  string                 DynamicUpdates,
  [in]  string                 IPAddress,
  [in]  string                 ScopeId,
  [in]  boolean                PassThru,
  [in]  string                 PolicyName,
  [in]  boolean                DisableDnsPtrRRUpdate,
  [in]  string                 DnsSuffix,
  [out] DhcpServerv4DnsSetting cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*NameProtection* \[in\]
</dt> <dd>

Enable/Disable name protection on the DHCP server. If Name protection is enabled and if there is an existing DNS record already by the same name, the DNS update for the client will fail instead of being overwritten.

</dd> <dt>

*UpdateDnsRRForOlderClients* \[in\]
</dt> <dd>

Enable/Disable DNS registration of A and PTR records for older clients which do not request DNS updates

</dd> <dt>

*DeleteDnsRROnLeaseExpiry* \[in\]
</dt> <dd>

Specifies if the DHCP server should delete the client's DNS resource records after the lease expires.Valid values are true, false. Can only be set if *DynamicUpdates* is set to Always or OnClientRequest.

</dd> <dt>

*DynamicUpdates* \[in\]
</dt> <dd>

Specifies the conditions under which to perform dynamic updates on the DNS server. Valid values are Always, Never, OnClientRequest. Always: The DHCP server will always perform dynamic DNS registration of A and PTR records for the clients. Never: DHCP will not perform any dynamic DNS registration. OnClientRequest: DHCP server will perform dynamic DNS registration of A and PTR records if the client has requested for the same in the DHCP client message.

<dt>

<span id="Always"></span><span id="always"></span><span id="ALWAYS"></span>

**Always** ("Always")


</dt> <dd></dd> <dt>

<span id="Never"></span><span id="never"></span><span id="NEVER"></span>

**Never** ("Never")


</dt> <dd></dd> <dt>

<span id="OnClientRequest"></span><span id="onclientrequest"></span><span id="ONCLIENTREQUEST"></span>

**OnClientRequest** ("OnClientRequest")


</dt> <dd></dd> </dl> </dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

IP address of the reservation for which the specified DNS update settings are to be set

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) for which the DNS update settings are to be set

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*PolicyName* \[in\]
</dt> <dd>

Specifies the policy for which DNS settings are to be modified.

**Windows Server 2012:** This parameter is supported beginning with Windows Server 2012 R2.

</dd> <dt>

*DisableDnsPtrRRUpdate* \[in\]
</dt> <dd>

If **True**, disables DNS dynamic updates for PTR records. Allowed only when the *ScopeID* or *PolicyName* parameters are specified. Not allowed if the *IPAddress* parameter is specified.

**Windows Server 2012:** This parameter is supported beginning with Windows Server 2012 R2.

</dd> <dt>

*DnsSuffix* \[in\]
</dt> <dd>

Contains guest domain for registering DHCP clients. Accepts domain names in the format as specified in RFC 1035. Allowed only when the *PolicyName* parameter is specified.

**Windows Server 2012:** This parameter is supported beginning with Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerv4DnsSetting**](dhcpserverv4dnssetting.md) object.

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

[**PS\_DhcpServerv4DnsSetting**](ps-dhcpserverv4dnssetting.md)
</dt> </dl>

 

 





