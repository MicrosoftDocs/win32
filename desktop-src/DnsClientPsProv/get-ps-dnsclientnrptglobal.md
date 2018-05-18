---
title: Get method of the PS\_DnsClientNrptGlobal class
description: Retrieves NRPT global settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4dca8f2d-a8fb-4442-8322-7172ae20f345'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-client'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DnsClientNrptGlobal class", "PS_DnsClientNrptGlobal class, Get method"]
topic_type:
- apiref
api_name:
- PS_DnsClientNrptGlobal.Get
api_location:
- DnsClientPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DnsClientNrptGlobal class

Retrieves NRPT global settings.

## Syntax


```mof
uint32 Get(
  [in]  string              Server,
  [in]  string              GpoName,
  [out] DnsClientNrptGlobal cmdletOutput
);
```



## Parameters

<dl> <dt>

*Server* \[in\]
</dt> <dd>

Server hosting the GPO.

</dd> <dt>

*GpoName* \[in\]
</dt> <dd>

Name of GPO, if not specified the default GPO on the domain.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsClientNrptGlobal**](ps-dnsclientnrptglobal.md) object contains all the properties of DNS client NRPT Global settings.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsClientNrptGlobal**](ps-dnsclientnrptglobal.md)
</dt> </dl>

 

 





