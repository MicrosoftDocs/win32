---
description: Packages the object type, version, and size information that is required in many NDIS 6.0 structures.
ms.assetid: 0dfb6022-1d8d-4bd9-bde3-2ee6d683f223
title: NDIS_OBJECT_HEADER structure (Ntddndis.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDIS_OBJECT_HEADER
api_type: 
- HeaderDef
api_location: 
- ntddndis.h
---

# NDIS\_OBJECT\_HEADER structure

The **NDIS\_OBJECT\_HEADER** structure packages the object type, version, and size information that is required in many NDIS 6.0 structures.

## Syntax


```C++
typedef struct _NDIS_OBJECT_HEADER {
  UCHAR  Type;
  UCHAR  Revision;
  USHORT Size;
} NDIS_OBJECT_HEADER, *PNDIS_OBJECT_HEADER;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Specifies the type of NDIS object that a structure describes.

</dd> <dt>

**Revision**
</dt> <dd>

Specifies the revision number of this structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size, in bytes, of the NDIS structure that contains the **NDIS\_OBJECT\_HEADER**. This size includes the size of the **NDIS\_OBJECT\_HEADER** member and all other members of the structure.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                       |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                                                        |
| Header<br/>                   | <dl> <dt>Ntddndis.h (include Windot11.h)</dt> </dl> |



## See also

<dl> <dt>

[**DOT11\_BSSID\_LIST**](dot11-bssid-list.md)
</dt> </dl>

 

 




