---
Description: Returns an image that represents the object described by handle, or returns an error if the object does not have or cannot provide such an image.
ms.assetid: BE5DA08C-46F9-44E1-89CD-85613DD3BDE4
title: IVisualTreeService2RenderTargetBitmap method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVisualTreeService2::RenderTargetBitmap method

Returns an image that represents the object described by handle, or returns an error if the object does not have or cannot provide such an image.

## Syntax


```C++
virtual HRESULT RenderTargetBitmap(
  [in]  InstanceHandle            handle,
  [in]  RenderTargetBitmapOptions options,
  [in]  unsigned int              maxPixelWidth,
  [in]  unsigned int              maxPixelHeight,
  [out] IBitmapData               **ppBitmapData
) = 0;
```



## Parameters

<dl> <dt>

*handle* \[in\]
</dt> <dd>

The handle associated with the visual for which the caller is requesting a bitmap.

</dd> <dt>

*options* \[in\]
</dt> <dd>

A flag that specifies whether only the texture associated with the visual should be rendered, or whether the texture and its children should be rendered.

</dd> <dt>

*maxPixelWidth* \[in\]
</dt> <dd>

The maximum width, in pixels, of the returned bitmap.

</dd> <dt>

*maxPixelHeight* \[in\]
</dt> <dd>

The maximum height, in pixels, of the returned bitmap.

</dd> <dt>

*ppBitmapData* \[out\]
</dt> <dd>

The structure containing the requested bitmap information as well as information pertaining to that bitmap.

</dd> </dl>

## Return value

The possible return codes include, but are not limited to, the values shown in the following table.



| Return code                                                                                  | Description                                                                                                                               |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded. *ppBitmapData* will be set to an [**IBitmapData**](/windows/previous-versions/xamlom/nn-xamlom-ibitmapdata?branch=master) containing an image. <br/>                |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | The image could not be acquired or converted. *ppBitmapData* will be set to **NULL**. <br/>                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | *handle* does not refer to an object that can return an image, the *options* value is invalid, or *ppBitmapData* is **NULL**. <br/> |



 

## Remarks

The returned image will have

-   Format: **DXGI\_FORMAT\_B8G8R8A8\_UNORM**
-   AlphaMode: **DXGI\_ALPHA\_MODE\_PREMULTIPLIED**

If the requested bitmap falls within the max pixel width and max pixel height specified, then the bitmap will be returned in its original size. If the size of the image is larger than either one of the two max values specified, then, before the bitmap is returned, the bitmap will be uniformly scaled down until its dimensions fall within the boundaries of the *maxPixelWidth* and *maxPixelHeight* specified.

## See also

<dl> <dt>

[**IVisualTreeService2**](/windows/previous-versions/xamlom/nn-xamlom-ivisualtreeservice2?branch=master)
</dt> </dl>

 

 




