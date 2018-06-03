---
title: Pointer Device Change
description: Values that can be passed in the wParam parameter of the WM\_POINTERDEVICECHANGE message.
ms.assetid: B95191D7-820B-445A-A3A4-811F9F1A8C4F
topic_type:
- apiref
api_name:
- PDC_ARRIVAL
- PDC_REMOVAL
- PDC_ORIENTATION_0
- PDC_ORIENTATION_90
- PDC_ORIENTATION_180
- PDC_ORIENTATION_270
- PDC_MODE_DEFAULT
- PDC_MODE_CENTERED
- PDC_MAPPING_CHANGE
- PDC_RESOLUTION
- PDC_ORIGIN
- PDC_MODE_ASPECTRATIOPRESERVED
api_location:
- winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Pointer Device Change

Values that can be passed in the *wParam* parameter of the [**WM\_POINTERDEVICECHANGE**](wm-pointerdevicechange.md) message.

<dl> <dt>

<span id="PDC_ARRIVAL"></span><span id="pdc_arrival"></span>**PDC\_ARRIVAL**
</dt> <dd> <dl> <dt>

0x001
</dt> <dt>



A new device is attached.


</dt> </dl> </dd> <dt>

<span id="PDC_REMOVAL"></span><span id="pdc_removal"></span>**PDC\_REMOVAL**
</dt> <dd> <dl> <dt>

0x002
</dt> <dt>



A device has been detached.


</dt> </dl> </dd> <dt>

<span id="PDC_ORIENTATION_0"></span><span id="pdc_orientation_0"></span>**PDC\_ORIENTATION\_0**
</dt> <dd> <dl> <dt>

0x004
</dt> <dt>



Orientation of the device.


</dt> </dl> </dd> <dt>

<span id="PDC_ORIENTATION_90"></span><span id="pdc_orientation_90"></span>**PDC\_ORIENTATION\_90**
</dt> <dd> <dl> <dt>

0x008
</dt> <dt>



Orientation of the device.


</dt> </dl> </dd> <dt>

<span id="PDC_ORIENTATION_180"></span><span id="pdc_orientation_180"></span>**PDC\_ORIENTATION\_180**
</dt> <dd> <dl> <dt>

0x010
</dt> <dt>



Orientation of the device.


</dt> </dl> </dd> <dt>

<span id="PDC_ORIENTATION_270"></span><span id="pdc_orientation_270"></span>**PDC\_ORIENTATION\_270**
</dt> <dd> <dl> <dt>

0x020
</dt> <dt>



Orientation of the device.


</dt> </dl> </dd> <dt>

<span id="PDC_MODE_DEFAULT"></span><span id="pdc_mode_default"></span>**PDC\_MODE\_DEFAULT**
</dt> <dd> <dl> <dt>

0x040
</dt> <dt>



The default display mode.


</dt> </dl> </dd> <dt>

<span id="PDC_MODE_CENTERED"></span><span id="pdc_mode_centered"></span>**PDC\_MODE\_CENTERED**
</dt> <dd> <dl> <dt>

0x080
</dt> <dt>



Centered display mode.


</dt> </dl> </dd> <dt>

<span id="PDC_MAPPING_CHANGE"></span><span id="pdc_mapping_change"></span>**PDC\_MAPPING\_CHANGE**
</dt> <dd> <dl> <dt>

0x100
</dt> <dt>



The change in display to digitizer mapping.


</dt> </dl> </dd> <dt>

<span id="PDC_RESOLUTION"></span><span id="pdc_resolution"></span>**PDC\_RESOLUTION**
</dt> <dd> <dl> <dt>

0x200
</dt> <dt>



Display resolution.


</dt> </dl> </dd> <dt>

<span id="PDC_ORIGIN"></span><span id="pdc_origin"></span>**PDC\_ORIGIN**
</dt> <dd> <dl> <dt>

0x400
</dt> <dt>



The display origin.


</dt> </dl> </dd> <dt>

<span id="PDC_MODE_ASPECTRATIOPRESERVED"></span><span id="pdc_mode_aspectratiopreserved"></span>**PDC\_MODE\_ASPECTRATIOPRESERVED**
</dt> <dd> <dl> <dt>

0x800
</dt> <dt>



The display aspect ratio.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[Constants](constants.md)
</dt> <dt>

[**POINTER\_INFO**](/windows/desktop/api/Winuser/ns-winuser-tagpointer_info)
</dt> </dl>

 

 





