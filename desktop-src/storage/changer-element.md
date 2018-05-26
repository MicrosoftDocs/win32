---
title: CHANGER\_ELEMENT structure
description: The CHANGER\_ELEMENT structure contains a description of a changer element.
ms.assetid: 85035147-0ae8-482a-9a12-1e4e53ae1969
keywords:
- CHANGER_ELEMENT structure Storage Devices
- PCHANGER_ELEMENT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CHANGER_ELEMENT
api_location:
- ntddchgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CHANGER\_ELEMENT structure

The CHANGER\_ELEMENT structure contains a description of a changer element.

## Syntax


```C++
typedef struct _CHANGER_ELEMENT {
  ELEMENT_TYPE ElementType;
  ULONG        ElementAddress;
} CHANGER_ELEMENT, *PCHANGER_ELEMENT;
```



## Members

<dl> <dt>

**ElementType**
</dt> <dd>

Indicates the type of element. Can be one of the following values taken from the [**ELEMENT\_TYPE**](element-type.md) enumeration.

<dl> <dt>

<span id="AllElements"></span><span id="allelements"></span><span id="ALLELEMENTS"></span>**AllElements**
</dt> <dd>

All elements of a changer, including its robotic transport, drives, slots, and IEport. **AllElements** is valid only in a **ChangerGetElementStatus** or **ChangerInitializeElementStatus** call.

</dd> </dl>

<dl> <dt>

<span id="ChangerTransport"></span><span id="changertransport"></span><span id="CHANGERTRANSPORT"></span>**ChangerTransport**
</dt> <dd>

The changer's robotic transport element, which is used to move media between IEports, slots, and drives.

</dd> </dl>

<dl> <dt>

<span id="ChangerSlot"></span><span id="changerslot"></span><span id="CHANGERSLOT"></span>**ChangerSlot**
</dt> <dd>

A storage element, which is a slot in the changer in which media is stored when not mounted in a drive.

</dd> </dl>

<dl> <dt>

<span id="ChangerIEPort"></span><span id="changerieport"></span><span id="CHANGERIEPORT"></span>**ChangerIEPort**
</dt> <dd>

An import/export element (IEport), which is a single or multiple-cartridge access port in some changers. An element is an IEport only if it is possible to move a piece of media from a slot to the IEport.

</dd> </dl>

<dl> <dt>

<span id="ChangerDrive"></span><span id="changerdrive"></span><span id="CHANGERDRIVE"></span>**ChangerDrive**
</dt> <dd>

A data transfer element where data can be read from and written to media.

</dd> </dl>

<dl> <dt>

<span id="ChangerDoor"></span><span id="changerdoor"></span><span id="CHANGERDOOR"></span>**ChangerDoor**
</dt> <dd>

A mechanism that provides access to all media in a changer at one time (as compared to an IEport that provides access to one or more, but not all, media). For example, a large front door or a magazine that contains all media in the changer are elements of this type. **ChangerDoor** is valid only in a **ChangerSetAccess** call.

</dd> </dl>

<dl> <dt>

<span id="ChangerKeypad"></span><span id="changerkeypad"></span><span id="CHANGERKEYPAD"></span>**ChangerKeypad**
</dt> <dd>

The keypad or other input control on the front panel of a changer. **ChangerKeypad** is valid only in a **ChangerSetAccess** call.

</dd> </dl> </dd> <dt>

**ElementAddress**
</dt> <dd>

Indicates the element's zero-based address used by the system. A changer miniclass driver is responsible for translating this address to the device-specific address used by the changer.

</dd> </dl>

## Remarks

CHANGER\_ELEMENT is used by both the changer class driver and a changer miniclass driver to describe a changer element.

On input, a changer miniclass driver must translate the zero-based address in **ElementAddress** to a device-specific address before accessing the element. On output, the driver must translate a device-specific address to the zero-based equivalent before filling in **ElementAddress**.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**CHANGER\_ELEMENT\_LIST**](changer-element-list.md)
</dt> <dt>

[**CHANGER\_ELEMENT\_STATUS**](changer-element-status.md)
</dt> <dt>

[**ELEMENT\_TYPE**](element-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_ELEMENT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






