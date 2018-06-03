---
title: MMCDisplayObject.URLtoEOT property
description: The URLtoEOT property returns a null-terminated string that contains the resource path to the EOT (embedded OpenType) file that contains the font for the symbol being displayed on a taskpad.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6148cf6-243d-4657-80d0-31caaba387b4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- URLtoEOT property MMC
- URLtoEOT property MMC , MMCDisplayObject object
- MMCDisplayObject object MMC , URLtoEOT property
topic_type:
- apiref
api_name:
- MMCDisplayObject.URLtoEOT
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCDisplayObject.URLtoEOT property

The **URLtoEOT** property returns a null-terminated string that contains the resource path to the EOT (embedded OpenType) file that contains the font for the symbol being displayed on a taskpad.

This property is read-only.

## Syntax


```VB
MMCDisplayObject.URLtoEOT
```



## Property value

## Remarks

The string will have the following form:

"res://*filepath*/*imgpath*"

where *filepath* is the full path to the snap-in's DLL that stores the image file as a resource, and *imgpath* is the resource path of the image file with the snap-in DLL.

For example, the following string specifies that the snap-in DLL (snapin.dll) has a path of "c:\\windows\\system32\\snapin.dll" and that the resource path is img/myfont.eot: "res://c:\\\\windows\\\\system32\\\\snapin.dll/img/myfont.eot".

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





