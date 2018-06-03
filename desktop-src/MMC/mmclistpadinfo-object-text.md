---
title: MMCListPadInfo.Text property
description: The Text property returns the text for an optional button.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 72c82451-df3a-46b2-bc96-37ef61b7efad
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Text property MMC
- Text property MMC , MMCListPadInfo class
- MMCListPadInfo class MMC , Text property
topic_type:
- apiref
api_name:
- MMCListPadInfo.Text
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCListPadInfo.Text property

The **Text** property returns the text for an optional button.

This property is read-only.

## Syntax


```VB
MMCListPadInfo.Text
```



## Property value

The returned property is the string specified in the **szButtonText** member of **MMC\_LISTPAD\_INFO** returned in the **IExtendTaskPad::GetListPadInfo** method.

## Remarks

In the MMC standard list view template, the text is placed on a button that is directly above the list control and to the right of the **Title** text.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





