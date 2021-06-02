---
description: The LINECALLTREATMENT\_ constants list treatments for calls that are unanswered or on hold. Except for basic parameter validation, call treatment is a straight pass-through by TAPI to the service provider.
ms.assetid: c28c9200-dd51-48b2-905c-fbe37c83b00f
title: LINECALLTREATMENT_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLTREATMENT\_ Constants

The **LINECALLTREATMENT\_** constants list treatments for calls that are unanswered or on hold. Except for basic parameter validation, call treatment is a straight pass-through by TAPI to the service provider.

<dl> <dt>

<span id="LINECALLTREATMENT_BUSY"></span><span id="linecalltreatment_busy"></span>**LINECALLTREATMENT\_BUSY**
</dt> <dd> <dl> <dt>



When the call is not actively connected to a device (offering or onhold), the party hears busy signal.


</dt> </dl> </dd> <dt>

<span id="LINECALLTREATMENT_MUSIC"></span><span id="linecalltreatment_music"></span>**LINECALLTREATMENT\_MUSIC**
</dt> <dd> <dl> <dt>



When the call is not actively connected to a device (offering or onhold), the party hears music.


</dt> </dl> </dd> <dt>

<span id="LINECALLTREATMENT_RINGBACK"></span><span id="linecalltreatment_ringback"></span>**LINECALLTREATMENT\_RINGBACK**
</dt> <dd> <dl> <dt>



When the call is not actively connected to a device (offering or onhold), the party hears ringback tone.


</dt> </dl> </dd> <dt>

<span id="LINECALLTREATMENT_SILENCE"></span><span id="linecalltreatment_silence"></span>**LINECALLTREATMENT\_SILENCE**
</dt> <dd> <dl> <dt>



When the call is not actively connected to a device (offering or onhold), the party hears silence.


</dt> </dl> </dd> </dl>

## Remarks

The value 0x00000000 is reserved to indicate that the service provider does not support call treatments. Values in the range 0x00000005 through 0x000000FF are reserved for future definition. Values in the range 0x00000100 through 0xFFFFFFFF are reserved for assignment by service providers, and may include identification of specific musical selections or recorded announcements.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




