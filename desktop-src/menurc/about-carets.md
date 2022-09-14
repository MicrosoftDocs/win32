---
title: About Carets
description: This topic discusses carets.
ms.assetid: 4487c93c-9a0f-467c-86b1-969f664d5526
keywords:
- resources,carets
- carets,removing
- blinking lines
- blinking blocks
- blinking bitmaps
- carets,visibility
- carets,blink times
- blink times
- carets,positions
- removing carets
ms.topic: article
ms.date: 05/31/2018
---

# About Carets

The system provides one caret per message queue. A window should create a caret only when it has the keyboard focus or is active. The window should destroy the caret before losing the keyboard focus or becoming inactive. For more information on keyboard input, see [Keyboard Input](/windows/desktop/inputdev/keyboard-input).

Use the [**CreateCaret**](/windows/desktop/api/Winuser/nf-winuser-createcaret) function to specify the parameters for a caret. The system forms a caret by inverting the pixel color within the rectangle specified by the caret's position, width, and height. The width and height are specified in logical units; therefore, the appearance of a caret is subject to the window's mapping mode.

The following topics are discussed in this section.

-   [Caret Visibility](#caret-visibility)
-   [Caret Blink Time](#caret-blink-time)
-   [Caret Position](#caret-position)
-   [Removing a Caret](#removing-a-caret)

## Caret Visibility

After the caret is defined, use the [**ShowCaret**](/windows/desktop/api/Winuser/nf-winuser-showcaret) function to make the caret visible. When the caret appears, it automatically begins flashing. To display a solid caret, the system inverts every pixel in the rectangle; to display a gray caret, the system inverts every other pixel; to display a bitmap caret, the system inverts only the white bits of the bitmap.

## Caret Blink Time

The elapsed time, in milliseconds, required to invert the caret is called the *blink time*. The caret will blink as long as the thread that owns the message queue has a message pump processing the messages.

The user can set the blink time of the caret using the Control Panel and applications should respect the settings that the user has chosen. An application can determine the caret's blink time by using the [**GetCaretBlinkTime**](/windows/desktop/api/Winuser/nf-winuser-getcaretblinktime) function. If you are writing an application that allows the user to adjust the blink time, such as a Control Panel applet, use the [**SetCaretBlinkTime**](/windows/desktop/api/Winuser/nf-winuser-setcaretblinktime) function to set the rate of the blink time to a specified number of milliseconds.

The *flash time* is the elapsed time, in milliseconds, required to display, invert, and restore the caret's display. The flash time of a caret is twice as much as the blink time.

## Caret Position

You can determine the position of the caret using the [**GetCaretPos**](/windows/desktop/api/Winuser/nf-winuser-getcaretpos) function. The position, in client coordinates, is copied to a structure specified by a parameter in **GetCaretPos**. An application can move a caret in a window by using the [**SetCaretPos**](/windows/desktop/api/Winuser/nf-winuser-setcaretpos) function. A window can move a caret only if it already owns the caret. **SetCaretPos** can move the caret whether it is visible or not.

## Removing a Caret

You can temporarily remove a caret by hiding it, or you can permanently remove the caret by destroying it. To hide the caret, use the [**HideCaret**](/windows/desktop/api/Winuser/nf-winuser-hidecaret) function. This is useful when your application must redraw the screen while processing a message, but must keep the caret out of the way. When the application finishes drawing, it can display the caret again by using the [**ShowCaret**](/windows/desktop/api/Winuser/nf-winuser-showcaret) function. Hiding the caret does not destroy its shape or invalidate the insertion point. Hiding the caret is cumulative; that is, if the application calls **HideCaret** five times, it must also call **ShowCaret** five times before the caret will reappear.

To remove the caret from the screen and destroy its shape, use using the [**DestroyCaret**](/windows/desktop/api/Winuser/nf-winuser-destroycaret) function. **DestroyCaret** destroys the caret only if the window involved in the current task owns the caret.

 

 