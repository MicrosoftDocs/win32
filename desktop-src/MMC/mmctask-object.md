---
title: MMCTask Object object
description: The MMCTask object represents a task to be added to the taskpad.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '33865e60-576f-40b8-ab89-9327e3b89277'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCTask Object object MMC", "MMCTask Object object MMC , described"]
topic_type:
- apiref
api_name:
- MMCTask Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# MMCTask Object object

The MMCTask object represents a task to be added to the taskpad.

An MMCTask object is returned by the GetFirstTask and GetNextTask methods of the MMCCtrl control. The MMCTask object's properties represent the members of the MMC\_TASK structure passed in the [**IEnumTASK::Next**](ienumtask-next.md) method that MMC called when it retrieved the information for that task during the setup of the taskpad. The MMCTask object also has one additional property that represents the snap-in's CLSID.

The MMC taskpad templates use the MMCTask object. To create a custom taskpad that communicates with the snap-in, the taskpad's HTML page should use the GetFirstTask and GetNextTask methods to retrieve the MMCTask objects for all the tasks and add them to the page.

## Members

The **MMCTask Object** object has these types of members:

-   [Properties](#properties)

### Properties

The **MMCTask Object** object has these properties.



| Property                                                           | Description                                                                                                                                                               |
|:-------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActionType**](mmctask-object-actiontype.md)<br/>         | Type of action triggered when a user clicks the task.<br/>                                                                                                          |
| [**ActionURL**](mmctask-object-actionurl.md)<br/>           | URL to which the task links when the user clicks the task. The string can also contain a script instead of a URL.<br/> Used only if **ActionType** is 1.<br/> |
| [**Clsid**](mmctask-object-clsid.md)<br/>                   | CLSID of the snap-in that created the task and owns it.<br/>                                                                                                        |
| [**CommandID**](mmctask-object-commandid.md)<br/>           | Command ID returned to the snap-in when the user clicks the task.<br/> Used only if **ActionType** is 0.<br/>                                                 |
| [**DisplayObject**](mmctask-object-displayobject.md)<br/>   | MMCDisplayObject object that contains information about the appearance of the task's button.<br/>                                                                   |
| [**Help**](mmctask-object-help.md)<br/>                     | Description for the task.<br/>                                                                                                                                      |
| [**Script**](mmctask-object-script.md)<br/>                 | Script to run when the user clicks the task.<br/> Used only if **ActionType** is 2.<br/>                                                                      |
| [**ScriptLanguage**](mmctask-object-scriptlanguage.md)<br/> | Script language of the script specified by the **Script** property.<br/> Used only if **ActionType** is 2.<br/>                                               |
| [**Text**](mmctask-object-text.md)<br/>                     | Text label for the task.<br/>                                                                                                                                       |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |



 

 





