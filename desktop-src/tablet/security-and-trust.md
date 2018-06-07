---
Description: The .NET Framework has a security model that treats applications differently depending on their origin.
ms.assetid: 37fa870a-6f38-44ae-943e-27697f6b9fba
title: Security and Trust
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Security and Trust

The .NET Framework has a security model that treats applications differently depending on their origin. Executables and assemblies that are from a user's machine generally run with full trust; the same executables and assemblies run over the Internet generally run with partial trust. This is to prevent malicious code from either reading or modifying information it should not have access to, such as local files, items in the Clipboard, and other resources. If an executable calls an assembly, which in turn calls another assembly that requires a certain level of trust, then the lowest level of trust of all the components in the chain is applied. However, an administrator on a machine can set specific permissions that override the default permissions.

An overview of the security model is given in [Secure, Light-Weight Client-Side Controls](http://go.microsoft.com/fwlink/p/?linkid=122505), and you can obtain more depth about the security model in [Code Access Security in Practice](http://msdn.microsoft.com/en-us/library/ff648663.aspx). A good overview on the security of libraries (which is especially important for [**UserControl**](https://msdn.microsoft.com/Windows.UI.Xaml.Controls.UserControl) objects on a Web page) can be found in [Using Libraries from Partially Trusted Code](http://go.microsoft.com/fwlink/p/?linkid=180600), and other security information on managed controls can be found in [Writing Secure Managed Controls](http://go.microsoft.com/fwlink/p/?linkid=180601).

## Permissions

Most managed objects and members in the Tablet PC Technologies API have two requirements:

-   Execution is always required.
-   FullTrust is required when the [InheritanceDemand](https://www.bing.com/search?q=InheritanceDemand) security action takes place. This means that full trust is required when a derived class inherits a class or overrides a method from the Tablet PC SDK.

The following table lists the classes and members that require additional permissions. The permissions for a given class also apply to all of its members not listed in this table.



| Class or Method                                                                       | Permissions                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-canpaste)                                                  | [UIPermissionClipboard.AllClipboard](https://www.bing.com/search?q=UIPermissionClipboard.AllClipboard)<br/>                                                                                                           |
| [**Ink.ClipboardCopy**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardcopy)                                    | [UIPermissionClipboard.OwnClipboard](https://www.bing.com/search?q=UIPermissionClipboard.OwnClipboard)<br/>                                                                                                           |
| [**Ink.ClipboardPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardpaste)                                  | [UIPermissionClipboard.AllClipboard](https://www.bing.com/search?q=UIPermissionClipboard.AllClipboard)<br/>                                                                                                           |
| [**InkCollector**](/windows/desktop/api/msinkaut/)                                            | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows)<br/>                                                                                                          |
| InkCollector(IntPtr)                                                                  | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows) and [SecurityPermissionFlag.UnmanagedCode](https://www.bing.com/search?q=SecurityPermissionFlag.UnmanagedCode)<br/>         |
| InkCollector.Handle                                                                   | [UIPermissionWindow.AllWindows](https://www.bing.com/search?q=UIPermissionWindow.AllWindows) and [SecurityPermissionFlag.UnmanagedCode](https://www.bing.com/search?q=SecurityPermissionFlag.UnmanagedCode) (see note below)<br/> |
| InkEdit                                                                               | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows)<br/>                                                                                                          |
| [InkOverlay](https://www.bing.com/search?q=InkOverlay)                                   | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows)<br/>                                                                                                          |
| InkOverlay(IntPtr)                                                                    | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows) and SecurityPermissionFlag.UnmanagedCode<br/>                                                                 |
| [InkOverlay.Handle](https://www.bing.com/search?q=InkOverlay.Handle)                      | [UIPermissionWindow.AllWindows](https://www.bing.com/search?q=UIPermissionWindow.AllWindows) and [SecurityPermissionFlag.UnmanagedCode](https://www.bing.com/search?q=SecurityPermissionFlag.UnmanagedCode) (see note below)<br/> |
| [InkPicture](https://www.bing.com/search?q=InkPicture)                                   | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows)<br/>                                                                                                          |
| [PenInputPanel](https://www.bing.com/search?q=PenInputPanel)                             | See note below.<br/>                                                                                                                                                                                     |
| [**InkRenderer**](/windows/desktop/api/msinkaut/)                                              | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows)<br/>                                                                                                          |
| [**Draw**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-draw), [**DrawStroke**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-drawstroke)        | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows) and [SecurityPermissionFlag.UnmanagedCode](https://www.bing.com/search?q=SecurityPermissionFlag.UnmanagedCode)<br/>         |
| Renderer.InkSpaceToPixel(IntPtr,Point), Renderer.InkSpaceToPixel(IntPtr,Point\[\])    | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows) and [SecurityPermissionFlag.UnmanagedCode](https://www.bing.com/search?q=SecurityPermissionFlag.UnmanagedCode)<br/>         |
| Renderer.PixelToInkSpace(IntPtr,Point), Renderer.PixelToInkSpace(IntPtr,Point\[\])    | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows) and [SecurityPermissionFlag.UnmanagedCode](https://www.bing.com/search?q=SecurityPermissionFlag.UnmanagedCode)<br/>         |
| [**DynamicRenderer**](/windows/desktop/api/RTSCom/)                                      | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows)<br/>                                                                                                          |
| DynamicRenderer(IntPtr)                                                               | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows) and [SecurityPermissionFlag.UnmanagedCode](https://www.bing.com/search?q=SecurityPermissionFlag.UnmanagedCode)<br/>         |
| [**RealTimeStylus**](/windows/desktop/api/RTSCom/)                                        | [UIPermissionWindow.SafeTopLevelWindows](https://www.bing.com/search?q=UIPermissionWindow.SafeTopLevelWindows)<br/>                                                                                                          |
| RealTimeStylus(IntPtr), RealTimeStylus(IntPtr,Boolean), RealTimeStylus(IntPtr,Tablet) | [UIPermissionWindow.AllWindows](https://www.bing.com/search?q=UIPermissionWindow.AllWindows) and [SecurityPermissionFlag.UnmanagedCode](https://www.bing.com/search?q=SecurityPermissionFlag.UnmanagedCode)<br/>                  |



 

> [!Note]  
> It is generally preferable to use a control rather than a handle (IntPtr) for constructors, because controls require fewer permissions. Similarly, it is preferable to use a Graphics object rather than a handle for [Renderer.Draw](https://www.bing.com/search?q=Renderer.Draw), [Renderer.InkSpaceToPixel](https://www.bing.com/search?q=Renderer.InkSpaceToPixel) and [Renderer.PixelToInkSpace](https://www.bing.com/search?q=Renderer.PixelToInkSpace).

 

> [!Note]  
> The [InkCollector.Handle](https://www.bing.com/search?q=InkCollector.Handle) and [InkOverlay.Handle](https://www.bing.com/search?q=InkOverlay.Handle) properties do not require [SecurityPermissionFlag.UnmanagedCode](https://www.bing.com/search?q=SecurityPermissionFlag.UnmanagedCode) permission if the handle is for a Windows Forms control, but they do for other windows.

 

> [!Note]  
> For the [PenInputPanel](https://www.bing.com/search?q=PenInputPanel) class, the following methods and properties require [SecurityPermissionFlag.AllFlags](https://www.bing.com/search?q=SecurityPermissionFlag.AllFlags): PenInputPanel(IntPtr), [AttachedEditWindow](https://www.bing.com/search?q=AttachedEditWindow), [Busy](https://www.bing.com/search?q=Busy), [CommitPendingInput](https://www.bing.com/search?q=CommitPendingInput), [CurrentPanel](https://www.bing.com/search?q=CurrentPanel), [DefaultPanel](https://www.bing.com/search?q=DefaultPanel), [EnableTsf](https://www.bing.com/search?q=EnableTsf), [Factoid](https://www.bing.com/search?q=Factoid), [Height](https://www.bing.com/search?q=Height), [HorizontalOffset](https://www.bing.com/search?q=HorizontalOffset), [InputFailed](https://www.bing.com/search?q=InputFailed), [Left](https://www.bing.com/search?q=Left), [MoveTo](https://www.bing.com/search?q=MoveTo), [PanelChanged](https://www.bing.com/search?q=PanelChanged), [PanelMoving](https://www.bing.com/search?q=PanelMoving), [Refresh](https://www.bing.com/search?q=Refresh), [Top](https://www.bing.com/search?q=Top), [VerticalOffset](https://www.bing.com/search?q=VerticalOffset), [Visible](https://www.bing.com/search?q=Visible), [VisibleChanged](https://www.bing.com/search?q=VisibleChanged), and [Width](https://www.bing.com/search?q=Width).

 

## Other Considerations

Some other known security considerations are:

-   Microsoft Internet Explorer 6 or higher is required in order for Web controls to work properly. With Internet Explorer 5.5, only initial managed controls load; you cannot load additional controls dynamically at run-time.
-   If you are using Windows XP Service Pack 2 (SP2) and CLR1.0, then having Web controls in Internet Explorer require adding the site as a trusted site, even if they are in the Intranet zone. However, when you do so, they will no longer run in the Trusted Site zone, although they do run in the Intranet zone. This issue is fixed with CLR1.1.

 

 




