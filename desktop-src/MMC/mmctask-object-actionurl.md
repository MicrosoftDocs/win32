---
title: MMCTask.ActionURL property
description: Returns the URL to which the task links when the user clicks the task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9607ead4-dd96-41a6-801c-9750fa18cb47
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ActionURL property MMC
- ActionURL property MMC , MMCTask class
- MMCTask class MMC , ActionURL property
topic_type:
- apiref
api_name:
- MMCTask.ActionURL
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCTask.ActionURL property

The ActionURL property returns the URL to which the task links when the user clicks the task. The string can also contain a script instead of a URL. This property is used only if ActionType is 1.

This property is read-only.

## Syntax


```VB
MMCTask.ActionURL
```



## Property value

The returned property is the string specified in the szActionURL member of the MMC\_TASK structure returned in the [**IEnumTASK::Next**](/windows/desktop/api/Mmc/nf-mmc-ienumtask-next) method.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





