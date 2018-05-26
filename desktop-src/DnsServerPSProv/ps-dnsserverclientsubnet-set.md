---
title: Set method of the Ps\_DnsServerClientSubnet class
description: Updates a client subnet record in the client subnet database on the DNS server.
audience: developer
ms.assetid: A5326F48-37D7-49F4-A43F-FFA4E3D6E249
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, Ps_DnsServerClientSubnet class
- Ps_DnsServerClientSubnet class, Set method
topic_type:
- apiref
api_name:
- Ps_DnsServerClientSubnet.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the Ps\_DnsServerClientSubnet class

Updates a client subnet record in the client subnet database on the DNS server.

## Syntax


```mof
uint32 Set(
  [in]  string                Name,
  [in]  string                IPv4Subnet[],
  [in]  string                IPv6Subnet[],
  [in]  string                Action,
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

*Action* \[in\]
</dt> <dd>

The action to perform on the record during the update operation.

The possible values are:

<dt>

Add
</dt> <dd>

Appended the update information to the record.

</dd> <dt>

Remove
</dt> <dd>

Removed the update information from the record.

</dd> <dt>

Reset
</dt> <dd>

Replaced the client subnet record with the update information.

</dd> </dl> </dd> <dt>

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

When this method returns, this parameter receives an embedded instance of the [**DnsServerClientSubnet**](dnsserverclientsubnet.md) object that represents the updated subnet record.

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

 

 





