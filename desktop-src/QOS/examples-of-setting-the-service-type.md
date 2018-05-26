---
title: Examples of Setting the Service Type
description: The first example is a sending application that requires GUARANTEED service type, but does not want kernel traffic control.
ms.assetid: 54468a1c-61b6-4773-a335-914ea641f22d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Examples of Setting the Service Type

The first example is a sending application that requires GUARANTEED service type, but does not want kernel traffic control. In this case, the application should set the ServiceType in its SendingFlowspec to the following:

SERVICETYPE\_GUARANTEED \| SERVICE\_NO\_TRAFFIC\_CONTROL

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

 

 




