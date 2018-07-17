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

An overview of the security model is given in [Secure, Light-Weight Client-Side Controls](http://go.microsoft.com/fwlink/p/?linkid=122505), and you can obtain more depth about the security model in [Code Access Security in Practice](http://msdn.microsoft.com/en-us/library/ff648663.aspx). A good overview on the security of libraries (which is especially important for [**UserControl**](https://msdn.microsoft.com/en-us/library/BR227647(v=Win.10).aspx) objects on a Web page) can be found in [Using Libraries from Partially Trusted Code](http://go.microsoft.com/fwlink/p/?linkid=180600), and other security information on managed controls can be found in [Writing Secure Managed Controls](http://go.microsoft.com/fwlink/p/?linkid=180601).

## Permissions

Most managed objects and members in the Tablet PC Technologies API have two requirements:

-   Execution is always required.
-   FullTrust is required when the [InheritanceDemand](T:System.Security.Permissions.SecurityAction) security action takes place. This means that full trust is required when a derived class inherits a class or overrides a method from the Tablet PC SDK.

The following table lists the classes and members that require additional permissions. The permissions for a given class also apply to all of its members not listed in this table.



| Class or Method                                                                       | Permissions                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-canpaste)                                                  | [UIPermissionClipboard.AllClipboard](T:System.Security.Permissions.UIPermissionClipboard)<br/>                                                                                                           |
| [**Ink.ClipboardCopy**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardcopy)                                    | [UIPermissionClipboard.OwnClipboard](T:System.Security.Permissions.UIPermissionClipboard)<br/>                                                                                                           |
| [**Ink.ClipboardPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardpaste)                                  | [UIPermissionClipboard.AllClipboard](T:System.Security.Permissions.UIPermissionClipboard)<br/>                                                                                                           |
| [**InkCollector**](inkcollector-class.md)                                            | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow)<br/>                                                                                                          |
| InkCollector(IntPtr)                                                                  | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow) and [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag)<br/>         |
| InkCollector.Handle                                                                   | [UIPermissionWindow.AllWindows](T:System.Security.Permissions.UIPermissionWindow) and [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag) (see note below)<br/> |
| InkEdit                                                                               | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow)<br/>                                                                                                          |
| [InkOverlay](frlrfMicrosoftInkInkOverlayClassTopic)                                   | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow)<br/>                                                                                                          |
| InkOverlay(IntPtr)                                                                    | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow) and SecurityPermissionFlag.UnmanagedCode<br/>                                                                 |
| [InkOverlay.Handle](frlrfMicrosoftInkInkOverlayClassHandleTopic)                      | [UIPermissionWindow.AllWindows](T:System.Security.Permissions.UIPermissionWindow) and [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag) (see note below)<br/> |
| [InkPicture](frlrfMicrosoftInkInkPictureClassTopic)                                   | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow)<br/>                                                                                                          |
| [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic)                             | See note below.<br/>                                                                                                                                                                                     |
| [**InkRenderer**](inkrenderer-class.md)                                              | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow)<br/>                                                                                                          |
| [**Draw**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-draw), [**DrawStroke**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-drawstroke)        | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow) and [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag)<br/>         |
| Renderer.InkSpaceToPixel(IntPtr,Point), Renderer.InkSpaceToPixel(IntPtr,Point\[\])    | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow) and [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag)<br/>         |
| Renderer.PixelToInkSpace(IntPtr,Point), Renderer.PixelToInkSpace(IntPtr,Point\[\])    | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow) and [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag)<br/>         |
| [**DynamicRenderer**](https://msdn.microsoft.com/en-us/library/ms701168(v=VS.85).aspx)                                      | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow)<br/>                                                                                                          |
| DynamicRenderer(IntPtr)                                                               | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow) and [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag)<br/>         |
| [**RealTimeStylus**](realtimestylus-class.md)                                        | [UIPermissionWindow.SafeTopLevelWindows](T:System.Security.Permissions.UIPermissionWindow)<br/>                                                                                                          |
| RealTimeStylus(IntPtr), RealTimeStylus(IntPtr,Boolean), RealTimeStylus(IntPtr,Tablet) | [UIPermissionWindow.AllWindows](T:System.Security.Permissions.UIPermissionWindow) and [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag)<br/>                  |



 

