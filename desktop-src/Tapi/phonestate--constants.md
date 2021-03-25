---
description: The PHONESTATE\_ bit-flag constants describe various status items for a phone device.
ms.assetid: 5db53dd4-606a-40b9-9159-b67a0ea1e400
title: PHONESTATE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONESTATE\_ Constants

The **PHONESTATE\_** bit-flag constants describe various status items for a phone device.

<dl> <dt>

<span id="PHONESTATE_CAPSCHANGE"></span><span id="phonestate_capschange"></span>**PHONESTATE\_CAPSCHANGE**
</dt> <dd> <dl> <dt>



Indicates that, due to configuration changes made by the user or other circumstances, one or more of the members in the [**PHONECAPS**](/windows/desktop/api/Tapi/ns-tapi-phonecaps) structure have changed. The application should use [**phoneGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps) to read the updated structure. If a service provider sends a [**PHONE\_STATE**](phone-state.md) message containing this value to TAPI, TAPI will pass it along to applications that have negotiated TAPI version 1.4 or later; applications negotiating a previous API version will receive PHONE\_STATE messages specifying PHONESTATE\_REINIT, requiring them to shut down and reinitialize their connection to TAPI to obtain the updated information.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_CONNECTED"></span><span id="phonestate_connected"></span>**PHONESTATE\_CONNECTED**
</dt> <dd> <dl> <dt>



The connection between the phone device and TAPI was just made. This happens when TAPI is first invoked or when the wire connecting the phone to the PC is plugged in with TAPI active.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_DEVSPECIFIC"></span><span id="phonestate_devspecific"></span>**PHONESTATE\_DEVSPECIFIC**
</dt> <dd> <dl> <dt>



The phone's device-specific information has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_DISCONNECTED"></span><span id="phonestate_disconnected"></span>**PHONESTATE\_DISCONNECTED**
</dt> <dd> <dl> <dt>



The connection between the phone device and TAPI was just broken. This happens when the wire connecting the phone set to the PC is unplugged while TAPI is active.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_DISPLAY"></span><span id="phonestate_display"></span>**PHONESTATE\_DISPLAY**
</dt> <dd> <dl> <dt>



The display of the phone has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_HANDSETGAIN"></span><span id="phonestate_handsetgain"></span>**PHONESTATE\_HANDSETGAIN**
</dt> <dd> <dl> <dt>



The handset's microphone gain setting has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_HANDSETHOOKSWITCH"></span><span id="phonestate_handsethookswitch"></span>**PHONESTATE\_HANDSETHOOKSWITCH**
</dt> <dd> <dl> <dt>



The handset hookswitch state has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_HANDSETVOLUME"></span><span id="phonestate_handsetvolume"></span>**PHONESTATE\_HANDSETVOLUME**
</dt> <dd> <dl> <dt>



The handset's speaker volume setting has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_HEADSETHOOKSWITCH"></span><span id="phonestate_headsethookswitch"></span>**PHONESTATE\_HEADSETHOOKSWITCH**
</dt> <dd> <dl> <dt>



The headset's hookswitch state has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_HEADSETGAIN"></span><span id="phonestate_headsetgain"></span>**PHONESTATE\_HEADSETGAIN**
</dt> <dd> <dl> <dt>



The headset's microphone gain setting has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_HEADSETVOLUME"></span><span id="phonestate_headsetvolume"></span>**PHONESTATE\_HEADSETVOLUME**
</dt> <dd> <dl> <dt>



The headset's speaker volume setting has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_LAMP"></span><span id="phonestate_lamp"></span>**PHONESTATE\_LAMP**
</dt> <dd> <dl> <dt>



A lamp of the phone has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_MONITORS"></span><span id="phonestate_monitors"></span>**PHONESTATE\_MONITORS**
</dt> <dd> <dl> <dt>



The number of monitors for the phone device.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_OTHER"></span><span id="phonestate_other"></span>**PHONESTATE\_OTHER**
</dt> <dd> <dl> <dt>



Phone-status items other than those listed below have changed. The application should check the current phone status to determine which items have changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_OWNER"></span><span id="phonestate_owner"></span>**PHONESTATE\_OWNER**
</dt> <dd> <dl> <dt>



The number of owners for the phone device.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_REINIT"></span><span id="phonestate_reinit"></span>**PHONESTATE\_REINIT**
</dt> <dd> <dl> <dt>



Items have changed in the configuration of phone devices. To become aware of these changes (as for the appearance of new phone devices), the application should reinitialize its use of TAPI.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_REMOVED"></span><span id="phonestate_removed"></span>**PHONESTATE\_REMOVED**
</dt> <dd> <dl> <dt>



Indicates that the device is being removed from the system by the service provider (most likely through user action, through a control panel or similar utility). A [**PHONE\_STATE**](phone-state.md) message with this value will normally be immediately followed by a [**PHONE\_CLOSE**](phone-close.md) message on the device. Subsequent attempts to access the device prior to TAPI being reinitialized will result in PHONEERR\_NODEVICE being returned to the application. If a service provider sends a PHONE\_STATE message containing this value to TAPI, TAPI will pass it along to applications that have negotiated TAPI version 1.4 or later; applications negotiating a previous API version will not receive any notification.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_RESUME"></span><span id="phonestate_resume"></span>**PHONESTATE\_RESUME**
</dt> <dd> <dl> <dt>



The application's use of the phone device is resumed after having been suspended for some time.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_RINGMODE"></span><span id="phonestate_ringmode"></span>**PHONESTATE\_RINGMODE**
</dt> <dd> <dl> <dt>



The ring mode of the phone has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_RINGVOLUME"></span><span id="phonestate_ringvolume"></span>**PHONESTATE\_RINGVOLUME**
</dt> <dd> <dl> <dt>



The ring volume of the phone has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_SPEAKERHOOKSWITCH"></span><span id="phonestate_speakerhookswitch"></span>**PHONESTATE\_SPEAKERHOOKSWITCH**
</dt> <dd> <dl> <dt>



The speakerphone's hookswitch state has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_SPEAKERGAIN"></span><span id="phonestate_speakergain"></span>**PHONESTATE\_SPEAKERGAIN**
</dt> <dd> <dl> <dt>



The speakerphone's microphone gain setting state has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_SPEAKERVOLUME"></span><span id="phonestate_speakervolume"></span>**PHONESTATE\_SPEAKERVOLUME**
</dt> <dd> <dl> <dt>



The speakerphone's speaker volume setting has changed.


</dt> </dl> </dd> <dt>

<span id="PHONESTATE_SUSPEND"></span><span id="phonestate_suspend"></span>**PHONESTATE\_SUSPEND**
</dt> <dd> <dl> <dt>



The application's use of the phone is temporarily suspended.


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

[**PHONE\_CLOSE**](phone-close.md)
</dt> <dt>

[**PHONE\_STATE**](phone-state.md)
</dt> <dt>

[**PHONECAPS**](/windows/desktop/api/Tapi/ns-tapi-phonecaps)
</dt> <dt>

[**phoneGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps)
</dt> </dl>

 

 




