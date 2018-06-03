---
title: Set method of the PS\_DnsServerRecursion class
description: Sets DNS Server Recursion settings.
audience: developer
ms.assetid: 033d64fc-8cbb-459d-a103-c9e7110780a0
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerRecursion class
- PS_DnsServerRecursion class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerRecursion.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DnsServerRecursion class

Sets DNS Server Recursion settings.

## Syntax


```mof
uint32 Set(
  [in]  string             ComputerName,
  [in]  uint32             AdditionalTimeout,
  [in]  uint32             RetryInterval,
  [in]  uint32             Timeout,
  [in]  boolean            Enable,
  [in]  boolean            PassThru,
  [in]  boolean            SecureResponse,
  [out] DnsServerRecursion cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*AdditionalTimeout* \[in\]
</dt> <dd>

The time interval in seconds for which the DNS server waits while recursing to obtain resource records for use in the additional section of DNS responses from a remote DNS server. The value SHOULD be limited to the range 0x00000000 to 0x0000000F, inclusive, but it MAY be any value. The default value SHOULD be 0x00000004, and the value zero SHOULD be treated as a flag value for the default, but it MAY be allowed and treated literally. Range = 0, 15

</dd> <dt>

*RetryInterval* \[in\]
</dt> <dd>

Elapsed seconds before retrying a recursive look up. If the property is undefined or zero, retries are made after three seconds. Users are discouraged from altering this property. There are certain situations when the property should be changed. one example is when the DNS Server contacts remote servers over a slow link, and the DNS Server is retrying before receiving response from the remote DNS. In this case, raising the time out to be slightly longer than the observed response time from the remote DNS would be reasonable. Range = 1, 15

</dd> <dt>

*Timeout* \[in\]
</dt> <dd>

Determines the number of seconds, 0x1-0xFFFFFFFF, a DNS server waits before discontinuing attempts to contact a remote server. The settings range from 0x1 through 0xFFFFFFFF. The default setting is 0xF, 15 seconds. This value should be increased when recursion occurs over a slow WAN link. Range = 1, 15

</dd> <dt>

*Enable* \[in\]
</dt> <dd>

Enables or Disables recursion

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*SecureResponse* \[in\]
</dt> <dd>

Indicates if the DNS server SHOULD screen DNS records received in remote query responses against the zone of authority for the remote server to prevent cache pollution.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

DNSServerRecursionSettings uint32 RecursionRetry. //Elapsed seconds before retrying a recursive look up. If the property is undefined or zero, retries are made after three seconds. Users are discouraged from altering this property. There are certain situations when the property should be changed. one example is when the DNS Server contacts remote servers over a slow link, and the DNS Server is retrying before receiving response from the remote DNS. In this case, raising the time out to be slightly longer than the observed response time from the remote DNS would be reasonable uint32 RecursionTimeout. //Elapsed seconds before the DNS Server gives up recursive query. If the property is undefined or zero, the DNS Server gives up after 15 seconds. In general, the 15-second time out is sufficient to allow any outstanding response to get back to the DNS Server. Users are discouraged from altering this property. One scenario where the property should be changed is when the DNS Server contacts remote servers over a slow link, and the DNS Server is observed rejecting queries (with SERVER\_FAILURE) before responses are received. Client resolvers also retry queries, so careful investigation is required to determine whether remote responses are actually associated with the query that timed out. In this case, raising the time out value to be slightly longer than the observed response time from the remote DNS would be reasonable. boolean NoRecursion. //Indicates whether the DNS Server performs recursive look ups. TRUE indicates recursive look ups are not performed. dnsServerRecursion

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerRecursion**](ps-dnsserverrecursion.md)
</dt> </dl>

 

 





