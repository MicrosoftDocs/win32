---
title: HBA\_ipaddress structure
description: The HBA\_ipaddress structure specifies an IP address in a way that is independent of the version of the IP protocol in use.
ms.assetid: 'c3f79350-29e8-4e31-a31d-359c9781777d'
keywords: ["HBA_ipaddress structure Storage Devices", "HBA_IPADDRESS structure Storage Devices", "PHBA_IPADDRESS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_IPADDRESS
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_ipaddress structure

The HBA\_ipaddress structure specifies an IP address in a way that is independent of the version of the IP protocol in use.

## Syntax


```C++
typedef struct HBA_ipaddress {
  int   ipversion;
  union {
    unsigned char ipv4address[4];
    unsigned char ipv6address[16];
  } ipaddress;
} HBA_IPADDRESS, *PHBA_IPADDRESS;
```



## Members

<dl> <dt>

**ipversion**
</dt> <dd>

Indicates the version of the IP protocol in use.

</dd> <dt>

**ipaddress**
</dt> <dd> <dl> <dt>

**ipv4address**
</dt> <dd>

Contains a dotted decimal IP4 address if version 4 of the IP protocol is in use.

</dd> <dt>

**ipv6address**
</dt> <dd>

Contains a dotted decimal IP6 address if version 6 of the IP protocol is in use.

</dd> </dl> </dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_ipaddress%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





