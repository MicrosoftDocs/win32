---
title: MMCListPadInfo.Text property
description: Returns the text label for the task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a3e7d74f-755b-4009-8cd2-49f9ca5bfc65
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Text property MMC
- Text property MMC , MMCListPadInfo class
- MMCListPadInfo class MMC , Text property
topic_type:
- apiref
api_name:
- MMCListPadInfo.Text
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCListPadInfo.Text property

The **Text** property returns the text label for the task.

This property is read-only.

## Syntax


```VB
MMCListPadInfo.Text
```



## Property value

The Text property is the string specified in the **szText** member of the [**MMC\_TASK**](/windows/desktop/api/Mmc/ne-mmc-_mmc_task_display_type) structure returned in the [**IEnumTASK::Next**](/windows/desktop/api/Mmc/nf-mmc-ienumtask-next) method.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





