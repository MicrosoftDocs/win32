---
title: Control Point Security Considerations
description: When you are creating a control point, you need to take into consideration the following security issues.
ms.assetid: 3281b4c3-d730-4273-9031-840a6ac655ce
ms.topic: article
ms.date: 05/31/2018
---

# Control Point Security Considerations

When you are creating a control point, you need to take into consideration the following security issues.

-   All control point searches are by default sent with a TTL of 1. This means that only devices within the same subnet are discovered. You can configure a higher TTL in the registry.
-   A device's device and service description is only downloaded if it is present on the same device which sent the device announcement.
-   A device is only sent control and subscription requests if its control and subscription URLs are on the same device that sent the device announcements.

 

 




