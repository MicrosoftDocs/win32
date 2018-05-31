---
title: HHN\_NAVCOMPLETE message
description: Sent when the user successfully navigates to a topic in a compiled help (.chm) file.
ms.assetid: 9F86892E-343B-4fd9-AFE6-177611B4EB52
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HHN\_NAVCOMPLETE message

Sent when the user successfully navigates to a topic in a compiled help (.chm) file.



| Notification code | lParam                                                                 |
|-------------------|------------------------------------------------------------------------|
| HHN\_NAVCOMPLETE  | A pointer to an [**HHN\_NOTIFY**](/previous-versions/windows/desktop/api/HtmlHelp/ns-htmlhelp-taghhn_notify) structure. |



 

## Remarks

-   Make sure that the help window definition includes the settings for notification messages. Otherwise, HTML Help will not send notification messages.

## Related topics

<dl> <dt>

[About Notification Messages](about-notification-messages.md)
</dt> </dl>

 

 




