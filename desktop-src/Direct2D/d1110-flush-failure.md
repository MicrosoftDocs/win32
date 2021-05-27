---
title: D1110 Flush Failure
ms.assetid: 44f122b0-08e3-4f63-a575-0f3619144823
description: A Flush call by a render target failed
keywords:
- D1110 Flush Failure Direct2D
topic_type:
- apiref
api_name:
- D1110 Flush Failure
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# D1110: Flush Failure

A Flush call by a render target failed \[*resource*\]. Tags \[*tag1*, *tag2*\].

## Placeholders

<dl> <dt>

<span id="resource"></span><span id="RESOURCE"></span>*resource*
</dt> <dd>

The address of the render target.

</dd> <dt>

<span id="tag1"></span><span id="TAG1"></span>*tag1*
</dt> <dd>

The first tag value. See [**SetTags**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-settags) for more information.

</dd> <dt>

<span id="tag2"></span><span id="TAG2"></span>*tag2*
</dt> <dd>

The second tag value. See [**SetTags**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-settags) for more information.

</dd> </dl> 

| &nbsp;      |  &nbsp; |
|-------------|---------|
| Error Level | Warning |



 

## Examples

**Example 1:** The following code shows that a draw call is in an invalid state. To avoid the warning message, use [**SetAntialiasMode**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-setantialiasmode) to set D2D1\_ANTIALIAS\_MODE\_ANTIALIASED before a [**FillOpacityMask**](id2d1rendertarget-fillopacitymask.md) call.


```C++
       
        if(SUCCEEDED(hr))
        {
            hr = m_pRenderTarget->CreateBitmap(
                D2D1::SizeU(1,1),
                NULL,
                0,
                D2D1::BitmapProperties(D2D1::PixelFormat(
                    DXGI_FORMAT_A8_UNORM, 
                    D2D1_ALPHA_MODE_PREMULTIPLIED
                    )),
                &m_pBitmap
                );                    
        }


        m_pRenderTarget->FillOpacityMask(
            m_pBitmapMask,
            m_pFernBitmapBrush,
            D2D1_OPACITY_MASK_CONTENT_GRAPHICS,
            &rcBrushRect
            );

        hr = m_pRenderTarget->Flush();

        hr = m_pRenderTarget->EndDraw();
```





This example produces the following debug message:

``` syntax
D2D DEBUG WARNING - Flush call on render target failed [88990001]. Tags [0, 0].
```

**Example 2:** The following code shows that the [**Flush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-flush) is called after the [**EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) call.


```C++
        // Calling Flush after EndDraw generates a
        // flush error message from the debug layer.
       hr = m_pRenderTarget->EndDraw();       
       
       hr = m_pRenderTarget->Flush();
```



This example produces the following debug message:

``` syntax
DEBUG WARNING - A Flush call by a render target failed [88990001]. Tags [0, 0].
```

## Possible Causes

The [**Flush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-flush) call can fail for one of two reasons. It may fail because the method was called outside of the [**BeginDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-begindraw)/[**EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) call, or it may fail because there was an error produced by one of the render target operations that have been processed since the last **Flush** call or **EndDraw** call. To fix the issue, the application should determine the cause of the error and take the appropriate action.

## Fixes

There are many reasons that a [**Flush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-flush) call might fail. The application should determine the cause of the error and take the appropriate action.

 

 