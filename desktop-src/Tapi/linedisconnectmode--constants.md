---
description: The LINEDISCONNECTMODE\_ bit-flag constants describe different reasons for a remote disconnect request. A disconnect mode is available as call status to the application after the call state transitions to disconnected.
ms.assetid: 1b26f13c-b0bf-4d2c-8514-f0c376e36bcd
title: LINEDISCONNECTMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEDISCONNECTMODE\_ Constants

The **LINEDISCONNECTMODE\_** bit-flag constants describe different reasons for a remote disconnect request. A disconnect mode is available as call status to the application after the call state transitions to disconnected.

<dl> <dt>

<span id="LINEDISCONNECTMODE_BADADDRESS"></span><span id="linedisconnectmode_badaddress"></span>**LINEDISCONNECTMODE\_BADADDRESS**
</dt> <dd> <dl> <dt>



The destination address is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_BLOCKED"></span><span id="linedisconnectmode_blocked"></span>**LINEDISCONNECTMODE\_BLOCKED**
</dt> <dd> <dl> <dt>



The call could not be connected because calls from the origination address are not being accepted at the destination address. This differs from LINEDISCONNECTMODE\_REJECT in that blocking is implemented in the network (a passive reject) while a rejection is implemented in the destination equipment (an active reject). The blocking can be due to a specific exclusion of the origination address, or because the destination accepts calls from only a selected set of origination address (closed user group). (TAPI versions 2.0 and later)

LINEDISCONNECTMODE\_BLOCKED is appropriate as a blocklisted response. For example, a modem has received an answer, gone more than six seconds without detecting Ringback, failed to connect a defined number of times, determines that the phone number is not valid to call, and issues a 'blocklisted' response.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_BUSY"></span><span id="linedisconnectmode_busy"></span>**LINEDISCONNECTMODE\_BUSY**
</dt> <dd> <dl> <dt>



The remote user's station is busy.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_CANCELLED"></span><span id="linedisconnectmode_cancelled"></span>**LINEDISCONNECTMODE\_CANCELLED**
</dt> <dd> <dl> <dt>



The call was cancelled. (TAPI versions 2.0 and later)


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_CONGESTION"></span><span id="linedisconnectmode_congestion"></span>**LINEDISCONNECTMODE\_CONGESTION**
</dt> <dd> <dl> <dt>



The network is congested.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_DONOTDISTURB"></span><span id="linedisconnectmode_donotdisturb"></span>**LINEDISCONNECTMODE\_DONOTDISTURB**
</dt> <dd> <dl> <dt>



The call could not be connected because the destination has invoked the Do Not Disturb feature. (TAPI versions 2.0 and later)


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_FORWARDED"></span><span id="linedisconnectmode_forwarded"></span>**LINEDISCONNECTMODE\_FORWARDED**
</dt> <dd> <dl> <dt>



The call was forwarded by the switch.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_INCOMPATIBLE"></span><span id="linedisconnectmode_incompatible"></span>**LINEDISCONNECTMODE\_INCOMPATIBLE**
</dt> <dd> <dl> <dt>



The remote user's station equipment is incompatible with the type of call requested.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_NOANSWER"></span><span id="linedisconnectmode_noanswer"></span>**LINEDISCONNECTMODE\_NOANSWER**
</dt> <dd> <dl> <dt>



The remote user's station does not answer.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_NODIALTONE"></span><span id="linedisconnectmode_nodialtone"></span>**LINEDISCONNECTMODE\_NODIALTONE**
</dt> <dd> <dl> <dt>



A dial tone was not detected within a service-provider defined timeout, at a point during dialing when one was expected (such as at a "W" in the dialable string). This can also occur without a service-provider-defined timeout period or without a value specified in the **dwWaitForDialTone** member of the [**LINEDIALPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linedialparams) structure. (TAPI versions 1.4 and later)


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_NORMAL"></span><span id="linedisconnectmode_normal"></span>**LINEDISCONNECTMODE\_NORMAL**
</dt> <dd> <dl> <dt>



