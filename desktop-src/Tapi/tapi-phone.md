---
description: The tapi/phone device class consists of all phone devices. You access these devices by using the TAPI phone functions.
ms.assetid: c2e52fdf-e07a-4897-8af5-0a101d6c237a
title: tapi/phone
ms.topic: article
ms.date: 05/31/2018
---

# tapi/phone

The tapi/phone device class consists of all phone devices. You access these devices by using the TAPI phone functions.

The [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) function fills a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_BINARY value and appending this additional member:

``` syntax
DWORD dwDeviceI;  // phone device identifier
```

The **dwDeviceId** member is the identifier of the phone device associated with the phone handle given by [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid).

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) function also fills a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting **dwStringFormat** to STRINGFORMAT\_BINARY and appending this additional member:

``` syntax
DWORD adwDeviceIds[];  // array of phone device identifiers
```

The **adwDeviceIds** member is an array containing the device identifiers of all phone devices that are associated with the given line device. If there are no associated phone devices, [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) returns the LINEERR\_INVALDEVICECLASS value.

 

 