> [!Note]  
> It is generally preferable to use a control rather than a handle (IntPtr) for constructors, because controls require fewer permissions. Similarly, it is preferable to use a Graphics object rather than a handle for [Renderer.Draw](frlrfMicrosoftInkRendererClassDrawTopic), [Renderer.InkSpaceToPixel](frlrfMicrosoftInkRendererClassInkSpaceToPixelTopic) and [Renderer.PixelToInkSpace](frlrfMicrosoftInkRendererClassPixelToInkSpaceTopic).

 

> [!Note]  
> The [InkCollector.Handle](frlrfMicrosoftInkInkCollectorClassHandleTopic) and [InkOverlay.Handle](frlrfMicrosoftInkInkOverlayClassHandleTopic) properties do not require [SecurityPermissionFlag.UnmanagedCode](T:System.Security.Permissions.SecurityPermissionFlag) permission if the handle is for a Windows Forms control, but they do for other windows.

 

> [!Note]  
> For the [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) class, the following methods and properties require [SecurityPermissionFlag.AllFlags](T:System.Security.Permissions.SecurityPermissionFlag): PenInputPanel(IntPtr), [AttachedEditWindow](frlrfMicrosoftInkPenInputPanelClassAttachedEditWindowTopic), [Busy](frlrfMicrosoftInkPenInputPanelClassBusyTopic), [CommitPendingInput](frlrfMicrosoftInkPenInputPanelClassCommitPendingInputTopic), [CurrentPanel](frlrfMicrosoftInkPenInputPanelClassCurrentPanelTopic), [DefaultPanel](frlrfMicrosoftInkPenInputPanelClassDefaultPanelTopic), [EnableTsf](frlrfMicrosoftInkPenInputPanelClassEnableTsfTopic), [Factoid](frlrfMicrosoftInkPenInputPanelClassFactoidTopic), [Height](frlrfMicrosoftInkPenInputPanelClassHeightTopic), [HorizontalOffset](frlrfMicrosoftInkPenInputPanelClassHorizontalOffsetTopic), [InputFailed](frlrfMicrosoftInkPenInputPanelClassInputFailedTopic), [Left](frlrfMicrosoftInkPenInputPanelClassLeftTopic), [MoveTo](frlrfMicrosoftInkPenInputPanelClassMoveToTopic), [PanelChanged](frlrfMicrosoftInkPenInputPanelClassPanelChangedTopic), [PanelMoving](frlrfMicrosoftInkPenInputPanelClassPanelMovingTopic), [Refresh](frlrfMicrosoftInkPenInputPanelClassRefreshTopic), [Top](frlrfMicrosoftInkPenInputPanelClassTopTopic), [VerticalOffset](frlrfMicrosoftInkPenInputPanelClassVerticalOffsetTopic), [Visible](frlrfMicrosoftInkPenInputPanelClassVisibleTopic), [VisibleChanged](frlrfMicrosoftInkPenInputPanelClassVisibleChangedTopic), and [Width](frlrfMicrosoftInkPenInputPanelClassWidthTopic).

 

## Other Considerations

Some other known security considerations are:

-   Microsoft Internet Explorer 6 or higher is required in order for Web controls to work properly. With Internet Explorer 5.5, only initial managed controls load; you cannot load additional controls dynamically at run-time.
-   If you are using Windows XP Service Pack 2 (SP2) and CLR1.0, then having Web controls in Internet Explorer require adding the site as a trusted site, even if they are in the Intranet zone. However, when you do so, they will no longer run in the Trusted Site zone, although they do run in the Intranet zone. This issue is fixed with CLR1.1.

 

 




