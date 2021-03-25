---
title: ID2D1Factory CreateDrawingStateBlock methods
description: Creates an ID2D1DrawingStateBlock that can be used with the SaveDrawingState and RestoreDrawingState methods of a render target.
ms.assetid: c2b5875f-9f14-4752-a426-2745fdaa543a
keywords:
- CreateDrawingStateBlock methods Direct2D
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

# ID2D1Factory::CreateDrawingStateBlock methods

Creates an [**ID2D1DrawingStateBlock**](/windows/win32/api/d2d1/nn-d2d1-id2d1drawingstateblock) that can be used with the [**SaveDrawingState**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-savedrawingstate) and [**RestoreDrawingState**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-restoredrawingstate) methods of a render target.

### Overload list



| Method                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDrawingStateBlock(D2D1\_DRAWING\_STATE\_DESCRIPTION\*,IDWriteRenderingParams\*,ID2D1DrawingStateBlock\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createdrawingstateblock(constd2d1_drawing_state_description_idwriterenderingparams_id2d1drawingstateblock)) | Creates an [**ID2D1DrawingStateBlock**](/windows/win32/api/d2d1/nn-d2d1-id2d1drawingstateblock) that can be used with the [**SaveDrawingState**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-savedrawingstate) and [**RestoreDrawingState**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-restoredrawingstate) methods of a render target.<br/>  |
| [**CreateDrawingStateBlock(ID2D1DrawingStateBlock\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createdrawingstateblock(id2d1drawingstateblock))                                                                                                                            | Creates an [**ID2D1DrawingStateBlock**](/windows/win32/api/d2d1/nn-d2d1-id2d1drawingstateblock) that can be used with the [**SaveDrawingState**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-savedrawingstate) and [**RestoreDrawingState**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-restoredrawingstate) methods of a render target. <br/> |
| [**CreateDrawingStateBlock(D2D1\_DRAWING\_STATE\_DESCRIPTION&,ID2D1DrawingStateBlock\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createdrawingstateblock(constd2d1_drawing_state_description__id2d1drawingstateblock))                                                      | Creates an [**ID2D1DrawingStateBlock**](/windows/win32/api/d2d1/nn-d2d1-id2d1drawingstateblock) that can be used with the [**SaveDrawingState**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-savedrawingstate) and [**RestoreDrawingState**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-restoredrawingstate) methods of a render target.<br/>  |



## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory)
</dt> </dl>

 

