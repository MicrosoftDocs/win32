---
title: Remove method of the PS\_DnsServerVirtualizationInstance class
description: Removes a DNS server virtualization instance.
audience: developer
ms.assetid: 5a368111-ed44-464c-aefd-cacfedbcdb37
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DnsServerVirtualizationInstance class
- PS_DnsServerVirtualizationInstance class, Remove method
topic_type:
- apiref
api_name:
- PS_DnsServerVirtualizationInstance.Remove
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DnsServerVirtualizationInstance class

Removes a DNS server virtualization instance.

## Syntax


```mof
uint32 Remove(
  [in]  string                          Name,
  [in]  string                          ComputerName,
  [in]  boolean                         PassThru,
  [in]  boolean                         Force,
  [in]  boolean                         RemoveZoneFiles,
  [out] DnsServerVirtualizationInstance cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*RemoveZoneFiles* \[in\]
</dt> <dd>

If specified, removes all the zone files of the primary file backed zones hosted by the virtualization instance.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

VirtualizationInstance

FriendlyName

Description

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

[**PS\_DnsServerVirtualizationInstance**](ps-dnsservervirtualizationinstance.md)
</dt> </dl>

 

 





