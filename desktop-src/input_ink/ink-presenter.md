---
Description: The ink presenter APIs enable Microsoft Win32 apps to manage the input, processing, and rendering of ink input (standard and modified) through an InkPresenter object inserted into the app's DirectComposition visual tree.
ms.assetid: 8BD52813-3741-4C1F-B62A-B3C366A86362
title: Ink presenter
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ink presenter

The ink presenter APIs enable Microsoft Win32 apps to manage the input, processing, and rendering of ink input (standard and modified) through an [**InkPresenter**](https://msdn.microsoft.com/en-us/library/Dn922011(v=WIN.10).aspx) object inserted into the app's [DirectComposition](https://msdn.microsoft.com/en-us/library/Hh437371(v=VS.85).aspx) visual tree.

> [!Note]
>
> Standard ink input (pen tip or eraser tip/button) is not modified with a secondary affordance, such as a pen barrel button, right mouse button, or similar.

 

Universal Windows Platform (UWP) apps using Extensible Application Markup Language (XAML) provide this functionality through an [**InkCanvas**](https://msdn.microsoft.com/en-us/library/Dn858535(v=WIN.10).aspx) control along with an [**InkPresenter**](https://msdn.microsoft.com/en-us/library/Dn922011(v=WIN.10).aspx) object that connects to the XAML [DirectComposition](https://msdn.microsoft.com/en-us/library/Hh437371(v=VS.85).aspx) visual tree. For more detail, see [Pen and stylus interactions](https://msdn.microsoft.com/en-us/library/Mt187311(v=WIN.10).aspx).

[Ink renderer](ink-renderer.md) is designed for use by Universal Windows app developers interested in providing XAML-based [**InkCanvas**](https://msdn.microsoft.com/en-us/library/Dn858535(v=WIN.10).aspx)/[**InkPresenter**](https://msdn.microsoft.com/en-us/library/Dn922011(v=WIN.10).aspx) functionality in native Win32 apps.

## In this section



| Topic                                                               | Description                                                                                                         |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [Ink presenter classes](ink-presenter-classes.md)<br/>       | The topics contained in this section provide the reference specifications for Ink presenter classes. <br/>    |
| [Ink presenter interfaces](ink-presenter-interfaces.md)<br/> | The topics contained in this section provide the reference specifications for Ink presenter interfaces. <br/> |



 

## Related topics

<dl> <dt>

[Ink input](input-ink-portal.md)
</dt> <dt>

[Pen and stylus interactions](https://msdn.microsoft.com/en-us/library/Mt187311(v=WIN.10).aspx)
</dt> <dt>

**Samples**
</dt> <dt>

[Ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620308)
</dt> <dt>

[Simple ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620312)
</dt> <dt>

[Complex ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620314)
</dt> </dl>

 

 




