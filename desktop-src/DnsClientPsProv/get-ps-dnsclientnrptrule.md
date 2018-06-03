---
title: Get method of the PS\_DnsClientNrptRule class
description: Retrieves DNS client Name Resolution Policy Table rules.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9be261b3-e303-496f-a782-db2c175e65f9
ms.prod: windows-server-dev
ms.technology:
- dns-client
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsClientNrptRule class
- PS_DnsClientNrptRule class, Get method
topic_type:
- apiref
api_name:
- PS_DnsClientNrptRule.Get
api_location:
- DnsClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsClientNrptRule class

Retrieves DNS client Name Resolution Policy Table rules.

## Syntax


```mof
uint32 Get(
  [in]  string            GpoName,
  [in]  string            Name[],
  [in]  string            Server,
  [out] DnsClientNrptRule cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*GpoName* \[in\]
</dt> <dd>

Name of GPO, if not specified the default GPO on the domain.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name which uniquely identifies a rule.

</dd> <dt>

*Server* \[in\]
</dt> <dd>

Server hosting the gpo.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsClientNrptRule**](ps-dnsclientnrptrule.md) object containing all the properties of DNS client NRPT rule.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsClientNrptRule**](ps-dnsclientnrptrule.md)
</dt> </dl>

 

 





