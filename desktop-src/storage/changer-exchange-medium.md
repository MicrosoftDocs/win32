---
title: CHANGER\_EXCHANGE\_MEDIUM structure
description: The CHANGER\_EXCHANGE\_MEDIUM structure is used with the IOCTL\_CHANGER\_EXCHANGE\_MEDIUM request to exchange locations of two pieces of media.
ms.assetid: 'b0f03d83-61d3-4aa1-ae4e-a8bdc9f13a9f'
keywords: ["CHANGER_EXCHANGE_MEDIUM structure Storage Devices", "PCHANGER_EXCHANGE_MEDIUM structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CHANGER_EXCHANGE_MEDIUM
api_location:
- ntddchgr.h
api_type:
- HeaderDef
---

# CHANGER\_EXCHANGE\_MEDIUM structure

The CHANGER\_EXCHANGE\_MEDIUM structure is used with the [**IOCTL\_CHANGER\_EXCHANGE\_MEDIUM**](ioctl-changer-exchange-medium.md) request to exchange locations of two pieces of media.

## Syntax


```C++
typedef struct _CHANGER_EXCHANGE_MEDIUM {
  CHANGER_ELEMENT Transport;
  CHANGER_ELEMENT Source;
  CHANGER_ELEMENT Destination1;
  CHANGER_ELEMENT Destination2;
  BOOLEAN         Flip1;
  BOOLEAN         Flip2;
} CHANGER_EXCHANGE_MEDIUM, *PCHANGER_EXCHANGE_MEDIUM;
```



## Members

<dl> <dt>

**Transport**
</dt> <dd>

Indicates which transport element to use for the exchange operation. This member contains a structure of type [**CHANGER\_ELEMENT**](changer-element.md). The **ElementType** member of the CHANGER\_ELEMENT structure must be assigned a value of **ChangerTransport**.

</dd> <dt>

**Source**
</dt> <dd>

Indicates the element that contains the piece of media to be moved.

</dd> <dt>

**Destination1**
</dt> <dd>

Indicates the destination of the piece of media originally at **Source**.

</dd> <dt>

**Destination2**
</dt> <dd>

Indicates the destination of the piece of media originally at **Destination1**.

</dd> <dt>

**Flip1**
</dt> <dd>

Indicates, when **TRUE**, that the piece of media moved to **Destination1** should be flipped. This member is valid only if the **Features0** member of the [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) structure is set to CHANGER\_MEDIUM\_FLIP. When **FALSE**, this member indicates that the media does not ready to be flipped.

</dd> <dt>

**Flip2**
</dt> <dd>

Indicates, when **TRUE**, that the medium moved to **Destination2** should be flipped. This member is valid only if the **Features0** member of the GET\_CHANGER\_PARAMETERS structure is set to CHANGER\_MEDIUM\_FLIP. When **FALSE**, this member indicates that the media does not ready to be flipped.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CHANGER\_EXCHANGE\_MEDIUM**](ioctl-changer-exchange-medium.md)
</dt> <dt>

[**ChangerExchangeMedium**](changerexchangemedium.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_EXCHANGE_MEDIUM%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






