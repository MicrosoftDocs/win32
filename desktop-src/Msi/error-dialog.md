---
description: An Error dialog box is a modal dialog box box that displays an error message. More than one Error dialog box can exist in each installation.
ms.assetid: 11d4fe8b-ec5f-4576-95e5-c86344f0195c
title: Error Dialog
ms.topic: article
ms.date: 05/31/2018
---

# Error Dialog

An Error dialog box is a modal dialog box box that displays an error message. More than one Error dialog box can exist in each installation.

An ErrorDialog property needs to be set that specifies which dialog box is to be used. If this property is not set or does not point to a valid Error dialog box, then the error messages will not be displayed. In this case, the error is only logged with a warning about the missing dialog box.

An Error dialog box must have the [Error Dialog style bit](error-dialog-style-bit.md) set. The dialog box must have a [Text control](text-control.md) named ErrorText. The record for the Error dialog box in the [Dialog table](dialog-table.md) must have the ErrorText control entered into the Control\_First field.

The dialog box must contain seven [PushButtons](pushbutton-control.md). All of these buttons specify the [EndDialog](enddialog-controlevent.md) ControlEvent in the [ControlEvent table](controlevent-table.md). Each button specifies one of the following attributes: **ErrorAbort**, **ErrorCancel**, **ErrorIgnore**, **ErrorNo**, **ErrorOk**, **ErrorRetry**, **ErrorYes**.

> [!Note]  
> The focus of these controls should not be linked through the use of the Control\_Next column in the [Control table](control-table.md).

 

These buttons should be placed in approximately the same position in the dialog box because when it is created, only a subset of these seven buttons is created, depending on the message. The X coordinate of the buttons is modified so the buttons that are displayed are evenly spaced. The Y coordinate, height, and width of the buttons are unchanged. Because the buttons are arranged horizontally, no other control can be placed in the same horizontal region of the dialog box.

For an Error dialog box, the Control\_Default and Control\_Cancel fields in the [Dialog table](dialog-table.md) are ignored. The Control\_First field for an Error dialog box must specify the ErrorText control.

If an [Icon control](icon-control.md) named ErrorIcon is included on this dialog, the following standard Windows icons are displayed:

-   IDI\_ERROR in response to imtFatalExit messages.
-   IDI\_WARNING in response to imtError and imtWarning messages.
-   IDI\_INFORMATION in response to imtOutOfDiskSpace messages.

The ErrorIcon control should be created with the [FixedSize control attribute](fixedsize-control-attribute.md) set to avoid improper sizing of the standard Windows icons.

 

 



