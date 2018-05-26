---
title: Set method of the PS\_DhcpServerv6DnsSetting class
description: Configures how the DNS server should be updated by the DHCP server with client-related information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 87edf126-b4a4-4af2-84e0-8e54911daa04
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerv6DnsSetting class
- PS_DhcpServerv6DnsSetting class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6DnsSetting.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DhcpServerv6DnsSetting class

Configures how the DNS server should be updated by the DHCP server with client-related information.

## Syntax


```mof
uint32 Set(
  [in]  string                 ComputerName,
  [in]  boolean                NameProtection,
  [in]  boolean                DeleteDnsRROnLeaseExpiry,
  [in]  string                 DynamicUpdates,
  [in]  string                 IPAddress,
  [in]  string                 Prefix,
  [in]  boolean                PassThru,
  [out] DhcpServerv6DnsSetting cmdletOutput
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

Enables or disables name protection on the DHCP server. If Name protection is enabled and if there is an existing DNS record already by the same name, the DNS update for the client will fail instead of being overwritten.

</dd> <dt>

*DeleteDnsRROnLeaseExpiry* \[in\]
</dt> <dd>

Specifies if the DHCP server should delete the client's DNS resource records after the lease expires. Valid values are true, false. Can only be set if *DynamicUpdates* is set to Always or OnClientRequest.

</dd> <dt>

*DynamicUpdates* \[in\]
</dt> <dd>

Specifies the conditions under which to perform dynamic updates on the DNS server. Valid values are Always, Never, OnClientRequest. Always - DHCP server will always perform dynamic DNS registration of A and PTR records for the clients. Never - DHCP will not perform any dynamic DNS registration OnClientRequest - DHCP server will perform dynamic DNS registration of A and PTR records if the client has requested for the same in the DHCP client message.

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

IP Address of the reservation on which the DNS update behavior is to be configured.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

Subnet prefix of the IPv6 scope on which the DNS update behavior is to be configured.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6DnsSetting**](dhcpserverv6dnssetting.md) class.

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

[**PS\_DhcpServerv6DnsSetting**](ps-dhcpserverv6dnssetting.md)
</dt> </dl>

 

 





