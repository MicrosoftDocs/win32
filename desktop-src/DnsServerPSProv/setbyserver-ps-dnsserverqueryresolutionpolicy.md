---
title: SetByServer method of the PS\_DnsServerQueryResolutionPolicy class
description: Sets the DNS server name resolution policy by server.
audience: developer
ms.assetid: 409da2c8-9d5d-436c-a992-0d18641a292e
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByServer method
- SetByServer method, PS_DnsServerQueryResolutionPolicy class
- PS_DnsServerQueryResolutionPolicy class, SetByServer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByServer method of the PS\_DnsServerQueryResolutionPolicy class

Sets the DNS server name resolution policy by server.

## Syntax


```mof
uint32 SetByServer(
  [in]  boolean         PassThru,
  [in]  string          ComputerName,
  [in]  string          Name,
  [in]  string          TransportProtocol,
  [in]  string          TimeOfDay,
  [in]  string          RecursionScope,
  [in]  string          ServerInterfaceIP,
  [in]  string          QType,
  [in]  uint32          ProcessingOrder,
  [in]  string          ClientSubnet,
  [in]  string          Condition,
  [in]  string          InternetProtocol,
  [in]  string          Fqdn,
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

Optional DNS server name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy to set.

</dd> <dt>

*TransportProtocol* \[in\]
</dt> <dd>

Transport protocol criteria.

</dd> <dt>

*TimeOfDay* \[in\]
</dt> <dd>

Time of day criteria.

</dd> <dt>

*RecursionScope* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ServerInterfaceIP* \[in\]
</dt> <dd>

The server interface.

</dd> <dt>

*QType* \[in\]
</dt> <dd>

The query type.

</dd> <dt>

*ProcessingOrder* \[in\]
</dt> <dd>

The order in which the query will be processed.

</dd> <dt>

*ClientSubnet* \[in\]
</dt> <dd>

Client subnet record name.

</dd> <dt>

*Condition* \[in\]
</dt> <dd>

The condition of the policy.

And

Or

</dd> <dt>

*InternetProtocol* \[in\]
</dt> <dd>

Internet Protocol criteria.

</dd> <dt>

*Fqdn* \[in\]
</dt> <dd>

Fully-qualified domain name.

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

 

 





