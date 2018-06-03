---
title: Still Image API
description: Applications use the Still Image API to gain access to Still Image features.
ms.assetid: d9b9d6b9-9cad-4688-bfdf-750fde50ab3e
keywords:
- architecture,Still Image API
- STI architecture,Still Image API
- Still Image (STI),API
- STI (Still Image),API
- still images,Still Image API
- Still Image API,about
- Still Image (STI),Event Monitor
- STI (Still Image),Event Monitor
- Still Image API,Event Monitor
- Still Image (STI),Control Panel
- STI (Still Image),Control Panel
- Still Image API,Control Panel
- still images,Still Image Event Monitor
- still images,Still Image Control Panel
- Still Image Event Monitor
- Still Image Control Panel
- GetSTILaunchInformation method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Still Image API

Applications use the Still Image API to gain access to Still Image features. An application does not need to communicate directly with the Event Monitor or the Control Panel. The Event Monitor launches an application that is associated with a device event. That is the only communication it has with an application.

The application gets the launch information it needs by calling the [GetSTILaunchInformation](istillimage-getstilaunchinformation.md) method. If this method provides the application with valid push event information, then the application was launched by a push event. If it does not, the application was launched in another way (for example, the user double-clicked the program's icon). In this way, applications can distinguish whether or not they were launched by a push event and respond accordingly.

 

 




