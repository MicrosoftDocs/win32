---
title: SignalAndServiceStatusSpanningEvent\_State enumeration
description: Specifies the state of a television broadcasting service.
ms.assetid: 88da8346-661c-4638-809d-4ef01f191cbe
keywords:
- SignalAndServiceStatusSpanningEvent_State enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- SignalAndServiceStatusSpanningEvent_State
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- bdamedia.h
api_type:
- HeaderDef
---

# SignalAndServiceStatusSpanningEvent\_State enumeration

Specifies the state of a television broadcasting service.

## Syntax


```C++
typedef enum  { 
  SignalAndServiceStatusSpanningEvent_Clear          = 0,
  SignalAndServiceStatusSpanningEvent_NoTVSignal     = 1,
  SignalAndServiceStatusSpanningEvent_ServiceOffAir  = 2
} SignalAndServiceStatusSpanningEvent_State;
```



## Constants

<dl> <dt>

<span id="SignalAndServiceStatusSpanningEvent_Clear"></span><span id="signalandservicestatusspanningevent_clear"></span><span id="SIGNALANDSERVICESTATUSSPANNINGEVENT_CLEAR"></span>**SignalAndServiceStatusSpanningEvent\_Clear**
</dt> <dd>

The signal is clear.

</dd> <dt>

<span id="SignalAndServiceStatusSpanningEvent_NoTVSignal"></span><span id="signalandservicestatusspanningevent_notvsignal"></span><span id="SIGNALANDSERVICESTATUSSPANNINGEVENT_NOTVSIGNAL"></span>**SignalAndServiceStatusSpanningEvent\_NoTVSignal**
</dt> <dd>

There is no signal.

</dd> <dt>

<span id="SignalAndServiceStatusSpanningEvent_ServiceOffAir"></span><span id="signalandservicestatusspanningevent_serviceoffair"></span><span id="SIGNALANDSERVICESTATUSSPANNINGEVENT_SERVICEOFFAIR"></span>**SignalAndServiceStatusSpanningEvent\_ServiceOffAir**
</dt> <dd>

The service is not broadcasting.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdamedia.h</dt> </dl> |



 

 





