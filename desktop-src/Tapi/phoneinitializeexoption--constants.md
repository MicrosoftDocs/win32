---
description: The PHONEINITIALIZEEXOPTION\_ constants specify which event notification mechanism to use when initializing a session.
ms.assetid: 7d8b122d-bebe-4904-abc8-d680b0899e25
title: PHONEINITIALIZEEXOPTION_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONEINITIALIZEEXOPTION\_ Constants

The **PHONEINITIALIZEEXOPTION\_** constants specify which event notification mechanism to use when initializing a session.

<dl> <dt>

<span id="PHONEINITIALIZEEXOPTION_USECOMPLETIONPORT"></span><span id="phoneinitializeexoption_usecompletionport"></span>**PHONEINITIALIZEEXOPTION\_USECOMPLETIONPORT**
</dt> <dd> <dl> <dt>



The application desires to use the Completion Port event notification mechanism.


</dt> </dl> </dd> <dt>

<span id="PHONEINITIALIZEEXOPTION_USEEVENT"></span><span id="phoneinitializeexoption_useevent"></span>**PHONEINITIALIZEEXOPTION\_USEEVENT**
</dt> <dd> <dl> <dt>



The application desires to use the Event Handle event notification mechanism.


</dt> </dl> </dd> <dt>

<span id="PHONEINITIALIZEEXOPTION_USEHIDDENWINDOW"></span><span id="phoneinitializeexoption_usehiddenwindow"></span>**PHONEINITIALIZEEXOPTION\_USEHIDDENWINDOW**
</dt> <dd> <dl> <dt>



The application desires to use the Hidden Window event notification mechanism.


</dt> </dl> </dd> </dl>

## Remarks

See [**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa) for further details on the operation of these options.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




