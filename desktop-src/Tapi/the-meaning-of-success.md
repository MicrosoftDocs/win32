---
description: When an opertion returns SUCCESS, the function has successfully progressed to a point that is defined by the API on a function by function basis.
ms.assetid: e4077d77-dee1-4f1a-a6ee-20ca2f92a1ec
title: The Meaning of SUCCESS
ms.topic: article
ms.date: 05/31/2018
---

# The Meaning of SUCCESS

## TAPI 2.x

When an operation returns a SUCCESS indication (either synchronously upon function return for synchronous operations, or asynchronously through a [**LINE\_REPLY**](./line-reply.md) or [**PHONE\_REPLY**](./phone-reply.md) message for asynchronous operations), the following is assumed to be true:

-   The function has successfully progressed to a point that is defined by the API on a function-by-function basis. After that point has been reached, either the operation is completely finished, or it will be in a state such that independent state messages will inform the application about subsequent progress.

    For example, a service provider's implementation of [**lineMakeCall**](/windows/win32/api/tapi/nf-tapi-linemakecall) should return SUCCESS no later than when the call enters the proceeding call state. Ideally, the provider should indicate SUCCESS as soon as possible, such as when the call enters the dial tone call state (if applicable). Once SUCCESS has been returned to the application, LINE\_CALLSTATE messages will inform the application about the progress of the call. Service providers that delay returning the **lineMakeCall** SUCCESS indication, for example, until after dialing is complete, must be aware that this places that provider at a disadvantage because the usability at the application level may be severely limited. For example, it would not be possible for a user to cancel the call setup request in progress until after dialing is complete and all digits had been sent to the switch.

-   Functions that return information (such as [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo)) return SUCCESS only when the requested information is available to the application. Functions that return handles (to lines or calls), can return SUCCESS only after the handle is valid. No messages should be sent about that line or call prior to the SUCCESS indication of the function that caused its creation. The service provider is responsible for suppressing such messages.
-   Functions that enable certain permanent conditions (such as [**lineMonitorDigits**](/windows/win32/api/tapi/nf-tapi-linemonitordigits)) return SUCCESS only after the condition is enabled, not when the condition is removed again (for example, not when all digit monitoring has completed).
-   Call-control functions (such as [**lineHold**](/windows/win32/api/tapi/nf-tapi-linehold) or [**lineSetupTransfer**](/windows/win32/api/tapi/nf-tapi-linesetuptransfer), but not [**lineMakeCall**](/windows/win32/api/tapi/nf-tapi-linemakecall)) return SUCCESS when the operation is completed. Some telephone networks do not provide acknowledgment (positive or negative) about the completion of certain requests made by service providers. In such situations, the service provider must decide upon success or failure of the request. Therefore, SUCCESS may indicate that the service provider has initiated actions to fulfill the request, but not necessarily anything more. For example, the provider may receive no affirmative acknowledgment to its request from the switch, although it has already sent a success message to the application.

## TAPI 3.x

When an operation returns a SUCCESS indication (either synchronously upon function return for synchronous operations, or asynchronously with a call to the [**ASYNC\_COMPLETION**](/windows/win32/api/tspi/nc-tspi-async_completion) callback procedure for asynchronous operations), then the following are assumed to be true:

-   The function has successfully progressed up to a service-provider-defined point. The service provider defines the point on a function-by-function basis. After reaching that point, either the operation is completely finished, or it is in a state such that subsequent independent state messages will inform the application about progress.
-   Functions that return information (such as [**TSPI\_linePark**](/windows/win32/api/tspi/nf-tspi-tspi_linepark) or [**TSPI\_lineDevSpecific**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecific)) return SUCCESS only when the requested information is available to the caller. Functions that return handles (to opened lines, opened phones, or calls) return the handles immediately on function return. Both the service provider and the caller must treat the handles as "not yet valid" until the eventual SUCCESS indication. The service provider is responsible for preventing any callback messages to the [**LINEEVENT**](/windows/win32/api/tspi/nc-tspi-lineevent) or [**PHONEEVENT**](/windows/desktop/api/tspi/nc-tspi-phoneevent) procedure about that opened line, opened phone, or call until after the SUCCESS indication. If the eventual result is an error, any handle returned immediately becomes invalid without any further action.
-   Functions that enable certain permanent conditions (like [**TSPI\_lineMonitorDigits**](/windows/win32/api/tspi/nf-tspi-tspi_linemonitordigits)) return SUCCESS only after the condition is enabled, not when the condition is removed again (for example, not when digit monitoring is complete).
-   Call control functions (such as [**TSPI\_lineHold**](/windows/win32/api/tspi/nf-tspi-tspi_linehold) and [**TSPI\_lineSetupTransfer**](/windows/win32/api/tspi/nf-tspi-tspi_linesetuptransfer), but not [**TSPI\_lineMakeCall**](/windows/win32/api/tspi/nf-tspi-tspi_linemakecall)) return SUCCESS when the operation is completed. In telephony environments that do not provide positive acknowledgment of these functions, the service provider is forced to make a best-effort decision as to the success or failure of the function.
-   A service provider's implementation of [**TSPI\_lineMakeCall**](/windows/win32/api/tspi/nf-tspi-tspi_linemakecall) must return SUCCESS no later than when the call enters the *proceeding* call state. Ideally, the provider indicates SUCCESS as soon as possible, such as when the call enters the *dialtone* call state (if applicable). When SUCCESS is returned to the application, [**LINE\_CALLSTATE**](/previous-versions/windows/desktop/legacy/ms725219(v=vs.85)) messages inform the caller about the progress of the call. Service providers that delay returning the **TSPI\_lineMakeCall** SUCCESS indication, for example, until after dialing is complete, severely limit flexibility at the application level. Delay in returning SUCCESS in **TSPI\_lineMakeCall** prevents a user from canceling the call setup request in progress until after dialing is complete, and all digits are sent to the switch.

 

 
