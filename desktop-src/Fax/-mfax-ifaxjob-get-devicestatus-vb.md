---
Description: The DeviceStatus property is a null-terminated string that describes the status of the port associated with the fax job.
ms.assetid: e97bb951-22a5-46a8-a5de-7b56fa052f40
title: FaxJob.DeviceStatus property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJob.DeviceStatus property

The **DeviceStatus** property is a null-terminated string that describes the status of the port associated with the fax job.

This property is read-only.

## Syntax


```VB
Property DeviceStatus As String
```



## Property value

A **String** that receives a localized null-terminated string that contains a fax device status. Following are the English string equivalents.

<dt>

<span id="Dialing"></span><span id="dialing"></span><span id="DIALING"></span>

<span id="Dialing"></span><span id="dialing"></span><span id="DIALING"></span>**Dialing** (Dialing)


</dt> <dd>

The device is dialing a fax number.

</dd> <dt>

<span id="Sending"></span><span id="sending"></span><span id="SENDING"></span>

<span id="Sending"></span><span id="sending"></span><span id="SENDING"></span>**Sending** (Sending)


</dt> <dd>

The device is sending a fax document.

</dd> <dt>

<span id="Receiving"></span><span id="receiving"></span><span id="RECEIVING"></span>

<span id="Receiving"></span><span id="receiving"></span><span id="RECEIVING"></span>**Receiving** (Receiving)


</dt> <dd>

The device is receiving a fax document.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (Completed)


</dt> <dd>

The device completed sending or receiving a fax transmission.

</dd> <dt>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>**Unavailable** (Unavailable)


</dt> <dd>

The device is not available because it is in use by another application.

</dd> <dt>

<span id="Busy"></span><span id="busy"></span><span id="BUSY"></span>

<span id="Busy"></span><span id="busy"></span><span id="BUSY"></span>**Busy** (Busy)


</dt> <dd>

The device encountered a busy signal.

</dd> <dt>

<span id="No_Answer"></span><span id="no_answer"></span><span id="NO_ANSWER"></span>

<span id="No_Answer"></span><span id="no_answer"></span><span id="NO_ANSWER"></span>**No Answer** (No Answer)


</dt> <dd>

The receiving device did not answer the call.

</dd> <dt>

<span id="Bad_Address"></span><span id="bad_address"></span><span id="BAD_ADDRESS"></span>

<span id="Bad_Address"></span><span id="bad_address"></span><span id="BAD_ADDRESS"></span>**Bad Address** (Bad Address)


</dt> <dd>

The device dialed an invalid fax number.

</dd> <dt>

<span id="No_Dial_Tone"></span><span id="no_dial_tone"></span><span id="NO_DIAL_TONE"></span>

<span id="No_Dial_Tone"></span><span id="no_dial_tone"></span><span id="NO_DIAL_TONE"></span>**No Dial Tone** (No Dial Tone)


</dt> <dd>

The sending device cannot complete the call because it does not detect a dial tone.

</dd> <dt>

<span id="Disconnected"></span><span id="disconnected"></span><span id="DISCONNECTED"></span>

<span id="Disconnected"></span><span id="disconnected"></span><span id="DISCONNECTED"></span>**Disconnected** (Disconnected)


</dt> <dd>

The fax call was disconnected by the sender or the caller.

</dd> <dt>

<span id="Fatal_Error"></span><span id="fatal_error"></span><span id="FATAL_ERROR"></span>

<span id="Fatal_Error"></span><span id="fatal_error"></span><span id="FATAL_ERROR"></span>**Fatal Error** (Fatal Error)


</dt> <dd>

The device has encountered a fatal protocol error.

</dd> <dt>

<span id="Not_a_Fax_Call"></span><span id="not_a_fax_call"></span><span id="NOT_A_FAX_CALL"></span>

<span id="Not_a_Fax_Call"></span><span id="not_a_fax_call"></span><span id="NOT_A_FAX_CALL"></span>**Not a Fax Call** (Not a Fax Call)


</dt> <dd>

The device received a call that was a data call or a voice call.

</dd> <dt>

<span id="Call_Delayed"></span><span id="call_delayed"></span><span id="CALL_DELAYED"></span>

<span id="Call_Delayed"></span><span id="call_delayed"></span><span id="CALL_DELAYED"></span>**Call Delayed** (Call Delayed)


</dt> <dd>

The device delayed a fax call because the sending device received a busy signal multiple times. The device cannot retry the call because dialing restrictions exist. (Some countries/regions restrict the number of retry attempts when a number is busy.)

</dd> <dt>

<span id="Call_Blacklisted"></span><span id="call_blacklisted"></span><span id="CALL_BLACKLISTED"></span>

<span id="Call_Blacklisted"></span><span id="call_blacklisted"></span><span id="CALL_BLACKLISTED"></span>**Call Blacklisted** (Call Blacklisted)


</dt> <dd>

The device could not complete a call because the telephone number was blocked or reserved; emergency numbers such as 911 are blocked.

</dd> <dt>

<span id="Initializing"></span><span id="initializing"></span><span id="INITIALIZING"></span>

<span id="Initializing"></span><span id="initializing"></span><span id="INITIALIZING"></span>**Initializing** (Initializing)


</dt> <dd>

The device is initializing a call.

</dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (Offline)


</dt> <dd>

The device is offline and unavailable.

</dd> <dt>

<span id="Ringing"></span><span id="ringing"></span><span id="RINGING"></span>

<span id="Ringing"></span><span id="ringing"></span><span id="RINGING"></span>**Ringing** (Ringing)


</dt> <dd>

The device is ringing.

</dd> <dt>

<span id="Available"></span><span id="available"></span><span id="AVAILABLE"></span>

<span id="Available"></span><span id="available"></span><span id="AVAILABLE"></span>**Available** (Available)


</dt> <dd>

The device is available.

</dd> <dt>

<span id="Aborting"></span><span id="aborting"></span><span id="ABORTING"></span>

<span id="Aborting"></span><span id="aborting"></span><span id="ABORTING"></span>**Aborting** (Aborting)


</dt> <dd>

The device is aborting a fax job.

</dd> <dt>

<span id="Routing"></span><span id="routing"></span><span id="ROUTING"></span>

<span id="Routing"></span><span id="routing"></span><span id="ROUTING"></span>**Routing** (Routing)


</dt> <dd>

The device is routing a received fax document.

</dd> <dt>

<span id="Answered"></span><span id="answered"></span><span id="ANSWERED"></span>

<span id="Answered"></span><span id="answered"></span><span id="ANSWERED"></span>**Answered** (Answered)


</dt> <dd>

The device answered a new call.

</dd> <dt>

<span id="Handled"></span><span id="handled"></span><span id="HANDLED"></span>

<span id="Handled"></span><span id="handled"></span><span id="HANDLED"></span>**Handled** (Handled)


</dt> <dd>

The fax service processed the outbound fax document; the fax service provider will transmit the document.

</dd> </dl>

## Remarks

If the job is in the job queue waiting transmission, the fax server has not associated a device with the job. In this instance, **DeviceStatus** is "Unknown".

**DeviceStatus** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxJob**](-mfax-faxjob-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxJob**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjob)
</dt> <dt>

[**IFaxJobs**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjobs)
</dt> </dl>

 

 




