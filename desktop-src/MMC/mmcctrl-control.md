---
title: MMCCtrl Control object
description: The MMCCtrl control is used on a taskpad DHTML page to get the taskpad configuration information (text, graphics, tasks) from the snap-in and communicate data back to the snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f86b8a67-4ae6-4d28-bbcc-190e935002a9'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCCtrl Control object MMC", "MMCCtrl Control object MMC , described"]
topic_type:
- apiref
api_name:
- MMCCtrl Control
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# MMCCtrl Control object

The **MMCCtrl** control is used on a taskpad DHTML page to get the taskpad configuration information (text, graphics, tasks) from the snap-in and communicate data back to the snap-in.

The MMC taskpad templates use the **MMCCtrl** control. To create a custom taskpad that communicates with the snap-in, the **MMCCtrl** control should be placed as an object on the taskpad HTML page and its methods should be used to add tasks and send back notifications. Optionally, your taskpad HTML page can use methods to retrieve a title string, banner image, background image, and list control labels from the snap-in.

## Members

The **MMCCtrl Control** object has these types of members:

-   [Methods](#methods)

### Methods

The **MMCCtrl Control** object has these methods.



| Method                                           | Description                                                                                                                                                      |
|:-------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetBackground**](getbackground.md)           | Returns an **MMCDisplayObject** object used to display the background on a taskpad.<br/>                                                                   |
| [**GetDescriptiveText**](getdescriptivetext.md) | Returns the taskpad description string.<br/>                                                                                                               |
| [**GetFirstTask**](getfirsttask.md)             | Returns an **MMCTask** object that represents the first task.<br/>                                                                                         |
| [**GetListPadInfo**](getlistpadinfo.md)         | Returns an **MMCListPadInfo** object that represents list pad information.<br/>                                                                            |
| [**GetNextTask**](getnexttask.md)               | Returns an **MMCTask** object that represents the next task.<br/>                                                                                          |
| [**GetTitle**](gettitle.md)                     | Returns the string to be used for the taskpad's title.<br/>                                                                                                |
| [**TaskNotify**](tasknotify.md)                 | Sends a notification and data to the specified snap-in through that snap-in's [**IExtendTaskPad::TaskNotify**](iextendtaskpad-tasknotify.md) method.<br/> |



 

## Remarks

### Class ID

545AE700-50BF-11D1-9FE9-00600832DB4A

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |



 

 





