---
title: PingIPAddress\_OUT structure
description: The PingIPAddress\_OUT structure holds the output data for the PingIPAddress method.
ms.assetid: '26512dc5-9d3d-4dd5-bce3-37feb64dded8'
keywords: ["PingIPAddress_OUT structure Storage Devices", "PPingIPAddress_OUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- PingIPAddress_OUT
api_location:
- iscsimgt.h
api_type:
- HeaderDef
---

# PingIPAddress\_OUT structure

The PingIPAddress\_OUT structure holds the output data for the PingIPAddress method.

## Syntax


```C++
typedef struct _PingIPAddress_OUT {
  ULONG Status;
  ULONG ResponsesReceived;
} PingIPAddress_OUT, *PPingIPAddress_OUT;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

A status of type ISDSC\_ERROR.

</dd> <dt>

**ResponsesReceived**
</dt> <dd>

The number of responses that were received.

</dd> </dl>

## Remarks

We recommend that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PingIPAddress_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





