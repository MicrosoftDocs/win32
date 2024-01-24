---
description: Declares an object to be a pick-any constant, to avoid redundant reloads of that object if it is used (and declared) in multiple places in the DirectXMath Library.
ms.assetid: FDE5C004-9E8E-4890-8FDC-987C1569D8E5
title: XMGLOBALCONST macro
ms.topic: reference
ms.date: 05/31/2018
---

# XMGLOBALCONST macro

Declares an object to be a *pick-any* constant, to avoid redundant reloads of that object if it is used (and declared) in multiple places in the DirectXMath Library.

## Syntax

``` syntax
#define XMGLOBALCONST  extern const __declspec(selectany)
```

## Remarks

Using XMGLOBALCONST permits the specification of global constants. This helps to reduce the size of an application's data segment, avoid redundant object creation and destruction, and reduce load and store operations.

## Requirements

**Header:** Declared in DirectXMath.h.

## Related topics

<dl> <dt>

[DirectXMath Library Macros](ovw-xnamath-reference-macros.md)
</dt> <dt>

[Global Constants in the DirectXMath Library](pg-xnamath-internals.md)
</dt> <dt>

[selectany](/previous-versions/visualstudio/visual-studio-6.0/aa273550(v=vs.60))
</dt> <dt>

[declspec](/previous-versions/visualstudio/visual-studio-6.0/aa273692(v=vs.60))
</dt> </dl>

 

 
