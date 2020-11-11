---
title: Button States
description: This section discusses how selecting a button changes its state and how the application should respond.
ms.assetid: 7302f0f3-f29d-43d7-8e25-4f36d5ef6a86
ms.topic: article
ms.date: 05/31/2018
---

# Button States

This section discusses how selecting a button changes its state and how the application should respond.

The section consists of the following topics:

-   [Button Selection](#button-selection)
-   [Elements of a Button State](#elements-of-a-button-state)
    -   [Focus State](#focus-state)
    -   [Push State](#push-state)
    -   [Check State](#check-state)
-   [Changes to a Button State](#changes-to-a-button-state)

## Button Selection

The user can select a button in three ways: by clicking it with the mouse, by tabbing to it and then pressing the ENTER key, or (if the button is part of a group defined by the [**WS\_GROUP**](/windows/desktop/winmsg/window-styles) style) by tabbing to the selected button in the group and using the arrow keys to move within that group. The two tabbing methods are part of the predefined keyboard interface provided by the system. For a complete description of this interface, see [Dialog Boxes](/windows/desktop/dlgbox/dialog-boxes).

Selecting a button typically causes the following events:

-   The system gives the button the keyboard focus.
-   The button sends its parent window a message to notify it of the selection.
-   The parent window (or the system) sends the button a message to change its state.
-   The parent window (or the system) repaints the button to reflect its new state.

## Elements of a Button State

A button's state can be characterized by its focus state, push state, and check state.

-   [Focus State](#focus-state)
-   [Push State](#push-state)
-   [Check State](#check-state)

### Focus State

The focus state applies to a check box, radio button, push button, or owner-drawn button. A button receives the keyboard focus when the user selects it and loses the focus when the user selects another control. Only one control can have the keyboard focus at a time.

When a button has the keyboard focus, the system typically highlights the text, icon, or bitmap of a button by surrounding it with a dotted line. In addition, a push button has a heavy dark border when it has the focus. The system automatically changes the highlight for an automatic button, but the application must change the highlight for a non-automatic button by sending messages.

### Push State

The push state applies to a push button, check box, radio button, or three-state check box, but does not apply to other buttons. The push state of a button can be either pushed or not pushed. When a push button (or any button with the [**BS\_PUSHLIKE**](button-styles.md) style) is pushed, the button is drawn as a sunken button. When it is not pushed, it is drawn as a raised button. When a check box, radio button, or three-state check box is clicked, the background of the button is grayed. When it is not pushed, the background of the button is not grayed.

### Check State

The check state applies to a check box, radio button, or three-state check box, but does not apply to other buttons. The state can be checked, cleared, or (for three-state check boxes) indeterminate. A check box is checked when it contains a check mark, and is cleared when it does not. A radio button is checked when it contains a black dot; it is cleared when it does not. A three-state check box is checked when it contains a check mark, is cleared when it does not, and is indeterminate when it contains a grayed box. The system automatically changes the check state of an automatic button, but the application must change the check state of a non-automatic button.

## Changes to a Button State

When the user selects a button, it is generally necessary to change one or more of the button's state elements. The system automatically changes the focus state for all button types, the push state for push buttons or buttons with the [**BS\_PUSHLIKE**](button-styles.md) style, and the check state for all automatic buttons. The application must make all other state changes, taking into account the button's type, style, and current state. The following list shows the state elements that must be changed for each button type:

-   A check box must change the check state.
-   A radio button must change the check state. It may also be necessary to change the check state of other radio buttons in the same group to ensure the mutually exclusive nature of radio buttons.
-   Because the state of an owner-drawn button is application dependent, what the application must change in the button can vary. No elements of a group box must be changed, because users cannot select group boxes.

An application can determine a button's state by sending it a [**BM\_GETCHECK**](bm-getcheck.md) or [**BM\_GETSTATE**](bm-getstate.md) message; the application can set a button's state by sending it a [**BM\_SETCHECK**](bm-setcheck.md) or [**BM\_SETSTATE**](bm-setstate.md) message.

 

 