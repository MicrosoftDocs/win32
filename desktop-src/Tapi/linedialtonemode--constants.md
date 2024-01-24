---
description: The LINEDIALTONEMODE\_ bit-flag constants describe different types of dial tones. A special dial tone typically carries a special meaning (as with message waiting).
ms.assetid: 0b040482-35cf-42e8-84bc-33002635b591
title: LINEDIALTONEMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEDIALTONEMODE\_ Constants

The **LINEDIALTONEMODE\_** bit-flag constants describe different types of dial tones. A special dial tone typically carries a special meaning (as with message waiting).

<dl> <dt>

<span id="LINEDIALTONEMODE_EXTERNAL"></span><span id="linedialtonemode_external"></span>**LINEDIALTONEMODE\_EXTERNAL**
</dt> <dd> <dl> <dt>



This is an external (public network) dial tone.


</dt> </dl> </dd> <dt>

<span id="LINEDIALTONEMODE_INTERNAL"></span><span id="linedialtonemode_internal"></span>**LINEDIALTONEMODE\_INTERNAL**
</dt> <dd> <dl> <dt>



This is an internal dial tone, as within a PBX.


</dt> </dl> </dd> <dt>

<span id="LINEDIALTONEMODE_NORMAL"></span><span id="linedialtonemode_normal"></span>**LINEDIALTONEMODE\_NORMAL**
</dt> <dd> <dl> <dt>



This is a normal dial tone, which typically is a continuous tone.


</dt> </dl> </dd> <dt>

<span id="LINEDIALTONEMODE_SPECIAL"></span><span id="linedialtonemode_special"></span>**LINEDIALTONEMODE\_SPECIAL**
</dt> <dd> <dl> <dt>



This is a special dial tone indicating that a certain condition (known by the switch or network) is currently in effect. Special dial tones typically use an interrupted tone. As with a normal dial tone, this indicates that the switch is ready to receive the number to be dialed.


</dt> </dl> </dd> <dt>

<span id="LINEDIALTONEMODE_UNAVAIL"></span><span id="linedialtonemode_unavail"></span>**LINEDIALTONEMODE\_UNAVAIL**
</dt> <dd> <dl> <dt>



The dial tone mode is unavailable and will not become known.


</dt> </dl> </dd> <dt>

<span id="LINEDIALTONEMODE_UNKNOWN"></span><span id="linedialtonemode_unknown"></span>**LINEDIALTONEMODE\_UNKNOWN**
</dt> <dd> <dl> <dt>



The dial tone mode is not currently known but may become known later.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 16 bits can be assigned for device-specific extensions. The low-order 16 bits are reserved.

The **LINEDIALTONEMODE\_constants** are used within the [**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus) data structure for a call in the dialtone state.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