This is a normal disconnect request by the remote party. The call was terminated normally.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_NUMBERCHANGED"></span><span id="linedisconnectmode_numberchanged"></span>**LINEDISCONNECTMODE\_NUMBERCHANGED**
</dt> <dd> <dl> <dt>



The call could not be connected because the destination number has been changed, but automatic redirection to the new number is not provided. (TAPI versions 2.0 and later)


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_OUTOFORDER"></span><span id="linedisconnectmode_outoforder"></span>**LINEDISCONNECTMODE\_OUTOFORDER**
</dt> <dd> <dl> <dt>



The call could not be connected or was disconnected because the destination device is out of order (hardware failure). (TAPI versions 2.0 and later)


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_PICKUP"></span><span id="linedisconnectmode_pickup"></span>**LINEDISCONNECTMODE\_PICKUP**
</dt> <dd> <dl> <dt>



The call was picked up from elsewhere.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_QOSUNAVAIL"></span><span id="linedisconnectmode_qosunavail"></span>**LINEDISCONNECTMODE\_QOSUNAVAIL**
</dt> <dd> <dl> <dt>



The call could not be connected or was disconnected because the minimum quality of service could not be obtained or sustained. This differs from LINEDISCONNECTMODE\_INCOMPATIBLE in that the lack of resources may be a temporary condition at the destination. (TAPI versions 2.0 and later)


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_REJECT"></span><span id="linedisconnectmode_reject"></span>**LINEDISCONNECTMODE\_REJECT**
</dt> <dd> <dl> <dt>



The remote user has rejected the call.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_TEMPFAILURE"></span><span id="linedisconnectmode_tempfailure"></span>**LINEDISCONNECTMODE\_TEMPFAILURE**
</dt> <dd> <dl> <dt>



The call could not be connected or was disconnected because of a temporary failure in the network; the call can be reattempted later and is expected to eventually complete. (TAPI versions 2.0 and later)

LINEDISCONNECTMODE\_TEMPFAILURE is appropriate as a delayed response. For example, a modem getting a busy signal or equivalent too many times in a particular time period concludes that the number should not be called again until a defined time has elapsed and issues a 'delayed' response.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_UNAVAIL"></span><span id="linedisconnectmode_unavail"></span>**LINEDISCONNECTMODE\_UNAVAIL**
</dt> <dd> <dl> <dt>



The reason for the disconnect is unavailable and will not become known later.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_UNKNOWN"></span><span id="linedisconnectmode_unknown"></span>**LINEDISCONNECTMODE\_UNKNOWN**
</dt> <dd> <dl> <dt>



The reason for the disconnect request is unknown but may become known later.


</dt> </dl> </dd> <dt>

<span id="LINEDISCONNECTMODE_UNREACHABLE"></span><span id="linedisconnectmode_unreachable"></span>**LINEDISCONNECTMODE\_UNREACHABLE**
</dt> <dd> <dl> <dt>



The remote user could not be reached.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 16 bits can be assigned for device-specific extensions. The low-order 16 bits are reserved.

A remote disconnect request for a given call results in the call state transitioning to the disconnected state and a [**LINE\_CALLSTATE**](line-callstate.md) message is sent to the application. The LINEDISCONNECTMODE\_ information provides details about the remote disconnect request. It is available in the call's [**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus) structure when the call is in the disconnected state. While a call is in this state, the application is still allowed to query the call's information and status. For example, user-user information that is received as part of the remote disconnect is available then. The application can clear a disconnected call by dropping the call.

For backward compatibility, it is the responsibility of the service provider to examine the negotiated API version on the line, and to not use this LINEDISCONNECTMODE\_ value if it is not supported on the negotiated version (LINEDISCONNECTMODE\_NORMAL or \_UNKNOWN could be used instead).

## Requirements



|                         |                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_CALLSTATE**](line-callstate.md)
</dt> <dt>

[**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus)
</dt> <dt>

[**LINEDIALPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linedialparams)
</dt> </dl>

 

 




