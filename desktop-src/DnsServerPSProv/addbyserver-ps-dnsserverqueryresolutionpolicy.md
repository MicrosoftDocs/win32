---
title: AddByServer method of the PS\_DnsServerQueryResolutionPolicy class
description: Adds a query resolution policy to the DNS server by server.
audience: developer
ms.assetid: f2fdc8b1-451d-4802-8b50-93832ab190d5
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByServer method
- AddByServer method, PS_DnsServerQueryResolutionPolicy class
- PS_DnsServerQueryResolutionPolicy class, AddByServer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByServer method of the PS\_DnsServerQueryResolutionPolicy class

Adds a query resolution policy to the DNS server by server.

## Syntax


```mof
uint32 AddByServer(
  [in]  boolean         PassThru,
  [in]  string          ComputerName,
  [in]  string          Name,
  [in]  string          Fqdn,
  [in]  string          ClientSubnet,
  [in]  string          TimeOfDay,
  [in]  string          TransportProtocol,
  [in]  string          InternetProtocol,
  [in]  string          Action,
  [in]  boolean         ApplyOnRecursion,
  [in]  string          ServerInterfaceIP,
  [in]  string          QType,
  [in]  uint32          ProcessingOrder,
  [in]  string          Condition,
  [in]  string          RecursionScope,
  [in]  boolean         Disable,
  [out] DnsServerPolicy cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the policy.

</dd> <dt>

*Fqdn* \[in\]
</dt> <dd>

The fully-qualified domain name.

</dd> <dt>

*ClientSubnet* \[in\]
</dt> <dd>

Client subnet record name.

</dd> <dt>

*TimeOfDay* \[in\]
</dt> <dd>

Time of day criteria.

</dd> <dt>

*TransportProtocol* \[in\]
</dt> <dd>

Transport protocol criteria.

</dd> <dt>

*InternetProtocol* \[in\]
</dt> <dd>

Internet Protocol criteria

</dd> <dt>

*Action* \[in\]
</dt> <dd>

Action taken if policy is matched

</dd> <dt>

*ApplyOnRecursion* \[in\]
</dt> <dd>

**true** to apply on recursion; otherwise, **false.**

</dd> <dt>

*ServerInterfaceIP* \[in\]
</dt> <dd>

The server interface.

</dd> <dt>

*QType* \[in\]
</dt> <dd>

Query type.

</dd> <dt>

*ProcessingOrder* \[in\]
</dt> <dd>

The order in which the query will be processed.

</dd> <dt>

*Condition* \[in\]
</dt> <dd>

The condition of the policy.

And

Or

</dd> <dt>

*RecursionScope* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Disable* \[in\]
</dt> <dd>

**true** to disable; otherwise **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**DnsServerPolicy**](dnsserverpolicy.md). This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerQueryResolutionPolicy**](ps-dnsserverqueryresolutionpolicy.md)
</dt> </dl>

 

 





