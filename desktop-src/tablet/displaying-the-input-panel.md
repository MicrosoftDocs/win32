---
description: Overview of displaying the input panel.
ms.assetid: 6301dde1-e46b-42a0-ae0b-ccd984e9199b
title: Displaying the Input Panel
ms.topic: article
ms.date: 05/31/2018
---

# Displaying the Input Panel

\[[**PenInputPanel**](peninputpanel-class.md) has been replaced by [**TextInputPanel**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanel) ([Microsoft.Ink.TextInput](/previous-versions/dotnet/netframework-3.5/ms581554(v=vs.90)) for managed code). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

The order of the various focus events for a control is as follows:

-   [Control.Enter](/dotnet/api/system.windows.forms.control.enter?view=netcore-3.1)
-   [Control.GotFocus](/dotnet/api/system.windows.forms.control.gotfocus?view=netcore-3.1)
-   [Control.Leave](/dotnet/api/system.windows.forms.control.leave?view=netcore-3.1)
-   [Control.Validating](/dotnet/api/system.windows.forms.control.validating?view=netcore-3.1)
-   [Control.Validated](/dotnet/api/system.windows.forms.control.validated?view=netcore-3.1)
-   [Control.LostFocus](/dotnet/api/system.windows.forms.control.lostfocus?view=netcore-3.1)

There is no guarantee that the control actually has focus by the time the [Control.Visible](/dotnet/api/system.windows.forms.control.visible?view=netcore-3.1) property is written when it is set in the [Control.Enter](/dotnet/api/system.windows.forms.control.enter?view=netcore-3.1) event handler. The Control.Enter event is the best place to attach the [PenInputPanel](/previous-versions/ms583923(v=vs.100)) object to a control, but the [Control.GotFocus](/dotnet/api/system.windows.forms.control.gotfocus?view=netcore-3.1) event is the best place to change the [PenInputPanel.Visible](/previous-versions/ms571984(v=vs.100)) property.

 

 
