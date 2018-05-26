---
title: MMCListPadInfo.NotifyID property
description: Returns the command ID that is returned to the snap-in when the user clicks the optional listpad button.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 71898260-395e-4415-8c64-dc7518b30b86
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- NotifyID property MMC
- NotifyID property MMC , MMCListPadInfo class
- MMCListPadInfo class MMC , NotifyID property
topic_type:
- apiref
api_name:
- MMCListPadInfo.NotifyID
api_location:
- Cic.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCListPadInfo.NotifyID property

The NotifyID property returns the command ID that is returned to the snap-in when the user clicks the optional listpad button.

This property is read-only.

## Syntax


```VB
MMCListPadInfo.NotifyID
```



## Property value

The returned property is the long integer specified in the nCommandID member of MMC\_LISTPAD\_INFO returned in the [**IExtendTaskPad::GetListPadInfo**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-getlistpadinfo?branch=master) method.

## Remarks

When the user clicks the button, the taskpad calls the TaskNotify method of the MMCCtrl control with pvArg set to the value in the NotifyID property of the MMCListPadInfo object.

The value of this property should be ignored if the Text property is **NULL**.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





