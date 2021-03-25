---
description: The TAPI LINE\_MONITORTONE message is sent when a tone is detected. The sending of this message is controlled with the lineMonitorTones function.
ms.assetid: ffdca615-5341-4f02-bb38-b8133cd9477d
title: LINE_MONITORTONE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_MONITORTONE message

The TAPI **LINE\_MONITORTONE** message is sent when a tone is detected. The sending of this message is controlled with the [**lineMonitorTones**](/windows/desktop/api/Tapi/nf-tapi-linemonitortones) function.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the call.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the call's line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The application-specific **dwAppSpecific** member of the [**LINEMONITORTONE**](/windows/desktop/api/Tapi/ns-tapi-linemonitortone) structure for the tone that was detected.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Unused.

</dd> <dt>

*dwParam3* 
</dt> <dd>

The "tick count" (number of milliseconds since Windows started) at which the tone was detected. For API versions earlier than 2.0, this parameter is unused.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_MONITORTONE** message is only sent to the application that has requested the tone be monitored.

Because this timestamp may have been generated on a computer other than the one on which the application is executing, it is useful only for comparison to other similarly timestamped messages generated on the same line device ( [**LINE\_GATHERDIGITS**](line-gatherdigits.md), [**LINE\_GENERATE**](line-generate.md), [**LINE\_MONITORDIGITS**](line-monitordigits.md), **LINE\_MONITORTONE**), in order to determine their relative timing (separation between events). The tick count can "wrap around" after approximately 49.7 days; applications must take this into account when performing calculations.

If the service provider does not generate the timestamp (for example, if it was created using an earlier version of TAPI), then TAPI provides a timestamp at the point closest to the service provider generating the event so that the synthesized timestamp is as accurate as possible.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_GATHERDIGITS**](line-gatherdigits.md)
</dt> <dt>

[**LINE\_GENERATE**](line-generate.md)
</dt> <dt>

[**LINE\_MONITORDIGITS**](line-monitordigits.md)
</dt> <dt>

[**LINEMONITORTONE**](/windows/desktop/api/Tapi/ns-tapi-linemonitortone)
</dt> <dt>

[**lineMonitorTones**](/windows/desktop/api/Tapi/nf-tapi-linemonitortones)
</dt> </dl>

 

 




