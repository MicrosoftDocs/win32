---
title: MMCTask.ActionType property
description: The returned property returns the type of action triggered when a user clicks the task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fa08b73a-98f5-420a-8098-89c821933078
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ActionType property MMC
- ActionType property MMC , MMCTask class
- MMCTask class MMC , ActionType property
topic_type:
- apiref
api_name:
- MMCTask.ActionType
api_location:
- Cic.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCTask.ActionType property

The returned property returns the type of action triggered when a user clicks the task.

This property is read-only.

## Syntax


```VB
MMCTask.ActionType
```



## Property value

The **ActionType** property is the long integer specified in the eActionType member of the MMC\_TASK structure returned in the [**IEnumTASK::Next**](ienumtask-next.md) method.

## Remarks

This property determines which of the following properties are set: [**CommandID**](mmctask-object-commandid.md), [**ActionURL**](mmctask-object-actionurl.md), [**Script**](mmctask-object-script.md), and [**ScriptLanguage**](mmctask-object-scriptlanguage.md).

The following table describes the action types.



| Value | Meaning                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | When the user clicks the task, the taskpad calls the TaskNotify method of the MMCCtrl control with pvArg set to the value in the CommandID property of the task.<br/> If the MMCTask object specifies this value, the CommandID property contains the command ID and the ActionURL, Script, and ScriptLanguage are not used.<br/>                                                              |
| 1     | When the user clicks the task, the taskpad activates the link specified by the ActionURL property of the task.<br/> If the MMCTask object specifies this value, the ActionURL property contains the URL and the CommandID, Script, and ScriptLanguage are not used.<br/>                                                                                                                       |
| 2     | When the user clicks the task, the taskpad executes the script contained in the Script property using the window.execScript method using the script language specified in the ScriptLanguage property.<br/> If the object specifies this value, the Script property contains the script and the ScriptLanguage property is the script language. The CommandID and ActionURL are not used.<br/> |



 

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





