---
title: MMCDisplayObject.MouseOverBitmap property
description: The MouseOverBitmap property returns a null-terminated string that contains the resource path to the image file for the image displayed for the task when the user moves the mouse over the task's image or text area.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a4567748-1729-4c72-b387-663d00dd4e45
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MouseOverBitmap property MMC
- MouseOverBitmap property MMC , MMCDisplayObject object
- MMCDisplayObject object MMC , MouseOverBitmap property
topic_type:
- apiref
api_name:
- MMCDisplayObject.MouseOverBitmap
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCDisplayObject.MouseOverBitmap property

The **MouseOverBitmap** property returns a null-terminated string that contains the resource path to the image file for the image displayed for the task when the user moves the mouse over the task's image or text area.

This property is read-only.

## Syntax


```VB
MMCDisplayObject.MouseOverBitmap
```



## Property value

## Remarks

The string will have the following form:

"res://*filepath*/*imgpath*"

where *filepath* is the full path to the snap-in's DLL that stores the image file as a resource, and *imgpath* is the resource path of the image file with the snap-in DLL.

For example, the following string specifies that the snap-in DLL(snapin.dll) has a path of "c:\\windows\\system32\\snapin.dll" and that the resource path is img/mon.gif: "res://c:\\\\windows\\\\system32\\\\snapin.dll/img/mon.bmp".

If **MouseOverBitmap** points to a **NULL** string, [**MouseOffBitmap**](mouseoffbitmap.md) must be a valid string that contains the location of a valid image. If one of these strings is **NULL**, the other string is used for both. If both mouse image locations are **NULL**, the task is not displayed.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





