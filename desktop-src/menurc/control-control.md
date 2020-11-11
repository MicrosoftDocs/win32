---
title: CONTROL control
description: Defines a user-defined control.
ms.assetid: e5e7b7af-e2b0-41ff-b697-b9ea80e7c61f
keywords:
- CONTROL control Menus and Other Resources
topic_type:
- apiref
api_name:
- CONTROL
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CONTROL control

Defines a user-defined control.

``` syntax
CONTROL text, id, class, style, x, y, width, height [, extended-style]
```

<dl> <dt>

<span id="class"></span><span id="CLASS"></span>*class*
</dt> <dd>

Redefined name, character string, or a 16-bit unsigned integer value that defines the class. This can be any one of the control classes; for a list of the control classes, see the first list following this description. If the value is a redefined name supplied by the application, it must be a string enclosed in double quotation marks (").

</dd> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Redefined name or integer value that specifies the style of the given control. The exact meaning of *style* depends on the *class* value. The sections following this description show the control classes and corresponding styles.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Remarks

The six possible control classes are described in the following sections.

### The Button Control Class

A button control is a small rectangular child window that the user can turn on or off by clicking it with the mouse. Button controls can be used alone or in groups, and can either be labeled or appear without text. Button controls typically change appearance when the user clicks them.

The button styles are described in the following topic: [Button Styles](../controls/button-styles.md).

### The Combo Box Control Class

Combo box controls consist of a selection field similar to an edit control plus a list box. The list box may be displayed at all times or may be dropped down when the user selects a "pop box" next to the selection field.

Depending on the style of the combo box, the user can or cannot edit the contents of the selection field. If the list box is visible, typing characters into the selection box will cause the first entry that matches the characters typed to be highlighted. Conversely, selecting an item in the list box displays the selected text in the selection field.

The combo box control styles are described in the following topic: [Combo Box Styles](../controls/combo-box-styles.md).

### The Edit Control Class

An edit control is a rectangular child window in which the user can enter text from the keyboard. The user selects the control, and gives it the input focus, by clicking the mouse inside it or pressing the TAB key. The user can enter text when the control displays a flashing insertion point. The mouse can be used to move the cursor and select characters to be replaced, or to position the cursor for inserting characters. The BACKSPACE key can be used to delete characters.

Edit controls use the fixed-pitch font and display Unicode characters. They expand tab characters into as many space characters as are required to move the cursor to the next tab stop. Tab stops are assumed to be at every eighth character position.

The edit control styles are described in the following topic: [Edit Control Styles](../controls/edit-control-styles.md).

### The List Box Control Class

List box controls consist of a list of character strings. The control is used whenever an application needs to present a list of names, such as filenames, that the user can view and select. The user can select a string by pointing to the string with the mouse and clicking a mouse button. When a string is selected, it is highlighted and a notification message is passed to the parent window. A scroll bar can be used with a list box control to scroll lists that are too long or too wide for the control window.

The list box control styles are described in the following topic: [List Box Styles](../controls/list-box-styles.md).

### The Scroll-Bar Control Class

A scroll-bar control is a rectangle that contains a scroll thumb and has direction arrows at both ends. The scroll bar sends a notification message to its parent whenever the user clicks the mouse in the control. The parent is responsible for updating the thumb position, if necessary. Scroll-bar controls have the same appearance and function as the scroll bars used in ordinary windows. But unlike scroll bars, scroll-bar controls can be positioned anywhere within a window and used whenever needed to provide scrolling input for a window.

The scroll bar styles are described in the following topic: [Scroll Bar Control Styles](../controls/scroll-bar-control-styles.md).

### The Static Control Class

Static controls are simple text fields, boxes, and rectangles that can be used to label, box, or separate other controls. Static controls take no input and provide no output.

The static control styles are described in the following topic: [Static Control Styles](../controls/static-control-styles.md).

 

 