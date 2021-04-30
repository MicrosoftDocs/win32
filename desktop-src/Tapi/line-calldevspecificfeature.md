---
description: The TSPI LINE\_CALLDEVSPECIFICFEATURE message is sent to the LINEEVENT callback function to notify TAPI about device-specific events occurring on a line or address.
ms.assetid: bf470f5b-f7e5-4f98-9b60-12da599ebf26
title: LINE_CALLDEVSPECIFICFEATURE message (Tspi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_CALLDEVSPECIFICFEATURE message

The TSPI **LINE\_CALLDEVSPECIFICFEATURE** message is sent to the [**LINEEVENT**](/windows/win32/api/tspi/nc-tspi-lineevent) callback function to notify TAPI about device-specific events occurring on a line or address. The meaning of the message and the interpretation of the *dwParam1* through *dwParam3* parameters is device specific.


```C++
            
```



## Parameters

<dl> <dt>

*htLine* 
</dt> <dd>

The TAPI opaque object handle to the line device.

</dd> <dt>

*htCall* 
</dt> <dd>

The TAPI opaque object handle to the call device.

</dd> <dt>

*dwMsg* 
</dt> <dd>

The value LINE\_CALLDEVSPECIFICFEATURE.

</dd> <dt>

*dwParam1* 
</dt> <dd>

Device specific.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Device specific.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Device specific.

</dd> </dl>

## Remarks

The **LINE\_CALLDEVSPECIFICFEATURE** message is used by a service provider in conjunction with the [**TSPI\_lineDevSpecificFeature**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecificfeature) function. Its meaning is device specific.

TAPI sends the [**LINE\_DEVSPECIFICFEATURE**](/previous-versions/windows/desktop/legacy/ms725227(v=vs.85)) message to applications in response to receiving this message from a service provider. The *htLine* and *htCall* parameters are translated to the appropriate *hCall* as the *hDevice* parameter at the TAPI level. The *dwParam1*, *dwParam2*, and *dwParam3* parameters are passed through unmodified.

There is no directly corresponding message at the TAPI level, although this message is very similar to LINE\_DEVSPECIFICFEATURE. At the TSPI level, the device-specific feature messages are split between those reporting events on lines and addresses, and those reporting events on calls.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_DEVSPECIFICFEATURE**](/previous-versions/windows/desktop/legacy/ms725227(v=vs.85))
</dt> <dt>

[**TSPI\_lineDevSpecificFeature**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecificfeature)
</dt> </dl>

 

