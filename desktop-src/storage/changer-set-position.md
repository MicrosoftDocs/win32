---
title: CHANGER\_SET\_POSITION structure
description: The CHANGER\_SET\_POSITION structure is used in conjunction with theIOCTL\_CHANGER\_SET\_POSITION request to set the changers robotic transport mechanism to the specified element address.
ms.assetid: 1c71473a-98db-41a1-9ca5-ce59f345b5f7
keywords:
- CHANGER_SET_POSITION structure Storage Devices
- PCHANGER_SET_POSITION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CHANGER_SET_POSITION
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

# CHANGER\_SET\_POSITION structure

The CHANGER\_SET\_POSITION structure is used in conjunction with the[**IOCTL\_CHANGER\_SET\_POSITION**](ioctl-changer-set-position.md) request to set the changer's robotic transport mechanism to the specified element address.

## Syntax


```C++
typedef struct _CHANGER_SET_POSITION {
  CHANGER_ELEMENT Transport;
  CHANGER_ELEMENT Destination;
  BOOLEAN         Flip;
} CHANGER_SET_POSITION, *PCHANGER_SET_POSITION;
```



## Members

<dl> <dt>

**Transport**
</dt> <dd>

Contains a structure of type [**CHANGER\_ELEMENT**](changer-element.md) that indicates the transport element to move. The **ElementType** member of the CHANGER\_ELEMENT structure must be assigned a value of **ChangerTransport**.

</dd> <dt>

**Destination**
</dt> <dd>

Contains a structure of type [**CHANGER\_ELEMENT**](changer-element.md) that indicates the final destination of the transport element. **ElementType** must be **ChangerSlot**, **ChangerDrive**, or **ChangerIEPort**.

</dd> <dt>

**Flip**
</dt> <dd>

Indicates, when **TRUE**, that the **Transport** should be flipped. When **FALSE** this member indicates that the transport is not ready to be flipped. This member is applicable only if CHANGER\_MEDIUM\_FLIP is set in the **Features0** member of the [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) structure.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**ChangerSetPosition**](changersetposition.md)
</dt> <dt>

[**IOCTL\_CHANGER\_SET\_POSITION**](ioctl-changer-set-position.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_SET_POSITION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






