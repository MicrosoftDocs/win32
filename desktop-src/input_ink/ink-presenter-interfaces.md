---
Description: 'The topics contained in this section provide the reference specifications for Ink presenter interfaces.'
ms.assetid: '68172566-586C-41AC-82B8-5DBE8B50EC8F'
title: Ink presenter interfaces
---

# Ink presenter interfaces

The topics contained in this section provide the reference specifications for [Ink presenter](ink-presenter.md) interfaces.

## In this section



| Topic                                                                   | Description                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IInkCommitRequestHandler**](iinkcommitrequesthandler.md)<br/> | An [**IInkCommitRequestHandler**](iinkcommitrequesthandler.md) object enables the app (instead of an [**IInkPresenterDesktop**](iinkpresenterdesktop.md) object) to commit all pending Microsoft DirectComposition commands to the app's [DirectComposition](directcomp.directcomposition_portal) visual tree.<br/>   |
| [**IInkDesktopHost**](iinkdesktophost.md)<br/>                   | An [**IInkDesktopHost**](iinkdesktophost.md) object enables ink input, processing, and rendering through the creation of an app thread to host an [**IInkPresenterDesktop**](iinkpresenterdesktop.md) object and insert it into the app's [DirectComposition](directcomp.directcomposition_portal) visual tree. <br/> |
| [**IInkHostWorkItem**](iinkhostworkitem.md)<br/>                 | An [**IInkHostWorkItem**](iinkhostworkitem.md) object represents an ink operation to be executed on an [**IInkDesktopHost**](iinkdesktophost.md) object thread.<br/>                                                                                                                                                  |
| [**IInkPresenterDesktop**](iinkpresenterdesktop.md)<br/>         | An [**IInkPresenterDesktop**](iinkpresenterdesktop.md) object represents an [**InkPresenter**](w_ui_input_ink.inkpresenter) that can be configured and inserted into the [DirectComposition](directcomp.directcomposition_portal) visual tree of the Classic Windows app. <br/>                                        |



 

## Related topics

<dl> <dt>

[Ink presenter](ink-presenter.md)
</dt> <dt>

[Pen and stylus interactions](dev_custom_user_input.pen_and_stylus_interactions)
</dt> <dt>

**Samples**
</dt> <dt>

[Ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620308)
</dt> <dt>

[Simple ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620312)
</dt> <dt>

[Complex ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620314)
</dt> </dl>

 

 




