---
description: The .NET Framework has a security model that treats applications differently depending on their origin.
ms.assetid: 37fa870a-6f38-44ae-943e-27697f6b9fba
title: Security and Trust
ms.topic: article
ms.date: 05/31/2018
---

# Security and Trust

The .NET Framework has a security model that treats applications differently depending on their origin. Executables and assemblies that are from a user's machine generally run with full trust; the same executables and assemblies run over the Internet generally run with partial trust. This is to prevent malicious code from either reading or modifying information it should not have access to, such as local files, items in the Clipboard, and other resources. If an executable calls an assembly, which in turn calls another assembly that requires a certain level of trust, then the lowest level of trust of all the components in the chain is applied. However, an administrator on a machine can set specific permissions that override the default permissions.

An overview of the security model is given in [Secure, Light-Weight Client-Side Controls](/archive/msdn-magazine/2002/january/dhtml-and-net-host-secure-lightweight-client-side-controls-in-microsoft-internet-explorer), and you can obtain more depth about the security model in [Code Access Security in Practice](/previous-versions/msp-n-p/ff648663(v=pandp.10)). A good overview on the security of libraries (which is especially important for [**UserControl**](/uwp/api/Windows.UI.Xaml.Controls.UserControl?view=winrt-19041&preserve-view=true) objects on a Web page) can be found in [Using Libraries from Partially Trusted Code](/docs/?url=%2flibrary%2fcpguide%2fhtml%2fcpconusinglibrariesfrompartiallytrustedcode.asp), and other security information on managed controls can be found in [Writing Secure Managed Controls](/docs/?url=%2flibrary%2fcpguide%2fhtml%2fcpconwritingsecuremanagedcontrols.asp%3fframe%3dtrue).

## Permissions

Most managed objects and members in the Tablet PC Technologies API have two requirements:

-   Execution is always required.
-   FullTrust is required when the [InheritanceDemand](/previous-versions/windows/) security action takes place. This means that full trust is required when a derived class inherits a class or overrides a method from the Tablet PC SDK.

The following table lists the classes and members that require additional permissions. The permissions for a given class also apply to all of its members not listed in this table.



| Class or Method                                                                       | Permissions                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-canpaste)                                                  | [UIPermissionClipboard.AllClipboard](/dotnet/api/system.security.permissions.uipermissionclipboard?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                           |
| [**Ink.ClipboardCopy**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardcopy)                                    | [UIPermissionClipboard.OwnClipboard](/dotnet/api/system.security.permissions.uipermissionclipboard?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                           |
| [**Ink.ClipboardPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardpaste)                                  | [UIPermissionClipboard.AllClipboard](/dotnet/api/system.security.permissions.uipermissionclipboard?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                           |
| [**InkCollector**](inkcollector-class.md)                                            | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                          |
| InkCollector(IntPtr)                                                                  | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true) and [SecurityPermissionFlag.UnmanagedCode](/previous-versions/windows/)<br/>         |
| InkCollector.Handle                                                                   | [UIPermissionWindow.AllWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true) and [SecurityPermissionFlag.UnmanagedCode](/previous-versions/windows/) (see note below)<br/> |
| InkEdit                                                                               | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                          |
| [InkOverlay](/previous-versions/ms552322(v=vs.100))                                   | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                          |
| InkOverlay(IntPtr)                                                                    | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true) and SecurityPermissionFlag.UnmanagedCode<br/>                                                                 |
| [InkOverlay.Handle](/previous-versions/ms833109(v=msdn.10))                      | [UIPermissionWindow.AllWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true) and [SecurityPermissionFlag.UnmanagedCode](/previous-versions/windows/) (see note below)<br/> |
| [InkPicture](/previous-versions/aa514604(v=msdn.10))                                   | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                          |
| [PenInputPanel](/previous-versions/aa514041(v=msdn.10))                             | See note below.<br/>                                                                                                                                                                                     |
| [**InkRenderer**](inkrenderer-class.md)                                              | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                          |
| [**Draw**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-draw), [**DrawStroke**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-drawstroke)        | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true) and [SecurityPermissionFlag.UnmanagedCode](/previous-versions/windows/)<br/>         |
| Renderer.InkSpaceToPixel(IntPtr,Point), Renderer.InkSpaceToPixel(IntPtr,Point\[\])    | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true) and [SecurityPermissionFlag.UnmanagedCode](/previous-versions/windows/)<br/>         |
| Renderer.PixelToInkSpace(IntPtr,Point), Renderer.PixelToInkSpace(IntPtr,Point\[\])    | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true) and [SecurityPermissionFlag.UnmanagedCode](/previous-versions/windows/)<br/>         |
| [**DynamicRenderer**](/previous-versions/windows/desktop/legacy/ms701168(v=vs.85))                                      | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                          |
| DynamicRenderer(IntPtr)                                                               | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true) and [SecurityPermissionFlag.UnmanagedCode](/previous-versions/windows/)<br/>         |
| [**RealTimeStylus**](realtimestylus-class.md)                                        | [UIPermissionWindow.SafeTopLevelWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true)<br/>                                                                                                          |
| RealTimeStylus(IntPtr), RealTimeStylus(IntPtr,Boolean), RealTimeStylus(IntPtr,Tablet) | [UIPermissionWindow.AllWindows](/dotnet/api/system.security.permissions.uipermissionwindow?view=dotnet-plat-ext-3.1&preserve-view=true) and [SecurityPermissionFlag.UnmanagedCode](/previous-versions/windows/)<br/>                  |



 

