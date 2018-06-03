---
title: SetBySecureHostingServiceMode method of the MSFT\_HgsClientConfiguration class
description: Modifies the configuration of the Host Guardian Service client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: A200642B-811B-4D9D-979D-EABD3C873585
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetBySecureHostingServiceMode method
- SetBySecureHostingServiceMode method, MSFT_HgsClientConfiguration interface
- MSFT_HgsClientConfiguration interface, SetBySecureHostingServiceMode method
topic_type:
- apiref
api_name:
- MSFT_HgsClientConfiguration.SetBySecureHostingServiceMode
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetBySecureHostingServiceMode method of the MSFT\_HgsClientConfiguration class

Modifies the configuration of the Host Guardian Service client.

## Syntax


```mof
uint32 SetBySecureHostingServiceMode(
  [in]  string                      KeyProtectionServerUrl,
  [in]  string                      AttestationServerUrl,
  [out] MSFT_HgsClientConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*KeyProtectionServerUrl* \[in\]
</dt> <dd>

URL for the key protection server.

</dd> <dt>

*AttestationServerUrl* \[in\]
</dt> <dd>

URL for the attestation server.

</dd> <dt>

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

 

 





