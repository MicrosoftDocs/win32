---
description: The phoneDevSpecific function and its associated PHONE\_DEVSPECIFIC message enable an application to access device-specific phone features that are unavailable through the common telephony services for phones.
ms.assetid: b4c8d721-26e4-4895-9f09-0f67fe4d346b
title: Functions and Messages
ms.topic: article
ms.date: 05/31/2018
---

# Functions and Messages

The [**phoneDevSpecific**](/windows/desktop/api/Tapi/nf-tapi-phonedevspecific) function and its associated [**PHONE\_DEVSPECIFIC**](phone-devspecific.md) message enable an application to access device-specific phone features that are unavailable through the common telephony services for phones. In other words, **phoneDevSpecific** is the device-specific escape function that allows vendor-dependent extensions, and PHONE\_DEVSPECIFIC is the device-specific message that is sent to the application.

The parameter profile of the [**phoneDevSpecific**](/windows/desktop/api/Tapi/nf-tapi-phonedevspecific) function is generic in that little interpretation of the parameters is made by TAPI. Rather, the interpretation of the parameters is defined by the service provider and must be understood by an application that uses them. The parameters are simply passed through by TAPI from the application to the service provider. An application that relies on device-specific extensions will usually not work with other service providers, but applications written to the common telephony phone services will work with the extended service provider.

 

 



