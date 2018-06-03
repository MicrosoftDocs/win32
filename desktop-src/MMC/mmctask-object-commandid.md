---
title: MMCTask.CommandID property
description: Returns the command ID returned to the snap-in when the user clicks the task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 20712926-a2cc-4d07-9afc-aa65664d41ed
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CommandID property MMC
- CommandID property MMC , MMCTask class
- MMCTask class MMC , CommandID property
topic_type:
- apiref
api_name:
- MMCTask.CommandID
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCTask.CommandID property

The CommandID property returns the command ID returned to the snap-in when the user clicks the task. This property is used only if [**ActionType**](mmctask-object-actiontype.md) is 0.

This property is read-only.

## Syntax


```VB
MMCTask.CommandID
```



## Property value

The returned property is the long integer specified in the nCommandID member of the [**MMC\_TASK**](/windows/desktop/api/Mmc/ne-mmc-_mmc_task_display_type) structure returned in the [**IEnumTASK::Next**](/windows/desktop/api/Mmc/nf-mmc-ienumtask-next) method.

## Remarks

When the user clicks the task, the taskpad calls the TaskNotify method of the MMCCtrl control with pvArg set to the value in the CommandID property of the task object.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





