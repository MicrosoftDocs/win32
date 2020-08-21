---
title: About Static Controls
description: This topic discusses how static controls are used.
ms.assetid: 155904e1-a963-496d-9b22-6e95ed0ebd47
ms.topic: article
ms.date: 05/31/2018
---

# About Static Controls

Applications often use static controls to label other controls or to separate a group of controls. Although static controls are child windows, they cannot be selected. Therefore, they cannot receive the keyboard focus and cannot have a keyboard interface. A static control that has the SS\_NOTIFY style receives mouse input, notifying the parent window when the user clicks or double clicks the control. Static controls belong to the STATIC window class.

Although static controls can be used in overlapped, pop-up, and child windows, they are designed for use in dialog boxes, where the system standardizes their behavior. By using static controls outside dialog boxes, a developer increases the risk that the application might behave in a nonstandard fashion. Typically, a developer either uses static controls in dialog boxes or uses the SS\_OWNERDRAW style to create customized static controls.

The following topics are discussed in this section.

-   [Static Control Types](#static-control-types)
    -   [Simple Graphics Static Control](#simple-graphics-static-control)
    -   [Text Static Control](#text-static-control)
    -   [Image Static Control](#image-static-control)
    -   [Owner-Drawn Static Control](#owner-drawn-static-control)
-   [Static Control Default Message Processing](#static-control-default-message-processing)

## Static Control Types

There are four types of static controls. Each type has one or more [Static Control Styles](static-control-styles.md).

-   [Simple Graphics Static Control](#simple-graphics-static-control)
-   [Text Static Control](#text-static-control)
-   [Image Static Control](#image-static-control)
-   [Owner-Drawn Static Control](#owner-drawn-static-control)

### Simple Graphics Static Control

A simple graphics static control displays a frame or a filled rectangle. A frame can be drawn in a number of styles, included black, gray, or white. In addition, a frame can be drawn with an etched style to give it a three-dimensional appearance. The frame styles include SS\_BLACKFRAME, SS\_GRAYFRAME, SS\_WHITEFRAME, SS\_ETCHEDHORZ, SS\_ETCHEDVERT, and SS\_ETCHEDFRAME.

A rectangle can be filled with color in one of three styles: black, gray, or white. These styles are defined by the constants SS\_BLACKRECT, SS\_GRAYRECT, and SS\_WHITERECT.

The graphics styles cannot be combined.

### Text Static Control

A text static control displays text in a rectangle in one of five styles:

-   left-aligned without word wrap
-   left-aligned with word wrap
-   centered
-   right-aligned
-   simple

These styles are defined by the constants SS\_LEFTNOWORDWRAP, SS\_LEFT, SS\_CENTER, SS\_RIGHT, and SS\_SIMPLE, respectively. The system rearranges the text in these controls in predefined ways, except for "simple" text, which is not rearranged.

An application can change the text in a text static control at any time by using the [**SetWindowText**](/windows/desktop/api/winuser/nf-winuser-setwindowtexta) function or the [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext) message.

The system displays as much text as it can in the static control and clips whatever does not fit. To calculate an appropriate size for the control, retrieve the font metrics for the text. For more information about fonts and font metrics, see [Fonts and Text](/windows/desktop/gdi/fonts-and-text).

By default, the window text for a static control, as for other controls, can contain an ampersand that defines the following character as the shortcut key for the control (or, in the case of most static controls, for the control that it labels, which is the next control in the tab order). If you wish to display ampersands in the text rather than using them to define shortcuts, include the SS\_NOPREFIX style.

### Image Static Control

An image static control can display bitmaps, icons (including animated icons), or enhanced metafiles. The type of graphic that a particular static control displays depends on the control's style: SS\_BITMAP, SS\_ICON, or SS\_ENHMETAFILE. An application specifies the style when it creates the control and also specifies a handle to the bitmap, icon, or metafile for the control to display. After the control is created, an application can associate a different graphic with the control by sending it an [**STM\_SETIMAGE**](stm-setimage.md) message, specifying a handle to the new graphic object. An application can retrieve a handle to the graphic object currently associated with a static control by sending it an [**STM\_GETIMAGE**](stm-getimage.md) message. An application sends messages to a static control by using the [**SendDlgItemMessage**](/windows/desktop/api/winuser/nf-winuser-senddlgitemmessagea) function.

### Owner-Drawn Static Control

By using the SS\_OWNERDRAW style, an application can take responsibility for painting a static control. The parent window of an owner-drawn static control (its owner) receives a [**WM\_DRAWITEM**](wm-drawitem.md) message whenever the static control needs to be painted. The message includes a pointer to a [**DRAWITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-drawitemstruct) structure that contains information that the owner window uses when drawing the control.

## Static Control Default Message Processing

The window procedure for the predefined static control window class performs default processing for all messages that the static control procedure does not process. When the static control returns **FALSE** for any message, the predefined window procedure checks the messages and carries out the default action described in the following table. In the table, a text static control is a static control with the style SS\_LEFTNOWORDWRAP, SS\_LEFT, SS\_CENTER, SS\_RIGHT, or SS\_SIMPLE.



| Message                                                | Default action                                                                                                                              |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CREATE**](/windows/desktop/winmsg/wm-create)                     | Loads the graphic object and sizes the window to the object's size, for graphic static controls. Takes no action for other static controls. |
| [**WM\_DESTROY**](/windows/desktop/winmsg/wm-destroy)                   | Frees and destroys any graphic object, for graphic static controls. Takes no action for other static controls.                              |
| [**WM\_ENABLE**](/windows/desktop/winmsg/wm-enable)                     | Repaints visible static controls.                                                                                                           |
| [**WM\_ERASEBKGND**](/windows/desktop/winmsg/wm-erasebkgnd)             | Returns **TRUE**, indicating the control erases the background.                                                                             |
| [**WM\_GETDLGCODE**](/windows/desktop/dlgbox/wm-getdlgcode)             | Returns DLGC\_STATIC.                                                                                                                       |
| [**WM\_GETFONT**](/windows/desktop/winmsg/wm-getfont)                   | Returns a handle to the font for text static controls.                                                                                      |
| [**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext)                   | Returns the number of characters copied.                                                                                                    |
| [**WM\_GETTEXTLENGTH**](/windows/desktop/winmsg/wm-gettextlength)       | Returns the length, in characters, of the text for a text static control.                                                                   |
| [**WM\_LBUTTONDBLCLK**](/windows/desktop/inputdev/wm-lbuttondblclk)     | Sends the parent window an [STN\_DBLCLK](stn-dblclk.md) notification code if the control style is SS\_NOTIFY.                              |
| [**WM\_LBUTTONDOWN**](/windows/desktop/inputdev/wm-lbuttondown)         | Sends the parent window an [STN\_CLICKED](stn-clicked.md) notification code if the control style is SS\_NOTIFY.                            |
| [**WM\_NCLBUTTONDBLCLK**](/windows/desktop/inputdev/wm-nclbuttondblclk) | Sends the parent window an [STN\_DBLCLK](stn-dblclk.md) notification code if the control style is SS\_NOTIFY.                              |
| [**WM\_NCLBUTTONDOWN**](/windows/desktop/inputdev/wm-nclbuttondown)     | Sends the parent window an [STN\_CLICKED](stn-clicked.md) notification code if the control style is SS\_NOTIFY.                            |
| [**WM\_NCHITTEST**](/windows/desktop/inputdev/wm-nchittest)             | Returns HTCLIENT if the control style is SS\_NOTIFY; otherwise, returns HTTRANSPARENT.                                                      |
| [**WM\_PAINT**](/windows/desktop/gdi/wm-paint)                          | Repaints the control.                                                                                                                       |
| [**WM\_SETFONT**](/windows/desktop/winmsg/wm-setfont)                   | Sets the font and repaints for text static controls.                                                                                        |
| [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext)                   | Sets the text and repaints for text static controls.                                                                                        |



 

The predefined window procedure passes all other messages to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) for default processing.

 

 