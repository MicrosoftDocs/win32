---
description: 'Step 4: Draw the Bitmap on the Client Area'
ms.assetid: fb22468c-9113-46ff-a576-8dee30c458be
title: 'Step 4: Draw the Bitmap on the Client Area'
ms.topic: article
ms.date: 05/31/2018
---

# Step 4: Draw the Bitmap on the Client Area

\[This API is not supported and may be altered or unavailable in the future.\]

This topic is Step 4 of [Grabbing a Poster Frame](grabbing-a-poster-frame.md).

The final step is to draw the bitmap onto the client area of the application window, using the [**SetDIBitsToDevice**](/windows/win32/api/wingdi/nf-wingdi-setdibitstodevice) function. This example simply paints the bitmap in the upper-left corner of the client area, without regard to the window size:


```C++
case WM_PAINT:
    {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hwnd, &ps);
        if (pbmi)
        {
            int result = SetDIBitsToDevice(hdc, 0, 0, 
                pbmi->biWidth,
                pbmi->biHeight,
                0, 0, 0,
                pbmi->biHeight,
                pBuffer,
                reinterpret_cast<BITMAPINFO*>(pbmi),
                DIB_RGB_COLORS);
        }
        EndPaint(hwnd, &ps);
    }
    break;
```



The *pBuffer* and *pbmi* variables are declared in [Step 1: Create the Windows Framework](step-1--create-the-windows-framework.md), and their values are obtained in [Step 3: Implement the Frame-Grabbing Function](step-3--implement-the-frame-grabbing-function.md).

## Related topics

<dl> <dt>

[Grabbing a Poster Frame](grabbing-a-poster-frame.md)
</dt> </dl>

 

 
