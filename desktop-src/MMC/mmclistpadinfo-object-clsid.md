---
title: MMCListPadInfo.Clsid property
description: Returns the CLSID of the snap-in that created the list view taskpad and owns it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b4f7f3b5-da5e-4bf1-ac38-ef3fb2253576
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Clsid property MMC
- Clsid property MMC , MMCListPadInfo class
- MMCListPadInfo class MMC , Clsid property
topic_type:
- apiref
api_name:
- MMCListPadInfo.Clsid
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCListPadInfo.Clsid property

The Clsid property returns the CLSID of the snap-in that created the list view taskpad and owns it.

This property is read-only.

## Syntax


```VB
MMCListPadInfo.Clsid
```



## Property value

A String that represents the CLSID.

## Remarks

To specify the snap-in that owns the list view taskpad, the value of the Clsid property can be used for the szClsid parameter when the taskpad calls the TaskNotify method of the MMCCtrl control to send a list view button notification to that snap-in.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





