---
description: The LINEPARKMODE\_ bit-flag constants describe different ways of parking calls.
ms.assetid: 4b182c16-9d58-4244-bc5a-05c393800948
title: LINEPARKMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEPARKMODE\_ Constants

The **LINEPARKMODE\_** bit-flag constants describe different ways of parking calls.

<dl> <dt>

<span id="LINEPARKMODE_DIRECTED"></span><span id="lineparkmode_directed"></span>**LINEPARKMODE\_DIRECTED**
</dt> <dd> <dl> <dt>



Specifies directed call park. The address where the call is to be parked must be supplied to the switch.


</dt> </dl> </dd> <dt>

<span id="LINEPARKMODE_NONDIRECTED"></span><span id="lineparkmode_nondirected"></span>**LINEPARKMODE\_NONDIRECTED**
</dt> <dd> <dl> <dt>



Specifies nondirected call park. The address where the call is parked is selected by the switch and provided by the switch to the application.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

The **LINEPARKMODE\_ constants** are used when parking a call. Consult a line's address device capabilities to find out which park mode is available.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




