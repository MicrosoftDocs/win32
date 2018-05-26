---
title: SetByServer method of the PS\_DnsServerZoneTransferPolicy class
description: Edits a zone transfer policy by server.
audience: developer
ms.assetid: 283deab7-c468-43b8-82fa-4f32485d253b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByServer method
- SetByServer method, PS_DnsServerZoneTransferPolicy class
- PS_DnsServerZoneTransferPolicy class, SetByServer method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransferPolicy.SetByServer
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByServer method of the PS\_DnsServerZoneTransferPolicy class

Edits a zone transfer policy by server

## Syntax


```mof
uint32 SetByServer(
  [in]  boolean         PassThru,
  [in]  string          ComputerName,
  [in]  string          ClientSubnet,
  [in]  string          Condition,
  [in]  string          InternetProtocol,
  [in]  string          Name,
  [in]  uint32          ProcessingOrder,
  [in]  string          ServerInterfaceIP,
  [in]  string          TimeOfDay,
  [in]  string          TransportProtocol,
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

*Name* \[in\]
</dt> <dd>

The name of the policy.

</dd> <dt>

*ProcessingOrder* \[in\]
</dt> <dd>

The order in which the query will be processed.

</dd> <dt>

*ServerInterfaceIP* \[in\]
</dt> <dd>

The server interface.

</dd> <dt>

*TimeOfDay* \[in\]
</dt> <dd>

Time of day criteria.

</dd> <dt>

*TransportProtocol* \[in\]
</dt> <dd>

Transport protocol criteria.

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

[**PS\_DnsServerZoneTransferPolicy**](ps-dnsserverzonetransferpolicy.md)
</dt> </dl>

 

 





