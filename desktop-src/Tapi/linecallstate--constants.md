---
description: The LINECALLSTATE\_ bit-flag constants describe the call states a call can be in.
ms.assetid: 18d881ee-cf98-4dec-a561-333c2518935d
title: LINECALLSTATE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLSTATE\_ Constants

The **LINECALLSTATE\_** bit-flag constants describe the call states a call can be in.

<dl> <dt>

<span id="LINECALLSTATE_ACCEPTED"></span><span id="linecallstate_accepted"></span>**LINECALLSTATE\_ACCEPTED**
</dt> <dd> <dl> <dt>



The call was in the offering state and has been accepted. This indicates to other (monitoring) applications that the current owner application has claimed responsibility for answering the call. In ISDN, the accepted state is entered when the called-party equipment sends a message to the switch indicating that it is willing to present the call to the called person. This has the side effect of alerting (ringing) the users at both ends of the call. An incoming call can always be immediately answered without first being separately accepted.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_BUSY"></span><span id="linecallstate_busy"></span>**LINECALLSTATE\_BUSY**
</dt> <dd> <dl> <dt>



The call is receiving a busy tone. A busy tone indicates that the call cannot be completed either a circuit (trunk) or the remote party's station are in use. See [**LINEBUSYMODE\_ Constants**](linebusymode--constants.md).


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_CONFERENCED"></span><span id="linecallstate_conferenced"></span>**LINECALLSTATE\_CONFERENCED**
</dt> <dd> <dl> <dt>



The call is a member of a conference call and is logically in the connected state.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_CONNECTED"></span><span id="linecallstate_connected"></span>**LINECALLSTATE\_CONNECTED**
</dt> <dd> <dl> <dt>



The call has been established and the connection is made. Information is able to flow over the call between the originating address and the destination address.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_DIALING"></span><span id="linecallstate_dialing"></span>**LINECALLSTATE\_DIALING**
</dt> <dd> <dl> <dt>



The originator is dialing digits on the call. The dialed digits are collected by the switch. Note that neither [**lineGenerateDigits**](/windows/desktop/api/Tapi/nf-tapi-linegeneratedigits) nor [**TSPI\_lineGenerateDigits**](/windows/win32/api/tspi/nf-tspi-tspi_linegeneratedigits) will place the line into the dialing state.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_DIALTONE"></span><span id="linecallstate_dialtone"></span>**LINECALLSTATE\_DIALTONE**
</dt> <dd> <dl> <dt>



The call is receiving a dial tone from the switch, which means that the switch is ready to receive a dialed number. See [**LINEDIALTONEMODE\_ Constants**](linedialtonemode--constants.md) for identifiers of special dial tones, such as a stutter tone of normal voice mail.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_DISCONNECTED"></span><span id="linecallstate_disconnected"></span>**LINECALLSTATE\_DISCONNECTED**
</dt> <dd> <dl> <dt>



The remote party has disconnected from the call.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_IDLE"></span><span id="linecallstate_idle"></span>**LINECALLSTATE\_IDLE**
</dt> <dd> <dl> <dt>



The call exists but has not been connected. No activity exists on the call, which means that no call is currently active. A call can never transition out of the idle state.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_OFFERING"></span><span id="linecallstate_offering"></span>**LINECALLSTATE\_OFFERING**
</dt> <dd> <dl> <dt>



The call is being offered to the station, signaling the arrival of a new call. The offering state is not the same as causing a phone or computer to ring. In some environments, a call in the offering state does not ring the user until the switch instructs the line to ring. An example use might be where an incoming call appears on several station sets but only the primary address rings. The instruction to ring does not affect any call states.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_ONHOLD"></span><span id="linecallstate_onhold"></span>**LINECALLSTATE\_ONHOLD**
</dt> <dd> <dl> <dt>



The call is on hold by the switch. This frees the physical line, which allows another call to use the line.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_ONHOLDPENDCONF"></span><span id="linecallstate_onholdpendconf"></span>**LINECALLSTATE\_ONHOLDPENDCONF**
</dt> <dd> <dl> <dt>



The call is currently on hold while it is being added to a conference.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_ONHOLDPENDTRANSFER"></span><span id="linecallstate_onholdpendtransfer"></span>**LINECALLSTATE\_ONHOLDPENDTRANSFER**
</dt> <dd> <dl> <dt>



The call is currently on hold awaiting transfer to another number.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_PROCEEDING"></span><span id="linecallstate_proceeding"></span>**LINECALLSTATE\_PROCEEDING**
</dt> <dd> <dl> <dt>



Dialing has completed and the call is proceeding through the switch or telephone network. This occurs after dialing is complete and before the call reaches the dialed party, as indicated by ringback, busy, or answer.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_RINGBACK"></span><span id="linecallstate_ringback"></span>**LINECALLSTATE\_RINGBACK**
</dt> <dd> <dl> <dt>



The station to be called has been reached, and the destination's switch is generating a ring tone back to the originator. A *ringback* means that the destination address is being alerted to the call.


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_SPECIALINFO"></span><span id="linecallstate_specialinfo"></span>**LINECALLSTATE\_SPECIALINFO**
</dt> <dd> <dl> <dt>



The call is receiving a special information signal, which precedes a prerecorded announcement indicating why a call cannot be completed. See [**LINESPECIALINFO\_ Constants**](linespecialinfo--constants.md).


</dt> </dl> </dd> <dt>

<span id="LINECALLSTATE_UNKNOWN"></span><span id="linecallstate_unknown"></span>**LINECALLSTATE\_UNKNOWN**
</dt> <dd> <dl> <dt>



The call exists, but its state is currently unknown. This may be the result of poor call progress detection by the service provider. A call state message with the call state set to unknown may also be generated to inform the TAPI DLL about a new call at a time when the actual call state of the call is not exactly known.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 8 bits can define a device-specific substate of any of the predefined states, provided that one of the LINECALLSTATE\_ bits defined above is also set. The low-order 24 bits are reserved for predefined states.

The **LINECALLSTATE\_constants** are used as parameters by the [**LINE\_CALLSTATE**](line-callstate.md) message sent to the application. The message carries the new call state that the call transitioned to. These constants are also used as members in the [**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus) structure returned by the [**lineGetCallStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetcallstatus) function.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_CALLSTATE**](line-callstate.md)
</dt> <dt>

[**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus)
</dt> <dt>

[**lineGenerateDigits**](/windows/desktop/api/Tapi/nf-tapi-linegeneratedigits)
</dt> <dt>

[**lineGetCallStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetcallstatus)
</dt> </dl>

 

