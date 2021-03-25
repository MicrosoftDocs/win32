---
description: The TAPI LINE\_MONITORDIGITS message is sent when a digit is detected. The sending of this message is controlled with the lineMonitorDigits function.
ms.assetid: 1c1a729c-a6bb-4432-9617-4a892c76cb8d
title: LINE_MONITORDIGITS message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_MONITORDIGITS message

The TAPI **LINE\_MONITORDIGITS** message is sent when a digit is detected. The sending of this message is controlled with the [**lineMonitorDigits**](/windows/desktop/api/Tapi/nf-tapi-linemonitordigits) function.


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

The low-order byte contains the last digit received in a text representation.

</dd> <dt>

*dwParam2* 
</dt> <dd>

The digit mode that was detected. This parameter must be one and only one of the [**LINEDIGITMODE\_ constants**](linedigitmode--constants.md).

</dd> <dt>

*dwParam3* 
</dt> <dd>

The "tick count" (number of milliseconds since Windows started) at which the specified digit was detected. For TAPI versions earlier than 2.0, this parameter is unused.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_MONITORDIGITS** message is sent to the application that has enabled digit monitoring.

Because this timestamp may have been generated on a computer other than the one on which the application is executing, it is useful only for comparison to other similarly timestamped messages generated on the same line device ( [**LINE\_GATHERDIGITS**](line-gatherdigits.md), [**LINE\_GENERATE**](line-generate.md), [**LINE\_MONITORMEDIA**](line-monitormedia.md), [**LINE\_MONITORTONE**](line-monitortone.md)), in order to determine their relative timing (separation between events). The tick count can "wrap around" after approximately 49.7 days; applications must take this into account when performing calculations.

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

[**LINE\_MONITORMEDIA**](line-monitormedia.md)
</dt> <dt>

[**LINE\_MONITORTONE**](line-monitortone.md)
</dt> <dt>

[**lineMonitorDigits**](/windows/desktop/api/Tapi/nf-tapi-linemonitordigits)
</dt> </dl>

 

 




