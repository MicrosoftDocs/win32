---
title: Get method of the PS\_DnsServerZone class
description: Lists the zones that exist on the specified DNS server.
audience: developer
ms.assetid: 43fbb5fc-1220-465f-82c7-067f7fc14d63
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerZone class
- PS_DnsServerZone class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerZone.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DnsServerZone class

Lists the zones that exist on the specified DNS server.

## Syntax


```mof
uint32 Get(
  [in]  string        Name[],
  [in]  string        ComputerName,
  [in]  string        VirtualizationInstance,
  [out] DnsServerZone cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone. If This parameter is not specified all the zones are listed

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

One or more embedded instances of the [**DnsServerZone**](dnsserverzone.md) class.

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

[**PS\_DnsServerZone**](ps-dnsserverzone.md)
</dt> </dl>

 

 





