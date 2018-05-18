---
title: GetPresharedKeyForId\_IN structure
description: The GetPresharedKeyForId\_IN structure holds the input data for the GetPresharedKeyForId method.
ms.assetid: '4b3d3c5d-c34c-4ed8-bf62-1d885442ee1e'
keywords: ["GetPresharedKeyForId_IN structure Storage Devices", "PGetPresharedKeyForId_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- GetPresharedKeyForId_IN
api_location:
- iscsiop.h
api_type:
- HeaderDef
---

# GetPresharedKeyForId\_IN structure

The GetPresharedKeyForId\_IN structure holds the input data for the [GetPresharedKeyForId](https://msdn.microsoft.com/library/windows/hardware/ff554970) method. This method is required if the initiator supports Internet Key Exchange (IKE). It can help to determine whether IKE identification payload is configured with a preshared key.

## Syntax


```C++
typedef struct _GetPresharedKeyForId_IN {
  ULONG PortNumber;
  UCHAR IdType;
  ULONG IdSize;
  UCHAR Id[1];
} GetPresharedKeyForId_IN, *PGetPresharedKeyForId_IN;
```



## Members

<dl> <dt>

**PortNumber**
</dt> <dd>

The number of the port that the connection was made through. A value of -1 indicates that the connection can be made through any available port.

</dd> <dt>

**IdType**
</dt> <dd>

The type of identifier that the initiator puts in the Internet Key Exchange (IKE) identification payload to identify itself to the target.



| Identification payload type | Meaning                                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID\_IPV4\_ADDR<br/>   | The initiator identifies itself to the target during the key exchange with a single 4-byte version 4 IP address.<br/>                                     |
| ID\_FQDN<br/>         | The initiator identifies itself to the target during the key exchange with a fully qualified domain name string (for example, "website.com"). <br/>       |
| ID\_USER\_FQDN<br/>   | The initiator identifies itself to the target during the key exchange with a fully qualified user name string (for example, "someone@example.com"). <br/> |
| ID\_IPV6\_ADDR<br/>   | The initiator identifies itself to the target during the key exchange with a single 16-byte version 6 IP address.<br/>                                    |



 

</dd> <dt>

**IdSize**
</dt> <dd>

The size, in bytes, of the identifier in **Id***.*

</dd> <dt>

**Id**
</dt> <dd>

The identifier that the initiator uses to identify itself to the target during key exchange.

</dd> </dl>

## Remarks

You must implement this method if the initiator supports IKE.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[GetPresharedKeyForId](https://msdn.microsoft.com/library/windows/hardware/ff554970)
</dt> <dt>

[**GetPresharedKeyForId\_OUT**](getpresharedkeyforid-out.md)
</dt> <dt>

[MSiSCSI\_SecurityConfigOperations WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563135)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GetPresharedKeyForId_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






