---
title: ISCSI\_IP\_Address structure
description: The ISCSI\_IP\_Address structure defines an IP address.
ms.assetid: 'ec4c2add-33e0-4e3d-8f19-892cca4720a7'
keywords: ["ISCSI_IP_Address structure Storage Devices", "PISCSI_IP_Address structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_IP_Address
api_location:
- iscsidef.h
api_type:
- HeaderDef
---

# ISCSI\_IP\_Address structure

The ISCSI\_IP\_Address structure defines an IP address.

## Syntax


```C++
typedef struct _ISCSI_IP_Address {
  ULONG Type;
  ULONG IpV4Address;
  UCHAR IpV6Address[16];
  ULONG IpV6FlowInfo;
  ULONG IpV6ScopeId;
  WCHAR TextAddress[256 + 1];
} ISCSI_IP_Address, *PISCSI_IP_Address;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

A [**ISCSIIPADDRESSTYPE**](iscsiipaddresstype.md) value that indicates the type of IP address.

</dd> <dt>

**IpV4Address**
</dt> <dd>

If **Type** = **ISCSI\_IP\_ADDRESS\_IPV4**, the binary version 4 IP address. Otherwise, **IpV4Address** is not defined.

</dd> <dt>

**IpV6Address**
</dt> <dd>

If **Type** = **ISCSI\_IP\_ADDRESS\_IPV6**, the binary version 6 IP address. Otherwise, **IpV6Address** is not defined.

</dd> <dt>

**IpV6FlowInfo**
</dt> <dd>

If **Type** = **ISCSI\_IP\_ADDRESS\_IPV6**, the flow information for this IP address, as defined in version 6 of the IP protocol. Otherwise, **IpV6FlowInfo** is not defined.

</dd> <dt>

**IpV6ScopeId**
</dt> <dd>

If **Type** = **ISCSI\_IP\_ADDRESS\_IPV6**, the scope ID of this IP address, as defined in version 6 of the IP protocol,. Otherwise, **IpV6ScopeId** is not defined.

</dd> <dt>

**TextAddress**
</dt> <dd>

If **Type** = **ISCSI\_IP\_ADDRESS\_TEXT**, the DNS or dotted decimal text address. Otherwise, **TextAddress** is not defined.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsidef.h (include Iscsidef.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[**ISCSIIPADDRESSTYPE**](iscsiipaddresstype.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_IP_Address%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






