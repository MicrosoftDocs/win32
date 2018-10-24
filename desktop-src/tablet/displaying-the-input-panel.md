---
Description: Overview of displaying the input panel.
ms.assetid: 6301dde1-e46b-42a0-ae0b-ccd984e9199b
title: Displaying the Input Panel
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Displaying the Input Panel

\[[**PenInputPanel**](peninputpanel-class.md) has been replaced by [**TextInputPanel**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanel) ([Microsoft.Ink.TextInput](https://msdn.microsoft.com/library/ms581554(v=VS.90).aspx) for managed code). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

The order of the various focus events for a control is as follows:

-   [Control.Enter](https://msdn.microsoft.com/library/ash3dt4f(v=VS.90).aspx)
-   [Control.GotFocus](https://msdn.microsoft.com/library/t31a9w7d(v=VS.90).aspx)
-   [Control.Leave](https://msdn.microsoft.com/library/5weh0kcx(v=VS.90).aspx)
-   [Control.Validating](https://msdn.microsoft.com/library/35htw7by(v=VS.90).aspx)
-   [Control.Validated](https://msdn.microsoft.com/library/1x7dyebt(v=VS.90).aspx)
-   [Control.LostFocus](https://msdn.microsoft.com/library/98wbb910(v=VS.90).aspx)

There is no guarantee that the control actually has focus by the time the [Control.Visible](https://msdn.microsoft.com/library/3k8kd8ah(v=VS.90).aspx) property is written when it is set in the [Control.Enter](https://msdn.microsoft.com/library/ash3dt4f(v=VS.90).aspx) event handler. The Control.Enter event is the best place to attach the [PenInputPanel](https://msdn.microsoft.com/library/ms583923(v=VS.90).aspx) object to a control, but the [Control.GotFocus](https://msdn.microsoft.com/library/t31a9w7d(v=VS.90).aspx) event is the best place to change the [PenInputPanel.Visible](https://msdn.microsoft.com/library/ms571984(v=VS.90).aspx) property.

 

 



