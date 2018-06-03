---
title: Get method of the PS\_DnsClientNrptPolicy class
description: Retrieves Name Resolution Policy Table configured on the machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a1b159f3-82af-478e-9509-937e2d988c68
ms.prod: windows-server-dev
ms.technology:
- dns-client
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsClientNrptPolicy class
- PS_DnsClientNrptPolicy class, Get method
topic_type:
- apiref
api_name:
- PS_DnsClientNrptPolicy.Get
api_location:
- DnsClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsClientNrptPolicy class

Retrieves Name Resolution Policy Table configured on the machine.

## Syntax


```mof
uint32 Get(
  [in]  boolean                      Effective,
  [in]  string                       Namespace,
  [out] DnsClientPolicyConfiguration cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Effective* \[in\]
</dt> <dd>

If this parameter is specified then EffectiveNrptPolicy is returned.

</dd> <dt>

*Namespace* \[in\]
</dt> <dd>

Namespace of which the policy information is to be found out.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsClientPolicyConfiguration**](dnsclientpolicyconfiguration.md) object containing all the properties of DNS client NRPT policy. If *Effective* is specified, only the contents of Effective policy are retrieved.

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

[**PS\_DnsClientNrptPolicy**](ps-dnsclientnrptpolicy.md)
</dt> </dl>

 

 





