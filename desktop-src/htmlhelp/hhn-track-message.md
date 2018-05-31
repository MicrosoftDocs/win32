---
title: HHN\_TRACK message
description: Sent when a user clicks a button on the toolbar or a tab in the Navigation pane of the HTML Help Viewer. The message is sent before the action is taken.
ms.assetid: ED5C45E1-B26C-4a1f-836B-E93E2EE31D40
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HHN\_TRACK message

Sent when a user clicks a button on the toolbar or a tab in the Navigation pane of the HTML Help Viewer. The message is sent before the action is taken.



| Notification code | lParam                                                            |
|-------------------|-------------------------------------------------------------------|
| HHN\_TRACK        | A pointer to an [**HHNTRACK**](hhntrack-structure.md) structure. |



 

## Remarks

-   Make sure that the help window definition includes the settings for notification messages. Otherwise, HTML Help will not send notification messages.
-   If the button click results in navigation to a different topic, an [HHN\_NAVCOMPLETE](hhn-navcomplete-message.md) message is also sent.

## Related topics

<dl> <dt>

[About Notification Messages](about-notification-messages.md)
</dt> </dl>

 

 




