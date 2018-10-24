---
title: How to Ensure That Your Application Displays Properly on High-DPI Displays
description: Describes how to create a window the displays properly on high-DPI displays.
ms.assetid: 72a4b076-1cf0-4dc9-bd75-43b5173fc2a0
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to Ensure That Your Application Displays Properly on High-DPI Displays

Although Direct2D addresses many high-DPI issues for you, there are two steps you should take to ensure that your application works properly on high-DPI displays:

-   [Step 1: Use the System DPI When Creating Windows](#step-1-use-the-system-dpi-when-creating-windows)
-   [Step 2: Declare That the Application is DPI-Aware](#step-2-declare-that-the-application-is-dpi-aware)
-   [Related topics](#related-topics)

## Step 1: Use the System DPI When Creating Windows

The [**ID2D1Factory**](https://msdn.microsoft.com/en-us/library/Dd371246(v=VS.85).aspx) interface provides the [**GetDesktopDpi**](https://msdn.microsoft.com/en-us/library/Dd371316(v=VS.85).aspx) method for retrieving the system DPI. It provides the horizontal and vertical dimensions of the display in dots per inch (DPI). To use these values to set the width of a window, use the following formula:

<*horizontal DPI*> \* <*width*, in pixels> / <*default horizontal DPI*>

...where *horizontal DPI* is the value retrived by [**GetDesktopDpi**](https://msdn.microsoft.com/en-us/library/Dd371316(v=VS.85).aspx) and *default horizontal DPI* is 96. The formula is similar for the vertical size:

<*vertical DPI*> \* <*height*, in pixels> / <*default vertical DPI*>

...where *vertical DPI* is the value retrieved by the [**GetDesktopDpi**](https://msdn.microsoft.com/en-us/library/Dd371316(v=VS.85).aspx) method and *default vertical DPI* is 96.

The following code uses the [**GetDesktopDpi**](https://msdn.microsoft.com/en-us/library/Dd371316(v=VS.85).aspx) method to retrieve the system DPI and then creates a 640 × 480 window, scaled to the system DPI.


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



> [!Note]
>
> Starting with Windows 8, you can use the [**Windows::Graphics::Display::DisplayProperties**](https://msdn.microsoft.com/library/windows/apps/br226143) class to get the system DPI.

 

## Step 2: Declare That the Application is DPI-Aware

When an application declares itself to be DPI-aware, it is a statement specifying that the application behaves well at DPI settings up to 200 DPI. In Windows Vista and Windows 7, when DPI virtualization is enabled, applications that are not DPI-aware are scaled, and applications receive virtualized data from the system APIs, such as the [**GetSystemMetric**](https://msdn.microsoft.com/library/windows/desktop/ms724385) function. To declare that your application is DPI-aware, complete the following steps.

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

[Direct2D and High-DPI](direct2d-and-high-dpi.md)
</dt> </dl>

 

 




