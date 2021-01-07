---
description: The comm/datamodem/portname device class consists of the device names to which modems are attached.
ms.assetid: 174519f6-3e73-4f05-9718-9e38680a0fb7
title: comm/datamodem/portname
ms.topic: article
ms.date: 05/31/2018
---

# comm/datamodem/portname

The comm/datamodem/portname device class consists of the device names to which modems are attached. When this device name is specified in a call to the [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) function, the function fills the [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure with a null-terminated ANSI (not Unicode) string specifying the name of the port to which the specified modem is attached, such as "COM1\\0". This is intended primarily for identification purposes in the user interface, but could be used under some circumstances to open the device directly, bypassing the service provider (if the service provider does not already have the device open itself). If there is no port associated with the device, a null string ("\\0") is returned in the **VARSTRING** structure (with a string length of 1).

 

 



