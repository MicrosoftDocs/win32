---
description: The ink presenter APIs enable Microsoft Win32 apps to manage the input, processing, and rendering of ink input (standard and modified) through an InkPresenter object inserted into the app's DirectComposition visual tree.
ms.assetid: 8BD52813-3741-4C1F-B62A-B3C366A86362
title: Ink presenter
ms.topic: article
ms.date: 02/03/2020
---

# Ink presenter

The ink presenter APIs enable Microsoft Win32 apps to manage the input, processing, and rendering of ink input (standard and modified) through an [**InkPresenter**](/uwp/api/windows.ui.input.inking.inkpresenter) object inserted into the app's [DirectComposition](../directcomp/directcomposition-portal.md) visual tree.

> [!Note]
>
> Standard ink input (pen tip or eraser tip/button) is not modified with a secondary affordance, such as a pen barrel button, right mouse button, or similar.

Universal Windows Platform (UWP) apps using Extensible Application Markup Language (XAML) provide this functionality through an [**InkCanvas**](/uwp/api/Windows.UI.Xaml.Controls.InkCanvas) control along with an [**InkPresenter**](/uwp/api/windows.ui.input.inking.inkpresenter) object that connects to the XAML [DirectComposition](../directcomp/directcomposition-portal.md) visual tree. For more detail, see [Pen and stylus interactions](/windows/uwp/design/input/pen-and-stylus-interactions).

[Ink renderer](ink-renderer.md) is designed for use by Universal Windows app developers interested in providing XAML-based [**InkCanvas**](/uwp/api/Windows.UI.Xaml.Controls.InkCanvas)/[**InkPresenter**](/uwp/api/windows.ui.input.inking.inkpresenter) functionality in native Win32 apps.

## In this section



| Topic                                                               | Description                                                                                                         |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [Ink presenter classes](ink-presenter-classes.md)<br/>       | The topics contained in this section provide the reference specifications for Ink presenter classes. <br/>    |
| [Ink presenter interfaces](ink-presenter-interfaces.md)<br/> | The topics contained in this section provide the reference specifications for Ink presenter interfaces. <br/> |



 

## Related topics

[Ink presenter](ink-presenter.md), [Pen and stylus interactions](/windows/uwp/design/input/pen-and-stylus-interactions), [Ink Analysis sample](/samples/microsoft/windows-universal-samples/inkanalysis/), [Simple inking sample](/samples/microsoft/windows-universal-samples/simpleink/), [Complex inking sample](/samples/microsoft/windows-universal-samples/complexink/)
