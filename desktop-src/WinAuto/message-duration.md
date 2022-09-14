---
title: Message duration parameter
description: Applications typically use pop-up windows to briefly display important notification messages to the user. An application creates the window, displays it for an application-defined duration, and then destroys the window.
ms.assetid: a3f7a8d8-78e7-4fb0-8ee2-bd9341857153
ms.topic: article
ms.date: 05/31/2018
---

# Message duration parameter

Applications typically use pop-up windows to briefly display important notification messages to the user. An application creates the window, displays it for an application-defined duration, and then destroys the window.

Because users with visual impairments or cognitive conditions might need more time to read notification pop-ups, applications should not hard code the duration. Instead, an application should set the duration based on the value of the **SPI\_GETMESSAGEDURATION** system parameter. To retrieve this parameter, use the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function.

Assistive technology applications can set the message duration, based on user input, by setting the **SPI\_SETMESSAGEDURATION** system parameter.

 

 