> [!Note]  
> It is generally preferable to use a control rather than a handle (IntPtr) for constructors, because controls require fewer permissions. Similarly, it is preferable to use a Graphics object rather than a handle for [Renderer.Draw](/previous-versions/ms828488(v=msdn.10)), [Renderer.InkSpaceToPixel](/previous-versions/ms828495(v=msdn.10)) and [Renderer.PixelToInkSpace](/previous-versions/ms828505(v=msdn.10)).

 

> [!Note]  
> The [InkCollector.Handle](/previous-versions/ms836504(v=msdn.10)) and [InkOverlay.Handle](/previous-versions/ms833109(v=msdn.10)) properties do not require [SecurityPermissionFlag.UnmanagedCode](/previous-versions/windows/) permission if the handle is for a Windows Forms control, but they do for other windows.

 

> [!Note]  
> For the [PenInputPanel](/previous-versions/aa514041(v=msdn.10)) class, the following methods and properties require [SecurityPermissionFlag.AllFlags](/previous-versions/windows/): PenInputPanel(IntPtr), [AttachedEditWindow](/previous-versions/ms582240(v=vs.100)), [Busy](/previous-versions/ms571975(v=vs.100)), [CommitPendingInput](/previous-versions/ms569650(v=vs.100)), [CurrentPanel](/previous-versions/ms571976(v=vs.100)), [DefaultPanel](/previous-versions/ms571977(v=vs.100)), [EnableTsf](/previous-versions/ms569656(v=vs.100)), [Factoid](/previous-versions/ms571978(v=vs.100)), [Height](/previous-versions/ms571979(v=vs.100)), [HorizontalOffset](/previous-versions/ms571980(v=vs.100)), [InputFailed](/previous-versions/ms567738(v=vs.100)), [Left](/previous-versions/ms571981(v=vs.100)), [MoveTo](/previous-versions/ms569667(v=vs.100)), [PanelChanged](/previous-versions/ms567741(v=vs.100)), [PanelMoving](/previous-versions/ms567748(v=vs.100)), [Refresh](/previous-versions/ms569778(v=vs.100)), [Top](/previous-versions/ms571982(v=vs.100)), [VerticalOffset](/previous-versions/ms571983(v=vs.100)), [Visible](/previous-versions/ms571984(v=vs.100)), [VisibleChanged](/previous-versions/ms567754(v=vs.100)), and [Width](/previous-versions/ms571985(v=vs.100)).

 

## Other Considerations

Some other known security considerations are:

-   Microsoft Internet Explorer 6 or higher is required in order for Web controls to work properly. With Internet Explorer 5.5, only initial managed controls load; you cannot load additional controls dynamically at run-time.
-   If you are using Windows XP Service Pack 2 (SP2) and CLR1.0, then having Web controls in Internet Explorer require adding the site as a trusted site, even if they are in the Intranet zone. However, when you do so, they will no longer run in the Trusted Site zone, although they do run in the Intranet zone. This issue is fixed with CLR1.1.

 

 
