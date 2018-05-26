---
title: Get method of the PS\_DnsServerZoneDelegation class
description: Retrieves the delegations of the specified DNS server zone.
audience: developer
ms.assetid: 201e57d4-0dbf-4bcb-8465-b2fa61217175
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerZoneDelegation class
- PS_DnsServerZoneDelegation class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneDelegation.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DnsServerZoneDelegation class

Retrieves the delegations of the specified DNS server zone.

## Syntax


```mof
uint32 Get(
  [in]  string                  ChildZoneName,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerZoneDelegation cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ChildZoneName* \[in\]
</dt> <dd>

If child name is not specified retrieve all the children of the parent

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the Parent

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerZoneDelegation**](dnsserverzonedelegation.md) class.

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

[**PS\_DnsServerZoneDelegation**](ps-dnsserverzonedelegation.md)
</dt> </dl>

 

 





