---
Description: The topics contained in this section provide the reference specifications for Ink presenter interfaces.
ms.assetid: 68172566-586C-41AC-82B8-5DBE8B50EC8F
title: Ink presenter interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ink presenter interfaces

The topics contained in this section provide the reference specifications for [Ink presenter](ink-presenter.md) interfaces.

## In this section



| Topic                                                                   | Description                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IInkCommitRequestHandler**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkcommitrequesthandler?branch=master)<br/> | An [**IInkCommitRequestHandler**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkcommitrequesthandler?branch=master) object enables the app (instead of an [**IInkPresenterDesktop**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkpresenterdesktop?branch=master) object) to commit all pending Microsoft DirectComposition commands to the app's [DirectComposition](directcomp.directcomposition_portal) visual tree.<br/>   |
| [**IInkDesktopHost**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkdesktophost?branch=master)<br/>                   | An [**IInkDesktopHost**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkdesktophost?branch=master) object enables ink input, processing, and rendering through the creation of an app thread to host an [**IInkPresenterDesktop**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkpresenterdesktop?branch=master) object and insert it into the app's [DirectComposition](directcomp.directcomposition_portal) visual tree. <br/> |
| [**IInkHostWorkItem**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkhostworkitem?branch=master)<br/>                 | An [**IInkHostWorkItem**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkhostworkitem?branch=master) object represents an ink operation to be executed on an [**IInkDesktopHost**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkdesktophost?branch=master) object thread.<br/>                                                                                                                                                  |
| [**IInkPresenterDesktop**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkpresenterdesktop?branch=master)<br/>         | An [**IInkPresenterDesktop**](/windows/previous-versions/InkPresenterDesktop/nn-inkpresenterdesktop-iinkpresenterdesktop?branch=master) object represents an [**InkPresenter**](w_ui_input_ink.inkpresenter) that can be configured and inserted into the [DirectComposition](directcomp.directcomposition_portal) visual tree of the Classic Windows app. <br/>                                        |



 

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

 

 




