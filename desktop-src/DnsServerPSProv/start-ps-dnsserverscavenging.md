---
title: Start method of the PS\_DnsServerScavenging class
description: Notifies a DNS server to attempt an immediate search for stale resource records in a specified DNS server.
audience: developer
ms.assetid: 'bafd41fd-8ff3-4864-8b1b-1230301efd54'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Start method", "Start method, PS_DnsServerScavenging class", "PS_DnsServerScavenging class, Start method"]
topic_type:
- apiref
api_name:
- PS_DnsServerScavenging.Start
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Start method of the PS\_DnsServerScavenging class

Notifies a DNS server to attempt an immediate search for stale resource records in a specified DNS server.

## Syntax


```mof
uint32 Start(
  [in] string  ComputerName,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default is **false**.

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

 

 





