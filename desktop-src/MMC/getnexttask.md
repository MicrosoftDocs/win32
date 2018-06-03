---
title: MMCCtrl.GetNextTask method
description: The GetNextTask method returns an MMCTask object that represents the next task in the set of tasks to be displayed on the taskpad.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2ca28723-a4e6-47a3-9061-71f63eb97007
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetNextTask method MMC
- GetNextTask method MMC , MMCCtrl class
- MMCCtrl class MMC , GetNextTask method
topic_type:
- apiref
api_name:
- MMCCtrl.GetNextTask
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCCtrl.GetNextTask method

The **GetNextTask** method returns an MMCTask object that represents the next task in the set of tasks to be displayed on the taskpad.

## Syntax


```VB
MMCCtrl.GetNextTask()
```



## Parameters

This method has no parameters.

## Return value

An MMCTask object that represents the next task to be placed on the taskpad. If there are no more tasks for the taskpad, **NULL** is returned.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





