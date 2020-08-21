---
title: IDCompositionMatrixTransform SetMatrixElement(int, int, IDCompositionAnimation ) method
description: Animates the value of one element of the matrix of this 2D transform.
ms.assetid: 16A9E136-5F0C-4F34-A127-BF06C4530499
keywords:
- SetMatrixElement method DirectComposition
- SetMatrixElement method DirectComposition , IDCompositionMatrixTransform interface
- IDCompositionMatrixTransform interface DirectComposition , SetMatrixElement method
topic_type:
- apiref
api_name:
- IDCompositionMatrixTransform.SetMatrixElement
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IDCompositionMatrixTransform::SetMatrixElement(int, int, IDCompositionAnimation\*) method

Animates the value of one element of the matrix of this 2D transform.

## Syntax


```C++
HRESULT SetMatrixElement(
  [in] int                    row,
  [in] int                    column,
  [in] IDCompositionAnimation *animation
);
```



## Parameters

<dl> <dt>

*row* \[in\]
</dt> <dd>

The row index of the element to change. This value must be between 0 and 2, inclusive.

</dd> <dt>

*column* \[in\]
</dt> <dd>

The column index of the element to change. This value must be between 0 and 1, inclusive.

</dd> <dt>

*animation* \[in\]
</dt> <dd>

An animation that represents how the value of the specified element changes over time. This parameter must not be NULL.

</dd> </dl>

## Return value

If the function succeeds, it returns S\_OK. Otherwise, it returns an **HRESULT** error code. See [DirectComposition Error Codes](directcomposition-error-codes.md) for a list of error codes.

## Remarks

This method makes a copy of the specified animation. If the object referenced by the *animation* parameter is changed after calling this method, the change does not affect the element unless this method is called again. If the element was previously animated, calling this method replaces the previous animation with the new animation.

This method fails if *animation* is an invalid pointer or if it was not created by the same [**IDCompositionDevice**](/windows/win32/api/dcomp/nn-dcomp-idcompositiondevice) interface as the affected transform. The interface cannot be a custom implementation; only interfaces created by Microsoft DirectComposition can be used with this method.

## See also

<dl> <dt>

[**IDCompositionMatrixTransform**](/windows/win32/api/dcomp/nn-dcomp-idcompositionmatrixtransform)
</dt> </dl>

 

 