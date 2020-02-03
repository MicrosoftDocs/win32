---
Description: The topics contained in this section provide the reference specifications for Ink presenter interfaces.
ms.assetid: 68172566-586C-41AC-82B8-5DBE8B50EC8F
title: Ink presenter interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ink presenter interfaces

The topics contained in this section provide the reference specifications for [Ink presenter](ink-presenter.md) interfaces.

## In this section



| Topic                                                                   | Description                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IInkCommitRequestHandler**](https://msdn.microsoft.com/en-us/library/Mt622147(v=VS.85).aspx)<br/> | An [**IInkCommitRequestHandler**](https://msdn.microsoft.com/en-us/library/Mt622147(v=VS.85).aspx) object enables the app (instead of an [**IInkPresenterDesktop**](https://msdn.microsoft.com/en-us/library/Mt622155(v=VS.85).aspx) object) to commit all pending Microsoft DirectComposition commands to the app's [DirectComposition](https://msdn.microsoft.com/en-us/library/Hh437371(v=VS.85).aspx) visual tree.<br/>   |
| [**IInkDesktopHost**](https://msdn.microsoft.com/en-us/library/Mt622149(v=VS.85).aspx)<br/>                   | An [**IInkDesktopHost**](https://msdn.microsoft.com/en-us/library/Mt622149(v=VS.85).aspx) object enables ink input, processing, and rendering through the creation of an app thread to host an [**IInkPresenterDesktop**](https://msdn.microsoft.com/en-us/library/Mt622155(v=VS.85).aspx) object and insert it into the app's [DirectComposition](https://msdn.microsoft.com/en-us/library/Hh437371(v=VS.85).aspx) visual tree. <br/> |
| [**IInkHostWorkItem**](https://msdn.microsoft.com/en-us/library/Mt622153(v=VS.85).aspx)<br/>                 | An [**IInkHostWorkItem**](https://msdn.microsoft.com/en-us/library/Mt622153(v=VS.85).aspx) object represents an ink operation to be executed on an [**IInkDesktopHost**](https://msdn.microsoft.com/en-us/library/Mt622149(v=VS.85).aspx) object thread.<br/>                                                                                                                                                  |
| [**IInkPresenterDesktop**](https://msdn.microsoft.com/en-us/library/Mt622155(v=VS.85).aspx)<br/>         | An [**IInkPresenterDesktop**](https://msdn.microsoft.com/en-us/library/Mt622155(v=VS.85).aspx) object represents an [**InkPresenter**](https://msdn.microsoft.com/en-us/library/Dn922011(v=WIN.10).aspx) that can be configured and inserted into the [DirectComposition](https://msdn.microsoft.com/en-us/library/Hh437371(v=VS.85).aspx) visual tree of the Classic Windows app. <br/>                                        |



 

## Related topics

<dl> <dt>

[Ink presenter](ink-presenter.md)
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

 

 




