---
title: WMDMMessage enumeration
description: The WMDMMessage enumeration type defines message types and states.
ms.assetid: e178db6b-2493-442e-95d1-04609b7726fe
keywords:
- WMDMMessage enumeration windows Media Device Manager
topic_type:
- apiref
api_name:
- WMDMMessage
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WMDMMessage enumeration

The **WMDMMessage** enumeration type defines message types and states.

## Syntax


```C++
enum WMDMMessage {
  WMDM_MSG_DEVICE_ARRIVAL, 
  WMDM_MSG_DEVICE_REMOVAL, 
  WMDM_MSG_MEDIA_ARRIVAL, 
  WMDM_MSG_MEDIA_REMOVAL 

};
```



## Constants

<dl> <dt>

<span id="WMDM_MSG_DEVICE_ARRIVAL"></span><span id="wmdm_msg_device_arrival"></span>**WMDM\_MSG\_DEVICE\_ARRIVAL**
</dt> <dd>

A Windows Media Device Manager device has been plugged in.

</dd> <dt>

<span id="WMDM_MSG_DEVICE_REMOVAL"></span><span id="wmdm_msg_device_removal"></span>**WMDM\_MSG\_DEVICE\_REMOVAL**
</dt> <dd>

A Windows Media Device Manager device has been removed.

</dd> <dt>

<span id="WMDM_MSG_MEDIA_ARRIVAL"></span><span id="wmdm_msg_media_arrival"></span>**WMDM\_MSG\_MEDIA\_ARRIVAL**
</dt> <dd>

Media has been inserted in a Windows Media Device Manager device.

</dd> <dt>

<span id="WMDM_MSG_MEDIA_REMOVAL"></span><span id="wmdm_msg_media_removal"></span>**WMDM\_MSG\_MEDIA\_REMOVAL**
</dt> <dd>

Media has been removed from a Windows Media Device Manager device.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 





