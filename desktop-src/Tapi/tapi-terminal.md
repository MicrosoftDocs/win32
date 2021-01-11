---
description: The tapi/terminal device class consists of the phone devices associated with each terminal on a line or the terminal on each line associated with a phone device. You access these devices by using the TAPI line device or phone device functions.
ms.assetid: 466ed2cd-f737-4df4-8633-4fb5c95b4b6c
title: tapi/terminal
ms.topic: article
ms.date: 05/31/2018
---

# tapi/terminal

The tapi/terminal device class consists of the phone devices associated with each terminal on a line or the terminal on each line associated with a phone device. You access these devices by using the TAPI [line device](line-device-functions.md) or [phone device functions](phone-device-functions.md).

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) function fills a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_BINARY value and appending this additional member:

``` syntax
DWORD adwDeviceId[];  // array of phone device identifiers
```

The **adwDeviceId** member is an array of phone device identifiers. There is one array element for each terminal specified by the **dwNumTerminals** member in the [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps) structure for the given line device. Each element specifies the identifier of the phone device associated with the corresponding terminal on the line. If there is no phone device associated with a terminal, the element is set to –1 (0xFFFFFFFF).

The [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) function fills a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_BINARY value and appending this additional member:

``` syntax
DWORD adwTerminalID[];  // array of terminal identifiers
```

The **adwTerminalID** member is an array of terminal identifiers. There is one array element for each line device identifier specified by the [**lineInitialize**](/windows/desktop/api/Tapi/nf-tapi-lineinitialize) or [**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa) function. Each array element contains the terminal identifier associated with the phone device for the given line device. If there is no phone device, the element is set to –1 (0xFFFFFFFF). The terminal identifiers range in value from zero to one less than the number specified by the **dwNumTerminals** member in the [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps) structure.

 

 



