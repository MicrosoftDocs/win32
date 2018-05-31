---
title: IVMDisplay \_GenerateThumbnail method
description: The \_GenerateThumbnail method returns an array of pixels representing a thumbnail image of the virtual machine's screen.
ms.assetid: fc7a0c55-933c-4c14-92bf-dd1b600b526f
keywords:
- _GenerateThumbnail method Virtual Server
- _GenerateThumbnail method Virtual Server , IVMDisplay interface
- IVMDisplay interface Virtual Server , _GenerateThumbnail method
topic_type:
- apiref
api_name:
- IVMDisplay._GenerateThumbnail
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMDisplay::\_GenerateThumbnail method

The **\_GenerateThumbnail** method returns an array of pixels representing a thumbnail image of the virtual machine's screen.

## Syntax


```C++
HRESULT _GenerateThumbnail(
  [out] unsigned long thumbnailImage[3072]
);
```



## Parameters

<dl> <dt>

*thumbnailImage* \[out\]
</dt> <dd>

The array of pixels representing a thumbnail image of the virtual machine's screen.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code/value                                                                                                                                                 | Description                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/> |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>    |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error occurred.<br/> |



 

## Remarks

This interface returns the thumbnail more efficiently than the [**Thumbnail**](ivmdisplay-thumbnail.md) property, but is not usable from scripting clients. The thumbnail is always 64 pixels wide by 48 pixels high. Each pixel is 32 bits, where the upper 8 bits represent the blue value of the pixel, the next 8 bits represent the green value of the pixel, and the next 8 bits represent the red value of the pixel. The first 64 elements in the array is the first row of the thumbnail, the next 64 elements is the second row, and so on. This method returns a static array of pixels, which is more efficient than returning a **SAFEARRAY** of **VARIANT**s, but is not compatible with scripting clients.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDisplay**](ivmdisplay.md)
</dt> </dl>

 

 





