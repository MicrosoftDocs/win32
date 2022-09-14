---
title: IManipulationProcessor MinimumScaleRotateRadius property
description: Specifies how large the distance contacts on a scale or rotate gesture need to be to trigger manipulation.
ms.assetid: b4c49f41-c5ea-4c6a-872b-2d982e588b09
keywords:
- MinimumScaleRotateRadius property Windows Touch
- MinimumScaleRotateRadius property Windows Touch , IManipulationProcessor interface
- IManipulationProcessor interface Windows Touch , MinimumScaleRotateRadius property
topic_type:
- apiref
api_name:
- IManipulationProcessor.MinimumScaleRotateRadius
- IManipulationProcessor.get_MinimumScaleRotateRadius
- IManipulationProcessor.put_MinimumScaleRotateRadius
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
- manipulations.h
---

# IManipulationProcessor::MinimumScaleRotateRadius property

Specifies how large the distance contacts on a scale or rotate gesture need to be to trigger manipulation.

This property is read/write.

## Syntax


```C++
HRESULT put_MinimumScaleRotateRadius(
  [in]  FLOAT MinimumScaleRotateRadius
);

HRESULT get_MinimumScaleRotateRadius(
  [out] FLOAT *MinimumScaleRotateRadius
);
```



## Property value

Specifies the minimum distance between contacts to trigger scale or rotate gestures.

## Error codes

## Remarks

> [!Note]  
> This property is set in centipixels (100ths of a pixel).

 

Setting this value will make the manipulation processor ignore gestures that have too small of a radius. This is useful if you want to prevent a user from manipulating an object to too small of a radius. For example, if you are using a manipulation processor with a circle and want the ensure that it maintains a radius greater than 100 pixels, you would set this value to 10000.

## Examples


```C++
pManip->put_MinimumScaleRotateRadius(4000.0f);  
```



## See also

<dl> <dt>

[**IManipulationProcessor**](/windows/desktop/api/manipulations/nn-manipulations-imanipulationprocessor)
</dt> </dl>

 

 




