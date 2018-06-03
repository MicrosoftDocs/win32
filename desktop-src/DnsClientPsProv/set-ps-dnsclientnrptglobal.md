---
title: Set method of the PS\_DnsClientNrptGlobal class
description: Modifies Global NRPT settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9f9a85e7-3696-4475-a705-b850b1902ed1
ms.prod: windows-server-dev
ms.technology:
- dns-client
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsClientNrptGlobal class
- PS_DnsClientNrptGlobal class, Set method
topic_type:
- apiref
api_name:
- PS_DnsClientNrptGlobal.Set
api_location:
- DnsClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DnsClientNrptGlobal class

Modifies Global NRPT settings.

## Syntax


```mof
uint32 Set(
  [in]  string              EnableDAForAllNetworks,
  [in]  string              GpoName,
  [in]  string              SecureNameQueryFallback,
  [in]  string              QueryPolicy,
  [in]  string              Server,
  [in]  boolean             PassThru,
  [out] DnsClientNrptGlobal cmdletOutput
);
```



## Parameters

<dl> <dt>

*EnableDAForAllNetworks* \[in\]
</dt> <dd>

Property that controls Direct Access.

</dd> <dt>

*GpoName* \[in\]
</dt> <dd>

Name of GPO, if not specified the default GPO on the domain.

</dd> <dt>

*SecureNameQueryFallback* \[in\]
</dt> <dd>

Property for controlling DNS client name resolution fallback policy.

</dd> <dt>

*QueryPolicy* \[in\]
</dt> <dd>

Property for controlling DNS client query policy.

</dd> <dt>

*Server* \[in\]
</dt> <dd>

Server hosting the GPO.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies if result of the cmdlet should be displayed.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsClientNrptGlobal**](ps-dnsclientnrptglobal.md) object contains all the properties of DNS client NRPT Global settings.

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

[**PS\_DnsClientNrptGlobal**](ps-dnsclientnrptglobal.md)
</dt> </dl>

 

 





