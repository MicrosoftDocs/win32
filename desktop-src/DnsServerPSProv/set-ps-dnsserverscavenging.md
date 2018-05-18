---
title: Set method of the PS\_DnsServerScavenging class
description: Sets scavenging settings on the Server.
audience: developer
ms.assetid: 'a280450e-9393-4095-a29b-fbf586b659e1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DnsServerScavenging class", "PS_DnsServerScavenging class, Set method"]
topic_type:
- apiref
api_name:
- PS_DnsServerScavenging.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DnsServerScavenging class

Sets scavenging settings on the Server.

## Syntax


```mof
uint32 Set(
  [in]  boolean             ApplyOnAllZones,
  [in]  string              ComputerName,
  [in]  boolean             ScavengingState,
  [in]  datetime            RefreshInterval,
  [in]  datetime            ScavengingInterval,
  [in]  datetime            NoRefreshInterval,
  [in]  boolean             PassThru,
  [out] DnsServerScavenging cmdletOutput
);
```



## Parameters

<dl> <dt>

*ApplyOnAllZones* \[in\]
</dt> <dd>

The server settings get applied on all zones

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*ScavengingState* \[in\]
</dt> <dd>

Enable Automatic scavenging of stale records. Determines whether the DNS scavenging feature is enabled by default on newly created zones. 0: Disables scavenging. This is the default setting. 1: Enables scavenging

</dd> <dt>

*RefreshInterval* \[in\]
</dt> <dd>

Sets a period of time that is allowed for dynamic updates to DNS records. This value is inherited automatically by zones on the server. To change the default, enter a value in the range of 0x1-0xFFFFFFFF. The default value from the server is 0xA8. Range = 0, 8760

</dd> <dt>

*ScavengingInterval* \[in\]
</dt> <dd>

Determines whether the scavenging feature for the DNS server is enabled, and sets the number of hours (0x0-0xFFFFFFFF) between scavenging cycles. The default setting is 0x0, which disables scavenging for the DNS server. A setting greater than 0x0 enables scavenging for the server and sets the number of hours between scavenging cycles.

Range = 0, 8760

</dd> <dt>

*NoRefreshInterval* \[in\]
</dt> <dd>

Sets a period of time in which no refreshes are accepted for dynamically updated records. This value is inherited automatically by zones on the server. To change the default, enter a value in the range of 0x1-0xFFFFFFFF. The default value from the server is 0xA8. Range = 0, 8760

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerScavenging**](ps-dnsserverscavenging.md)
</dt> </dl>

 

 





