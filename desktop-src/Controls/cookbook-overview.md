---
title: Enabling Visual Styles
description: This topic explains how to configure your application to ensure that common controls are displayed in the user's preferred visual style.
ms.assetid: eb6c2469-25b9-43c4-a6ca-391a7b2859b3
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Visual Styles

This topic explains how to configure your application to ensure that common controls are displayed in the user's preferred visual style.

This topic includes the following sections.

-   [Using Manifests or Directives to Ensure That Visual Styles Can Be Applied to Applications](#using-manifests-or-directives-to-ensure-that-visual-styles-can-be-applied-to-applications)
-   [Using ComCtl32.dll Version 6 in an Application That Uses Only Standard Extensions](#using-comctl32dll-version-6-in-an-application-that-uses-only-standard-extensions)
-   [Using ComCtl32 Version 6 in Control Panel or a DLL That Is Run by RunDll32.exe](#using-comctl32-version-6-in-control-panel-or-a-dll-that-is-run-by-rundll32exe)
-   [Adding Visual Style Support to an Extension, Plug-in, MMC Snap-in or a DLL That Is Brought into a Process](#adding-visual-style-support-to-an-extension-plug-in-mmc-snap-in-or-a-dll-that-is-brought-into-a-process)
-   [Turning Off Visual Styles](#turning-off-visual-styles)
-   [Using Visual Styles with HTML Content](#using-visual-styles-with-html-content)
-   [When Visual Styles are not Applied](#when-visual-styles-are-not-applied)
-   [Making Your Application Compatible with Earlier Versions of Windows](#making-your-application-compatible-with-earlier-versions-of-windows)
-   [Related topics](#related-topics)

## Using Manifests or Directives to Ensure That Visual Styles Can Be Applied to Applications

To enable your application to use visual styles, you must use ComCtl32.dll version 6 or later. Because version 6 is not redistributable, it is available only when your application is running on a version of Windows that contains it. Windows ships with both version 5 and version 6. ComCtl32.dll version 6 contains both the user controls and the common controls. By default, applications use the user controls defined in User32.dll and the common controls defined in ComCtl32.dll version 5. For a list of DLL versions and their distribution platforms, see [Common Control Versions](common-control-versions.md).

If you want your application to use visual styles, you must add an application manifest or compiler directive that indicates that ComCtl32.dll version 6 should be used if it is available.

An application manifest enables an application to specify which versions of an assembly it requires. In Microsoft Win32, an assembly is a set of DLLs and a list of versionable objects that are contained within those DLLs.

Manifests are written in XML. The name of the application manifest file is the name of your executable followed by the file name extension .manifest; for example, MyApp.exe.manifest. The following sample manifest shows that the first section describes the manifest itself. The following table shows the attributes set by the **assemblyIdentity** element in the manifest description section.



| Attribute             | Description                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| version               | Version of the manifest. The version must be in the form major.minor.revision.build (that is, n.n.n.n, where n <=65535). |
| processorArchitecture | Processor for which your application is developed.                                                                          |
| name                  | Includes company name, product name and application name.                                                                   |
| type                  | Type of your application, such as Win32.                                                                                    |



 

The sample manifest also provides a description of your application and specifies application dependencies. The following table shows the attributes set by the **assemblyIdentity** element in the dependency section.



| Attribute             | Description                                      |
|-----------------------|--------------------------------------------------|
| type                  | Type of the dependency component, such as Win32. |
| name                  | Name of the component.                           |
| version               | Version of the component.                        |
| processorArchitecture | Processor that the component is designed for.    |
| publicKeyToken        | Key token used with this component.              |
| language              | Language of the component.                       |



 

Following is an example of a manifest file.

> [!IMPORTANT]
> Set the **processorArchitecture** entry to **"X86"** if your application targets the 32 bit Windows platform, or to **"amd64"** if your application targets the 64 bit Windows platform. You can also specify **"\*"**, which ensures that all platforms are targeted, as shown in the following examples.

 


```C++
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="1.0.0.0"
    processorArchitecture="*"
    name="CompanyName.ProductName.YourApplication"
    type="win32"
/>
<description>Your application description here.</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="*"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
```



If you are using Microsoft Visual C++ 2005 or later, you can add the following compiler directive to your source code instead of manually creating a manifest. For readability, the directive is broken into several lines here.


```C++
#pragma comment(linker,"\"/manifestdependency:type='win32' \
name='Microsoft.Windows.Common-Controls' version='6.0.0.0' \
processorArchitecture='*' publicKeyToken='6595b64144ccf1df' language='*'\"")
```



The following topics describe the steps for applying visual styles to different types of applications. Notice that the manifest format is the same in each case.

## Using ComCtl32.dll Version 6 in an Application That Uses Only Standard Extensions

The following are examples of applications that do not use third-party extensions.

-   Calculator
-   FreeCell (in Windows Vista and Windows 7)
-   Minesweeper (in Windows Vista and Windows 7)
-   Notepad
-   Solitaire (in Windows Vista and Windows 7)

**To create a manifest and enable your application to use visual styles.**

1.  Link to ComCtl32.lib and call [**InitCommonControls**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrols).
2.  Add a file called YourApp.exe.manifest to your source tree that has the XML manifest format.
    ```C++
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity
        version="1.0.0.0"
        processorArchitecture="*"
        name="CompanyName.ProductName.YourApplication"
        type="win32"
    />
    <description>Your application description here.</description>
    <dependency>
        <dependentAssembly>
            <assemblyIdentity
                type="win32"
                name="Microsoft.Windows.Common-Controls"
                version="6.0.0.0"
                processorArchitecture="*"
                publicKeyToken="6595b64144ccf1df"
                language="*"
            />
        </dependentAssembly>
    </dependency>
    </assembly>
    ```

    

3.  Add the manifest to your application's resource file as follows:
    ```C++
    CREATEPROCESS_MANIFEST_RESOURCE_ID RT_MANIFEST "YourApp.exe.manifest"
    ```

    

    > [!Note]  
    > When you add the previous entry to the resource you must format it on one line. Alternatively, you can place the XML manifest file in the same directory as your application's executable file. The operating system will load the manifest from the file system first, then check the resource section of the executable. The file system version takes precedence.

     

When you build your application, the manifest will be added as a binary resource.

## Using ComCtl32 Version 6 in Control Panel or a DLL That Is Run by RunDll32.exe

**To create a manifest and enable your application to use visual styles.**

1.  Link to ComCtl32.lib and call [**InitCommonControls**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrols).
2.  Add a file called YourApp.cpl.manifest to your source tree that has the XML manifest format.
    ```C++
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity
        version="1.0.0.0"
        processorArchitecture="*"
        name="CompanyName.ProductName.YourApplication"
        type="win32"
    />
    <description>Your application description here.</description>
    <dependency>
        <dependentAssembly>
            <assemblyIdentity
                type="win32"
                name="Microsoft.Windows.Common-Controls"
                version="6.0.0.0"
                processorArchitecture="*"
                publicKeyToken="6595b64144ccf1df"
                language="*"
            />
        </dependentAssembly>
    </dependency>
    </assembly>
    ```

    

3.  Add the manifest to your application's resource file as resource ID 123.

> [!Note]  
> When you author a Control Panel application, place it in the appropriate category. Control Panel now supports categorization of Control Panel applications. This means that Control Panel applications can be assigned identifiers and separated into task areas such as Add or Remove Programs, Appearance and Themes, or Date, Time, Language, and Regional Options.

 

## Adding Visual Style Support to an Extension, Plug-in, MMC Snap-in or a DLL That Is Brought into a Process

Support for visual styles can be added to an extension, plug-in, MMC snap-in, or a DLL that is brought into a process. For example, use the following steps to add visual styles support for an Microsoft Management Console (MMC) snap-in.

1.  Compile your snap-in with the -DISOLATION\_AWARE\_ENABLED flag or insert the following statement before the \#include "windows.h" statement.

    ```C++
    #define ISOLATION_AWARE_ENABLED 1
    ```

    

    For more information about ISOLATION\_AWARE\_ENABLED, see [Isolating Components](/windows/desktop/SbsCs/isolating-components).

2.  Include the common control header file in your snap-in source.
    ```C++
    #include <commctrl.h>
    ```

    

3.  Add a file called YourApp.manifest to your source tree that uses the XML manifest format.
    ```C++
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity
        version="1.0.0.0"
        processorArchitecture="*"
        name="CompanyName.ProductName.YourApplication"
        type="win32"
    />
    <description>Your application description here.</description>
    <dependency>
        <dependentAssembly>
            <assemblyIdentity
                type="win32"
                name="Microsoft.Windows.Common-Controls"
                version="6.0.0.0"
                processorArchitecture="*"
                publicKeyToken="6595b64144ccf1df"
                language="*"
            />
        </dependentAssembly>
    </dependency>
    </assembly>
    ```

    

4.  Add the manifest to your snap-in's resource file. See [Using ComCtl32 Version 6 in an Application That Uses Extensions, Plug-ins, or a DLL That Is Brought into a Process](/previous-versions//ms649781(v=vs.85)) for details on adding a manifest to a resource file.

## Turning Off Visual Styles

You can turn off visual styles for a control or for all controls in a window by calling the [**SetWindowTheme**](/windows/desktop/api/Uxtheme/nf-uxtheme-setwindowtheme) function as follows:


```C++
SetWindowTheme(hwnd, L" ", L" ");
```



In the previous example, *hwnd* is the handle of the window in which to disable visual styles. After the call, the control renders without visual styles.

## Using Visual Styles with HTML Content

HTML pages that modify the Cascading Style Sheets (CSS) properties such as background or border do not have visual styles applied to them. They display the specified CSS attribute. When specified as part of the content, most CSS properties do apply to elements that have visual styles applied.

By default, visual styles are applied to intrinsic HTML controls on pages displayed in Microsoft Internet Explorer 6 and later versions. To turn off visual styles for an HTML page, add a META tag to the <head> section. This technique also applies to content packaged as HTML Applications (HTAs). To turn off visual styles, the META tag must be as follows:


```
<META HTTP-EQUIV="MSThemeCompatible" CONTENT="no">
```



> [!Note]  
> If the browser setting and the tag setting do not agree, the page will not apply visual styles. For example, if the META tag is set to "no" and the browser is set to enable visual styles, visual styles will not be applied to the page. However, if either the browser or META tag is set to "yes" and the other item is not specified, visual styles will be applied.

 

Visual styles might change the layout of your content. Also, if you set certain attributes on intrinsic HTML controls, such as the width of a button, you might find that the label on the button is unreadable under certain visual styles.

You must thoroughly test your content using visual styles to determine whether applying visual styles has an adverse effect on your content and layout.

## When Visual Styles are not Applied

To avoid applying visual styles to a top level window, give the window a non-null region (**SetWindowRgn**). The system assumes that a window with a non-NULL region is a specialized window that does not use visual styles. A child window associated with a non-visual-styles top level window may still apply visual styles even though the parent window does not.

If you want to disable the use of visual styles for all windows in your application, call [**SetThemeAppProperties**](/windows/desktop/api/Uxtheme/nf-uxtheme-setthemeappproperties) and do not pass the STAP\_ALLOW\_NONCLIENT flag. If an application does not call **SetThemeAppProperties**, the assumed flag values are STAP\_ALLOW\_NONCLIENT \| STAP\_ALLOW\_CONTROLS \| STAP\_ALLOW\_WEBCONTENT. The assumed values cause the nonclient area, the controls, and web content to have a visual style applied.

## Making Your Application Compatible with Earlier Versions of Windows

Much of the visual style architecture is designed to make it simple to continue to ship your product on earlier versions of Windows that do not support changing the appearance of controls. When shipping an application for more than one operating system, be aware of the following:

-   In versions of Windows prior to Windows 8, visual styles are off when high contrast is on. To support high contrast, a legacy application that supports visual styles needs to provide a separate code path to properly draw UI elements in high contrast. In Windows 8, high contrast is a part of visual styles; however, a Windows 8 application (one that includes the Windows 8 GUID in compatibility section of its application manifest) still needs to provide a separate code path to render correctly in high contrast on Windows 7 an earlier.
-   If you use the features in ComCtl32.dll version 6, such as the tile view or link control, you must handle the case where those controls are not available on your user's computer. ComCtl32.dll version 6 is not redistributable.
-   Test your application to make sure you are not relying on features of ComCtl32.dll version 6 without first checking for the current version.
-   Do not link to UxTheme.lib.
-   Write error-handling code for instances when visual styles do not work as expected.
-   Installing your application's manifest in earlier versions will not affect the rendering of controls.

## Related topics

<dl> <dt>

[Visual Styles](themes-overview.md)
</dt> </dl>

 

 
