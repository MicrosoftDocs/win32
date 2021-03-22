---
description: This topic applies to Windows XP Service Pack 2 or later. The KSTOPOLOGY\_CONNECTION structure describes a node connection within a kernel-streaming (KS) filter. A node can be connected to another node within the filter, or to a pin on the filter.
ms.assetid: 8fca47b7-4c52-46db-809c-77a0e3414276
title: KSTOPOLOGY_CONNECTION structure (Ks.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KSTOPOLOGY_CONNECTION
api_type: 
- HeaderDef
api_location: 
- Ks.h
---

# KSTOPOLOGY\_CONNECTION structure

This topic applies to Windows XP Service Pack 2 or later.

The **KSTOPOLOGY\_CONNECTION** structure describes a node connection within a kernel-streaming (KS) filter. A node can be connected to another node within the filter, or to a pin on the filter.

## Syntax


```C++
typedef struct {
  ULONG FromNode;
  ULONG FromNodePin;
  ULONG ToNode;
  ULONG ToNodePin;
} KSTOPOLOGY_CONNECTION, *PKSTOPOLOGY_CONNECTION;
```



## Members

<dl> <dt>

**FromNode**
</dt> <dd>

Index of the upstream node in the connection. If the upstream connection is a pin, rather than a node, the value is KSFILTER\_NODE.

</dd> <dt>

**FromNodePin**
</dt> <dd>

If the value of the **FromNode** field is KSFILTER\_NODE, this field specifies the index of the upstream pin. Otherwise, this field is ignored.

</dd> <dt>

**ToNode**
</dt> <dd>

Index of the downstream node in the connection. If the downstream connection is a pin, rather than a node, the value is KSFILTER\_NODE.

</dd> <dt>

**ToNodePin**
</dt> <dd>

If the value of the **ToNode** field is KSFILTER\_NODE, this field specifies the index of the downstream pin. Otherwise, this field is ignored.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ks.h</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Structures](directshow-structures.md)
</dt> <dt>

[**IKsTopologyInfo::get\_ConnectionInfo**](/previous-versions/windows/desktop/api/Vidcap/nf-vidcap-ikstopologyinfo-get_connectioninfo)
</dt> </dl>

 

 




