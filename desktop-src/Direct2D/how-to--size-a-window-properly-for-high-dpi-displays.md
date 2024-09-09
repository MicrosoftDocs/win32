---
title: Displaying properly on a high-DPI display
description: Describes the steps to create a window for your application that displays properly on high-DPI displays.
ms.assetid: 72a4b076-1cf0-4dc9-bd75-43b5173fc2a0
ms.topic: article
ms.date: 05/26/2022
---

# Displaying properly on a high-DPI display

Although Direct2D addresses many high-DPI issues for you, there are two steps you should take to ensure that your application works properly on high-DPI displays.

## Step 1: Use the window's own DPI after creating it

The [**GetDpiForWindow**](/windows/win32/api/winuser/nf-winuser-getdpiforwindow) function retrieves the dots per inch (dpi) value for a specified window. To use that value to set the width of a window, use the following formula:

<*DPI*> \* <*width*, in pixels> / <*default DPI*>

...where *DPI* is the value retrived by **GetDpiForWindow**, and *default DPI* is 96 (defined as `USER_DEFAULT_SCREEN_DPI` in `winuser.h` header). The formula is similar for the vertical axis:

<*DPI*> \* <*height*, in pixels> / <*default vertical DPI*>

The code example in step 2.3 of [Create a simple Direct2D application](/windows/win32/Direct2D/direct2d-quickstart) retrieves a window's DPI, and then sets its size to 640 × 480, scaled to the DPI.

> [!NOTE]
> For a Universal Windows Platform (UWP) app, you can use the [**DisplayInformation::LogicalDpi**](/uwp/api/windows.graphics.display.displayinformation.logicaldpi) property.

## Step 2: Declare That the application is DPI-aware

When an application declares itself to be DPI-aware, it is a statement specifying that the application behaves well at DPI settings up to 200 DPI. In Windows Vista and Windows 7, when DPI virtualization is enabled, applications that are not DPI-aware are scaled, and applications receive virtualized data from the system APIs, such as the [**GetSystemMetric**](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics) function. To declare that your application is DPI-aware, complete the following steps.

1.  Create a file called DeclareDPIAware.manifest.
2.  Copy the following xml into the file and save it:
    ```cpp
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3" >
      <asmv3:application>
        <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">
          <dpiAware>true</dpiAware>
        </asmv3:windowsSettings>
      </asmv3:application>
    </assembly>
    ```

3.  In the project's .vcproj file, add the following entry inside each Configuration element under VisualStudioProject/Configurations:
    ```cpp
    <Tool
        Name="VCManifestTool"
        AdditionalManifestFiles="DeclareDPIAware.manifest"
    />
    ```

## Related topics

* [Direct2D and high DPI](direct2d-and-high-dpi.md)
