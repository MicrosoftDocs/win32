---
Description: Overview of best practices when using the pen input panel object.
ms.assetid: 5b127743-0c88-4c4c-bcb6-5a91690cd2a1
title: Best Practices
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Best Practices

There are a few guidelines to keep in mind when using the [**PenInputPanel**](/windows/desktop/api/msinkaut/) object.

-   [Prefer InkEdit Control](#prefer-inkedit-control)
-   [Disable Ink Mode on InkEdit Controls](#disable-ink-mode-on-inkedit-controls)
-   [Using Windowless Controls](#using-windowless-controls)
-   [Related topics](#related-topics)

## Prefer InkEdit Control

[InkEdit](inkedit-control-reference.md) is the preferred control to which to attach the [**PenInputPanel**](/windows/desktop/api/msinkaut/) object. The InkEdit control provides support for the [Text Services Framework (TSF)](text-services-framework.md).

## Disable Ink Mode on InkEdit Controls

When attached to an [InkEdit](inkedit-control-reference.md) control, set the [**InkMode**](/windows/desktop/api/inked/nf-inked-iinkedit-get_inkmode) property of the InkEdit control to the [**InkMode**](/windows/desktop/api/inked/ne-inked-inkmode) value. If the **InkMode** property is not set to the **InkMode** value, the InkEdit control interprets the first tap as a stroke, passes it to the recognizer, and inserts the text in the InkEdit control. Since you already have a [**PenInputPanel**](/windows/desktop/api/msinkaut/) object attached to accept ink input, there is no need to have the InkEdit control also enabled for ink input.

## Using Windowless Controls

When a [**PenInputPanel**](/windows/desktop/api/msinkaut/) object is attached to a parent window that contains more than one windowless control, the **PenInputPanel** object does not know how to track the caret as focus moves among windowless children. Handwriting input can be sent to the wrong child when focus moves from one windowless control to another while input is pending.

To use the [**PenInputPanel**](/windows/desktop/api/msinkaut/) object in a windowless environment, the following technique can be used:

1.  Instantiate a [TextBox](https://www.bing.com/search?q=TextBox) control and position it over the windowless control.
2.  Attach the [**PenInputPanel**](/windows/desktop/api/msinkaut/) object to the new text box control.
3.  Let the text box control collect the recognized text from the [**PenInputPanel**](/windows/desktop/api/msinkaut/) object.
4.  When focus changes away from the text box control, call the [**CommitPendingInput**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-commitpendinginput) method of the [**PenInputPanel**](/windows/desktop/api/msinkaut/) object.
5.  Copy the recognized text from the text box control to the windowless child.
6.  Detach the [**PenInputPanel**](/windows/desktop/api/msinkaut/) object by setting its [AttachedEditControl](https://www.bing.com/search?q=AttachedEditControl) (managed code only) property or [**AttachedEditWindow**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_attachededitwindow) property to null.
7.  Destroy the text box control.

## Related topics

<dl> <dt>

[**PenInputPanel Class**](/windows/desktop/api/msinkaut/)
</dt> <dt>

[Microsoft.Ink.PenInputPanel](https://www.bing.com/search?q=Microsoft.Ink.PenInputPanel)
</dt> <dt>

[Text Services Framework](http://go.microsoft.com/fwlink/p/?linkid=9037)
</dt> </dl>

 

 



