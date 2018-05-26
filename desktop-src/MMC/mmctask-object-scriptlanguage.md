---
title: MMCTask.ScriptLanguage property
description: Returns the script language of the script specified by the Script property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22c21ba5-86ba-471c-9a0d-6d6ca62475c7
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ScriptLanguage property MMC
- ScriptLanguage property MMC , MMCTask class
- MMCTask class MMC , ScriptLanguage property
topic_type:
- apiref
api_name:
- MMCTask.ScriptLanguage
api_location:
- Cic.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCTask.ScriptLanguage property

The ScriptLanguage property returns the script language of the script specified by the Script property. This property is used only if ActionType is 2.

This property is read-only.

## Syntax


```VB
MMCTask.ScriptLanguage
```



## Property value

The returned property is a String that represents the script language specified at the beginning of the string specified in the szScript member of the MMC\_TASK structure returned in the [**IEnumTASK::Next**](/windows/win32/Mmc/nf-mmc-ienumtask-next?branch=master) method. If no script language is specified, the default language is JavaScript.

## Remarks

This property contains the script language to use when running the script specified by the Script property using the window.execScript method on the taskpad DHTML page.

The ScriptLanguage property can have the following values:

-   VBSCRIPT
-   JSCRIPT
-   JAVASCRIPT

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





