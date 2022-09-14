---
description: Windows 8 disables standard Windows 2000 Display Driver Model (XDDM) mirror drivers and offers the desktop duplication API instead.
ms.assetid: 523FBFAD-5D78-4EE3-A3B7-8FD5BA39DC46
title: Desktop Duplication API
ms.topic: article
ms.date: 05/31/2018
---

# Desktop Duplication API

Windows 8 disables standard Windows 2000 Display Driver Model (XDDM) mirror drivers and offers the desktop duplication API instead. The desktop duplication API provides remote access to a desktop image for collaboration scenarios. Apps can use the desktop duplication API to access frame-by-frame updates to the desktop. Because apps receive updates to the desktop image in a DXGI surface, the apps can use the full power of the GPU to process the image updates.

-   [Updating the desktop image data](#updating-the-desktop-image-data)
-   [Rotating the desktop image](#rotating-the-desktop-image)
-   [Updating the desktop pointer](#updating-the-desktop-pointer)
-   [Related topics](#related-topics)

## Updating the desktop image data

DXGI provides a surface that contains a current desktop image through the new [**IDXGIOutputDuplication::AcquireNextFrame**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-acquirenextframe) method. The format of the desktop image is always [**DXGI\_FORMAT\_B8G8R8A8\_UNORM**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) no matter what the current display mode is. Along with this surface, these [**IDXGIOutputDuplication**](/windows/desktop/api/DXGI1_2/nn-dxgi1_2-idxgioutputduplication) methods return the indicated types of info that help you determine which pixels within the surface you need to process:

-   [**IDXGIOutputDuplication::GetFrameDirtyRects**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-getframedirtyrects) returns dirty regions, which are non-overlapping rectangles that indicate the areas of the desktop image that the operating system updated since you processed the previous desktop image.
-   [**IDXGIOutputDuplication::GetFrameMoveRects**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-getframemoverects) returns move regions, which are rectangles of pixels in the desktop image that the operating system moved to another location within the same image. Each move region consists of a destination rectangle and a source point. The source point specifies the location from where the operating system copied the region and the destination rectangle specifies to where the operating system moved that region. Move regions are always non-stretched regions so the source is always the same size as the destination.

Suppose the desktop image was transmitted over a slow connection to your remote client app. The amount of data that is sent over the connection is reduced by receiving only data about how your client app must move regions of pixels rather than actual pixel data. To process the moves, your client app must have stored the complete last image.

While the operating system accumulates unprocessed desktop image updates, it might run out of space to accurately store the update regions. In this situation, the operating system starts to accumulate the updates by coalescing them with existing update regions to cover all new updates. As a result, the operating system covers pixels that it has not actually updated in that frame yet. But this situation doesn’t produce visual issues on your client app because you receive the entire desktop image and not just the updated pixels.

To reconstruct the correct desktop image, your client app must first process all the move regions and then process all the dirty regions. Either of these lists of dirty and move regions can be completely empty. The example code from the [Desktop Duplication Sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/DXGI%20desktop%20duplication%20sample) shows how to process both the dirty and move regions in a single frame:


```C++
//
// Get next frame and write it into Data
//
HRESULT DUPLICATIONMANAGER::GetFrame(_Out_ FRAME_DATA* Data)
{
    HRESULT hr = S_OK;

    IDXGIResource* DesktopResource = NULL;
    DXGI_OUTDUPL_FRAME_INFO FrameInfo;

    //Get new frame
    hr = DeskDupl->AcquireNextFrame(500, &FrameInfo, &DesktopResource);
    if (FAILED(hr))
    {
        if ((hr != DXGI_ERROR_ACCESS_LOST) && (hr != DXGI_ERROR_WAIT_TIMEOUT))
        {
            DisplayErr(L"Failed to acquire next frame in DUPLICATIONMANAGER", L"Error", hr);
        }
        return hr;
    }

    // If still holding old frame, destroy it
    if (AcquiredDesktopImage)
    {
        AcquiredDesktopImage->Release();
        AcquiredDesktopImage = NULL;
    }

    // QI for IDXGIResource
    hr = DesktopResource->QueryInterface(__uuidof(ID3D11Texture2D), reinterpret_cast<void **>(&AcquiredDesktopImage));
    DesktopResource->Release();
    DesktopResource = NULL;
    if (FAILED(hr))
    {
        DisplayErr(L"Failed to QI for ID3D11Texture2D from acquired IDXGIResource in DUPLICATIONMANAGER", L"Error", hr);
        return hr;
    }

    // Get metadata
    if (FrameInfo.TotalMetadataBufferSize)
    {
        // Old buffer too small
        if (FrameInfo.TotalMetadataBufferSize > MetaDataSize)
        {
            if (MetaDataBuffer)
            {
                delete [] MetaDataBuffer;
                MetaDataBuffer = NULL;
            }
            MetaDataBuffer = new (std::nothrow) BYTE[FrameInfo.TotalMetadataBufferSize];
            if (!MetaDataBuffer)
            {
                DisplayErr(L"Failed to allocate memory for metadata in DUPLICATIONMANAGER", L"Error", E_OUTOFMEMORY);
                MetaDataSize = 0;
                Data->MoveCount = 0;
                Data->DirtyCount = 0;
                return E_OUTOFMEMORY;
            }
            MetaDataSize = FrameInfo.TotalMetadataBufferSize;
        }

        UINT BufSize = FrameInfo.TotalMetadataBufferSize;

        // Get move rectangles
        hr = DeskDupl->GetFrameMoveRects(BufSize, reinterpret_cast<DXGI_OUTDUPL_MOVE_RECT*>(MetaDataBuffer), &BufSize);
        if (FAILED(hr))
        {
            if (hr != DXGI_ERROR_ACCESS_LOST)
            {
                DisplayErr(L"Failed to get frame move rects in DUPLICATIONMANAGER", L"Error", hr);
            }
            Data->MoveCount = 0;
            Data->DirtyCount = 0;
            return hr;
        }
        Data->MoveCount = BufSize / sizeof(DXGI_OUTDUPL_MOVE_RECT);

        BYTE* DirtyRects = MetaDataBuffer + BufSize;
        BufSize = FrameInfo.TotalMetadataBufferSize - BufSize;

        // Get dirty rectangles
        hr = DeskDupl->GetFrameDirtyRects(BufSize, reinterpret_cast<RECT*>(DirtyRects), &BufSize);
        if (FAILED(hr))
        {
            if (hr != DXGI_ERROR_ACCESS_LOST)
            {
                DisplayErr(L"Failed to get frame dirty rects in DUPLICATIONMANAGER", L"Error", hr);
            }
            Data->MoveCount = 0;
            Data->DirtyCount = 0;
            return hr;
        }
        Data->DirtyCount = BufSize / sizeof(RECT);

        Data->MetaData = MetaDataBuffer;
    }

    Data->Frame = AcquiredDesktopImage;
    Data->FrameInfo = FrameInfo;

    return hr;
}

//
// Release frame
//
HRESULT DUPLICATIONMANAGER::DoneWithFrame()
{
    HRESULT hr = S_OK;

    hr = DeskDupl->ReleaseFrame();
    if (FAILED(hr))
    {
        DisplayErr(L"Failed to release frame in DUPLICATIONMANAGER", L"Error", hr);
        return hr;
    }

    if (AcquiredDesktopImage)
    {
        AcquiredDesktopImage->Release();
        AcquiredDesktopImage = NULL;
    }

    return hr;
}
```



## Rotating the desktop image

You must add explicit code to your desktop duplication client app to support rotated modes. In a rotated mode, the surface that you receive from [**IDXGIOutputDuplication::AcquireNextFrame**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-acquirenextframe) is always in the un-rotated orientation, and the desktop image is rotated within the surface. For example, if the desktop is set to 768x1024 at 90 degrees rotation, **AcquireNextFrame** returns a 1024x768 surface with the desktop image rotated within it. Here are some rotation examples.



| Display mode set from display control panel | Display mode returned by GDI or DXGI | Surface returned from [**AcquireNextFrame**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-acquirenextframe)                |
|---------------------------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1024x768 landscape                          | 1024x768 0 degree rotation           | 1024x768\[newline\] ![nonrotated remote desktop](images/dxgi-outdupl-0-rotate.png)<br/>            |
| 1024x768 portrait                           | 768x1024 90 degree rotation          | 1024x768\[newline\] ![rotated 90 degrees remote desktop](images/dxgi-outdupl-90-rotate.png)<br/>   |
| 1024x768 landscape (flipped)                | 1024x768 180 degree rotation         | 1024x768\[newline\] ![rotated 180 degrees remote desktop](images/dxgi-outdupl-180-rotate.png)<br/> |
| 1024x768 portrait (flipped)                 | 768x1024 270 degree rotation         | 1024x768\[newline\] ![rotated 270 degrees remote desktop](images/dxgi-outdupl-270-rotate.png)<br/> |



 

The code in your desktop duplication client app must rotate the desktop image appropriately before you display the desktop image.

> [!Note]  
> In multi-monitor scenarios, you can rotate the desktop image for each monitor independently.

 

## Updating the desktop pointer

You need to use the desktop duplication API to determine if your client app must draw the mouse pointer shape onto the desktop image. Either the mouse pointer is already drawn onto the desktop image that [**IDXGIOutputDuplication::AcquireNextFrame**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-acquirenextframe) provides or the mouse pointer is separate from the desktop image. If the mouse pointer is drawn onto the desktop image, the pointer position data that is reported by **AcquireNextFrame** (in the **PointerPosition** member of [**DXGI\_OUTDUPL\_FRAME\_INFO**](/windows/desktop/api/DXGI1_2/ns-dxgi1_2-dxgi_outdupl_frame_info) that the *pFrameInfo* parameter points to) indicates that a separate pointer isn’t visible. If the graphics adapter overlays the mouse pointer on top of the desktop image, **AcquireNextFrame** reports that a separate pointer is visible. So, your client app must draw the mouse pointer shape onto the desktop image to accurately represent what the current user will see on their monitor.

To draw the desktop’s mouse pointer, use the **PointerPosition** member of [**DXGI\_OUTDUPL\_FRAME\_INFO**](/windows/desktop/api/DXGI1_2/ns-dxgi1_2-dxgi_outdupl_frame_info) from the *pFrameInfo* parameter of [**AcquireNextFrame**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-acquirenextframe) to determine where to locate the top left hand corner of the mouse pointer on the desktop image. When you draw the first frame, you must use the [**IDXGIOutputDuplication::GetFramePointerShape**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-getframepointershape) method to obtain info about the shape of the mouse pointer. Each call to **AcquireNextFrame** to get the next frame also provides the current pointer position for that frame. On the other hand, you need to use **GetFramePointerShape** again only if the shape changes. So, keep a copy of the last pointer image and use it to draw on the desktop unless the shape of the mouse pointer changes.

> [!Note]  
> Together with the pointer shape image, [**GetFramePointerShape**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutputduplication-getframepointershape) provides the size of the hot spot location. The hot spot is given for informational purposes only. The location of where to draw the pointer image is independent to the hotspot.

 

This example code from the [Desktop Duplication Sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/DXGI%20desktop%20duplication%20sample) shows how to get the mouse pointer shape:


```C++
//
// Retrieves mouse info and write it into PtrInfo
//
HRESULT DUPLICATIONMANAGER::GetMouse(_Out_ PTR_INFO* PtrInfo, _In_ DXGI_OUTDUPL_FRAME_INFO* FrameInfo, INT OffsetX, INT OffsetY)
{
    HRESULT hr = S_OK;

    // A non-zero mouse update timestamp indicates that there is a mouse position update and optionally a shape change
    if (FrameInfo->LastMouseUpdateTime.QuadPart == 0)
    {
        return hr;
    }

    bool UpdatePosition = true;

    // Make sure we don't update pointer position wrongly
    // If pointer is invisible, make sure we did not get an update from another output that the last time that said pointer
    // was visible, if so, don't set it to invisible or update.
    if (!FrameInfo->PointerPosition.Visible && (PtrInfo->WhoUpdatedPositionLast != OutputNumber))
    {
        UpdatePosition = false;
    }

    // If two outputs both say they have a visible, only update if new update has newer timestamp
    if (FrameInfo->PointerPosition.Visible && PtrInfo->Visible && (PtrInfo->WhoUpdatedPositionLast != OutputNumber) && (PtrInfo->LastTimeStamp.QuadPart > FrameInfo->LastMouseUpdateTime.QuadPart))
    {
        UpdatePosition = false;
    }

    // Update position
    if (UpdatePosition)
    {
        PtrInfo->Position.x = FrameInfo->PointerPosition.Position.x + OutputDesc.DesktopCoordinates.left - OffsetX;
        PtrInfo->Position.y = FrameInfo->PointerPosition.Position.y + OutputDesc.DesktopCoordinates.top - OffsetY;
        PtrInfo->WhoUpdatedPositionLast = OutputNumber;
        PtrInfo->LastTimeStamp = FrameInfo->LastMouseUpdateTime;
        PtrInfo->Visible = FrameInfo->PointerPosition.Visible != 0;
    }

    // No new shape
    if (FrameInfo->PointerShapeBufferSize == 0)
    {
        return hr;
    }

    // Old buffer too small
    if (FrameInfo->PointerShapeBufferSize > PtrInfo->BufferSize)
    {
        if (PtrInfo->PtrShapeBuffer)
        {
            delete [] PtrInfo->PtrShapeBuffer;
            PtrInfo->PtrShapeBuffer = NULL;
        }
        PtrInfo->PtrShapeBuffer = new (std::nothrow) BYTE[FrameInfo->PointerShapeBufferSize];
        if (!PtrInfo->PtrShapeBuffer)
        {
            DisplayErr(L"Failed to allocate memory for pointer shape in DUPLICATIONMANAGER", L"Error", E_OUTOFMEMORY);
            PtrInfo->BufferSize = 0;
            return E_OUTOFMEMORY;
        }

        // Update buffer size
        PtrInfo->BufferSize = FrameInfo->PointerShapeBufferSize;
    }

    UINT BufferSizeRequired;
    // Get shape
    hr = DeskDupl->GetFramePointerShape(FrameInfo->PointerShapeBufferSize, reinterpret_cast<VOID*>(PtrInfo->PtrShapeBuffer), &BufferSizeRequired, &(PtrInfo->ShapeInfo));
    if (FAILED(hr))
    {
        if (hr != DXGI_ERROR_ACCESS_LOST)
        {
            DisplayErr(L"Failed to get frame pointer shape in DUPLICATIONMANAGER", L"Error", hr);
        }
        delete [] PtrInfo->PtrShapeBuffer;
        PtrInfo->PtrShapeBuffer = NULL;
        PtrInfo->BufferSize = 0;
        return hr;
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[DXGI 1.2 Improvements](dxgi-1-2-improvements.md)
</dt> </dl>

 

 
