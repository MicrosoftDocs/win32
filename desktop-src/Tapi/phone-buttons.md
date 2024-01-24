---
description: TAPI models a phones buttons and lamps as button-lamp pairs.
ms.assetid: e4c50bd6-a256-407f-af3b-b24383a30ea0
title: Phone Buttons
ms.topic: article
ms.date: 05/31/2018
---

# Phone Buttons

TAPI models a phone's buttons and lamps as button-lamp pairs. A button with no lamp next to it or a lamp with no button is specified using a "dummy" indicator for the missing lamp or button. A button with multiple lamps is modeled by using multiple button-lamp pairs.

Information associated with a phone button can be set and retrieved. When a button is pressed, a [**PHONE\_BUTTON**](phone-button.md) message is sent to the application function. The parameters of this message are a handle to the phone device and the button-lamp identifier of the button that was pressed. The keypad buttons '0' through '9', '\*', and '\#' are assigned the fixed button-lamp identifiers 0 through 11.

The functions associated with buttons are [**phoneSetButtonInfo**](/windows/desktop/api/Tapi/nf-tapi-phonesetbuttoninfo), which sets the information associated with a button on a phone device, and [**phoneGetButtonInfo**](/windows/desktop/api/Tapi/nf-tapi-phonegetbuttoninfo), which returns information associated with a button on a phone device. The PHONE\_BUTTON message is sent to an application when a button on the phone is pressed.

The information associated with a button does not carry any semantic meaning as far as TAPI is concerned. It is useful for device-specific applications that understand the meaning of this information for a given phone device, or for display to the user, such as online help.

 

 



