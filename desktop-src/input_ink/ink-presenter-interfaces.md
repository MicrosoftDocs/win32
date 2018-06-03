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
| [**IInkCommitRequestHandler**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkcommitrequesthandler)<br/> | An [**IInkCommitRequestHandler**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkcommitrequesthandler) object enables the app (instead of an [**IInkPresenterDesktop**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkpresenterdesktop) object) to commit all pending Microsoft DirectComposition commands to the app's [DirectComposition](https://msdn.microsoft.com/windows/desktop/40e2d02b-77e8-425f-ac5e-3dcddef08173) visual tree.<br/>   |
| [**IInkDesktopHost**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkdesktophost)<br/>                   | An [**IInkDesktopHost**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkdesktophost) object enables ink input, processing, and rendering through the creation of an app thread to host an [**IInkPresenterDesktop**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkpresenterdesktop) object and insert it into the app's [DirectComposition](https://msdn.microsoft.com/windows/desktop/40e2d02b-77e8-425f-ac5e-3dcddef08173) visual tree. <br/> |
| [**IInkHostWorkItem**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkhostworkitem)<br/>                 | An [**IInkHostWorkItem**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkhostworkitem) object represents an ink operation to be executed on an [**IInkDesktopHost**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkdesktophost) object thread.<br/>                                                                                                                                                  |
| [**IInkPresenterDesktop**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkpresenterdesktop)<br/>         | An [**IInkPresenterDesktop**](/previous-versions/windows/desktop/api/InkPresenterDesktop/nn-inkpresenterdesktop-iinkpresenterdesktop) object represents an [**InkPresenter**](https://www.bing.com/search?q=**InkPresenter**) that can be configured and inserted into the [DirectComposition](https://msdn.microsoft.com/windows/desktop/40e2d02b-77e8-425f-ac5e-3dcddef08173) visual tree of the Classic Windows app. <br/>                                        |



 

## Related topics

<dl> <dt>

[Ink presenter](ink-presenter.md)
</dt> <dt>

[Pen and stylus interactions](https://www.bing.com/search?q=Pen and stylus interactions)
</dt> <dt>

**Samples**
</dt> <dt>

[Ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620308)
</dt> <dt>

[Simple ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620312)
</dt> <dt>

[Complex ink sample](http://go.microsoft.com/fwlink/p/?LinkID=620314)
</dt> </dl>

 

 




