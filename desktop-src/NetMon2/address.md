---
description: Is obsolete and should not be used.
ms.assetid: cbe89779-403d-406e-af3c-d6530bf3008e
title: ADDRESS structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ADDRESS
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# ADDRESS structure

The **ADDRESS** structure is obsolete and should not be used.

## Syntax


```C++
typedef struct _ADDRESS {
  DWORD Type;
  union {
    BYTE                  MACAddress[MAC_ADDRESS_SIZE];
    BYTE                  IPAddress[IP_ADDRESS_SIZE];
    BYTE                  IPXRawAddress[IPX_ADDRESS_SIZE];
    IPX_ADDRESS           IPXAddress;
    BYTE                  VinesIPRawAddress[VINES_IP_ADDRESS_SIZE];
    VINES_IP_ADDRESS      VinesIPAddress;
    ETHERNET_SRC_ADDRESS  EthernetSrcAddress;
    ETHERNET_DST_ADDRESS  EthernetDstAddress;
    TOKENRING_SRC_ADDRESS TokenringSrcAddress;
    TOKENRING_DST_ADDRESS TokenringDstAddress;
    FDDI_SRC_ADDRESS      FddiSrcAddress;
    FDDI_DST_ADDRESS      FddiDstAddress;
  };
  WORD  Flags;
} ADDRESS, *LPADDRESS;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Address type. Values can be one of the following:

<dl> <dd>ADDRESS_TYPE_ETHERNET</dd> <dd>ADDRESS_TYPE_IP</dd> <dd>ADDRESS_TYPE_IPX</dd> <dd>ADDRESS_TYPE_TOKENRING</dd> <dd>ADDRESS_TYPE_FDDI</dd> <dd>ADDRESS_TYPE_XNS</dd> <dd>ADDRESS_TYPE_ANY</dd> <dd>ADDRESS_TYPE_ANY_GROUP</dd> <dd>ADDRESS_TYPE_FIND_HIGHEST</dd> <dd>ADDRESS_TYPE_VINES_IP</dd> <dd>ADDRESS_TYPE_LOCAL_ONLY</dd> <dd>ADDRESS_TYPE_ATM</dd> <dd>ADDRESS_TYPE_1394</dd> </dl> </dd> <dt>

**MACAddress**
</dt> <dd>

View of the data expressed as a raw MAC address.

</dd> <dt>

**IPAddress**
</dt> <dd>

View of the data expressed as a raw IP address.

</dd> <dt>

**IPXRawAddress**
</dt> <dd>

View of the data expressed as a raw IPX address.

</dd> <dt>

**IPXAddress**
</dt> <dd>

View of the data expressed as a decoded IPX address value.

</dd> <dt>

**VinesIPRawAddress**
</dt> <dd>

View of the data expressed as a raw Vines IP address.

</dd> <dt>

**VinesIPAddress**
</dt> <dd>

View of the data expressed as a decoded Vines IP address.

</dd> <dt>

**EthernetSrcAddress**
</dt> <dd>

View of the data expressed as an Ethernet source address.

</dd> <dt>

**EthernetDstAddress**
</dt> <dd>

View of the data expressed as an Ethernet destination address.

</dd> <dt>

**TokenringSrcAddress**
</dt> <dd>

A view of the data as a token ring source address.

</dd> <dt>

**TokenringDstAddress**
</dt> <dd>

A view of the data as a token ring destination address.

</dd> <dt>

**FddiSrcAddress**
</dt> <dd>

View of the data expressed as an FDDI source address.

</dd> <dt>

**FddiDstAddress**
</dt> <dd>

View of the data expressed as an FDDI destination address.

</dd> <dt>

**Flags**
</dt> <dd>

A set of flags that modify the address properties.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




