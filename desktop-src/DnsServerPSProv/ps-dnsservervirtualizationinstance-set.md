---
title: Set method of the PS\_DnsServerVirtualizationInstance class
description: Sets a specified DNS server virtualization instance.
audience: developer
ms.assetid: 3d57c663-4f2f-447a-99b7-8a27f09b11d7
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerVirtualizationInstance class
- PS_DnsServerVirtualizationInstance class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerVirtualizationInstance.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DnsServerVirtualizationInstance class

Sets a specified DNS server virtualization instance.

## Syntax


```mof
uint32 Set(
  [in]  string                          ComputerName,
  [in]  string                          Name,
  [in]  boolean                         PassThru,
  [in]  string                          Description,
  [in]  string                          FriendlyName,
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

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description of the virtualization instance.

</dd> <dt>

*FriendlyName* \[in\]
</dt> <dd>

User-friendly name of the virtualization instance.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The updated [**DnsServerVirtualizationInstance**](dnsservervirtualizationinstance.md).

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

 

 





