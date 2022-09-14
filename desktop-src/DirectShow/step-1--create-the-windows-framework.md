---
description: 'Step 1: Create the Windows Framework'
ms.assetid: 678c6261-cbd0-4865-a1dd-03de55eca996
title: 'Step 1: Create the Windows Framework'
ms.topic: article
ms.date: 05/31/2018
---

# Step 1: Create the Windows Framework

\[This API is not supported and may be altered or unavailable in the future.\]

Start by creating the basic framework of a Windows application, including WinMain and a window procedure. The WinMain function is not shown here; call [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) before the message loop to initialize the COM library, and [**CoUninitialize**](/windows/win32/api/combaseapi/nf-combaseapi-couninitialize) after the message loop exits. Start with the following minimal window procedure:


```C++
LRESULT CALLBACK MainWndProc(HWND hwnd, UINT msg, WPARAM wparam, LPARAM lparam)
{
    static BITMAPINFOHEADER *pbmi = NULL;
    static BYTE *pBuffer = NULL;
    switch (msg)
    {
    case WM_CLOSE:
        DestroyWindow(hwnd);
        break;
    case WM_DESTROY:
        if (pbmi) delete [] pbmi;
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hwnd, msg, wparam, lparam);
    }
    return 0;
}
```



When you retrieve a poster frame from the Media Detector, it returns a buffer that contains a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure followed by the image bits. Therefore, define two static variables in the window procedure: *pbmi* will hold a pointer to the **BITMAPINFOHEADER** structure, and *pBuffer* will hold a pointer to the bitmap. The application will allocate the buffer in *pbmi* using `new`, so it must delete the buffer before the window is destroyed. The *pBuffer* pointer is calculated as an offset from *pbmi*, so there is no need to delete it.

Next: [Step 2: Add a Menu Command to Grab a Poster Frame](step-2--add-a-menu-command-to-grab-a-poster-frame.md)

## Related topics

<dl> <dt>

[Grabbing a Poster Frame](grabbing-a-poster-frame.md)
</dt> </dl>

 

 
