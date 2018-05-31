---
title: BDANODE\_DESCRIPTOR structure
description: The BDANODE\_DESCRIPTOR structure describes a control node in BDA device filter.
ms.assetid: 6ab03494-6564-4d4d-83bf-a9a6e588aac3
keywords:
- BDANODE_DESCRIPTOR structure Microsoft TV Technologies
- PBDANODE_DESCRIPTOR structure pointer Microsoft TV Technologies
topic_type:
- apiref
api_name:
- BDANODE_DESCRIPTOR
api_location:
- Bdatypes.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# BDANODE\_DESCRIPTOR structure

The **BDANODE\_DESCRIPTOR** structure describes a control node in BDA device filter.

## Syntax


```C++
typedef struct _BDANODE_DESCRIPTOR {
  ULONG ulBdaNodeType;
  GUID  guidFunction;
  GUID  guidName;
} BDANODE_DESCRIPTOR, *PBDANODE_DESCRIPTOR;
```



## Members

<dl> <dt>

**ulBdaNodeType**
</dt> <dd>

Specifies the node type as it is used in the BDA template topology. Currently, the only defined node type is NODE\_TYPE\_PID\_MAPPER.

</dd> <dt>

**guidFunction**
</dt> <dd>

Specifies the function of the node in the topology. Set this parameter to one of the KSNODE\_BDA\_*XXX* GUID values in header file Bdamedia.h.

</dd> <dt>

**guidName**
</dt> <dd>

Specifies a GUID value that can be used to look up a displayable name for the node.

</dd> </dl>

## Remarks

This structure is used by the [**IBDA\_Topology::GetNodeDescriptors**](/windows/desktop/api/Bdaiface/nf-bdaiface-ibda_topology-getnodedescriptors) method.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[BDA Structures](bda-structures.md)
</dt> </dl>

 

 





