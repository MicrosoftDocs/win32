---
Description: Represents the input layout fields of a vertex buffer, one per field in the vertex buffer.
MS-HAID: vspixengine.InputLayoutStruct
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: InputLayoutStruct structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
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

 

 



