---
title: PingIPAddress\_IN structure
description: The PingIPAddress\_IN structure holds the input data for the PingIPAddress method.
ms.assetid: 2dec9594-727e-44e6-8be8-2416ea77e447
keywords:
- PingIPAddress_IN structure Storage Devices
- PPingIPAddress_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PingIPAddress_IN
api_location:
- iscsimgt.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PingIPAddress\_IN structure

The PingIPAddress\_IN structure holds the input data for the PingIPAddress method.

## Syntax


```C++
typedef struct _PingIPAddress_IN {
  ULONG            RequestCount;
  ULONG            RequestSize;
  ULONG            Timeout;
  ISCSI_IP_Address Address;
} PingIPAddress_IN, *PPingIPAddress_IN;
```



## Members

<dl> <dt>

**RequestCount**
</dt> <dd>

The number of ping requests to be sent to the specified IP address.

</dd> <dt>

**RequestSize**
</dt> <dd>

The size of each request (in bytes) to be sent.

</dd> <dt>

**Timeout**
</dt> <dd>

The timeout (in milliseconds) for each ping request.

</dd> <dt>

**Address**
</dt> <dd>

The IP address to which the ping request must be sent. The IP address is provided by the [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure.

</dd> </dl>

## Remarks

We recommend that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PingIPAddress_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






