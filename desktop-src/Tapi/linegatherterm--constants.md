---
description: The LINEGATHERTERM\_ bit-flag constants describe the conditions under which buffered digit gathering is terminated.
ms.assetid: 409e1984-e5a4-4636-ab53-5973fe7b78ea
title: LINEGATHERTERM_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEGATHERTERM\_ Constants

The **LINEGATHERTERM\_** bit-flag constants describe the conditions under which buffered digit gathering is terminated.

<dl> <dt>

<span id="LINEGATHERTERM_BUFFERFULL"></span><span id="linegatherterm_bufferfull"></span>**LINEGATHERTERM\_BUFFERFULL**
</dt> <dd> <dl> <dt>



The requested number of digits has been gathered. The buffer is full.


</dt> </dl> </dd> <dt>

<span id="LINEGATHERTERM_CANCEL"></span><span id="linegatherterm_cancel"></span>**LINEGATHERTERM\_CANCEL**
</dt> <dd> <dl> <dt>



The request was canceled by this application, by another application, or because the call terminated.


</dt> </dl> </dd> <dt>

<span id="LINEGATHERTERM_FIRSTTIMEOUT"></span><span id="linegatherterm_firsttimeout"></span>**LINEGATHERTERM\_FIRSTTIMEOUT**
</dt> <dd> <dl> <dt>



The first digit timeout expired. The buffer contains no digits.


</dt> </dl> </dd> <dt>

<span id="LINEGATHERTERM_INTERTIMEOUT"></span><span id="linegatherterm_intertimeout"></span>**LINEGATHERTERM\_INTERTIMEOUT**
</dt> <dd> <dl> <dt>



The inter-digit timeout expired. The buffer contains at least one digit.


</dt> </dl> </dd> <dt>

<span id="LINEGATHERTERM_TERMDIGIT"></span><span id="linegatherterm_termdigit"></span>**LINEGATHERTERM\_TERMDIGIT**
</dt> <dd> <dl> <dt>



One of the termination digits matched a received digit. The matched termination digit is the last digit in the buffer.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




