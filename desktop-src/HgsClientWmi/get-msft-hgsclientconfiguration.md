---
title: Get method of the MSFT\_HgsClientConfiguration class
description: Retrieves the local Host Guardian Service configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ab19caa8-3461-48fd-87f4-f76b71006e42
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_HgsClientConfiguration class
- MSFT_HgsClientConfiguration class, Get method
topic_type:
- apiref
api_name:
- MSFT_HgsClientConfiguration.Get
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the MSFT\_HgsClientConfiguration class

Retrieves the local Host Guardian Service configuration.

## Syntax


```mof
uint32 Get(
  [out] MSFT_HgsClientConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an embedded instance of a [**MSFT\_HgsClientConfiguration**](msft-hgsclientconfiguration.md) class that represents the configuration of the Host Guardian Service client.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_HgsClientConfiguration**](msft-hgsclientconfiguration.md)
</dt> </dl>

 

 





