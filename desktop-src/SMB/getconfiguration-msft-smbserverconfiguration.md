---
title: GetConfiguration method of the MSFT\_SmbServerConfiguration class
description: Retrieves SMB server configuration values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0b68d8c2-a9a5-4599-8e11-acc986f0b006
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetConfiguration method SMB
- GetConfiguration method SMB , MSFT_SmbServerConfiguration class
- MSFT_SmbServerConfiguration class SMB , GetConfiguration method
topic_type:
- apiref
api_name:
- MSFT_SmbServerConfiguration.GetConfiguration
api_location:
- SmbWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetConfiguration method of the MSFT\_SmbServerConfiguration class

Retrieves SMB server configuration values.

## Syntax


```mof
uint32 GetConfiguration(
  [out] MSFT_SmbServerConfiguration Output
);
```



## Parameters

<dl> <dt>

*Output* \[out\]
</dt> <dd>

An instance of the [**MSFT\_SmbServerConfiguration**](msft-smbserverconfiguration.md) class that represents the server configuration settings.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbServerConfiguration**](msft-smbserverconfiguration.md)
</dt> </dl>

 

 





