---
description: 'Step 2: Add a Menu Command to Grab a Poster Frame'
ms.assetid: 9a0f807b-5543-41d4-ad2a-030a4346131c
title: 'Step 2: Add a Menu Command to Grab a Poster Frame'
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 2: Add a Menu Command to Grab a Poster Frame

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

This topic is Step 2 of [Grabbing a Poster Frame](grabbing-a-poster-frame.md).

Next, add a command for the user to grab a poster frame from a file. Create a menu item with a resource ID of IDM\_BITMAP, and add the following case statement to the window procedure:


```C++
case WM_COMMAND:
    switch (LOWORD(wparam))
    {
    case IDM_BITMAP:
        {
            HRESULT hr = DoShowBitmap(hwnd, &pbmi);
            if (SUCCEEDED(hr))
            {
                pBuffer = reinterpret_cast<BYTE*>(pbmi) + 
                    sizeof(BITMAPINFOHEADER);
                InvalidateRect(hwnd, NULL, TRUE);
            }
            else
            {
                MessageBox(hwnd, TEXT("Cannot display the image."),
                    TEXT("Error"), MB_OK | MB_ICONERROR);
            }
        }
        break;  // IDM_BITMAP
    }
    break;  // WM_COMMAND
```



The DoShowBitmap function will return the allocated buffer in *pbmi*. Assuming the function succeeds, the address of the bitmap (


```C++
pBuffer
```



) can be calculated as an offset from *pbmi*. In the DoShowBitmap function, display an **Open File** dialog box for the user to choose a file, and then call the application-defined GetBitmap function, which will retrieve the bitmap:


```C++
HRESULT DoShowBitmap(HWND hwnd, BITMAPINFOHEADER** ppbmih)
{
    OPENFILENAME ofn;       // common dialog box structure
    // Initialize OPENFILENAME (not shown).
    // Display the Open File dialog box.  
    if (GetOpenFileName(&ofn) != TRUE) // failed to open file
    {
        return E_FAIL;
    }
    return GetBitmap(ofn.lpstrFile, ppbmih);
}
```



Next: [Step 3: Implement the Frame-Grabbing Function](step-3--implement-the-frame-grabbing-function.md)

## Related topics

<dl> <dt>

[Grabbing a Poster Frame](grabbing-a-poster-frame.md)
</dt> </dl>

 

 



