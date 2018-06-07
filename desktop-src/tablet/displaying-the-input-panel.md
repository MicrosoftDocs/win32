---
Description: Overview of displaying the input panel.
ms.assetid: 6301dde1-e46b-42a0-ae0b-ccd984e9199b
title: Displaying the Input Panel
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Displaying the Input Panel

\[[**PenInputPanel**](/windows/desktop/api/msinkaut/) has been replaced by [**TextInputPanel**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanel) ([Microsoft.Ink.TextInput](https://www.bing.com/search?q=Microsoft.Ink.TextInput) for managed code). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

The order of the various focus events for a control is as follows:

-   [Control.Enter](https://www.bing.com/search?q=Control.Enter)
-   [Control.GotFocus](https://www.bing.com/search?q=Control.GotFocus)
-   [Control.Leave](https://www.bing.com/search?q=Control.Leave)
-   [Control.Validating](https://www.bing.com/search?q=Control.Validating)
-   [Control.Validated](https://www.bing.com/search?q=Control.Validated)
-   [Control.LostFocus](https://www.bing.com/search?q=Control.LostFocus)

There is no guarantee that the control actually has focus by the time the [Control.Visible](https://www.bing.com/search?q=Control.Visible) property is written when it is set in the [Control.Enter](https://www.bing.com/search?q=Control.Enter) event handler. The Control.Enter event is the best place to attach the [PenInputPanel](https://www.bing.com/search?q=PenInputPanel) object to a control, but the [Control.GotFocus](https://www.bing.com/search?q=Control.GotFocus) event is the best place to change the [PenInputPanel.Visible](https://www.bing.com/search?q=PenInputPanel.Visible) property.

 

 



