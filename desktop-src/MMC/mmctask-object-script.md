---
title: MMCTask.Script property
description: The Script property returns the script to run when the user clicks the task. This property is used only if ActionType is 2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: aec842b6-b1ab-458d-adb3-216195ef95e3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Script property MMC
- Script property MMC , MMCTask class
- MMCTask class MMC , Script property
topic_type:
- apiref
api_name:
- MMCTask.Script
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCTask.Script property

The Script property returns the script to run when the user clicks the task. This property is used only if ActionType is 2.

This property is read-only.

## Syntax


```VB
MMCTask.Script
```



## Property value

The returned property is the string specified in the szScript member of the [**MMC\_TASK**](/windows/desktop/api/Mmc/ne-mmc-_mmc_task_display_type) structure returned in the [**IEnumTASK::Next**](/windows/desktop/api/Mmc/nf-mmc-ienumtask-next) method.

## Remarks

This property contains the script to run using the window.execScript method on the taskpad DHTML page. Be aware that the script language specified by the ScriptLanguage property should also be specified in the window.execScript method.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





