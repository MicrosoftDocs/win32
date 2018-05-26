---
Description: IViewHelper
ms.assetid: c2b3771a-da75-4d49-8d8f-ea6a07d1951b
title: IViewHelper
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IViewHelper

The **IViewHelper** COM interface provides methods to configure a [Video Present Network (VidPN)](display.multiple_monitors_and_video_present_networks). Hardware vendors should create TMM applications that implement **IViewHelper** so that the operating system can place a laptop computer display into clone view.

In addition to the methods that **IViewHelper** inherits from the **IUnknown** interface, **IViewHelper** supports the following methods:

<dl>

[**IViewHelper::Commit**](/windows/win32/Cloneviewhelper/nf-cloneviewhelper-iviewhelper-commit?branch=master)  
[**IViewHelper::GetActiveTopology**](/windows/win32/cloneviewhelper/nf-cloneviewhelper-iviewhelper-getactivetopology?branch=master)  
[**IViewHelper::GetConnectedIDs**](/windows/win32/cloneviewhelper/nf-cloneviewhelper-iviewhelper-getconnectedids?branch=master)  
[**IViewHelper::GetProceedOnNewConfiguration**](/windows/win32/Cloneviewhelper/nf-cloneviewhelper-iviewhelper-getproceedonnewconfiguration?branch=master)  
[**IViewHelper::SetActiveTopology**](/windows/win32/cloneviewhelper/nf-cloneviewhelper-iviewhelper-setactivetopology?branch=master)  
[**IViewHelper::SetConfiguration**](/windows/win32/cloneviewhelper/nf-cloneviewhelper-iviewhelper-setconfiguration?branch=master)  
</dl>

For more information on the **IUnknown** interface, see the Microsoft Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdisplay\display%5D:%20IViewHelper%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



