---
description: The TSPI LINE\_CALLDEVSPECIFIC message is sent to the LINEEVENT callback function to notify TAPI about device-specific events occurring on a call.
ms.assetid: accd753a-3be0-4c7d-bbc7-d294d1381144
title: LINE_CALLDEVSPECIFIC message (Tspi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_CALLDEVSPECIFIC message

The TSPI **LINE\_CALLDEVSPECIFIC** message is sent to the [**LINEEVENT**](/windows/win32/api/tspi/nc-tspi-lineevent) callback function to notify TAPI about device-specific events occurring on a call. The meaning of the message and the interpretation of the *dwParam1* through *dwParam3* parameters is device specific.


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

The value LINE\_CALLDEVSPECIFIC.

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

The **LINE\_CALLDEVSPECIFIC** message is used by a service provider in conjunction with the [**TSPI\_lineDevSpecific**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecific) function. Its meaning is device specific.

TAPI sends the [**LINE\_DEVSPECIFIC**](/previous-versions/windows/desktop/legacy/ms725225(v=vs.85)) message to applications in response to receiving this message from a service provider. The *htLine* and *htCall* parameters are translated to the appropriate *hCall* as the *hDevice* parameter at the TAPI level. The *dwParam1*, *dwParam2*, and *dwParam3* parameters are passed through unmodified.

There is no directly corresponding message at the TAPI level, although this message is very similar to [**LINE\_DEVSPECIFIC**](/previous-versions/windows/desktop/legacy/ms725225(v=vs.85)). At the TSPI level, the device-specific messages are split between those reporting events on lines and addresses, and those reporting events on calls.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_DEVSPECIFIC**](/previous-versions/windows/desktop/legacy/ms725225(v=vs.85))
</dt> <dt>

[**LINEEVENT**](/windows/win32/api/tspi/nc-tspi-lineevent)
</dt> <dt>

[**TSPI\_lineDevSpecific**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecific)
</dt> </dl>

 

