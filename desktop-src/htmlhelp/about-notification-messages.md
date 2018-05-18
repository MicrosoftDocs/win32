---
title: About Notification Messages
description: HTML Help notification messages are sent from a help window to the window that you specify in an HtmlHelp() call.
ms.assetid: 'C2A026AF-C759-4c72-8B7F-3848368E9AA6'
---

# About Notification Messages

HTML Help notification messages are sent from a help window to the window that you specify in an **HtmlHelp()** call. Use notification messages to track a user's activities in a help window. For example, if you want to invoke an action when a user clicks the **Refresh** button on the toolbar, you could use the [HHN\_TRACK](hhn-track-message.md) message.

Notification messages occur for the following events:

-   When a user clicks a button on the toolbar or clicks a tab on the Navigation pane of the [HTML Help Viewer](about-the-html-help-viewer.md), an [HHN\_TRACK](hhn-track-message.md) message is sent that identifies the button or tab that was clicked.
-   When a user navigates to a topic, an [HHN\_NAVCOMPLETE](hhn-navcomplete-message.md) message is sent that identifies the topic navigated to.
-   When a help window is created, an [HHN\_WINDOW\_CREATE](hhn-window-create-message.md) message is sent that identifies the window being created.

## To enable notification message tracking

HTML Help sends notification messages from help windows that have the following [**HH\_WINTYPE**](hh-wintype-structure.md) property settings:

-   The value of *hwndCaller* must be non zero.
-   The value of *idNotify* must be non zero.
-   A value must be specified for **HHWIN\_PARAM\_PROPERTIES** in the *fsValidProperties* member.
-   A value must be specified for **HHWIN\_PROP\_TRACKING** in the *fsWinProperties* member.

## To specify the window that will receive notification messages

Notification messages are sent to the window specified in the *hwndCaller* parameter of the **HtmlHelp()** call.

HTML Help notification messages are sent via Windows **WM\_NOTIFY** messages.

> [!Note]  
> Notification messages are not sent if the value of *hwndCaller* is the desktop.

 

### Notification messages quick reference

-   [HHN\_NAVCOMPLETE](hhn-navcomplete-message.md)
-   [HHN\_TRACK](hhn-track-message.md)
-   [HHN\_WINDOW\_CREATE](hhn-window-create-message.md)

## Related topics

<dl> <dt>

[About the HTML Help API](html-help-api-overview.md)
</dt> </dl>

 

 




