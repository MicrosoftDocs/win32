---
description: Represents information about a single entry in the buffer layout of a mesh.
MS-HAID: vspixengine.MeshDataBufferLayoutEntry
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: MeshDataBufferLayoutEntry structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: FE1D796C-DFD8-4C6E-9914-3063408FE565
api_name: 
 - MeshDataBufferLayoutEntry
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.meshdatabufferlayoutentry"></span>MeshDataBufferLayoutEntry structure

Represents information about a single entry in the buffer layout of a mesh.

## Syntax


```C++
} MeshDataBufferLayoutEntry;
```

## Members

**pName**  
A COM string containing the name of the entry.

**numComponents**  
The number of homogenous components (values) that make up this entry.

**isPosition**  
true if the entry is a position; otherwise, false.

**format**  
The data format of the entry (register). For more information, see the REGISTER\_FORMAT enumeration.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



