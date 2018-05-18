---
title: MMCDisplayObject.DisplayObjectType property
description: The DisplayObjectType property returns the type of image displayed for a task or as the background in taskpad. The image can be one of three types symbol, GIF, or bitmap.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b83fe746-1363-43b6-ad26-36a3119480a4'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["DisplayObjectType property MMC", "DisplayObjectType property MMC , MMCDisplayObject class", "MMCDisplayObject class MMC , DisplayObjectType property"]
topic_type:
- apiref
api_name:
- MMCDisplayObject.DisplayObjectType
api_location:
- Cic.dll
api_type:
- COM
---

# MMCDisplayObject.DisplayObjectType property

The **DisplayObjectType** property returns the type of image displayed for a task or as the background in taskpad. The image can be one of three types: symbol, GIF, or bitmap.

This property is read-only.

## Syntax


```VB
MMCDisplayObject.DisplayObjectType
```



## Property value

## Remarks

The **DisplayObjectType** property returns a Long value. The meaning of the value is defined in the following table.



| Value           | Meaning                                                                                                                                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0<br/>    | The image displayed for the task or background is the symbol defined by the combination of the [**SymbolString**](symbolstring.md), [**FontFamilyName**](fontfamilyname.md), and [**URLtoEOT**](urltoeot.md) properties.<br/>                                                                   |
| 1<br/>    | The image displayed for the task or background is the symbol specified by an [**MMC\_TASK\_DISPLAY\_SYMBOL**](mmc-task-display-symbol.md) structure.<br/>                                                                                                                                         |
| 2, 3<br/> | The image displayed for the task or background is a transparent GIF or bitmap image.<br/> The images are specified by the [**MouseOverBitmap**](mouseoverbitmap.md) and [**MouseOffBitmap**](mouseoffbitmap.md) properties. There is no difference between enumerator values 2 and 3.<br/> |
| 4<br/>    | The image displayed for the task or background is a nontransparent bitmap image.<br/> The bitmap images are specified by the [**MouseOverBitmap**](mouseoverbitmap.md) and [**MouseOffBitmap**](mouseoffbitmap.md) properties.<br/>                                                        |



 

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





