---
title: User Interface Technologies
description: This topic provides a brief survey of the Microsoft technologies for developing UIs for Windows-based applications.
ms.assetid: 5ecbaaf0-704e-4c27-b3ce-b5436e577d62
ms.topic: article
ms.date: 05/31/2018
---

# User Interface Technologies

This topic provides a brief survey of the Microsoft technologies for developing UIs for Windows-based applications. It provides the information required to help you determine whether to use a particular technology, and identifies where you can find more information about it.

This topic describes the following technologies:

-   [User Interface Technologies for Unmanaged Applications](#user-interface-technologies-for-unmanaged-applications)
    -   [Windows Controls](#windows-controls)
    -   [Visual Styles](#visual-styles)
    -   [Windows Ribbon Framework](#windows-ribbon-framework)
    -   [Windows Animation Manager](#windows-animation-manager)
    -   [Desktop Window Manager](#desktop-window-manager)
    -   [Windows Automation API](#windows-automation-api)
    -   [Speech API](#speech-api)
    -   [Magnification API](#magnification-api)
    -   [Resource Compiler](#resource-compiler)
-   [User Interface Technologies for Managed Applications](#user-interface-technologies-for-managed-applications)
    -   [Windows Forms](#windows-forms)
    -   [Windows Presentation Foundation](#windows-presentation-foundation)
    -   [Silverlight](#silverlight)
    -   [Expression Blend 3 + SketchFlow](/windows)
    -   [UI Automation for Managed Applications](#ui-automation-for-managed-applications)

## User Interface Technologies for Unmanaged Applications

This section describes the Microsoft technologies for developing UIs for unmanaged Windows applications. These technologies are intended for experienced C/C++ developers who are familiar with WindowsAPI programming concepts, and who are using the Microsoft Windows Software Development Kit (SDK). Some technologies have additional prerequisites such as knowledge of graphics programming issues or familiarity with the basics of Component Object Model (COM) programming.

### Windows Controls

Windows controls are user interface elements that are used in conjunction with another window (typically a client window or dialog box) to enable the user to interact with an application. Many of the elements that make up the UI of a traditional Windows-based application are Windows controls, including items such as menus, scroll bars, buttons, list boxes, tree views, and so on.

Windows controls are supported by all versions of Windows. However, because the run-time components that support the controls have evolved over time, some controls and features introduced in later versions are not supported in earlier versions. Applications need to detect the versions and use only the available features.

You should use Windows controls if you want to create a traditional UI for an unmanaged Windows-based application that runs on a wide range of Windows versions.

For more information, see [Windows Controls](../controls/window-controls.md).

### Visual Styles

Visual Styles are specifications for the appearance of controls. For example, a Visual Style can define the overall appearance of controls, and enable software developers to configure the visual interface of those controls to coordinate with an application's appearance. Additionally, Visual Styles provide a mechanism for all Windows-based applications to standardize an application's appearance.

Visual styles are supported on Windows XP and later, and they only affect the appearance of the standard Windows controls and the Microsoft Win32 common controls.

You should use Visual Styles if you need to change the appearance of the standard Windows controls and common controls to match the look of your application UI.

For more information, see [Visual Styles](../controls/themes-overview.md).

### Windows Ribbon Framework

The Windows Ribbon framework is a rich command presentation system for Windows-based applications. It consists of a ribbon command bar that exposes the major features of an application through a series of tabs at the top of an application window, and a context menu system. The Windows Ribbon framework is supported on the following Windows versions:

-   Windows Vista with Service Pack 2 (SP2) and Platform Update for Windows Vista
-   Windows 7 and later
-   Windows Server 2008 R2
-   Windows Server 2008 with Service Pack 2 (SP2) and Platform Update for Windows Server 2008

You should use Windows Ribbon framework if you want to implement a command UI that is an alternative to the layered menus, toolbars, and task panes of traditional Windows applications.

The Windows Ribbon framework is intended for developers who are proficient in COM programming.

For more information, see [Windows Ribbon Framework](../windowsribbon/-uiplat-windowsribbon-entry.md).

### Windows Animation Manager

The Windows Animation Manager supports the animation of UI elements by providing a powerful animation engine and a standardized programmatic interface. The platform simplifies the development and maintenance of UI animation sequences and enables developers to implement UI animations that are consistent and intuitive. Windows Animation can be used with any graphics platform including Direct2D, Microsoft Direct3D, or Windows GDI+.

The Windows animation framework is supported on Windows Vista with Platform Update for Windows VistaWindows Vista with SP2 and Platform Update for Windows Vista, and Windows 7 and later.

You should use Windows Animation Manager if you want to add animation sequences to the UI of an unmanaged Windows-based application.

For more information, see [Windows Animation Manager](../uianimation/-main-portal.md).

### Desktop Window Manager

Desktop Window Manager (DWM) is a Windows run-time component that supports desktop composition, a feature introduced in Windows Vista. Through desktop composition, DWM enables visual effects in the UI, such as glass window frames, 3-D window transition animations, Windows Flip and Windows Flip3D, and high resolution support.

DWM exposes an API for controlling many of the visual effects associated with desktop composition. For example, an application can display thumbnails, apply a translucent and blurred effect to the client area of top-level windows, control the transparency and transition effects used in the non-client region of windows, and so on.

DWM is supported on Windows Vista and Windows Server 2008.

You should use DWM if your application needs to access and control the visual effects associated with desktop composition.

For more information, see [Desktop Window Manager](../dwm/dwm-overview.md).

### Windows Automation API

The Windows Automation API helps developers create applications that are accessible to the widest possible audience, including people with vision, hearing, or motion disabilities. The API works by exposing information about the elements that make up an application user interface. Assistive technology applications such as screen readers can use the information to present the UI in a way that can be used by people with disabilities.

The Windows Automation API consists of two separate API frameworks, Microsoft Active Accessibility and Microsoft UI Automation. Microsoft Active Accessibility is a legacy API that was introduced in Windows 95 as a platform add-in. UI Automation is the successor to Microsoft Active Accessibility, and is a Windows implementation of the UI Automation specification.

Full support for Microsoft Active Accessibility is built into Windows XP and Windows Server 2003. Microsoft Active Accessibility is also supported on Windows NT 4.0 with Service Pack 6 (SP6) and later, and Windows 98. UI Automation is supported on the following operating systems: Windows XP, Windows Server 2003, Windows Server 2003 R2, Windows Vista, Windows 7, Windows Server 2008, and Windows Server 2008 R2.

If your application contains custom controls or other custom UI features, you should use the Windows Automation API to ensure that the custom controls and features are fully accessible. In general, developers need a moderate level of understanding about COM objects and interfaces, Unicode, and Windows API programming.

For more information, see [Windows Automation API](../winauto/windows-automation-api-portal.md).

### Speech API

The Microsoft Speech API (SAPI) provides a high-level interface between an application and speech engines. SAPI implements all the low-level details needed to control and manage the real-time operations of various speech engines.

The two basic types of SAPI engines are text-to-speech (TTS) systems and speech recognizers. TTS systems synthesize text strings and files into spoken audio using synthetic voices. Speech recognizers convert human spoken audio into readable text strings and files.

You should use SAPI if you want to implement a UI that enables the user to interact with your application through TTS and speech recognition in addition to the standard input devices such as the keyboard, mouse, and display.

For more information, see [Microsoft Speech API (SAPI) 5.4](/previous-versions/windows/desktop/ee125663(v=vs.85)).

### Magnification API

The magnification API (MAPI) is used to magnify portions of the screen, and to apply color effects and other transforms. This API is primarily intended for assistive-technology applications that enlarge parts of the screen to make them easier to see.

MAPI is supported on Windows Vista, Windows 7, Windows Server 2008, and Windows Server 2008 R2. It is intended for developers who are familiar with graphics programming concepts.

For more information, see [Magnification API](/previous-versions/windows/desktop/magapi/entry-magapi-sdk).

### Resource Compiler

The Microsoft Windows Resource Compiler is an application development tool used to add UI and other resources to a Windows-based application. A resource is any non-executable data used by an application, and includes such things as dialog boxes, menus, strings, cursors, icons, bitmaps, and so on. The resource compiler is included in Microsoft Visual Studio and the Windows SDK.

For more information, see [Resource Compiler](../menurc/resource-compiler.md).

## User Interface Technologies for Managed Applications

This section describes the Microsoft technologies for developing UIs for managed Windows applications that run in the context of the .NET Framework. For more information, see [.NET Development](/previous-versions/ff361664(v=vs.100)).

### Windows Forms

Windows Forms is a graphical application programming interface for creating managed Windows applications that are based on the .NET Framework. In Windows Forms, a form is a visual surface on which you display information to the user, and through which you receive input from the user.

You build Windows Forms applications by adding controls to forms and developing responses to user actions, such as mouse clicks or key presses. A control is a discrete UI element that displays data or accepts data input. Windows Forms contains a variety of controls that you can add to forms: controls that display text boxes, buttons, drop-down boxes, radio buttons, and even Web pages. Windows Forms also supports creating custom controls.

For more information, see [Windows Forms](/previous-versions/dotnet/netframework-4.0/cc656767(v=vs.100)).

### Windows Presentation Foundation

Windows Presentation Foundation (WPF) is the successor to [Windows Forms](/previous-versions/dotnet/netframework-4.0/cc656767(v=vs.100)). WPF is a presentation system for building and rendering user interfaces in Windows-based client applications and browser-hosted applications. The core of WPF is a resolution-independent and vector-based rendering engine that is built to take advantage of modern graphics hardware. WPF extends the core with a comprehensive set of application-development features that include Extensible Application Markup Language (XAML), controls, data binding, layout, 2-D and 3-D graphics, animation, styles, templates, documents, media, text, and typography.

WPF is included in the .NET Framework, so you can build applications that incorporate other elements of the .NET Framework class library. WPF is supported on Windows Vista, Windows 7, Windows Server 2008, Windows Server 2008 R2, and is also available for Windows XP with Service Pack 2 (SP2), and Windows Server 2003.

For more information, see [Windows Presentation Foundation](/dotnet/framework/wpf/).

### Silverlight

Microsoft Silverlight is a powerful development platform for creating rich media applications and business applications for the Web, desktop, and mobile devices.

Based on the .NET Framework, the free Silverlight plug-in works across multiple browsers, devices, and operating systems to bring new interactivity to the Web. With extensive layout and styling options, powerful communication protocols, robust data access, and support for user interaction and high-definition media, Silverlight helps create fast, smooth, and visually rich customer experiences. Silverlight applications can be developed quickly with the Microsoft Web Platform, Visual Studio, and Expression Studio.

For more information, see [Microsoft Silverlight](/previous-versions/windows/silverlight/dotnet-windows-silverlight/cc838158(v=vs.95)).

### Expression Blend 3 + SketchFlow

Expression Blend 3 + SketchFlow is a visual tool for designing, prototyping, and creating sophisticated user interfaces for WPF and Silverlight desktop and web applications. You build an application by drawing shapes, drawing controls such as buttons and list boxes, making the pieces of your application respond to mouse clicks and other user input, and styling everything to look uniquely your own.

For more information, see [Prototyping with SketchFlow](/previous-versions/visualstudio/design-tools/expression-studio-3/ee341458(v=expression.30)).

### UI Automation for Managed Applications

UI Automation is an accessibility framework for Windows, available on all operating systems that support WPF.

UI Automation provides programmatic access to most UI elements on the desktop, enabling assistive technology products such as screen readers to provide information about the UI to end users and to manipulate the UI by means other than standard input. UI Automation also allows automated test scripts to interact with the UI.

For more information, see [UI Automation for Managed Applications](/dotnet/framework/ui-automation/).

 

 