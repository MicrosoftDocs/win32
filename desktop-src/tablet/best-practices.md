---
Description: 'Overview of best practices when using the pen input panel object.'
ms.assetid: '5b127743-0c88-4c4c-bcb6-5a91690cd2a1'
title: Best Practices
---

# Best Practices

There are a few guidelines to keep in mind when using the [**PenInputPanel**](peninputpanel-class.md) object.

-   [Prefer InkEdit Control](#prefer-inkedit-control)
-   [Disable Ink Mode on InkEdit Controls](#disable-ink-mode-on-inkedit-controls)
-   [Using Windowless Controls](#using-windowless-controls)
-   [Related topics](#related-topics)

## Prefer InkEdit Control

[InkEdit](inkedit-control-reference.md) is the preferred control to which to attach the [**PenInputPanel**](peninputpanel-class.md) object. The InkEdit control provides support for the [Text Services Framework (TSF)](text-services-framework.md).

## Disable Ink Mode on InkEdit Controls

When attached to an [InkEdit](inkedit-control-reference.md) control, set the [**InkMode**](inkedit-inkmode.md) property of the InkEdit control to the [**InkMode**](inkmode.md) value. If the **InkMode** property is not set to the **InkMode** value, the InkEdit control interprets the first tap as a stroke, passes it to the recognizer, and inserts the text in the InkEdit control. Since you already have a [**PenInputPanel**](peninputpanel-class.md) object attached to accept ink input, there is no need to have the InkEdit control also enabled for ink input.

## Using Windowless Controls

When a [**PenInputPanel**](peninputpanel-class.md) object is attached to a parent window that contains more than one windowless control, the **PenInputPanel** object does not know how to track the caret as focus moves among windowless children. Handwriting input can be sent to the wrong child when focus moves from one windowless control to another while input is pending.

To use the [**PenInputPanel**](peninputpanel-class.md) object in a windowless environment, the following technique can be used:

1.  Instantiate a [TextBox](T:System.Windows.Forms.TextBox) control and position it over the windowless control.
2.  Attach the [**PenInputPanel**](peninputpanel-class.md) object to the new text box control.
3.  Let the text box control collect the recognized text from the [**PenInputPanel**](peninputpanel-class.md) object.
4.  When focus changes away from the text box control, call the [**CommitPendingInput**](peninputpanel-commitpendinginput.md) method of the [**PenInputPanel**](peninputpanel-class.md) object.
5.  Copy the recognized text from the text box control to the windowless child.
6.  Detach the [**PenInputPanel**](peninputpanel-class.md) object by setting its [AttachedEditControl](frlrfMicrosoftInkPenInputPanelClassAttachedEditControlTopic) (managed code only) property or [**AttachedEditWindow**](peninputpanel-attachededitwindow.md) property to null.
7.  Destroy the text box control.

## Related topics

<dl> <dt>

[**PenInputPanel Class**](peninputpanel-class.md)
</dt> <dt>

[Microsoft.Ink.PenInputPanel](frlrfMicrosoftInkPenInputPanelClassTopic)
</dt> <dt>

[Text Services Framework](http://go.microsoft.com/fwlink/p/?linkid=9037)
</dt> </dl>

 

 



