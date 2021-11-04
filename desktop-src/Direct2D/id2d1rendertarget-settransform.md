---
title: ID2D1RenderTarget SetTransform methods
description: Applies the specified transform to the render target, replacing the existing transformation. All subsequent drawing operations occur in the transformed space.
ms.assetid: 04799366-6458-40ff-a2fb-5d227eab041d
keywords:
- SetTransform methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
api_name: 
---

# ID2D1RenderTarget::SetTransform methods

Applies the specified transform to the render target, replacing the existing transformation. All subsequent drawing operations occur in the transformed space.

### Overload list



| Method                                                                                              | Description                                                                                                                                                                |
|:----------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetTransform(D2D1\_MATRIX\_3X2\_F&)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-settransform(constd2d1_matrix_3x2_f_))  | Applies the specified transform to the render target, replacing the existing transformation. All subsequent drawing operations occur in the transformed space. <br/> |
| [**SetTransform(D2D1\_MATRIX\_3X2\_F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-settransform(constd2d1_matrix_3x2_f)) | Applies the specified transform to the render target, replacing the existing transformation. All subsequent drawing operations occur in the transformed space.<br/>  |



## Examples

The following example uses the **SetTransform** method to apply a rotation to the render target. For the complete example, see [How to Rotate an Object](how-to-rotate.md).


```C++
// Apply the rotation transform to the render target.
m_pRenderTarget->SetTransform(
    D2D1::Matrix3x2F::Rotation(
        45.0f,
        D2D1::Point2F(468.0f, 331.5f))
    );
```



For additional examples showing how to transform a render target, see [How to Scale an Object](how-to-scale.md), [How to Skew an Object](how-to-skew.md), and [How to Translate an Object](how-to-translate.md).

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget)
</dt> <dt>

[Transforms Overview](direct2d-transforms-overview.md)
</dt> <dt>

[How to Rotate an Object](how-to-rotate.md)
</dt> <dt>

[How to Scale an Object](how-to-scale.md)
</dt> <dt>

[How to Skew an Object](how-to-skew.md)
</dt> <dt>

[How to Translate an Object](how-to-translate.md)
</dt> <dt>

[How to Apply Multiple Transforms to an Object](how-to-apply-multiple-transforms.md)
</dt> </dl>

 

