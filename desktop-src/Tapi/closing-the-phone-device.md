---
description: The phoneClose function closes the specified phone device.
ms.assetid: 7607d779-0715-48a3-a4f2-bcf07026d7c5
title: Closing the Phone Device
ms.topic: article
ms.date: 05/31/2018
---

# Closing the Phone Device

The [**phoneClose**](/windows/desktop/api/Tapi/nf-tapi-phoneclose) function closes the specified phone device. The phone device can also be forcibly closed after the user has modified the configuration of that phone or its driver. If the user wants the configuration changes to be effective immediately (as opposed to after the next system restart), and they affect the application's current view of the device (such as a change in device capabilities), then a service provider can forcibly close the phone device.

These messages can also be sent unsolicited as a result of the phone device being reclaimed in some other manner. An application should therefore be prepared to handle unsolicited [**PHONE\_CLOSE**](phone-close.md) messages. At the time the phone device is closed, any outstanding asynchronous replies pertaining to that device are suppressed.

 

 



