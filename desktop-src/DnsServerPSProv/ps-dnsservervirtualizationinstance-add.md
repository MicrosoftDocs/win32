---
title: Add method of the PS\_DnsServerVirtualizationInstance class
description: Adds a DNS server virtualization instance.
audience: developer
ms.assetid: 009543c1-dc47-4586-a02c-6242acbd058b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DnsServerVirtualizationInstance class
- PS_DnsServerVirtualizationInstance class, Add method
topic_type:
- apiref
api_name:
- PS_DnsServerVirtualizationInstance.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DnsServerVirtualizationInstance class

Adds a DNS server virtualization instance.

## Syntax


```mof
uint32 Add(
  [in]  string                          ComputerName,
  [in]  string                          Name,
  [in]  string                          FriendlyName,
  [in]  string                          Description,
  [in]  boolean                         PassThru,
  [out] DnsServerVirtualizationInstance cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

</dd> <dt>

*FriendlyName* \[in\]
</dt> <dd>

user friendly name of the virtualization instance.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description of the virtualization instance.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsServerVirtualizationInstance**](dnsservervirtualizationinstance.md) that contains the friendly name, and a description.

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

 

 





