---
title: CHANGER\_MOVE\_MEDIUM structure
description: The CHANGER\_MOVE\_MEDIUM structure is used in conjunction with the IOCTL\_CHANGER\_MOVE\_MEDIUM request to move a piece of media from a source element to a destination.
ms.assetid: 'b19c8add-7377-40d2-8496-fcfa166ac143'
keywords: ["CHANGER_MOVE_MEDIUM structure Storage Devices", "PCHANGER_MOVE_MEDIUM structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CHANGER_MOVE_MEDIUM
api_location:
- ntddchgr.h
api_type:
- HeaderDef
---

# CHANGER\_MOVE\_MEDIUM structure

The CHANGER\_MOVE\_MEDIUM structure is used in conjunction with the [**IOCTL\_CHANGER\_MOVE\_MEDIUM**](ioctl-changer-move-medium.md) request to move a piece of media from a source element to a destination.

## Syntax


```C++
typedef struct _CHANGER_MOVE_MEDIUM {
  CHANGER_ELEMENT Transport;
  CHANGER_ELEMENT Source;
  CHANGER_ELEMENT Destination;
  BOOLEAN         Flip;
} CHANGER_MOVE_MEDIUM, *PCHANGER_MOVE_MEDIUM;
```



## Members

<dl> <dt>

**Transport**
</dt> <dd>

Contains a structure of type [**CHANGER\_ELEMENT**](changer-element.md) that indicates which transport element to use for the move operation. The **ElementType** member of the CHANGER\_ELEMENT structure must be assigned a value of **ChangerTransport**.

</dd> <dt>

**Source**
</dt> <dd>

Contains a structure of type [**CHANGER\_ELEMENT**](changer-element.md) that indicates the element that contains the piece of media to be moved to **Destination**. The **ElementType** must be **ChangerDrive**, **ChangerTransport**, **ChangerSlot**, or **ChangerIEPort**.

</dd> <dt>

**Destination**
</dt> <dd>

Contains a structure of type [**CHANGER\_ELEMENT**](changer-element.md) that indicates the destination of the piece of media originally at **Source**. The **ElementType** must be **ChangerDrive**, **ChangerTransport**, **ChangerSlot**, or **ChangerIEPort**.

</dd> <dt>

**Flip**
</dt> <dd>

Indicates, when **TRUE**, that the piece of media should be flipped. When **FALSE** the media is not ready to be flipped. This member is valid only if CHANGER\_MEDIUM\_FLIP is set in the **Features0** member of the [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) structure.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CHANGER\_MOVE\_MEDIUM**](ioctl-changer-move-medium.md)
</dt> <dt>

[**ChangerMoveMedium**](changermovemedium.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_MOVE_MEDIUM%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






