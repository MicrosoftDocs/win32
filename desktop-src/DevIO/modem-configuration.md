---
description: Modem configuration functions enable you to configure a modem before making a connection.
ms.assetid: 67d8f3c4-0295-4028-8b12-1a5e26979df5
title: Modem Configuration
ms.topic: article
ms.date: 05/31/2018
---

# Modem Configuration

Modem configuration functions enable you to configure a modem before making a connection. An application can set modem options and determine the features of a modem without using commands specific to any modem device. Following are the general features an application may set before making a call:

-   Primary mode of operation (synchronous, asynchronous, and whether error control is enabled).
-   V.42 error control (defined by CCITT recommendation V.42), including specific parameters. CCITT stands for the International Telegraph and Telephone Consultative Committee.
-   V.42bis (defined by CCITT recommendation V.42bis) and MNP5 data compression.
-   Time-out options, including call setup, inactivity, and buffered data delivery.

Before setting a modem's configuration, an application should determine the capabilities of the modem device by using the [**GetCommProperties**](/windows/desktop/api/Winbase/nf-winbase-getcommproperties) function. This function fills in a [**COMMPROP**](/windows/desktop/api/WinBase/ns-winbase-commprop) structure. This structure contains both a general portion, which applies to all communications devices, and a portion that is specific to each provider subtype. For modem devices, the provider-specific portion of the **COMMPROP** structure is a [**MODEMDEVCAPS**](/windows/desktop/api/Mcx/ns-mcx-modemdevcaps) structure.

An application can get and set the current configuration of a modem by using the [**GetCommConfig**](/windows/desktop/api/Winbase/nf-winbase-getcommconfig) and [**SetCommConfig**](/windows/desktop/api/Winbase/nf-winbase-setcommconfig) functions, both of which use a [**COMMCONFIG**](/windows/desktop/api/Winbase/ns-winbase-commconfig) structure. This structure contains both a general portion, which applies to all communications devices, and a portion that is specific to each provider subtype. For modem devices, the provider-specific portion of the **COMMCONFIG** structure is a [**MODEMSETTINGS**](/windows/desktop/api/Mcx/ns-mcx-modemsettings) structure.

After configuring a modem, an application can use the Telephony Application Programming Interface (TAPI) to actually establish a connection.

The modem configuration functions do not provide for long-term management and maintenance of a modem. Modem service providers should supply modem configuration dialog boxes for this purpose.

 

 



