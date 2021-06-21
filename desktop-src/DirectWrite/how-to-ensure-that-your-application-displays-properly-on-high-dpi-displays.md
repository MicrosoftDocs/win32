---
title: How to Ensure That Your Application Displays Properly on High-DPI Displays (DirectWrite)
description: Describes how to ensure that your application creates a window that displays properly on high-DPI displays.
ms.assetid: d174a337-c98e-46c7-86d2-c208900882d1
ms.topic: article
ms.date: 05/31/2018
---

# How to Ensure That Your Application Displays Properly on High-DPI Displays

Although [DirectWrite](direct-write-portal.md) addresses many high-DPI issues for you, there are two steps you should take to ensure that your application works properly on high-DPI displays:

-   [Step 1: Use the System DPI When Creating Windows](#step-1-use-the-system-dpi-when-creating-windows)
    -   [Direct2D](#direct2d)
    -   [GDI](#gdi)
-   [Step 2: Declare That the Application is DPI-Aware](#step-2-declare-that-the-application-is-dpi-aware)
-   [Related topics](#related-topics)

## Step 1: Use the System DPI When Creating Windows

This can be done by using [Direct2D](../direct2d/direct2d-portal.md) or by using [GDI](../gdi/windows-gdi.md).

### Direct2D

The [**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory) interface provides the [**GetDesktopDpi**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-getdesktopdpi) method for retrieving the system DPI. It provides the horizontal and vertical dimensions of the display in dots per inch (DPI). To use these values to set the width of a window, use the following formula:

<*horizontal DPI*> \* <*width*, in pixels> / <*default horizontal DPI*>

...where *horizontal DPI* is the value retrived by GetDpi and *default horizontal DPI* is 96. The formula is similar for the vertical size:

<*vertical DPI*> \* <*height*, in pixels> / <*default vertical DPI*>

...where *vertical DPI* is the value retrieved by the [**GetDesktopDpi**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-getdesktopdpi) method and *default vertical DPI* is 96.

The following code uses the [**GetDesktopDpi**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-getdesktopdpi) method to create a 640 x 480 window, scaled to the system DPI. (In the following code, *m\_spD2DFactory* is a smart pointer to an [**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory) instance.)


```C++
        // Because the CreateWindow function takes its size in pixels,
        // obtain the system DPI and use it to scale the window size.
        FLOAT dpiX, dpiY;

        // The factory returns the current system DPI. This is also the value it will use
        // to create its own windows.
        m_pDirect2dFactory->GetDesktopDpi(&dpiX, &dpiY);


        // Create the window.
        m_hwnd = CreateWindow(
            L"D2DDemoApp",
            L"Direct2D Demo App",
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            static_cast<UINT>(ceil(640.f * dpiX / 96.f)),
            static_cast<UINT>(ceil(480.f * dpiY / 96.f)),
            NULL,
            NULL,
            HINST_THISCOMPONENT,
            this
            );
```



### GDI

[GDI](interoperating-with-gdi.md) provides the [**GetDeviceCaps**](/windows/win32/api/wingdi/nf-wingdi-getdevicecaps) function for retrieving device information. You can retrieve DPI information by passing the *LOGPIXELSX* and *LOGPIXELSY* index values. The formula for determining the horizontal and vertical size of a window is the same as with the [Direct2D](../direct2d/direct2d-portal.md) example above.

The following code uses the [**GetDeviceCaps**](/windows/win32/api/wingdi/nf-wingdi-getdevicecaps) function to create a 640 x 480 window, scaled to the system DPI.


```C++
FLOAT dpiX, dpiY;

HDC screen = GetDC(0);
dpiX = static_cast<FLOAT>(GetDeviceCaps(screen, LOGPIXELSX));
dpiY = static_cast<FLOAT>(GetDeviceCaps(screen, LOGPIXELSY));
ReleaseDC(0, screen);

hWnd = CreateWindow(
         TEXT("DirectWriteApp"),
         TEXT("DirectWrite Demo App"),
         WS_OVERLAPPEDWINDOW,
         CW_USEDEFAULT,
         CW_USEDEFAULT,
         static_cast<INT>(dpiX * 640.f / 96.f),
         static_cast<INT>(dpiY * 480.f / 96.f),
         NULL,
         NULL,
         hInstance,
         NULL
         );
```



## Step 2: Declare That the Application is DPI-Aware

When an application declares itself to be DPI-aware, it is a statement specifying that the application behaves well at DPI settings up to 200 DPI. In Windows Vista and Windows 7, when DPI virtualization is enabled, applications that are not DPI-aware are scaled, and applications receive virtualized data from the system APIs, such as the [**GetSystemMetric**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) function. To declare that your application is DPI-aware, complete the following steps.

1.  Create a file called DeclareDPIAware.manifest.
2.  Copy the following xml into the file and save it:
    ```C++
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3" >
      <asmv3:application>
        <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">
          <dpiAware>true</dpiAware>
        </asmv3:windowsSettings>
      </asmv3:application>
    </assembly>
    ```

    

3.  In the project's .vcproj file, add the following entry inside each Configuration element under VisualStudioProject/Configurations:
    ```C++
    <Tool
        Name="VCManifestTool"
        AdditionalManifestFiles="DeclareDPIAware.manifest"
    />
    ```

    

## Related topics

<dl> <dt>

[Direct2D and High-DPI](../direct2d/direct2d-and-high-dpi.md)
</dt> </dl>

 

 