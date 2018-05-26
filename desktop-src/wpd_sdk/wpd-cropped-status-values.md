---
Description: The WPD\_CROPPED\_STATUS\_VALUES enumeration type describes the cropping status of an image.
ms.assetid: 7ee87fb7-1d17-4e89-aee7-e7abacbd790d
title: WPD\_CROPPED\_STATUS\_VALUES enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WPD\_CROPPED\_STATUS\_VALUES enumeration

The **WPD\_CROPPED\_STATUS\_VALUES** enumeration type describes the cropping status of an image.

## Syntax


```C++
typedef enum WPD_CROPPED_STATUS_VALUES { 
  WPD_CROPPED_STATUS_NOT_CROPPED            = 0,
  WPD_CROPPED_STATUS_CROPPED                = 1,
  WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED  = 2
} ;
```



## Constants

<dl> <dt>

<span id="WPD_CROPPED_STATUS_NOT_CROPPED"></span><span id="wpd_cropped_status_not_cropped"></span>**WPD\_CROPPED\_STATUS\_NOT\_CROPPED**
</dt> <dd>

The image has not been cropped.

</dd> <dt>

<span id="WPD_CROPPED_STATUS_CROPPED"></span><span id="wpd_cropped_status_cropped"></span>**WPD\_CROPPED\_STATUS\_CROPPED**
</dt> <dd>

The image has been cropped.

</dd> <dt>

<span id="WPD_CROPPED_STATUS_SHOULD_NOT_BE_CROPPED"></span><span id="wpd_cropped_status_should_not_be_cropped"></span>**WPD\_CROPPED\_STATUS\_SHOULD\_NOT\_BE\_CROPPED**
</dt> <dd>

The image has not been, and should not be, cropped.

</dd> </dl>

## Remarks

Indicates the cropped status of an image. This enumeration is used by the [WPD\_IMAGE\_CROPPED\_STATUS](image-properties.md#wpd-image-cropped-status) property.

## Requirements



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




