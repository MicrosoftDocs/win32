---
Description: The TakePicture method of the Item object causes a digital camera device to take a picture and returns an Item object that represents the resulting image. This method applies only to digital camera devices.
ms.assetid: d181048e-21ef-4fcc-a50a-5ba44bbde72e
title: Item.TakePicture method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Item.TakePicture method

The **TakePicture** method of the [**Item**](-wia-item.md) object causes a digital camera device to take a picture and returns an **Item** object that represents the resulting image. This method applies only to digital camera devices.

## Syntax


```JScript
retVal = Item.TakePicture()
```



## Parameters

This method has no parameters.

## Return value

Type: **IWiaDispatchItem**

An [**Item**](-wia-item.md) object that represents the image that this method creates.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wiavideo.h</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




