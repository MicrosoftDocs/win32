---
title: AxeProgressType enumeration
description: Describes the type of progress that is being reported by the assessment to the Axe engine in ReportProgress methods.
ms.assetid: 95086EC0-A9A8-40F6-BF1E-570AE88D6C43
keywords:
- ProgressType enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- ProgressType
api_location:
- AxeCore.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# AxeProgressType enumeration

Describes the type of progress that is being reported by the assessment to the Axe engine in [**ReportProgress**](support-reportprogress-overl.md) methods.

## Syntax


```C++
enum ProgressType {
  ProgressTypeNone             = 0, 
  ProgressTypePercent, 
  ProgressTypeMessage, 
  ProgressTypeHeartbeat, 
  ProgressTypeIncrement, 
  ProgressTypeCancelling, 
  ProgressTypeRemainingTime, 
  ProgressTypeWaitingForInput, 
  ProgressTypeOnOff, 
  ProgressTypeWarning, 
  ProgressTypeError, 
  ProgressTypeTestCase, 
  ProgressTypeIdle, 
  ProgressTypeInvalid 

};
```



## Constants

<dl> <dt>

<span id="ProgressTypeNone"></span><span id="progresstypenone"></span><span id="PROGRESSTYPENONE"></span>**ProgressTypeNone**
</dt> <dd>

There is no progress reported. This enumerator should never occur at runtime.

</dd> <dt>

<span id="ProgressTypePercent"></span><span id="progresstypepercent"></span><span id="PROGRESSTYPEPERCENT"></span>**ProgressTypePercent**
</dt> <dd>

The *progressValue* parameter is an integer in the range \[0-100\] that indicates the percentage complete. The *progressMessage* parameter can contain an optional message for the application to display.

</dd> <dt>

<span id="ProgressTypeMessage"></span><span id="progresstypemessage"></span><span id="PROGRESSTYPEMESSAGE"></span>**ProgressTypeMessage**
</dt> <dd>

The *progressMessage* parameter contains a message for the application to display. This could be the name of a phase or other custom messages. The *progressValue* parameter is 0 and has no meaning.

</dd> <dt>

<span id="ProgressTypeHeartbeat"></span><span id="progresstypeheartbeat"></span><span id="PROGRESSTYPEHEARTBEAT"></span>**ProgressTypeHeartbeat**
</dt> <dd>

The assessment is still running. The *progressValue* parameter is 0 and has no meaning. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="ProgressTypeIncrement"></span><span id="progresstypeincrement"></span><span id="PROGRESSTYPEINCREMENT"></span>**ProgressTypeIncrement**
</dt> <dd>

The *progressValue* parameter is one more than the last progress event increment. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="ProgressTypeCancelling"></span><span id="progresstypecancelling"></span><span id="PROGRESSTYPECANCELLING"></span>**ProgressTypeCancelling**
</dt> <dd>

The assessment has received a cancellation request and is ending. The *progressValue* parameter is 0 and has no meaning. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="ProgressTypeRemainingTime"></span><span id="progresstyperemainingtime"></span><span id="PROGRESSTYPEREMAININGTIME"></span>**ProgressTypeRemainingTime**
</dt> <dd>

The assessment has a limited amount of time that it is expecting to run. The *progressValue* parameter is the estimated number of seconds remaining before the assessment completes. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="ProgressTypeWaitingForInput"></span><span id="progresstypewaitingforinput"></span><span id="PROGRESSTYPEWAITINGFORINPUT"></span>**ProgressTypeWaitingForInput**
</dt> <dd>

The assessment has presented a user interface or a command line prompt and is waiting for input from the user. The **progressValue** parameter is 0 and has no meaning. The *progressMessage* parameter contains a string that explains why the assessment is waiting.

</dd> <dt>

<span id="ProgressTypeOnOff"></span><span id="progresstypeonoff"></span><span id="PROGRESSTYPEONOFF"></span>**ProgressTypeOnOff**
</dt> <dd>

The assessment reports that it is controlling a transition of the system s power state. This lets AXE know that the next system Power On transition is intentional and not an error. The *progressMessage* parameter is an empty string. The *progressValue* parameter contains one of the values from the [**OnOffProgressValue**](onoffprogressvalue.md) enumeration.

</dd> <dt>

<span id="ProgressTypeWarning"></span><span id="progresstypewarning"></span><span id="PROGRESSTYPEWARNING"></span>**ProgressTypeWarning**
</dt> <dd>

The *progressMessage* parameter contains a message for the application to display. This message is a warning message and the application can display it to differentiate it from basic messages or errors. The *progressValue* parameter is 0 and has no meaning.

</dd> <dt>

<span id="ProgressTypeError"></span><span id="progresstypeerror"></span><span id="PROGRESSTYPEERROR"></span>**ProgressTypeError**
</dt> <dd>

The *progressMessage* parameter contains a message for the application to display. This message is an error message and the application can display it to differentiate it from basic messages or warnings. The *progressValue* parameter is 0 and has no meaning.

</dd> <dt>

<span id="ProgressTypeTestCase"></span><span id="progresstypetestcase"></span><span id="PROGRESSTYPETESTCASE"></span>**ProgressTypeTestCase**
</dt> <dd>

The *progressMessage* parameter contains a message for the application to display. The *progressValue* parameter is non-zero if the *progressMessage* indicates a successful result and zero if the *progressMessage* indicates a failure.

</dd> <dt>

<span id="ProgressTypeIdle"></span><span id="progresstypeidle"></span><span id="PROGRESSTYPEIDLE"></span>**ProgressTypeIdle**
</dt> <dd>

This enumerator is only used by workloads executed by the Energy Efficiency assessment to report when an idle period occurs so that the energy used during that period can analyzed. The *progressValue* parameter is a value from the [**ProgressIdleValue**](progressidlevalue.md) enumeration. The *progressMessage* parameter is an empty string.

</dd> <dt>

<span id="ProgressTypeInvalid"></span><span id="progresstypeinvalid"></span><span id="PROGRESSTYPEINVALID"></span>**ProgressTypeInvalid**
</dt> <dd>

An invalid progress type was reported. This enumerator is most often used for range checking the enumerator values. It should not be used to report an actual progress type.

</dd> </dl>

## Remarks

Managed code uses the [**AxeProgressType**](https://www.bing.com/search?q=**AxeProgressType**) enum.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl> |



 

 





