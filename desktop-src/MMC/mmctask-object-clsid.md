---
title: MMCListPadInfo.Clsid property
description: Returns the CLSID of the snap-in that created the task and owns it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b96d6e05-0b3f-443c-ba28-b3a54ba79e33'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Clsid property MMC", "Clsid property MMC , MMCListPadInfo class", "MMCListPadInfo class MMC , Clsid property"]
topic_type:
- apiref
api_name:
- MMCListPadInfo.Clsid
api_location:
- Cic.dll
api_type:
- COM
---

# MMCListPadInfo.Clsid property

The Clsid property returns the CLSID of the snap-in that created the task and owns it.

This property is read-only.

## Syntax


```VB
MMCListPadInfo.Clsid
```



## Property value

The returned property is the CLSID.

## Remarks

To specify the snap-in that owns the task, the value of the Clsid property can be used for the szClsid parameter when the taskpad calls the TaskNotify method of the MMCCtrl control to send a notification from the task to that snap-in.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





