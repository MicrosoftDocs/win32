---
description: TSPIMessage is an enumeration type that defines the set of additional LINEEVENT and PHONEEVENT functions appearing in TSPI that do not appear in TAPI.
ms.assetid: b3c4ce68-033f-42f1-8c37-66326d21bf32
title: TSPIMessage
ms.topic: article
ms.date: 05/31/2018
---

# TSPIMessage

**TSPIMessage** is an enumeration type that defines the set of additional [**LINEEVENT**](/windows/win32/api/tspi/nc-tspi-lineevent) and [**PHONEEVENT**](/windows/desktop/api/tspi/nc-tspi-phoneevent) functions appearing in TSPI that do not appear in TAPI.

## Parameters

<dl> <dt>

<span id="TSPI_MESSAGE_BASE"></span><span id="tspi_message_base"></span>TSPI\_MESSAGE\_BASE
</dt> <dd>

The lowest number in the range of TSPI-specific message values. This value has no meaning by itself, but serves as a base for defining the other values.

</dd> <dt>

<span id="LINE_NEWCALL"></span><span id="line_newcall"></span>LINE\_NEWCALL
</dt> <dd>

Specifies that a new, incoming call has arrived and introduces it to TAPI. This must be the first message sent to TAPI for a new incoming call. TAPI returns its opaque identifier for the call as part of its handling of this message.

</dd> <dt>

<span id="LINE_CALLDEVSPECIFIC"></span><span id="line_calldevspecific"></span>LINE\_CALLDEVSPECIFIC
</dt> <dd>

Specifies that a device-specific event has occurred on a call device.

</dd> <dt>

<span id="LINE_CALLDEVSPECIFICFEATURE"></span><span id="line_calldevspecificfeature"></span>LINE\_CALLDEVSPECIFICFEATURE
</dt> <dd>

Specifies that a device-specific feature event has occurred on a call device.

</dd> </dl>

 

 
