---
title: SetByChangeToLocalMode method of the MSFT\_HgsClientConfiguration class
description: Modifies the configuration of the Host Guardian Service Client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d176743d-49be-4c73-99d4-abc02d887c63
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByChangeToLocalMode method
- SetByChangeToLocalMode method, MSFT_HgsClientConfiguration class
- MSFT_HgsClientConfiguration class, SetByChangeToLocalMode method
topic_type:
- apiref
api_name:
- MSFT_HgsClientConfiguration.SetByChangeToLocalMode
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByChangeToLocalMode method of the MSFT\_HgsClientConfiguration class

Modifies the configuration of the Host Guardian Service Client.

## Syntax


```mof
uint32 SetByChangeToLocalMode(
  [in]  boolean                     EnableLocalMode,
  [out] MSFT_HgsClientConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*EnableLocalMode* \[in\]
</dt> <dd>

Changes the Mode of Host Guardian Service client from 'Host Guardian Service' to 'Local' mode.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The configuration of the Host Guardian Service client.

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

 

 





