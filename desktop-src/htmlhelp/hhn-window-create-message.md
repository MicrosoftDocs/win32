---
title: HHN\_WINDOW\_CREATE message
description: Sent right before a help window is created.
ms.assetid: 074BA719-6CB4-4372-BB70-9B5BFF3CA130
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HHN\_WINDOW\_CREATE message

Sent right before a help window is created.



| Notification code   | lParam                                                                 |
|---------------------|------------------------------------------------------------------------|
| HHN\_WINDOW\_CREATE | A pointer to an [**HHN\_NOTIFY**](/windows/previous-versions/HtmlHelp/ns-htmlhelp-taghhn_notify?branch=master) structure. |



 

## Remarks

-   Make sure that the help window definition includes the settings for notification messages. Otherwise, HTML Help will not send notification messages.

## Related topics

<dl> <dt>

[About Notification Messages](about-notification-messages.md)
</dt> </dl>

 

 




