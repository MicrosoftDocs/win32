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

\[[**PenInputPanel**](peninputpanel-class.md) has been replaced by [**TextInputPanel**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanel) ([Microsoft.Ink.TextInput](frlrfMicrosoftInkTextInput) for managed code). Please refer to the [Programming the Text Input Panel](programming-the-text-input-panel.md).\]

The order of the various focus events for a control is as follows:

-   [Control.Enter](frlrfSystemWindowsFormsControlClassEnterTopic)
-   [Control.GotFocus](frlrfSystemWindowsFormsControlClassGotFocusTopic)
-   [Control.Leave](frlrfSystemWindowsFormsControlClassLeaveTopic)
-   [Control.Validating](frlrfSystemWindowsFormsControlClassValidatingTopic)
-   [Control.Validated](frlrfSystemWindowsFormsControlClassValidatedTopic)
-   [Control.LostFocus](frlrfSystemWindowsFormsControlClassLostFocusTopic)

There is no guarantee that the control actually has focus by the time the [Control.Visible](frlrfSystemWindowsFormsControlClassVisibleTopic) property is written when it is set in the [Control.Enter](frlrfSystemWindowsFormsControlClassEnterTopic) event handler. The Control.Enter event is the best place to attach the [PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic) object to a control, but the [Control.GotFocus](frlrfSystemWindowsFormsControlClassGotFocusTopic) event is the best place to change the [PenInputPanel.Visible](frlrfMicrosoftInkPenInputPanelClassVisibleTopic) property.

 

 



