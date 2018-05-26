---
title: ProgressType enumeration
description: Describes the type of progress that is being reported from the assessment to the Axe engine.
ms.assetid: 17199ff1-95c0-44f3-802e-4f3b59abe8ba
keywords:
- ProgressType enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- ProgressType
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ProgressType enumeration

Describes the type of progress that is being reported from the assessment to the Axe engine.

## Syntax


```C++
enum ProgressType {
  None             = 0, 
  Percent          = 1, 
  Message          = 2, 
  Heartbeat        = 3, 
  Increment        = 4, 
  Cancelling       = 5, 
  RemainingTime    = 6, 
  WaitingForInput  = 7, 
  OnOff            = 8 

};
```



## Constants

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None**
</dt> <dd>

There is no progress reported. It should never occur at runtime.

</dd> <dt>

<span id="Percent"></span><span id="percent"></span><span id="PERCENT"></span>**Percent**
</dt> <dd>

The *progressValue* parameter is an integer in the range \[0-100\] that indicates the percentage complete. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="Message"></span><span id="message"></span><span id="MESSAGE"></span>**Message**
</dt> <dd>

The *progressMessage* parameter contains a message for the client application to display. This could be the name of a phase or other custom messages. The *progressValue* parameter is 0 and has no meaning.

</dd> <dt>

<span id="Heartbeat"></span><span id="heartbeat"></span><span id="HEARTBEAT"></span>**Heartbeat**
</dt> <dd>

The assessment is still running. The *progressValue* parameter is 0 and has no meaning. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="Increment"></span><span id="increment"></span><span id="INCREMENT"></span>**Increment**
</dt> <dd>

The *progressValue* parameter is one more than the last Increment progress event contained. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="Cancelling"></span><span id="cancelling"></span><span id="CANCELLING"></span>**Cancelling**
</dt> <dd>

The assessment has received a cancellation request and is ending. The *progressValue* parameter is 0 and has no meaning. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="RemainingTime"></span><span id="remainingtime"></span><span id="REMAININGTIME"></span>**RemainingTime**
</dt> <dd>

The assessment has a limited amount of time that it is expecting to run. The *progressValue* parameter is the estimated number of seconds remaining before the assessment completes. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="WaitingForInput"></span><span id="waitingforinput"></span><span id="WAITINGFORINPUT"></span>**WaitingForInput**
</dt> <dd>

The assessment has presented a user interface or a command line prompt and is waiting for input from the user. The *progressValue* parameter is 0 and has no meaning. The *progressMessage* parameter contains a string that explains why the assessment is waiting.

</dd> <dt>

<span id="OnOff"></span><span id="onoff"></span><span id="ONOFF"></span>**OnOff**
</dt> <dd>

The assessment reports that it is controlling a transition of the system s power state. This lets AXE know that the next system Power On transition is intentional and not an error. The *progressMessage* parameter is an empty string.

The *progressValue* parameter contains one of the following values :

<dl> <dd>0 - Reboot (Restart)</dd> <dd>1 - Sleep</dd> <dd>2 - Hibernate</dd> <dd>3 - Full shutdown</dd> <dd>4 - Hiber-Shutdown</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





