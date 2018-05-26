---
title: GetConfiguration method of the MSFT\_SmbClientConfiguration class
description: Retrieves SMB client configuration settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2e6db9fe-d612-4f1f-95f6-81b897543109
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetConfiguration method SMB
- GetConfiguration method SMB , MSFT_SmbClientConfiguration class
- MSFT_SmbClientConfiguration class SMB , GetConfiguration method
topic_type:
- apiref
api_name:
- MSFT_SmbClientConfiguration.GetConfiguration
api_location:
- SmbWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetConfiguration method of the MSFT\_SmbClientConfiguration class

Retrieves SMB client configuration settings.

## Syntax


```mof
uint32 GetConfiguration(
  [out] MSFT_SmbClientConfiguration Output
);
```



## Parameters

<dl> <dt>

*Output* \[out\]
</dt> <dd>

An instance of the [**MSFT\_SmbClientConfiguration**](msft-smbclientconfiguration.md) class that represents the client configuration settings.

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

[**MSFT\_SmbClientConfiguration**](msft-smbclientconfiguration.md)
</dt> </dl>

 

 





