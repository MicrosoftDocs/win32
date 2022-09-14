---
description: The topics contained in this section provide the reference specifications for Ink presenter interfaces.
ms.assetid: 68172566-586C-41AC-82B8-5DBE8B50EC8F
title: Ink presenter interfaces
ms.topic: article
ms.date: 02/03/2020
---

# Ink presenter interfaces

The topics contained in this section provide the reference specifications for [Ink presenter](ink-presenter.md) interfaces.

## In this section

| Topic | Description |
|---|---|
| [**IInkCommitRequestHandler**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkcommitrequesthandler)<br/> | Enables your app (instead of an [**IInkPresenterDesktop**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkpresenterdesktop) object) to commit all pending Microsoft DirectComposition commands to the app's [DirectComposition](../directcomp/directcomposition-portal.md) visual tree.<br/>   |
| [**IInkDesktopHost**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkdesktophost)<br/>                   | Enables ink input, processing, and rendering through the creation of an app thread to host an [**IInkPresenterDesktop**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkpresenterdesktop) object and insert it into the app's [DirectComposition](../directcomp/directcomposition-portal.md) visual tree. <br/> |
| [**IInkHostWorkItem**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkhostworkitem)<br/>                 | Represents an ink operation to be executed on an [**IInkDesktopHost**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkpresenterdesktop) object thread.<br/>                                                                                                                                                  |
| [**IInkPresenterDesktop**](/windows/win32/api/inkpresenterdesktop/nn-inkpresenterdesktop-iinkpresenterdesktop)<br/>         | Represents an [**InkPresenter**](/uwp/api/Windows.UI.Input.Inking.InkPresenter) that can be configured and inserted into the [DirectComposition](../directcomp/directcomposition-portal.md) visual tree of the Classic Windows app. <br/>                                        |

## Related topics

[Ink presenter](ink-presenter.md), [Pen and stylus interactions](/windows/uwp/design/input/pen-and-stylus-interactions), [Ink Analysis sample](/samples/microsoft/windows-universal-samples/inkanalysis/), [Simple inking sample](/samples/microsoft/windows-universal-samples/simpleink/), [Complex inking sample](/samples/microsoft/windows-universal-samples/complexink/)
