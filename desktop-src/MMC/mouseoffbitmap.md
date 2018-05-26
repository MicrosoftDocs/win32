---
title: MMCDisplayObject.MouseOffBitmap property
description: The MouseOffBitmap property returns a null-terminated string that contains the resource path to the image file for the image displayed for the task when the mouse is not in the tasks image or text area.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 480909b1-6886-4e08-9da5-2db29dfb01c3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MouseOffBitmap property MMC
- MouseOffBitmap property MMC , MMCDisplayObject class
- MMCDisplayObject class MMC , MouseOffBitmap property
topic_type:
- apiref
api_name:
- MMCDisplayObject.MouseOffBitmap
api_location:
- Cic.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCDisplayObject.MouseOffBitmap property

The **MouseOffBitmap** property returns a null-terminated string that contains the resource path to the image file for the image displayed for the task when the mouse is not in the task's image or text area.

This property is read-only.

## Syntax


```VB
MMCDisplayObject.MouseOffBitmap
```



## Property value

## Remarks

See [**MouseOverBitmap**](mouseoverbitmap.md) for the format of the string.

If **MouseOffBitmap** points to a **NULL** string, [**MouseOverBitmap**](mouseoverbitmap.md) must be a valid string that contains the location of a valid image. If one of these strings is **NULL**, the other string is used for both. If both mouse image locations are **NULL**, the task is not displayed.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





