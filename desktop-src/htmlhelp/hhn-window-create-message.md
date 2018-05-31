---
title: HHN\_WINDOW\_CREATE message
description: Sent right before a help window is created.
ms.assetid: 074BA719-6CB4-4372-BB70-9B5BFF3CA130
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HHN\_WINDOW\_CREATE message

Sent right before a help window is created.



| Notification code   | lParam                                                                 |
|---------------------|------------------------------------------------------------------------|
| HHN\_WINDOW\_CREATE | A pointer to an [**HHN\_NOTIFY**](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghhn_notify) structure. |



 

## Remarks

-   Make sure that the help window definition includes the settings for notification messages. Otherwise, HTML Help will not send notification messages.

## Related topics

<dl> <dt>

[About Notification Messages](about-notification-messages.md)
</dt> </dl>

 

 




