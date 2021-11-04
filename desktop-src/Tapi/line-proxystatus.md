---
description: The LINE\_PROXYSTATUS message is sent when the available proxies change on a line that the application currently has open.
ms.assetid: e20d4b48-a72a-4a83-ae04-a608791a1a3a
title: LINE_PROXYSTATUS message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_PROXYSTATUS message

The **LINE\_PROXYSTATUS** message is sent when the available proxies change on a line that the application currently has open.

TAPISRV generates this message during a [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen) function using LINEPROXYSTATUS\_OPEN and LINEPROXYSTATUS\_ALLOPENFORACD or a [**lineClose**](/windows/desktop/api/Tapi/nf-tapi-lineclose) function using LINEPROXYSTATUS\_CLOSE (all [**LINEPROXYSTATUS\_ Constants**](lineproxystatus--constants.md)).


```C++
            
```



## Parameters

<dl> <dt>

*dwDevice* 
</dt> <dd>

The application's handle to the line device. This relates to the agent handler.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

Specifies the queue status that has changed. Can be one or more of the [**LINEPROXYSTATUS\_ constants**](lineproxystatus--constants.md).

</dd> <dt>

*dwParam2* 
</dt> <dd>

If *dwParam1* is set to LINEPROXYSTATUS\_OPEN or LINEPROXYSTATUS\_CLOSE, *dwParam2* indicates the related proxy request type, which is one of the following:

-   LINEPROXYREQUEST\_SETAGENTGROUP
-   LINEPROXYREQUEST\_SETAGENTSTATE
-   LINEPROXYREQUEST\_SETAGENTACTIVITY
-   LINEPROXYREQUEST\_GETAGENTCAPS
-   LINEPROXYREQUEST\_GETAGENTSTATUS
-   LINEPROXYREQUEST\_AGENTSPECIFIC
-   LINEPROXYREQUEST\_GETAGENTACTIVITYLIST
-   LINEPROXYREQUEST\_GETAGENTGROUPLIST
-   LINEPROXYREQUEST\_CREATEAGENT
-   LINEPROXYREQUEST\_SETAGENTMEASUREMENTPERIOD
-   LINEPROXYREQUEST\_GETAGENTINFO
-   LINEPROXYREQUEST\_CREATEAGENTSESSION
-   LINEPROXYREQUEST\_GETAGENTSESSIONLIST
-   LINEPROXYREQUEST\_SETAGENTSESSIONSTATE
-   LINEPROXYREQUEST\_GETAGENTSESSIONINFO
-   LINEPROXYREQUEST\_GETQUEUELIST
-   LINEPROXYREQUEST\_SETQUEUEMEASUREMENTPERIOD
-   LINEPROXYREQUEST\_GETQUEUEINFO
-   LINEPROXYREQUEST\_GETGROUPLIST
-   LINEPROXYREQUEST\_SETAGENTSTATEEX

Otherwise, *dwParam2* is set to zero.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Reserved. Set to zero.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen)
</dt> <dt>

[**lineClose**](/windows/desktop/api/Tapi/nf-tapi-lineclose)
</dt> <dt>

[**LINE\_PROXYREQUEST**](line-proxyrequest.md)
</dt> <dt>

[**LINEPROXYREQUEST\_ Constants**](lineproxyrequest--constants.md)
</dt> </dl>

 

 




