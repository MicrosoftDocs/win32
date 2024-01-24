---
description: If this bit is set, the dialog box is an error dialog.
ms.assetid: a8a95f6a-6465-433b-98a4-95281cddedd3
title: Error Dialog Style Bit
ms.topic: article
ms.date: 05/31/2018
---

# Error Dialog Style Bit

If this bit is set, the dialog box is an error dialog.

There can be more than one dialog with this style. The **ErrorDialog** property determines which dialog is used as an error dialog. The selected dialog can be only one of those that have this style bit set. The error dialog must have a static text control named ErrorText. This control receives the text of the error message. The dialog should also have the seven push buttons corresponding to the possible return values. The error message determines which of these buttons are actually displayed. The displayed buttons are rearranged so they are evenly distributed on the dialog. This rearrangement changes the X coordinate of the buttons, but not the other three coordinates. Therefore it is advisable that no other control should be authored in the same horizontal region of the dialog as the buttons. If the error message specifies no button, the **OK** button is displayed. The **Default** button, First active control and **Cancel** button values are ignored for an error dialog. The **Default** button defined in the error message will be assigned to all three values. The effect of pushing these buttons have to be defined in the [ControlEvent table](controlevent-table.md) just like for all other buttons. The title of the dialog is authored in a way similar to other dialogs. It can get overwritten by the error message if it specifies a header text after the button list.

## Value



| Decimal | Hexadecimal | Constant                       |
|---------|-------------|--------------------------------|
| 65536   | 0x00010000  | **msidbDialogAttributesError** |



 

 

 



