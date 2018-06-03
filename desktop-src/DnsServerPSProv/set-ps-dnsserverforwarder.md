---
title: Set method of the PS\_DnsServerForwarder class
description: Selects or resets IP addresses to which the DNS server forwards DNS queries when it cannot solve them locally.
audience: developer
ms.assetid: 9346d645-33fc-48e6-b7ea-12b78b823a60
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerForwarder class
- PS_DnsServerForwarder class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerForwarder.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DnsServerForwarder class

Selects or resets IP addresses to which the DNS server forwards DNS queries when it cannot solve them locally.

## Syntax


```mof
uint32 Set(
  [in]  string             IPAddress[],
  [in]  string             ComputerName,
  [in]  boolean            UseRootHint,
  [in]  uint32             Timeout,
  [in]  boolean            EnableReordering,
  [in]  boolean            PassThru,
  [out] DnsServerForwarder cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

Specifies the forwarders in the order they need to be configured.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*UseRootHint* \[in\]
</dt> <dd>

If the *UseRootHint* parameter is used, the DNS server does not perform its own iterative queries. This means the DNS server forwards unresolved queries only to the DNS servers in the list and does not try iterative queries if the forwarders do not resolve it. It is more efficient to set one IP address as a forwarder for a DNS server. This cmdlet can be used for internal servers in a network to forward their unresolved queries to one DNS server that has an external connection.

</dd> <dt>

*Timeout* \[in\]
</dt> <dd>

Sets the number of seconds that the DNS server waits for a response from the forwarder. By default, this value is 5 seconds. Range = 0 to 15.

</dd> <dt>

*EnableReordering* \[in\]
</dt> <dd>

Enables or Disables the ability of the DNS Server to reorder Forwarders dynamically.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

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

[**PS\_DnsServerForwarder**](ps-dnsserverforwarder.md)
</dt> </dl>

 

 





