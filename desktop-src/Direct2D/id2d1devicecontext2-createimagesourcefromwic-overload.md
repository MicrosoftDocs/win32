---
title: ID2D1DeviceContext2 CreateImageSourceFromWic methods (D2d1\_3.h)
description: Creates an image source object from a WIC bitmap source, while populating all pixel memory within the image source. The image is loaded and stored while using a minimal amount of memory.
ms.assetid: af02630d-a9ca-f5b4-6f2a-31a73ef603e5
keywords:
- CreateImageSourceFromWic methods Direct2D
topic_type:
- apiref
api_location:
- d2d1_3.h
api_type:
- HeaderDef
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1DeviceContext2::CreateImageSourceFromWic methods

Creates an image source object from a WIC bitmap source, while populating all pixel memory within the image source. The image is loaded and stored while using a minimal amount of memory.

### Overload list



| Method                                                                                                                                                                                       | Description                                                                                                                                                       |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateImageSourceFromWic (IWICBitmapSource\*, D2D1\_IMAGE\_SOURCE\_LOADING\_OPTIONS, ID2D1ImageSourceFromWic\*\*)**](/windows/win32/api/d2d1_3/nf-d2d1_3-id2d1devicecontext2-createimagesourcefromwic(iwicbitmapsource_d2d1_image_source_loading_options_id2d1imagesourcefromwic))                   | Version of the method that allows you to specify the WIC bitmap source, the output image source object, and loading options with default alpha mode.<br/>   |
| [**CreateImageSourceFromWic (IWICBitmapSource\*, D2D1\_IMAGE\_SOURCE\_LOADING\_OPTIONS, D2D1\_ALPHA\_MODE, ID2D1ImageSourceFromWic\*\*)**](/windows/win32/api/d2d1_3/nf-d2d1_3-id2d1devicecontext2-createimagesourcefromwic(iwicbitmapsource_d2d1_image_source_loading_options_d2d1_alpha_mode_id2d1imagesourcefromwic)) | Version of the method that allows you to specify the WIC bitmap source, the output image source object, and loading options, and alpha mode.<br/>           |
| [**CreateImageSourceFromWic (IWICBitmapSource\*, ID2D1ImageSourceFromWic\*\*)**](/windows/win32/api/d2d1_3/nf-d2d1_3-id2d1devicecontext2-createimagesourcefromwic(iwicbitmapsource_id2d1imagesourcefromwic))                                                          | Version of the method that allows you to specify the WIC bitmap source and the output image source object with default loading opitons and alpha mode.<br/> |



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D2d1\_3.h</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1DeviceContext2**](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1devicecontext2)
</dt> </dl>

�

�
