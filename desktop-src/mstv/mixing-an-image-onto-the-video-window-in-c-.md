---
title: Mixing an Image Onto the Video Window in C++
description: Mixing an Image Onto the Video Window in C++
ms.assetid: 'e39cf7b0-7a88-41e9-bddc-cdd0cc381996'
---

# Mixing an Image Onto the Video Window in C++

This topic applies to Windows XP or later.

This section describes how to display an alpha-blended image over the Video Control's video image. Internally, the Video Control uses the Video Mixing Renderer filter (VMR).

**Mixing an IPictureDisp Object**

In C++, you can specify the image either as an **IPictureDisp** object or as a bitmap. The **IPictureDisp** object is designed for Automation clients, and it is generally easier to work with a bitmap in C++. When you capture an image from the Video Control, however, it returns an **IPictureDisp** object. Therefore, the first example shows how to use the captured image as the mixing image. The result is to show a "snapshot" of the video in a corner of the window, while the video continues to play in the background.

First, submit a tune request and call the Video Control's [**IMSVidCtl::Run**](imsvidctl-run.md) method. (For more information, see [Tuning with the Video Control](tuning-with-the-video-control.md).)

To capture the image:

Call the [**IMSVidCtl::get\_VideoRendererActive**](imsvidctl-get-videorendereractive.md) method. This method returns a pointer to the [**IMSVidVideoRenderer**](imsvidvideorenderer.md) interface on the video renderer device.

Call the [**IMSVidVideoRenderer::Capture**](imsvidvideorenderer-capture.md) method. This method returns an **IPictureDisp** object, which contains the image.

Now you can use the **IPictureDisp** object as the VMR's mixer image, by calling the [**IMSVidVideoRenderer::SetupMixerBitmap**](imsvidvideorenderer-setupmixerbitmap.md) method. The method takes the following parameters:

-   The **IPictureDisp** pointer.
-   The desired opacity, expressed as an integer from 0 to 100.
-   The position of the image on the video window, specified as an [**IMSVidRect**](imsvidrect.md) interface.

The **IMSVidRect** interface is an Automation-compatible wrapper for a rectangle. The following example retrieves a rectangle by calling [**IMSVidVideoRenderer::get\_MixerBitmap**](imsvidvideorenderer-get-mixerbitmap.md), but then overrides the dimensions of the rectangle. It then captures an image and mixes it onto the video window. For brevity, the example omits any error checking.


```C++
CComPtr<IMSVidCtl> m_pVideoControl;  // Video Control
CComPtr<IMSVidVideoRenderer> pVideo; // video renderer device
CComPtr<IPictureDisp> pPic;          // picture object
CComPtr<IMSVidRect> pRect;           // Automation-compatible rectangle
RECT rcWin;

/* Build and run the filter graph (not shown). */

// Capture the image.
hr = m_pVideoControl->get_VideoRendererActive(&amp;pVideo);
hr = pVideo->Capture(&amp;pPic);

// Set the rectangle to 1/4 of the window.
hr = pVideo->get_MixerBitmapPositionRect(&amp;pRect);
::GetWindowRect(GetDlgItem(IDC_MSVIDCTL1), &amp;rcWin);
hr = pRect->put_Width(rcWin.right / 2);
hr = pRect->put_Height(rcWin.bottom / 2);
hr = pRect->put_Top(0);
hr = pRect->put_Left(0);

// Set the mixer bitmap.
long lOpacity = 80;  // 0 = transparent, 100 = opaque 
hr = pVideo->SetupMixerBitmap(pPic, lOpacity, pRect);
```



The position rectangle defaults to the entire video control window. If you don't want to specify the rectangle, you can use the [**IMSVidVideoRenderer::put\_MixerBitmap**](imsvidvideorenderer-put-mixerbitmap.md) and [**IMSVidVideoRenderer::put\_MixerBitmapOpacity**](imsvidvideorenderer-put-mixerbitmapopacity.md) methods:


