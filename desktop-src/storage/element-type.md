---
title: ELEMENT\_TYPE enumeration
description: The ELEMENT\_TYPE enumeration provides a list of changer element types defined by the SCSI-3 specification.
ms.assetid: '909e0645-3824-40ff-bec9-128a9939eb1e'
keywords: ["ELEMENT_TYPE enumeration Storage Devices", "PELEMENT_TYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ELEMENT_TYPE
api_location:
- ntddchgr.h
api_type:
- HeaderDef
---

# ELEMENT\_TYPE enumeration

The ELEMENT\_TYPE enumeration provides a list of changer element types defined by the *SCSI-3* specification.

## Syntax


```C++
typedef enum _ELEMENT_TYPE { 
  AllElements        = 0,
  ChangerTransport   = 1,
  ChangerSlot        = 2,
  ChangerIEPort      = 3,
  ChangerDrive       = 4,
  ChangerDoor        = 5,
  ChangerKeypad      = 6,
  ChangerMaxElement  = 7
} ELEMENT_TYPE, *PELEMENT_TYPE;
```



## Constants

<dl> <dt>

<span id="AllElements"></span><span id="allelements"></span><span id="ALLELEMENTS"></span>**AllElements**
</dt> <dd>

Indicates all elements of a changer, including its robotic transport, drives, slots, and IEport. **AllElements** is valid only in a [**ChangerGetElementStatus**](changergetelementstatus.md) or [**ChangerInitializeElementStatus**](changerinitializeelementstatus.md) call.

</dd> <dt>

<span id="ChangerTransport"></span><span id="changertransport"></span><span id="CHANGERTRANSPORT"></span>**ChangerTransport**
</dt> <dd>

Indicates the changer's robotic transport element, which is used to move media between IEports, slots, and drives.

</dd> <dt>

<span id="ChangerSlot"></span><span id="changerslot"></span><span id="CHANGERSLOT"></span>**ChangerSlot**
</dt> <dd>

Indicates a storage element, which is a slot in the changer in which media is stored when not mounted in a drive.

</dd> <dt>

<span id="ChangerIEPort"></span><span id="changerieport"></span><span id="CHANGERIEPORT"></span>**ChangerIEPort**
</dt> <dd>

Indicates an import/export element (IEport), which is a single or multiple-cartridge access port in some changers. An element is an IEport only if it is possible to move a piece of media from a slot to the IEport.

</dd> <dt>

<span id="ChangerDrive"></span><span id="changerdrive"></span><span id="CHANGERDRIVE"></span>**ChangerDrive**
</dt> <dd>

Indicates a data transfer element where data can be read from and written to media.

</dd> <dt>

<span id="ChangerDoor"></span><span id="changerdoor"></span><span id="CHANGERDOOR"></span>**ChangerDoor**
</dt> <dd>

Indicates a mechanism that provides access to all media in a changer at one time (as compared to an IEport that provides access to one or more, but not all, media). For example, a large front door or a magazine that contains all media in the changer are elements of this type. **ChangerDoor** is valid only in a [**ChangerSetAccess**](changersetaccess.md) call.

</dd> <dt>

<span id="ChangerKeypad"></span><span id="changerkeypad"></span><span id="CHANGERKEYPAD"></span>**ChangerKeypad**
</dt> <dd>

Indicates the keypad or other input control on the front panel of a changer. **ChangerKeypad** is valid only in a [**ChangerSetAccess**](changersetaccess.md) call.

</dd> <dt>

<span id="ChangerMaxElement"></span><span id="changermaxelement"></span><span id="CHANGERMAXELEMENT"></span>**ChangerMaxElement**
</dt> <dd>

Indicates the upper limit of the enumerators in this enumeration.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**ChangerGetElementStatus**](changergetelementstatus.md)
</dt> <dt>

[**ChangerInitializeElementStatus**](changerinitializeelementstatus.md)
</dt> <dt>

[**ChangerSetAccess**](changersetaccess.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ELEMENT_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






