---
title: Custom Draw
description: Custom draw is not a common control; it is a service that many common controls provide.
ms.assetid: 'vs|controls|~\controls\custdraw\custdraw.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Custom Draw

Custom draw is not a common control; it is a service that many common controls provide. The custom draw service allows an application greater flexibility in customizing a control's appearance. Your application can harness custom draw notifications to easily change the font used to display items or manually draw an item without having to do a full owner draw.

This section contains information about the programming elements used with custom draw.

## Overviews



| Topic                                      | Contents                                                                                                                                                               |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Custom Draw](about-custom-draw.md) | This section contains general information about custom draw functionality and provides a conceptual overview of how an application can support custom draw.<br/> |
| [Using Custom Draw](using-custom-draw.md) | This section contains examples that demonstrate how to implement custom draw. <br/>                                                                              |



 

## Notifications



| Topic                               | Contents                                                                                                                                                                 |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NM\_CUSTOMDRAW](nm-customdraw.md) | Notifies a control's parent window about custom drawing operations. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |



 

## Structures



| Topic                                | Contents                                                                                              |
|--------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) | Contains information specific to an [NM\_CUSTOMDRAW](nm-customdraw.md) notification code.<br/> |



 

 

 





