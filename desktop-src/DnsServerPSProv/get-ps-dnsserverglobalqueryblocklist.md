---
title: Get method of the PS\_DnsServerGlobalQueryBlockList class
description: Retrieves DNS Server block List settings.
audience: developer
ms.assetid: 541c35f0-57b5-46f7-9fbf-d08c5220fcb4
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerGlobalQueryBlockList class
- PS_DnsServerGlobalQueryBlockList class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerGlobalQueryBlockList.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerGlobalQueryBlockList class

Retrieves DNS Server block List settings

## Syntax


```mof
uint32 Get(
  [in]  string                        ComputerName,
  [out] DnsServerGlobalQueryBlockList cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerGlobalQueryBlockList**](dnsserverglobalqueryblocklist.md) class.

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

[**PS\_DnsServerGlobalQueryBlockList**](ps-dnsserverglobalqueryblocklist.md)
</dt> </dl>

 

 





