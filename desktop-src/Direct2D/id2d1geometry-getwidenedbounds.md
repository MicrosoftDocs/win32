---
title: ID2D1Geometry GetWidenedBounds methods
description: Gets the bounds of the geometry after it has been widened by the specified stroke width and style and transformed by the specified matrix.
ms.assetid: 1790ff9d-cb30-4cd4-af0d-385a37cad043
keywords:
- GetWidenedBounds methods Direct2D
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

# ID2D1Geometry::GetWidenedBounds methods

Gets the bounds of the geometry after it has been widened by the specified stroke width and style and transformed by the specified matrix.

### Overload list



| Method                                                                                                                                                                                                 | Description                                                                                                                                           |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetWidenedBounds(FLOAT,ID2D1StrokeStyle\*,D2D1\_MATRIX\_3X2\_F&,D2D1\_RECT\_F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-getwidenedbounds(float_id2d1strokestyle_constd2d1_matrix_3x2_f__d2d1_rect_f))              | Gets the bounds of the geometry after it has been widened by the specified stroke width and style and transformed by the specified matrix.<br/> |
| [**GetWidenedBounds(FLOAT,ID2D1StrokeStyle\*,D2D1\_MATRIX\_3X2\_F\*,D2D1\_RECT\_F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-getwidenedbounds(float_id2d1strokestyle_constd2d1_matrix_3x2_f_d2d1_rect_f))             | Gets the bounds of the geometry after it has been widened by the specified stroke width and style and transformed by the specified matrix.<br/> |
| [**GetWidenedBounds(FLOAT,ID2D1StrokeStyle\*,D2D1\_MATRIX\_3X2\_F&,FLOAT,D2D1\_RECT\_F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-getwidenedbounds(float_id2d1strokestyle_constd2d1_matrix_3x2_f__float_d2d1_rect_f))  | Gets the bounds of the geometry after it has been widened by the specified stroke width and style and transformed by the specified matrix.<br/> |
| [**GetWidenedBounds(FLOAT,ID2D1StrokeStyle\*,D2D1\_MATRIX\_3X2\_F\*,FLOAT,D2D1\_RECT\_F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-getwidenedbounds(float_id2d1strokestyle_constd2d1_matrix_3x2_f_float_d2d1_rect_f)) | Gets the bounds of the geometry after it has been widened by the specified stroke width and style and transformed by the specified matrix.<br/> |



## Examples

The following code shows how to use **GetWidenedBounds** to retrieve the bounds of the geometry after it has been widened by the specified stroke width and style and transformed by the specified matrix.


```C++
HRESULT hr = S_OK;

D2D1_RECT_F bounds;
D2D1_RECT_F inflatedPixelBounds;
D2D1_SIZE_U inflatedIntegerPixelSize;
D2D1_SIZE_U currentRTSize;
D2D1_MATRIX_3X2_F translateMatrix;
float dpiX, dpiY;
float scaleX = 1.0f;
float scaleY = 1.0f;

ID2D1BitmapRenderTarget *pCompatRT = NULL;
SafeReplace(&pCompatRT, *ppBitmapRT);

ID2D1SolidColorBrush *pBrush = NULL;

hr = pBaseRT->CreateSolidColorBrush(
    D2D1::ColorF(1.0f, 1.0f, 1.0f, 1.0f),
    &pBrush
    );
if (SUCCEEDED(hr))
{
    pBaseRT->GetDpi(&dpiX, &dpiY);
    if (fill)
    {
        hr = pIGeometry->GetBounds(
            pWorldTransform,
            &bounds
            );
    }
    else
    {
        hr = pIGeometry->GetWidenedBounds(
            strokeWidth,
            pStrokeStyle,
            pWorldTransform,
            &bounds
            );
    }

    if (SUCCEEDED(hr))
    {
        //
        // A rect where left > right is defined to be empty.
        //
        // The slightly baroque expression used below is an idiom that also
        // correctly handles NaNs (i.e., if any of the coordinates of the bounds is
        // a NaN, we want to treat the bounds as empty)
        //
        if (
            !(bounds.left <= bounds.right) ||
            !(bounds.top <= bounds.bottom)
           )
        {
            // Bounds are empty or ill-defined.

            // Make up a fake bounds
            inflatedPixelBounds.top = 0.0f;
            inflatedPixelBounds.left = 0.0f;
            inflatedPixelBounds.bottom = 1.0f;
            inflatedPixelBounds.right = 1.0f;
        }
        else
        {
            //
            // We inflate the pixel bounds by 1 in each direction to ensure we have
            // a border of completely transparent pixels around the geometry.  This
            // ensures that when the realization is stretched the alpha ramp still
            // smoothly falls off to 0 rather than being clipped by the rect.
            //
            inflatedPixelBounds.top = floorf(bounds.top*dpiY/96)-1.0f;
            inflatedPixelBounds.left = floorf(bounds.left*dpiX/96)-1.0f;
            inflatedPixelBounds.bottom = ceilf(bounds.bottom*dpiY/96)+1.0f;
            inflatedPixelBounds.right = ceilf(bounds.right*dpiX/96)+1.0f;
        }


        //
        // Compute the width and height of the underlying bitmap we will need.
        // Note: We round up the width and height to be a multiple of
        // sc_bitmapChunkSize. We do this primarily to ensure that we aren't
        // constantly reallocating bitmaps in the case where a realization is being
        // zoomed in on slowly and updated frequently.
        //

        inflatedIntegerPixelSize = D2D1::SizeU(
            static_cast<UINT>(inflatedPixelBounds.right - inflatedPixelBounds.left),
            static_cast<UINT>(inflatedPixelBounds.bottom - inflatedPixelBounds.top)
            );

        // Round up
        inflatedIntegerPixelSize.width =
            (inflatedIntegerPixelSize.width + sc_bitmapChunkSize - 1)/sc_bitmapChunkSize * sc_bitmapChunkSize;

        // Round up
        inflatedIntegerPixelSize.height =
            (inflatedIntegerPixelSize.height + sc_bitmapChunkSize - 1)/sc_bitmapChunkSize * sc_bitmapChunkSize;

        //
        // Compute the bounds we will pass to FillOpacityMask (which are in Device
        // Independent Pixels).
        //
        // Note: The DIP bounds do *not* use the rounded coordinates, since this
        // would cause us to render superfluous, fully-transparent pixels, which
        // would hurt fill rate.
        //
        D2D1_RECT_F inflatedDipBounds = D2D1::RectF(
            inflatedPixelBounds.left * 96/dpiX,
            inflatedPixelBounds.top * 96/dpiY,
            inflatedPixelBounds.right * 96/dpiX,
            inflatedPixelBounds.bottom * 96/dpiY
            );

        if (pCompatRT)
        {
            currentRTSize = pCompatRT->GetPixelSize();
        }
        else
        {
            // This will force the creation of a new target
            currentRTSize = D2D1::SizeU(0,0);
        }

        //
        // We need to ensure that our desired render target size isn't larger than
        // the max allowable bitmap size. If it is, we need to scale the bitmap
        // down by the appropriate amount.
        //

        if (inflatedIntegerPixelSize.width > maxRealizationDimension)
        {
            scaleX = maxRealizationDimension/static_cast<float>(inflatedIntegerPixelSize.width);
            inflatedIntegerPixelSize.width = maxRealizationDimension;
        }

        if (inflatedIntegerPixelSize.height > maxRealizationDimension)
        {
            scaleY = maxRealizationDimension/static_cast<float>(inflatedIntegerPixelSize.height);
            inflatedIntegerPixelSize.height = maxRealizationDimension;
        }


        //
        // If the necessary pixel dimensions are less than half the existing
        // bitmap's dimensions (in either direction), force the bitmap to be
        // reallocated to save memory.
        //
        // Note: The fact that we use > rather than >= is important for a subtle
        // reason: We'd like to have the property that repeated small changes in
        // geometry size do not cause repeated reallocations of memory. >= does not
        // ensure this property in the case where the geometry size is close to
        // sc_bitmapChunkSize, but > does.
        //
        // Example:
        //
        // Assume sc_bitmapChunkSize is 64 and the initial geometry width is 63
        // pixels. This will get rounded up to 64, and we will allocate a bitmap
        // with width 64. Now, say, we zoom in slightly, so the new geometry width
        // becomes 65 pixels. This will get rounded up to 128 pixels, and a new
        // bitmap will be allocated. Now, say the geometry drops back down to 63
        // pixels. This will get rounded up to 64. If we used >=, this would cause
        // another reallocation.  Since we use >, on the other hand, the 128 pixel
        // bitmap will be reused.
        //

        if (currentRTSize.width > 2*inflatedIntegerPixelSize.width ||
            currentRTSize.height > 2*inflatedIntegerPixelSize.height
           )
        {
            SafeRelease(&pCompatRT);
            currentRTSize.width = currentRTSize.height = 0;
        }

        if (inflatedIntegerPixelSize.width > currentRTSize.width ||
            inflatedIntegerPixelSize.height > currentRTSize.height
           )
        {
            SafeRelease(&pCompatRT);
        }

        if (!pCompatRT)
        {
            //
            // Make sure our new rendertarget is strictly larger than before.
            //
            currentRTSize.width =
                max(inflatedIntegerPixelSize.width, currentRTSize.width);

            currentRTSize.height =
                max(inflatedIntegerPixelSize.height, currentRTSize.height);

            D2D1_PIXEL_FORMAT alphaOnlyFormat =
                D2D1::PixelFormat(
                    DXGI_FORMAT_A8_UNORM,
                    D2D1_ALPHA_MODE_PREMULTIPLIED
                    );

            hr = pBaseRT->CreateCompatibleRenderTarget(
                NULL, // desiredSize
                &currentRTSize,
                &alphaOnlyFormat,
                D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS_NONE,
                &pCompatRT
                );
        }

        if (SUCCEEDED(hr))
        {
            //
            // Translate the geometry so it is flush against the left and top
            // sides of the render target.
            //

            translateMatrix =
                D2D1::Matrix3x2F::Translation(
                    -inflatedDipBounds.left,
                    -inflatedDipBounds.top
                    ) *
                D2D1::Matrix3x2F::Scale(
                    scaleX,
                    scaleY
                    );

            if (pWorldTransform)
            {
                pCompatRT->SetTransform(
                    *pWorldTransform * translateMatrix
                    );
            }
            else
            {
                pCompatRT->SetTransform(
                    translateMatrix
                    );
            }

            //
            // Render the geometry.
            //

            pCompatRT->BeginDraw();

            pCompatRT->Clear(
                D2D1::ColorF(0.0f, 0.0f, 0.0f, 0.0f)
                );

            if (fill)
            {
                pCompatRT->FillGeometry(
                    pIGeometry,
                    pBrush
                    );
            }
            else
            {
                pCompatRT->DrawGeometry(
                    pIGeometry,
                    pBrush,
                    strokeWidth,
                    pStrokeStyle
                    );
            }

            hr = pCompatRT->EndDraw();
            if (SUCCEEDED(hr))
            {
                //
                // Report back the source and dest bounds (to be used as input parameters
                // to FillOpacityMask.
                //
                *pMaskDestBounds = inflatedDipBounds;

                *pMaskSourceBounds = D2D1::Rect<float>(
                    0.0f,
                    0.0f,
                    static_cast<float>(inflatedDipBounds.right - inflatedDipBounds.left)*scaleX,
                    static_cast<float>(inflatedDipBounds.bottom - inflatedDipBounds.top)*scaleY
                    );

                if (*ppBitmapRT != pCompatRT)
                {
                    SafeReplace(ppBitmapRT, pCompatRT);
                }
            }
        }
    }
    pBrush->Release();
}
```



## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Geometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1geometry)
</dt> </dl>

 

