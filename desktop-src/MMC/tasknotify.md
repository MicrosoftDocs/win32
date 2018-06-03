---
title: MMCCtrl.TaskNotify method
description: Sends a notification and data to the specified snap-in through that snap-in's IExtendTaskPad TaskNotify method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 157685e3-b5a0-4cc8-ba9f-5f97bb85794b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- TaskNotify method MMC
- TaskNotify method MMC , MMCCtrl class
- MMCCtrl class MMC , TaskNotify method
topic_type:
- apiref
api_name:
- MMCCtrl.TaskNotify
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCCtrl.TaskNotify method

The TaskNotify method sends a notification and data to the specified snap-in through that snap-in's IExtendTaskPad::TaskNotify method.

## Syntax


```VB
MMCCtrl.TaskNotify( _
  ByVal szClsid, _
  ByVal pvArg, _
  ByVal pvParam _
)
```



## Parameters

<dl> <dt>

*szClsid* \[in\]
</dt> <dd>

A string that contains the CLSID of the snap-in that receives the notification and the data in pvArg and pvParam. For notifications for a task, the CLSID of the snap-in that owns a task can be retrieved from the **Clsid** property of the task's MMCTask object. For notifications for a list view button, the CLSID of the snap-in that owns the list-view control can be retrieved from the **Clsid** property of the MMCListPadInfo object.

</dd> <dt>

*pvArg* \[in\]
</dt> <dd>

A VARIANT that contains information passed back to the snap-in specified by szClsid.

<dl> <dt>

<span id="Taskpads_using_MMC_taskpad_templates_or_command_IDs"></span><span id="taskpads_using_mmc_taskpad_templates_or_command_ids"></span><span id="TASKPADS_USING_MMC_TASKPAD_TEMPLATES_OR_COMMAND_IDS"></span>Taskpads using MMC taskpad templates or command IDs
</dt> <dd></dd> </dl>

For the MMC-supplied taskpads, the VARIANT structure contains the command ID for the task or list view button that was clicked on the taskpad. List view buttons apply only to list view taskpads.

The command ID for a task can be retrieved from the **CommandID** property of the task's MMCTask object. A task's command ID was specified in the nCommandID of the **MMC\_TASK** structure passed in the IEnumTASK::Next method that MMC called when it retrieved the information for that task during the setup of the taskpad.

The command ID for a list view button can be retrieved from the **NotifyID** property of the MMCListPadInfo object. A list view button is the button specified in the szButtonText member of the **MMC\_LISTPAD\_INFO** passed in the IExtendTaskPad::GetListPadInfo method that MMC called when it was setting up the list view taskpad. The list view button's command ID was specified in the nCommandID member of **MMC\_LISTPAD\_INFO**.

<dl> <dt>

<span id="Taskpads_using_custom_HTML_pages"></span><span id="taskpads_using_custom_html_pages"></span><span id="TASKPADS_USING_CUSTOM_HTML_PAGES"></span>Taskpads using custom HTML pages
</dt> <dd></dd> </dl>

For custom taskpads, the VARIANT can contain any data that the script on the custom HTML page wants to pass back to the snap-in.

</dd> <dt>

*pvParam* \[in\]
</dt> <dd>

A pointer to a VARIANT that contains information passed back to the snap-in specified by szClsid.

This parameter is not used by taskpads that use the MMC taskpad templates unless this method is called by a scriptlet in a task. However, it can be used by custom taskpads to pass an additional value back to the snap-in.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| Header<br/>          | <dl> <dt>Mmc.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





