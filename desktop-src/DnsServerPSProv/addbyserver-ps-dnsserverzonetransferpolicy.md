---
title: AddByServer method of the PS\_DnsServerZoneTransferPolicy class
description: Adds a new zone transfer policy by server.
audience: developer
ms.assetid: 7903bab6-790c-4097-a846-f1ef1da2ea4b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByServer method
- AddByServer method, PS_DnsServerZoneTransferPolicy class
- PS_DnsServerZoneTransferPolicy class, AddByServer method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransferPolicy.AddByServer
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByServer method of the PS\_DnsServerZoneTransferPolicy class

Adds a new zone transfer policy by server.

## Syntax


```mof
uint32 AddByServer(
  [in]  string          ComputerName,
  [in]  boolean         PassThru,
  [in]  string          Action,
  [in]  string          ClientSubnet,
  [in]  string          Condition,
  [in]  string          InternetProtocol,
  [in]  boolean         Disable,
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

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*Action* \[in\]
</dt> <dd>

Action taken if policy is matched.

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

Internet Protocol criteria

</dd> <dt>

*Disable* \[in\]
</dt> <dd>

**true** to disable; otherwise **false**.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy.

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

time of day criteria.

</dd> <dt>

*TransportProtocol* \[in\]
</dt> <dd>

transport protocol criteria.

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

 

 





