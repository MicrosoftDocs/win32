---
title: About IP Address Controls
description: An Internet Protocol (IP) address control allows the user to enter an IP address in an easily understood format.
ms.assetid: cf6a59fc-661c-420a-a67f-a42619946357
ms.topic: article
ms.date: 05/31/2018
---

# About IP Address Controls

An Internet Protocol (IP) address control allows the user to enter an IP address in an easily understood format. This control also allows the application to obtain the address in numeric form rather than in text form.

-   [About IP Address Controls](#about-ip-address-controls)
-   [Creating an IP Address Control](#creating-an-ip-address-control)
-   [Is an IP Address Control an Edit Control?](#is-an-ip-address-control-an-edit-control)

## About IP Address Controls

Windows Internet Explorer Version 4.0 introduces the IP address control, a new control similar to an edit control that allows the user to enter a numeric address in Internet protocol (IP) format. This format consists of four three-digit fields. Each field is treated individually; the field numbers are zero-based and proceed from left to right as shown in this figure.

![diagram showing values in each of the four fields of an ip address control](images/ipa-scrn.png)

The control allows only numeric text to be entered in each of the fields. Once three digits have been entered in a given field, keyboard focus is automatically moved to the next field. If filling the entire field is not required by the application, the user can enter fewer than three digits. For example, if the field should only contain the number twenty-one, typing "21" and pressing the key will take the user to the next field.

The default range for each field is 0 to 255, but the application can set the range to any values between those limits with the [**IPM\_SETRANGE**](ipm-setrange.md) message.

> [!Note]  
> The IP address control is implemented in version 4.71 and later of Comctl32.dll.

 

## Creating an IP Address Control

Before creating an IP address control, call [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) with the **ICC\_INTERNET\_CLASSES** flag set in the **dwICC** member of the [**INITCOMMONCONTROLSEX**](/windows/win32/api/commctrl/ns-commctrl-initcommoncontrolsex) structure.

Use the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function to create an IP address control. The class name for the control is [**WC\_IPADDRESS**](common-control-window-classes.md), which is defined in Commctrl.h. No IP address control-specific styles exist; however, because this is a child control, use the [**WS\_CHILD**](/windows/desktop/winmsg/window-styles) style as a minimum.

## Is an IP Address Control an Edit Control?

An IP address control is not an edit control and it will not respond to EM\_ messages. It will, however, send the owner window the following edit control notifications through the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message. Note that the IP address control will also send private IPN\_ notifications through the [**WM\_NOTIFY**](wm-notify.md) message.



|     Notification                              |     Reason for notification                                                                                                                                                                                                    |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [EN\_SETFOCUS](en-setfocus.md)   | Sent when the IP address control gains the keyboard focus.                                                                                                                                              |
| [EN\_KILLFOCUS](en-killfocus.md) | Sent when the IP address control loses the keyboard focus.                                                                                                                                              |
| [EN\_CHANGE](en-change.md)       | Sent when any field in the IP address control changes. Like the [EN\_CHANGE](en-change.md) notification from a standard edit control, this notification is received after the screen has been updated. |



 

 

 