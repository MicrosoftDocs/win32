---
title: MMCListPadInfo.Title property
description: Returns the text label for the ListPad control.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d48bf33-4e7e-4792-8545-59eea3ebf5fa
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Title property MMC
- Title property MMC , MMCListPadInfo class
- MMCListPadInfo class MMC , Title property
topic_type:
- apiref
api_name:
- MMCListPadInfo.Title
api_location:
- Cic.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCListPadInfo.Title property

The Title property returns the text label for the ListPad control.

This property is read-only.

## Syntax


```VB
MMCListPadInfo.Title
```



## Property value

The returned property is the string specified in the szTitle member of [**MMC\_LISTPAD\_INFO**](/windows/win32/Mmc/ns-mmc-_mmc_listpad_info?branch=master) returned in the [**IExtendTaskPad::GetListPadInfo**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-getlistpadinfo?branch=master) method of the snap-in.

## Remarks

In the MMC standard list view template, the text is placed directly above the list control. This text can be the label for the objects within the list control (such as "Printers" if the list contains printers) or instructions (such as "Select a printer and click an action to perform.").

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





