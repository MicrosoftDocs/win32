---
title: MMCTask.Help property
description: The Help property returns the description of the task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8b1ae7e3-fec3-4c5f-a117-257bec0f464b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Help property MMC
- Help property MMC , MMCTask class
- MMCTask class MMC , Help property
topic_type:
- apiref
api_name:
- MMCTask.Help
api_location:
- Cic.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCTask.Help property

The **Help** property returns the description of the task.

This property is read-only.

## Syntax


```VB
MMCTask.Help
```



## Property value

The returned property is the string specified in the **szHelpString** member of the [**MMC\_TASK**](mmc-task.md) structure returned in the **IEnumTASK::Next** method.

## Remarks

The **Help** property specifies the descriptive text that should be displayed when the user moves the mouse over the mouse-over image or the label text for the task.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





