---
description: The LINEDEVSTATE\_ bit-flag constants describe various line status events.
ms.assetid: 41e8a777-a57a-4d6c-850f-e21b58081b0d
title: LINEDEVSTATE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEDEVSTATE\_ Constants

The **LINEDEVSTATE\_** bit-flag constants describe various line status events.

<dl> <dt>

<span id="LINEDEVSTATE_BATTERY"></span><span id="linedevstate_battery"></span>**LINEDEVSTATE\_BATTERY**
</dt> <dd> <dl> <dt>



The battery level has changed significantly (cellular).


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_CAPSCHANGE"></span><span id="linedevstate_capschange"></span>**LINEDEVSTATE\_CAPSCHANGE**
</dt> <dd> <dl> <dt>



Indicates that, due to configuration changes made by the user or other circumstances, one or more of the members in the [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps) structure for the address have changed. The application should use [**lineGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetdevcaps) to read the updated structure. If a service provider sends a [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message containing this value to TAPI, TAPI will pass it along to applications that have negotiated TAPI version 1.4 or later; applications negotiating a previous TAPI version will receive **LINE\_LINEDEVSTATE** messages specifying LINEDEVSTATE\_REINIT, requiring them to shut down and reinitialize their connection to TAPI to obtain the updated information.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_CLOSE"></span><span id="linedevstate_close"></span>**LINEDEVSTATE\_CLOSE**
</dt> <dd> <dl> <dt>



The line has been closed by another application.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_CONFIGCHANGE"></span><span id="linedevstate_configchange"></span>**LINEDEVSTATE\_CONFIGCHANGE**
</dt> <dd> <dl> <dt>



Indicates that configuration changes have been made to one or more of the media devices associated with the line device. The application, if it desires, can use [**lineGetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig) to read the updated information. If a service provider sends a [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message containing this value to TAPI, TAPI will pass it along to applications that have negotiated TAPI version 1.4 or later; applications negotiating a previous API version will not receive any notification.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_COMPLCANCEL"></span><span id="linedevstate_complcancel"></span>**LINEDEVSTATE\_COMPLCANCEL**
</dt> <dd> <dl> <dt>



Indicates that the call completion identified by the completion identifier contained in the *dwParam2* parameter of the [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message has been externally canceled and is no longer considered valid (if that value were to be passed in a subsequent call to [**lineUncompleteCall**](/windows/desktop/api/Tapi/nf-tapi-lineuncompletecall), the function would fail with LINEERR\_INVALCOMPLETIONID). If a service provider sends a [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message containing this value to TAPI, TAPI will pass it along to applications that have negotiated TAPI version 1.4 or later; applications negotiating a previous API version will not receive any notification.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_CONNECTED"></span><span id="linedevstate_connected"></span>**LINEDEVSTATE\_CONNECTED**
</dt> <dd> <dl> <dt>



The line was previously disconnected and is now connected to TAPI.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_DEVSPECIFIC"></span><span id="linedevstate_devspecific"></span>**LINEDEVSTATE\_DEVSPECIFIC**
</dt> <dd> <dl> <dt>



The line's device-specific information has changed.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_DISCONNECTED"></span><span id="linedevstate_disconnected"></span>**LINEDEVSTATE\_DISCONNECTED**
</dt> <dd> <dl> <dt>



This line was previously connected and is now disconnected from TAPI.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_INSERVICE"></span><span id="linedevstate_inservice"></span>**LINEDEVSTATE\_INSERVICE**
</dt> <dd> <dl> <dt>



The line is connected to TAPI. This happens when TAPI is first activated or when the line wire is physically plugged in and in-service at the switch while TAPI is active.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_LOCK"></span><span id="linedevstate_lock"></span>**LINEDEVSTATE\_LOCK**
</dt> <dd> <dl> <dt>



The locked status of the line device has changed. (For more information, see LINEDEVSTATUSFLAGS\_LOCKED in [**LINEDEVSTATUSFLAGS\_ Constants**](linedevstatusflags--constants.md).)


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_MAINTENANCE"></span><span id="linedevstate_maintenance"></span>**LINEDEVSTATE\_MAINTENANCE**
</dt> <dd> <dl> <dt>



Maintenance is being performed on the line at the switch. TAPI cannot be used to operate on the line device.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_MSGWAITOFF"></span><span id="linedevstate_msgwaitoff"></span>**LINEDEVSTATE\_MSGWAITOFF**
</dt> <dd> <dl> <dt>



The message waiting indicator is turned off.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_MSGWAITON"></span><span id="linedevstate_msgwaiton"></span>**LINEDEVSTATE\_MSGWAITON**
</dt> <dd> <dl> <dt>



The message waiting indicator is turned on.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_NUMCALLS"></span><span id="linedevstate_numcalls"></span>**LINEDEVSTATE\_NUMCALLS**
</dt> <dd> <dl> <dt>



The number of calls on the line device has changed.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_NUMCOMPLETIONS"></span><span id="linedevstate_numcompletions"></span>**LINEDEVSTATE\_NUMCOMPLETIONS**
</dt> <dd> <dl> <dt>



The number of outstanding call completions on the line device has changed.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_OPEN"></span><span id="linedevstate_open"></span>**LINEDEVSTATE\_OPEN**
</dt> <dd> <dl> <dt>



The line has been opened by another application.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_OTHER"></span><span id="linedevstate_other"></span>**LINEDEVSTATE\_OTHER**
</dt> <dd> <dl> <dt>



Device-status items other than those listed below have changed. The application should check the current device status to determine which items have changed.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_OUTOFSERVICE"></span><span id="linedevstate_outofservice"></span>**LINEDEVSTATE\_OUTOFSERVICE**
</dt> <dd> <dl> <dt>



The line is out of service at the switch or physically disconnected. TAPI cannot be used to operate on the line device.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_REINIT"></span><span id="linedevstate_reinit"></span>**LINEDEVSTATE\_REINIT**
</dt> <dd> <dl> <dt>



Items have changed in the configuration of line devices. To become aware of these changes (as for the appearance of new line devices) the application should reinitialize its use of TAPI.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_REMOVED"></span><span id="linedevstate_removed"></span>**LINEDEVSTATE\_REMOVED**
</dt> <dd> <dl> <dt>



Indicates that the device is being removed from the system by the service provider (most likely through user action, through a control panel or similar utility). A [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message with this value will normally be immediately followed by a [**LINE\_CLOSE**](line-close.md) message on the device. Subsequent attempts to access the device prior to TAPI being reinitialized will result in LINEERR\_NODEVICE being returned to the application. If a service provider sends a [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message containing this value to TAPI, TAPI will pass it along to applications that have negotiated TAPI version 1.4 or later; applications negotiating a previous API version will not receive any notification.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_RINGING"></span><span id="linedevstate_ringing"></span>**LINEDEVSTATE\_RINGING**
</dt> <dd> <dl> <dt>



The switch tells the line to alert the user.

**TAPI:** Service providers notify applications on each ring cycle by repeatedly sending [**LINE\_LINEDEVSTATE**](line-linedevstate.md) messages containing this constant. For example, in the United States, service providers send a message with this constant every six seconds.

**TSPI:** On a POTS device, the service provider can send the message whenever the central office sends ring voltage. On digital devices such as ISDN, the service provider may need to synthesize the repetition of the message if the switch generates only one ring request. Each repetition of the message should show the ring count increasing, so that toll save functions work properly.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_ROAMMODE"></span><span id="linedevstate_roammode"></span>**LINEDEVSTATE\_ROAMMODE**
</dt> <dd> <dl> <dt>



The roam mode of the line device has changed.


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_SIGNAL"></span><span id="linedevstate_signal"></span>**LINEDEVSTATE\_SIGNAL**
</dt> <dd> <dl> <dt>



The signal level has changed significantly (cellular).


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_TERMINALS"></span><span id="linedevstate_terminals"></span>**LINEDEVSTATE\_TERMINALS**
</dt> <dd> <dl> <dt>



The terminal settings have changed. This can happen, for example, if multiple line devices share terminals among them (for example, two lines sharing a phone terminal).


</dt> </dl> </dd> <dt>

<span id="LINEDEVSTATE_TRANSLATECHANGE"></span><span id="linedevstate_translatechange"></span>**LINEDEVSTATE\_TRANSLATECHANGE**
</dt> <dd> <dl> <dt>



Indicates that, due to configuration changes made by the user or other circumstances, one or more of the members in the [**LINETRANSLATECAPS**](/windows/desktop/api/Tapi/ns-tapi-linetranslatecaps) structure have changed. The application should use [**lineGetTranslateCaps**](/windows/desktop/api/Tapi/nf-tapi-linegettranslatecaps) to read the updated structure. If a service provider sends a [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message containing this value to TAPI, TAPI will pass it along to applications that have negotiated TAPI version 1.4 or later; applications negotiating a previous TAPI version will receive **LINE\_LINEDEVSTATE** messages specifying LINEDEVSTATE\_REINIT, requiring them to shut down and reinitialize their connection to TAPI to obtain the updated information.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_CLOSE**](line-close.md)
</dt> <dt>

[**LINE\_LINEDEVSTATE**](line-linedevstate.md)
</dt> <dt>

[**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps)
</dt> <dt>

[**lineGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetdevcaps)
</dt> <dt>

[**lineGetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig)
</dt> <dt>

[**lineGetTranslateCaps**](/windows/desktop/api/Tapi/nf-tapi-linegettranslatecaps)
</dt> <dt>

[**LINETRANSLATECAPS**](/windows/desktop/api/Tapi/ns-tapi-linetranslatecaps)
</dt> <dt>

[**lineUncompleteCall**](/windows/desktop/api/Tapi/nf-tapi-lineuncompletecall)
</dt> </dl>

 

 




