---
title: SetInterval method of the MSFT\_MTTaskManager class
description: Sets the interval seconds for a background data refresh.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 822bf0ed-42c4-40c1-adb6-8fb80a9e506c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetInterval method
- SetInterval method, MSFT_MTTaskManager class
- MSFT_MTTaskManager class, SetInterval method
topic_type:
- apiref
api_name:
- MSFT_MTTaskManager.SetInterval
api_location:
- MtTmProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetInterval method of the MSFT\_MTTaskManager class

Sets the interval seconds for a background data refresh.

## Syntax


```mof
uint32 SetInterval(
  [in] uint16 Seconds
);
```



## Parameters

<dl> <dt>

*Seconds* \[in\]
</dt> <dd>

The length of the interval, in seconds, to set the background data refresh.

</dd> </dl>

## Remarks

The last 60 samples will be cached.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MTTaskManager**](msft-mttaskmanager.md)
</dt> </dl>

 

 





