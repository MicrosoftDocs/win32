---
description: The TAPI PHONE\_BUTTON message is sent to notify the application that button press monitoring is enabled if it has detected a button press on the local phone.
ms.assetid: fe47eed7-89d1-488b-b945-9e1aedc1f63c
title: PHONE_BUTTON message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONE\_BUTTON message

The TAPI **PHONE\_BUTTON** message is sent to notify the application that button press monitoring is enabled if it has detected a button press on the local phone.


```C++
            
```



## Parameters

<dl> <dt>

*hPhone* 
</dt> <dd>

A handle to the phone device.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The application's callback instance provided when opening the phone device.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The button/lamp identifier of the button that was pressed. Note that button identifiers zero through 11 are always the KEYPAD buttons, with '0' being button identifier zero, '1' being button identifier 1 (and so on through button identifier 9), and with '\*' being button identifier 10, and '\#' being button identifier 11. Additional information about a button identifier is available with [**phoneGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps) and [**phoneGetButtonInfo**](/windows/desktop/api/Tapi/nf-tapi-phonegetbuttoninfo).

</dd> <dt>

*dwParam2* 
</dt> <dd>

The button mode of the button. This parameter uses one of the [**PHONEBUTTONMODE\_ constants**](phonebuttonmode--constants.md).

</dd> <dt>

*dwParam3* 
</dt> <dd>

Specifies whether this is a button-down event or a button-up event. This parameter uses one of the [**PHONEBUTTONSTATE\_ constants**](phonebuttonstate--constants.md).

</dd> </dl>

## Return value

No return value.

## Remarks

A **PHONE\_BUTTON** message is sent whenever a button changes state. An application is guaranteed that for each button down event, it is eventually sent a corresponding button up event. A service provider that is incapable of detecting the actual button up is required to generate the button up message shortly after the button down message for each button press.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**phoneGetButtonInfo**](/windows/desktop/api/Tapi/nf-tapi-phonegetbuttoninfo)
</dt> <dt>

[**phoneGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps)
</dt> </dl>

 

 




