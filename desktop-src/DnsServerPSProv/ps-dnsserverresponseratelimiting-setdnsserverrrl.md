---
title: SetDnsServerRRL method of the PS\_DnsServerResponseRateLimiting class
description: Sets the response rate limiting on a DNS server.
audience: developer
ms.assetid: 5f7b8ea4-f140-463d-ac8c-1d81fdd35932
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetDnsServerRRL method
- SetDnsServerRRL method, PS_DnsServerResponseRateLimiting class
- PS_DnsServerResponseRateLimiting class, SetDnsServerRRL method
topic_type:
- apiref
api_name:
- PS_DnsServerResponseRateLimiting.SetDnsServerRRL
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetDnsServerRRL method of the PS\_DnsServerResponseRateLimiting class

Sets the response rate limiting on a DNS server.

## Syntax


```mof
uint32 SetDnsServerRRL(
  [in]  uint32                        ResponsesPerSec,
  [in]  uint32                        ErrorsPerSec,
  [in]  uint32                        WindowInSec,
  [in]  uint32                        IPv4PrefixLength,
  [in]  uint32                        IPv6PrefixLength,
  [in]  uint32                        LeakRate,
  [in]  boolean                       ResetToDefault,
  [in]  uint32                        TruncateRate,
  [in]  uint32                        MaximumResponsesPerWindow,
  [in]  string                        Mode,
  [in]  string                        ComputerName,
  [in]  boolean                       PassThru,
  [in]  boolean                       Force,
  [out] DnsServerResponseRateLimiting cmdletOutput
);
```



## Parameters

<dl> <dt>

*ResponsesPerSec* \[in\]
</dt> <dd>

The maximum number of times that a requestor will be told the same answer within a one-second interval.

</dd> <dt>

*ErrorsPerSec* \[in\]
</dt> <dd>

This is similar to RESPONSES-PER-SECOND but applies only to the REFUSED, FORMERR and SERVFAIL response codes.

</dd> <dt>

*WindowInSec* \[in\]
</dt> <dd>

This is the period (in seconds) over which rates are measured and averaged for RRL. RRL will be applied if queries from same subnet, resulting in same response occur more frequently than expected in a specified time window. The default value is 5.

</dd> <dt>

*IPv4PrefixLength* \[in\]
</dt> <dd>

Requestor IP (version 4) addresses are grouped into buckets of size (32 - IPV4-PREFIX-LENGTH) ^ 2.

</dd> <dt>

*IPv6PrefixLength* \[in\]
</dt> <dd>

Requestor IP (version 6) addresses are grouped similarly to IP (version 4) addresses.

</dd> <dt>

*LeakRate* \[in\]
</dt> <dd>

When a query would be dropped due to rate limiting, the server randomly responds anyway once per LEAK-RATE queries. This gives the victim whose IP address is being forged some chance of getting an answer even during a flood of forgeries. LEAK-RATE should be from 2 to 10 and should approximate the real victim's retry count on a legitimate query. If LEAK-RATE is set to zero then this behavior is disabled.

</dd> <dt>

*ResetToDefault* \[in\]
</dt> <dd>

This parameter sets all the RRL settings to their default values.

</dd> <dt>

*TruncateRate* \[in\]
</dt> <dd>

When a query would be dropped due to rate limiting, the server randomly send back a truncated response instead once per TC-RATE queries. This tells a victim whose address is being forged to retry using TCP. It's recommended that TC-RATE be set lower than LEAK-RATE. If TC-RATE is set to zero then this behavior is disabled.

</dd> <dt>

*MaximumResponsesPerWindow* \[in\]
</dt> <dd>

The maximum responses that will be sent for a subnet-domain tuple in a window. This will be useful in putting an upper limit on responses in cases where leak rates are leading to reflection attack

</dd> <dt>

*Mode* \[in\]
</dt> <dd>

The mode of operation.

The possible values are.

"LogOnly"

"Enable" (default)

"Disable"

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default value is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**DnsServerResponseRateLimiting**](dnsserverresponseratelimiting.md) object that contains the RRL for a DNS server.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResponseRateLimiting**](ps-dnsserverresponseratelimiting.md)
</dt> </dl>

 

 





