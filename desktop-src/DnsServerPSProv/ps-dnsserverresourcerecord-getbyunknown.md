---
title: GetByUnknown method of the PS\_DnsServerResourceRecord class
description: Retrieves the resource record from a specified zone.
audience: developer
ms.assetid: a016bf03-9a7e-492b-85ef-c7464d0fdcda
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByUnknown method
- GetByUnknown method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, GetByUnknown method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.GetByUnknown
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetByUnknown method of the PS\_DnsServerResourceRecord class

Retrieves the resource record from a specified zone.

## Syntax


```mof
uint32 GetByUnknown(
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  string                  ZoneName,
  [in]  boolean                 Node,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [in]  uint16                  Type,
  [out] DnsServerResourceRecord cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the record to be retrieved.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*Node* \[in\]
</dt> <dd>

If specified, returns only the parameters at root of Name.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type for Unknown record.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class.

</dd> </dl>

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

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 





