---
description: Represents the input layout fields of a vertex buffer, one per field in the vertex buffer.
MS-HAID: vspixengine.InputLayoutStruct
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: InputLayoutStruct structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: CC7AAC2F-FDB1-4AD8-9B87-A97EE557FEAC
api_name: 
 - InputLayoutStruct
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.inputlayoutstruct"></span>InputLayoutStruct structure

Represents the input layout fields of a vertex buffer, one per field in the vertex buffer.

## Syntax


```C++
} InputLayoutStruct;
```

## Members

**SemanticName**  
A COM string containing the name of the associated semantic.

**SemanticIndex**  
The index of the associated semantic.

**Format**  
The format of the field. For more information see the DXGI\_FORMAT enumeration.

**InputSlot**  
The associated input slot.

**AlignedByteOffset**  

**InputSlotClass**  

**InstanceDataStepRate**  

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