```C++
hr = pVideo->put_MixerBitmap(pPic);
hr = pVideo->put_MixerBitmapOpacity(lOpacity);
```



**Mixing a Bitmap**

In C++, you can also mix a bitmap that is specified as a DirectDraw surface or as a handle to a GDI object. To do so, use the [**IMSVidVideoRenderer::put\_\_MixerBitmap**](imsvidvideorenderer-put--mixerbitmap.md) method. This method acts as a pass-through to the VMR's [**IVMRMixerBitmap::SetAlphaBitmap**](https://msdn.microsoft.com/library/windows/desktop/dd390454) method. As an alternative, you can use the [**IMSVidVideoRenderer::get\_\_MixerBitmap**](imsvidvideorenderer-get--mixerbitmap.md) method to obtain the VMR's [**IVMRMixerBitmap**](https://msdn.microsoft.com/library/windows/desktop/dd390448) interface and call **SetAlphaBitmap** directly.

For more information, see [Displaying an Application-Supplied Bitmap on the Composited Image](https://msdn.microsoft.com/library/windows/desktop/dd375479). The example shown here is modified from the example code in that topic.

The following example loads a bitmap resource and displays it in the upper-left corner of the video window, blended at 50% opacity. For brevity, the example omits any error checking.


```C++
HRESULT ShowBitmap(IMSVidCtl *pVideoControl, WORD nID)
{ 
    CComPtr<IVMRMixerBitmap> pVmrBitmap;
    CComPtr<IMSVidVideoRenderer> pVideo;
    HRESULT hr = pVideoControl->get_VideoRendererActive(&amp;pVideo);
    hr = pVideo->get__MixerBitmap(&amp;pVmrBitmap);
    if (SUCCEEDED(hr))
    {
        RECT rc;
        HBITMAP hBitmap = LoadBitmap(hInst, MAKEINTRESOURCE(nID));
        ::GetWindowRect(GetDlgItem(IDC_MSVIDCTL1), &amp;rc);
        hr = MixImage(hWnd, pVmrBitmap, hBitmap, rc.right, rc.bottom);
    }
}

HRESULT MixImage(HWND hwndApp, IVMRMixerBitmap* pBmp, HBITMAP hbm,
  long cx, long cy)
{
    HRESULT hr;
    BITMAP bm;
    HBITMAP hbmOld;
    HDC hdc = GetDC(hwndApp);
    HDC hdcBmp = CreateCompatibleDC(hdc);
    ReleaseDC(hwndApp, hdc);

    GetObject(hbm, sizeof(bm), &amp;bm);
    hbmOld = (HBITMAP)SelectObject(hdcBmp, hbm);

    VMRALPHABITMAP bmpInfo;  // Holds information about the bitmap.
    ZeroMemory(&amp;bmpInfo, sizeof(bmpInfo));
    bmpInfo.dwFlags = VMRBITMAP_HDC; // Tells the VMR we are using an HDC.
    bmpInfo.hdc = hdcBmp;

    // The source rectangle is the entire bitmap.
    SetRect(&amp;bmpInfo.rSrc, 0, 0, bm.bmWidth, bm.bmHeight);

    // The target rectangle is the upper left corner of the video image,
    // expressed as a percentage of the image.
    bmpInfo.rDest.left = 0.f;
    bmpInfo.rDest.top = 0.f;
    bmpInfo.rDest.right = static_cast<float>(bm.bmWidth) /
                          static_cast<float>(cx);
    bmpInfo.rDest.bottom = static_cast<float>(bm.bmHeight) /
                           static_cast<float>(cy);
    bmpInfo.fAlpha = 0.5f; // Set the alpha to 50%
    hr = pBmp->SetAlphaBitmap(&amp;bmpInfo);
  
    // Clean up.
    DeleteObject(SelectObject(hdcBmp, hbmOld));
    DeleteDC(hdcBmp);
    return hr;

}
```



 

 




