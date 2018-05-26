---
title: Add method of the Ps\_DnsServerClientSubnet class
description: Adds a client subnet record to the client subnet database on the DNS server.
audience: developer
ms.assetid: 649B3E41-1EFC-4B9C-97E8-1632DCCC3E4A
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, Ps_DnsServerClientSubnet class
- Ps_DnsServerClientSubnet class, Add method
topic_type:
- apiref
api_name:
- Ps_DnsServerClientSubnet.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the Ps\_DnsServerClientSubnet class

Adds a client subnet record to the client subnet database on the DNS server.

## Syntax


```mof
uint32 Add(
  [in]  string                Name,
  [in]  string                IPv4Subnet[],
  [in]  string                IPv6Subnet[],
  [in]  boolean               PassThru,
  [in]  string                ComputerName,
  [out] DnsServerClientSubnet cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the client subnet record.

</dd> <dt>

*IPv4Subnet* \[in\]
</dt> <dd>

The IPV4 subnet list for the record in Classless Inter-Domain Routing (CIDR) notation.

</dd> <dt>

*IPv6Subnet* \[in\]
</dt> <dd>

The IPV6 subnet list for the record in Classless Inter-Domain Routing (CIDR) notation.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the client subnet record in the *cmdletOutput* parameter; otherwise, **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of the remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, this parameter receives an embedded instance of the [**DnsServerClientSubnet**](dnsserverclientsubnet.md) object that represents the added subnet record.

</dd> </dl>

## Return value

If this operation succeeds, this method returns "0"; otherwise, it returns a WMI error code.

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

[**Ps\_DnsServerClientSubnet**](ps-dnsserverclientsubnet.md)
</dt> </dl>

 

 





