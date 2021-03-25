---
description: The LINEINITIALIZEEXOPTION\_ constants specify which event notification mechanism to use when initializing a session.
ms.assetid: 77674a45-7133-4518-af47-a9d58392b80b
title: LINEINITIALIZEEXOPTION_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEINITIALIZEEXOPTION\_ Constants

The **LINEINITIALIZEEXOPTION\_** constants specify which event notification mechanism to use when initializing a session.

<dl> <dt>

<span id="LINEINITIALIZEEXOPTION_CALLHUBTRACKING"></span><span id="lineinitializeexoption_callhubtracking"></span>**LINEINITIALIZEEXOPTION\_CALLHUBTRACKING**
</dt> <dd> <dl> <dt>



The application desires to use the call hub tracking event notification mechanism. This constant is exposed only to applications that negotiate a TAPI version of 3.0 or higher.


</dt> </dl> </dd> <dt>

<span id="LINEINITIALIZEEXOPTION_USECOMPLETIONPORT"></span><span id="lineinitializeexoption_usecompletionport"></span>**LINEINITIALIZEEXOPTION\_USECOMPLETIONPORT**
</dt> <dd> <dl> <dt>



The application desires to use the Completion Port event notification mechanism. This flag is exposed only to applications that negotiate a TAPI version of 2.0 or higher.


</dt> </dl> </dd> <dt>

<span id="LINEINITIALIZEEXOPTION_USEEVENT"></span><span id="lineinitializeexoption_useevent"></span>**LINEINITIALIZEEXOPTION\_USEEVENT**
</dt> <dd> <dl> <dt>



The application desires to use the Event Handle event notification mechanism. This flag is exposed only to applications that negotiate a TAPI version of 2.0 or higher.


</dt> </dl> </dd> <dt>

<span id="LINEINITIALIZEEXOPTION_USEHIDDENWINDOW"></span><span id="lineinitializeexoption_usehiddenwindow"></span>**LINEINITIALIZEEXOPTION\_USEHIDDENWINDOW**
</dt> <dd> <dl> <dt>



The application desires to use the Hidden Window event notification mechanism. This flag is exposed only to applications that negotiate a TAPI version of 2.0 or higher.


</dt> </dl> </dd> </dl>

## Remarks

See [**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa) for further details on the operation of these options.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




