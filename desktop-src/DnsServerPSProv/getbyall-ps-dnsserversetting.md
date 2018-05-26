---
title: GetByAll method of the PS\_DnsServerSetting class
description: Retrieve DNS server settings.
audience: developer
ms.assetid: 8cc65c8f-14db-4f49-b855-2573336aa13c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByAll method
- GetByAll method, PS_DnsServerSetting class
- PS_DnsServerSetting class, GetByAll method
topic_type:
- apiref
api_name:
- PS_DnsServerSetting.GetByAll
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetByAll method of the PS\_DnsServerSetting class

Retrieve DNS server settings.

## Syntax


```mof
uint32 GetByAll(
  [in]  boolean          All,
  [in]  string           ComputerName,
  [out] DnsServerSetting cmdletOutput
);
```



## Parameters

<dl> <dt>

*All* \[in\]
</dt> <dd>

Retrieves all the settings.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerSetting**](dnsserversetting.md) class.

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

[**PS\_DnsServerSetting**](ps-dnsserversetting.md)
</dt> </dl>

 

 





