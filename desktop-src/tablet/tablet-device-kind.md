---
description: Indicates the type of tablet device such as a pen, mouse or touch sensitive digitizer.
ms.assetid: 4cca1e09-99c0-4357-a6ef-159bc8d17d57
title: TABLET_DEVICE_KIND enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TABLET_DEVICE_KIND
api_type: 
- NA
api_location: 
---

# TABLET\_DEVICE\_KIND enumeration

Indicates the type of tablet device such as a pen, mouse or touch sensitive digitizer.

## Syntax


```C++
typedef enum _TABLET_DEVICE_KIND { 
  TABLET_DEVICE_MOUSE  = 0,
  TABLET_DEVICE_PEN,
  TABLET_DEVICE_TOUCH
} TABLET_DEVICE_KIND;
```



## Constants

<dl> <dt>

<span id="TABLET_DEVICE_MOUSE"></span><span id="tablet_device_mouse"></span>**TABLET\_DEVICE\_MOUSE**
</dt> <dd>

The tablet is a mouse. This includes touchpads found on many laptop computers.

</dd> <dt>

<span id="TABLET_DEVICE_PEN"></span><span id="tablet_device_pen"></span>**TABLET\_DEVICE\_PEN**
</dt> <dd>

The tablet utilizes an electromagnetic pen and digitizer.

</dd> <dt>

<span id="TABLET_DEVICE_TOUCH"></span><span id="tablet_device_touch"></span>**TABLET\_DEVICE\_TOUCH**
</dt> <dd>

The tablet utilizes a touch sensitive digitizer.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



## See also

<dl> <dt>

[**ITablet2::GetDeviceKind Method**](itablet2-getdevicekind.md)
</dt> </dl>

 

 




