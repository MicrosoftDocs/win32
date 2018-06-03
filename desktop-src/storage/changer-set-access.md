---
title: CHANGER\_SET\_ACCESS structure
description: The CHANGER\_SET\_ACCESS structure is used in conjunction with theIOCTL\_CHANGER\_SET\_ACCESS request to set the state of the device's import/export port (IEport), door, or keypad.
ms.assetid: 4349d772-89c6-4201-9d9d-2e0590d61424
keywords:
- CHANGER_SET_ACCESS structure Storage Devices
- PCHANGER_SET_ACCESS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CHANGER_SET_ACCESS
api_location:
- ntddchgr.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# CHANGER\_SET\_ACCESS structure

The CHANGER\_SET\_ACCESS structure is used in conjunction with the[**IOCTL\_CHANGER\_SET\_ACCESS**](ioctl-changer-set-access.md) request to set the state of the device's import/export port (IEport), door, or keypad.

## Syntax


```C++
typedef struct _CHANGER_SET_ACCESS {
  CHANGER_ELEMENT Element;
  ULONG           Control;
} CHANGER_SET_ACCESS, *PCHANGER_SET_ACCESS;
```



## Members

<dl> <dt>

**Element**
</dt> <dd>

Contains a [**CHANGER\_ELEMENT**](changer-element.md) structure that specifies the element type and the zero-based address of the element to set. The **ElementType** member of the CHANGER\_ELEMENT structure must be assigned one of the following values:

**ChangerIEPortChangerDoorChangerKeypad**

</dd> <dt>

**Control**
</dt> <dd>

Specifies the operation to perform on the element. The **Features0** member of [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) indicates whether the changer supports a particular category of operation.

<dl> <dt>

<span id="LOCK_ELEMENT"></span><span id="lock_element"></span>LOCK\_ELEMENT
</dt> <dd>

Lock the door, IEport, or keypad. Valid only if CHANGER\_LOCK\_UNLOCK is set.

</dd> <dt>

<span id="UNLOCK_ELEMENT"></span><span id="unlock_element"></span>UNLOCK\_ELEMENT
</dt> <dd>

Unlock the door, IEport, or keypad. Valid only if CHANGER\_LOCK\_UNLOCK is set.

</dd> <dt>

<span id="EXTEND_IEPORT"></span><span id="extend_ieport"></span>EXTEND\_IEPORT
</dt> <dd>

Extend the IEport. Valid only if CHANGER\_OPEN\_IEPORT is set.

</dd> <dt>

<span id="RETRACT_IEPORT"></span><span id="retract_ieport"></span>RETRACT\_IEPORT
</dt> <dd>

Retract the IEport. Valid only if CHANGER\_CLOSE\_IEPORT is set.

</dd> </dl> </dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CHANGER\_SET\_ACCESS**](ioctl-changer-set-access.md)
</dt> <dt>

[**ChangerSetAccess**](changersetaccess.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_SET_ACCESS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






