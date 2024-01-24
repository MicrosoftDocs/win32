---
description: The LINEGENERATETERM\_ bit-flag constants describe the conditions under which digit or tone generation is terminated.
ms.assetid: 5cdc43c0-2349-4ffc-9bf7-3b498b35db95
title: LINEGENERATETERM_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEGENERATETERM\_ Constants

The **LINEGENERATETERM\_** bit-flag constants describe the conditions under which digit or tone generation is terminated.

<dl> <dt>

<span id="LINEGENERATETERM_CANCEL"></span><span id="linegenerateterm_cancel"></span>**LINEGENERATETERM\_CANCEL**
</dt> <dd> <dl> <dt>



The digit or tone generation request was canceled by this application, by another application, or because the call terminated. This value can also be returned when digit or tone generation cannot be completed due to internal failure of the service provider.


</dt> </dl> </dd> <dt>

<span id="LINEGENERATETERM_DONE"></span><span id="linegenerateterm_done"></span>**LINEGENERATETERM\_DONE**
</dt> <dd> <dl> <dt>



The requested number of digits or requested tones have been generated for the requested duration.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




