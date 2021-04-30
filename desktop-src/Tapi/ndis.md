---
description: The ndis device class consists of devices that can be associated with network driver interface specification (NDIS) media access control (MAC) drivers to support network communications. You access these devices by using functions.
ms.assetid: 98cdd929-0bd7-4509-b2f5-4edd8d6a8080
title: ndis
ms.topic: article
ms.date: 05/31/2018
---

# ndis

The ndis device class consists of devices that can be associated with network driver interface specification (NDIS) media access control (MAC) drivers to support network communications. You access these devices by using functions.

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) and [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) functions fill a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_BINARY value and appending these additional members:

``` syntax
HANDLE  hDevice;          // NDIS connection identifier
CHAR    szDeviceType[1];  // name of device 
```

The **hDevice** member is the identifier to pass to a MAC, such as the asynchronous MAC for dial-up networking, to associate a network connection with the call/modem connection. The **szDeviceType** member is a null-terminated string specifying the name of the device associated with the identifier.

 

 



