---
description: The TAPIERR\_ constants provide information concerning function execution failures.
ms.assetid: 6d1cf18b-efeb-4703-9b8e-fce59b61b63f
title: TAPIERR_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# TAPIERR\_ Constants

The **TAPIERR\_ constants** provide information concerning function execution failures.

<dl> <dt>

<span id="TAPIERR_CONNECTED"></span><span id="tapierr_connected"></span>**TAPIERR\_CONNECTED**
</dt> <dd> <dl> <dt>



The operation cannot be performed while the call state is connected.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_DESTBUSY"></span><span id="tapierr_destbusy"></span>**TAPIERR\_DESTBUSY**
</dt> <dd> <dl> <dt>



The call destination is busy.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_DESTNOANSWER"></span><span id="tapierr_destnoanswer"></span>**TAPIERR\_DESTNOANSWER**
</dt> <dd> <dl> <dt>



The call destination did not answer.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_DESTUNAVAIL"></span><span id="tapierr_destunavail"></span>**TAPIERR\_DESTUNAVAIL**
</dt> <dd> <dl> <dt>



The call destination is not available.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_DEVICECLASSUNAVAIL"></span><span id="tapierr_deviceclassunavail"></span>**TAPIERR\_DEVICECLASSUNAVAIL**
</dt> <dd> <dl> <dt>



The device class needed is not available.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_DEVICEIDUNAVAIL"></span><span id="tapierr_deviceidunavail"></span>**TAPIERR\_DEVICEIDUNAVAIL**
</dt> <dd> <dl> <dt>



The device identifier needed is not available.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_DEVICEINUSE"></span><span id="tapierr_deviceinuse"></span>**TAPIERR\_DEVICEINUSE**
</dt> <dd> <dl> <dt>



The needed device is in use.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_DROPPED"></span><span id="tapierr_dropped"></span>**TAPIERR\_DROPPED**
</dt> <dd> <dl> <dt>



The call was dropped.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_INVALDESTADDRESS"></span><span id="tapierr_invaldestaddress"></span>**TAPIERR\_INVALDESTADDRESS**
</dt> <dd> <dl> <dt>



The pointer to the destination address is not valid, is **NULL**, or the destination address string is too long.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_INVALDEVICECLASS"></span><span id="tapierr_invaldeviceclass"></span>**TAPIERR\_INVALDEVICECLASS**
</dt> <dd> <dl> <dt>



The device class requested is not valid.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_INVALDEVICEID"></span><span id="tapierr_invaldeviceid"></span>**TAPIERR\_INVALDEVICEID**
</dt> <dd> <dl> <dt>



The device class identifier requested is not valid.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_INVALPOINTER"></span><span id="tapierr_invalpointer"></span>**TAPIERR\_INVALPOINTER**
</dt> <dd> <dl> <dt>



The pointer does not reference a valid memory location. One or more of the pointers *lpszDestAddress*, *lpszAppName*, *lpszCalledParty*, or *lpszComment* have been specified but are invalid.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_INVALWINDOWHANDLE"></span><span id="tapierr_invalwindowhandle"></span>**TAPIERR\_INVALWINDOWHANDLE**
</dt> <dd> <dl> <dt>



The window handle is not valid.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_NOREQUESTRECIPIENT"></span><span id="tapierr_norequestrecipient"></span>**TAPIERR\_NOREQUESTRECIPIENT**
</dt> <dd> <dl> <dt>



No recipient application is available to handle the request. The user should start the recipient application and try again.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_NOTADMIN"></span><span id="tapierr_notadmin"></span>**TAPIERR\_NOTADMIN**
</dt> <dd> <dl> <dt>



The operation requested require admin privileges.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_REQUESTCANCELLED"></span><span id="tapierr_requestcancelled"></span>**TAPIERR\_REQUESTCANCELLED**
</dt> <dd> <dl> <dt>



The assisted telephony request was canceled.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_REQUESTFAILED"></span><span id="tapierr_requestfailed"></span>**TAPIERR\_REQUESTFAILED**
</dt> <dd> <dl> <dt>



The request failed for unspecified reasons.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_REQUESTQUEUEFULL"></span><span id="tapierr_requestqueuefull"></span>**TAPIERR\_REQUESTQUEUEFULL**
</dt> <dd> <dl> <dt>



A recipient application is active, but the request queue is full or there is insufficient memory to expand the queue. The application can try again later.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_UNKNOWNREQUESTID"></span><span id="tapierr_unknownrequestid"></span>**TAPIERR\_UNKNOWNREQUESTID**
</dt> <dd> <dl> <dt>



The request identifier referenced is not valid.


</dt> </dl> </dd> <dt>

<span id="TAPIERR_UNKNOWNWINHANDLE"></span><span id="tapierr_unknownwinhandle"></span>**TAPIERR\_UNKNOWNWINHANDLE**
</dt> <dd> <dl> <dt>



An unknown window handle was referenced.


</dt> </dl> </dd> </dl>

## Remarks

Any other TAPIERR\_ values are obsolete and must not be used.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




