---
title: Set method of the PS\_DnsServerResourceRecordAging class
description: Ages RRs under a node.
audience: developer
ms.assetid: '9cc13e79-67e2-4826-ac82-41f0060dfe14'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DnsServerResourceRecordAging class", "PS_DnsServerResourceRecordAging class, Set method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordAging.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DnsServerResourceRecordAging class

Ages RRs under a node.

## Syntax


```mof
uint32 Set(
  [in] string  ComputerName,
  [in] string  ZoneName,
  [in] string  NodeName,
  [in] boolean Recurse,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies name of the zone whose records need to be aged

</dd> <dt>

*NodeName* \[in\]
</dt> <dd>

Specifies a specific node or subtree in the zone. NodeName specifies the node or subtree in the zone using the following: @ for root zone or FQDN. The FQDN of a node (the name with a period (.) at the end). A single label for the name relative to the zone root.

</dd> <dt>

*Recurse* \[in\]
</dt> <dd>

Specifies if records of all the nodes under the specified zone need to be aged

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

[**PS\_DnsServerResourceRecordAging**](ps-dnsserverresourcerecordaging.md)
</dt> </dl>

 

 





