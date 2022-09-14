---
title: WMDMMessage enumeration
description: The WMDMMessage enumeration type defines message types and states.
ms.assetid: '49a77100-8890-4e40-852f-c6fd436f22c5'
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
ms.topic: reference
ms.date: 05/31/2018
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



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 





