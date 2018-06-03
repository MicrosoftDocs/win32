---
title: GetChannels method of the MSFT\_MTEventProvider class
description: Gets all the event channels that are exported by this event provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7f6a32dc-6bb2-4732-8ddd-382c5f564828
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetChannels method
- GetChannels method, MSFT_MTEventProvider class
- MSFT_MTEventProvider class, GetChannels method
topic_type:
- apiref
api_name:
- MSFT_MTEventProvider.GetChannels
api_location:
- MtTmProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetChannels method of the MSFT\_MTEventProvider class

Gets all the event channels that are exported by this event provider.

## Syntax


```mof
uint32 GetChannels(
  [out] MSFT_MTEventChannel Result[]
);
```



## Parameters

<dl> <dt>

*Result* \[out\]
</dt> <dd>

[**MSFT\_MTEventChannel**](msft-mteventchannel.md) embedded instances containing the event channels.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MTEventProvider**](msft-mteventprovider.md)
</dt> </dl>

 

 





