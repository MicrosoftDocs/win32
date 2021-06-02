---
description: The tapi/line device class consists of all line devices. You access these devices using the TAPI line functions.
ms.assetid: 2215b10b-e410-462c-8cf9-42f3e688e82e
title: tapi/line
ms.topic: article
ms.date: 05/31/2018
---

# tapi/line

The tapi/line device class consists of all line devices. You access these devices using the TAPI line functions.

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) function fills a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_BINARY value and appending this additional member.

``` syntax
DWORD dwDeviceI;  // line device identifier
```

The **dwDeviceId** member is the identifier of the line device associated with the line handle given by [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid).

The [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) function also fills a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting **dwStringFormat** to STRINGFORMAT\_BINARY and appending this additional member:

``` syntax
DWORD adwDeviceIds[];  // array of line device identifiers
```

The **adwDeviceIds** member is an array containing the device identifiers of all line devices that are associated with the phone device. If there are no associated line devices, [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) returns the PHONEERR\_INVALDEVICECLASS value.

 

 



