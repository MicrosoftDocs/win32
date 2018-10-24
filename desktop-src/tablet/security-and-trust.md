---
Description: The .NET Framework has a security model that treats applications differently depending on their origin.
ms.assetid: 37fa870a-6f38-44ae-943e-27697f6b9fba
title: Security and Trust
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Security and Trust

The .NET Framework has a security model that treats applications differently depending on their origin. Executables and assemblies that are from a user's machine generally run with full trust; the same executables and assemblies run over the Internet generally run with partial trust. This is to prevent malicious code from either reading or modifying information it should not have access to, such as local files, items in the Clipboard, and other resources. If an executable calls an assembly, which in turn calls another assembly that requires a certain level of trust, then the lowest level of trust of all the components in the chain is applied. However, an administrator on a machine can set specific permissions that override the default permissions.

An overview of the security model is given in [Secure, Light-Weight Client-Side Controls](http://go.microsoft.com/fwlink/p/?linkid=122505), and you can obtain more depth about the security model in [Code Access Security in Practice](http://msdn.microsoft.com/en-us/library/ff648663.aspx). A good overview on the security of libraries (which is especially important for [**UserControl**](https://msdn.microsoft.com/en-us/library/BR227647(v=Win.10).aspx) objects on a Web page) can be found in [Using Libraries from Partially Trusted Code](http://go.microsoft.com/fwlink/p/?linkid=180600), and other security information on managed controls can be found in [Writing Secure Managed Controls](http://go.microsoft.com/fwlink/p/?linkid=180601).

## Permissions

Most managed objects and members in the Tablet PC Technologies API have two requirements:

-   Execution is always required.
-   FullTrust is required when the [InheritanceDemand](https://msdn.microsoft.com/library/3scex4y1(v=VS.96).aspx) security action takes place. This means that full trust is required when a derived class inherits a class or overrides a method from the Tablet PC SDK.

The following table lists the classes and members that require additional permissions. The permissions for a given class also apply to all of its members not listed in this table.



| Class or Method                                                                       | Permissions                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-canpaste)                                                  | [UIPermissionClipboard.AllClipboard](https://msdn.microsoft.com/library/y173aaya(v=VS.90).aspx)<br/>                                                                                                           |
| [**Ink.ClipboardCopy**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardcopy)                                    | [UIPermissionClipboard.OwnClipboard](https://msdn.microsoft.com/library/y173aaya(v=VS.90).aspx)<br/>                                                                                                           |
| [**Ink.ClipboardPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardpaste)                                  | [UIPermissionClipboard.AllClipboard](https://msdn.microsoft.com/library/y173aaya(v=VS.90).aspx)<br/>                                                                                                           |
| [**InkCollector**](inkcollector-class.md)                                            | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx)<br/>                                                                                                          |
| InkCollector(IntPtr)                                                                  | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx) and [SecurityPermissionFlag.UnmanagedCode](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx)<br/>         |
| InkCollector.Handle                                                                   | [UIPermissionWindow.AllWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx) and [SecurityPermissionFlag.UnmanagedCode](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx) (see note below)<br/> |
| InkEdit                                                                               | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx)<br/>                                                                                                          |
| [InkOverlay](https://msdn.microsoft.com/library/ms552322(v=VS.100).aspx)                                   | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx)<br/>                                                                                                          |
| InkOverlay(IntPtr)                                                                    | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx) and SecurityPermissionFlag.UnmanagedCode<br/>                                                                 |
| [InkOverlay.Handle](https://msdn.microsoft.com/library/ms833109(v=MSDN.10).aspx)                      | [UIPermissionWindow.AllWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx) and [SecurityPermissionFlag.UnmanagedCode](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx) (see note below)<br/> |
| [InkPicture](https://msdn.microsoft.com/library/Aa514604(v=MSDN.10).aspx)                                   | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx)<br/>                                                                                                          |
| [PenInputPanel](https://msdn.microsoft.com/library/Aa514041(v=MSDN.10).aspx)                             | See note below.<br/>                                                                                                                                                                                     |
| [**InkRenderer**](inkrenderer-class.md)                                              | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx)<br/>                                                                                                          |
| [**Draw**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-draw), [**DrawStroke**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-drawstroke)        | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx) and [SecurityPermissionFlag.UnmanagedCode](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx)<br/>         |
| Renderer.InkSpaceToPixel(IntPtr,Point), Renderer.InkSpaceToPixel(IntPtr,Point\[\])    | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx) and [SecurityPermissionFlag.UnmanagedCode](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx)<br/>         |
| Renderer.PixelToInkSpace(IntPtr,Point), Renderer.PixelToInkSpace(IntPtr,Point\[\])    | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx) and [SecurityPermissionFlag.UnmanagedCode](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx)<br/>         |
| [**DynamicRenderer**](https://msdn.microsoft.com/en-us/library/ms701168(v=VS.85).aspx)                                      | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx)<br/>                                                                                                          |
| DynamicRenderer(IntPtr)                                                               | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx) and [SecurityPermissionFlag.UnmanagedCode](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx)<br/>         |
| [**RealTimeStylus**](realtimestylus-class.md)                                        | [UIPermissionWindow.SafeTopLevelWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx)<br/>                                                                                                          |
| RealTimeStylus(IntPtr), RealTimeStylus(IntPtr,Boolean), RealTimeStylus(IntPtr,Tablet) | [UIPermissionWindow.AllWindows](https://msdn.microsoft.com/library/twekyadz(v=VS.90).aspx) and [SecurityPermissionFlag.UnmanagedCode](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx)<br/>                  |



 

> [!Note]  
> It is generally preferable to use a control rather than a handle (IntPtr) for constructors, because controls require fewer permissions. Similarly, it is preferable to use a Graphics object rather than a handle for [Renderer.Draw](https://msdn.microsoft.com/library/ms828488(v=MSDN.10).aspx), [Renderer.InkSpaceToPixel](https://msdn.microsoft.com/library/ms828495(v=MSDN.10).aspx) and [Renderer.PixelToInkSpace](https://msdn.microsoft.com/library/ms828505(v=MSDN.10).aspx).

 

> [!Note]  
> The [InkCollector.Handle](https://msdn.microsoft.com/library/ms836504(v=MSDN.10).aspx) and [InkOverlay.Handle](https://msdn.microsoft.com/library/ms833109(v=MSDN.10).aspx) properties do not require [SecurityPermissionFlag.UnmanagedCode](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx) permission if the handle is for a Windows Forms control, but they do for other windows.

 

> [!Note]  
> For the [PenInputPanel](https://msdn.microsoft.com/library/Aa514041(v=MSDN.10).aspx) class, the following methods and properties require [SecurityPermissionFlag.AllFlags](https://msdn.microsoft.com/library/xc5yzfbx(v=VS.96).aspx): PenInputPanel(IntPtr), [AttachedEditWindow](https://msdn.microsoft.com/library/ms582240(v=VS.90).aspx), [Busy](https://msdn.microsoft.com/library/ms571975(v=VS.90).aspx), [CommitPendingInput](https://msdn.microsoft.com/library/ms569650(v=VS.90).aspx), [CurrentPanel](https://msdn.microsoft.com/library/ms571976(v=VS.90).aspx), [DefaultPanel](https://msdn.microsoft.com/library/ms571977(v=VS.90).aspx), [EnableTsf](https://msdn.microsoft.com/library/ms569656(v=VS.90).aspx), [Factoid](https://msdn.microsoft.com/library/ms571978(v=VS.90).aspx), [Height](https://msdn.microsoft.com/library/ms571979(v=VS.90).aspx), [HorizontalOffset](https://msdn.microsoft.com/library/ms571980(v=VS.90).aspx), [InputFailed](https://msdn.microsoft.com/library/ms567738(v=VS.90).aspx), [Left](https://msdn.microsoft.com/library/ms571981(v=VS.90).aspx), [MoveTo](https://msdn.microsoft.com/library/ms569667(v=VS.90).aspx), [PanelChanged](https://msdn.microsoft.com/library/ms567741(v=VS.90).aspx), [PanelMoving](https://msdn.microsoft.com/library/ms567748(v=VS.90).aspx), [Refresh](https://msdn.microsoft.com/library/ms569778(v=VS.90).aspx), [Top](https://msdn.microsoft.com/library/ms571982(v=VS.90).aspx), [VerticalOffset](https://msdn.microsoft.com/library/ms571983(v=VS.90).aspx), [Visible](https://msdn.microsoft.com/library/ms571984(v=VS.90).aspx), [VisibleChanged](https://msdn.microsoft.com/library/ms567754(v=VS.90).aspx), and [Width](https://msdn.microsoft.com/library/ms571985(v=VS.90).aspx).

 

## Other Considerations

Some other known security considerations are:

-   Microsoft Internet Explorer 6 or higher is required in order for Web controls to work properly. With Internet Explorer 5.5, only initial managed controls load; you cannot load additional controls dynamically at run-time.
-   If you are using Windows XP Service Pack 2 (SP2) and CLR1.0, then having Web controls in Internet Explorer require adding the site as a trusted site, even if they are in the Intranet zone. However, when you do so, they will no longer run in the Trusted Site zone, although they do run in the Intranet zone. This issue is fixed with CLR1.1.

 

 




