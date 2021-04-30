---
description: The LINECALLINFOSTATE\_ bit-flag constants describe various call information items about which an application can be notified in the LINE\_CALLINFO message.
ms.assetid: c216d9b7-8e2f-4604-ba93-1d9e1a5d23fc
title: LINECALLINFOSTATE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLINFOSTATE\_ Constants

The **LINECALLINFOSTATE\_** bit-flag constants describe various call information items about which an application can be notified in the [**LINE\_CALLINFO**](line-callinfo.md) message.

<dl> <dt>

<span id="LINECALLINFOSTATE_APPSPECIFIC"></span><span id="linecallinfostate_appspecific"></span>**LINECALLINFOSTATE\_APPSPECIFIC**
</dt> <dd> <dl> <dt>



The application-specific field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_BEARERMODE"></span><span id="linecallinfostate_bearermode"></span>**LINECALLINFOSTATE\_BEARERMODE**
</dt> <dd> <dl> <dt>



The bearer mode field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_CALLDATA"></span><span id="linecallinfostate_calldata"></span>**LINECALLINFOSTATE\_CALLDATA**
</dt> <dd> <dl> <dt>



The **CallData** member in [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) has been updated.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_CALLEDID"></span><span id="linecallinfostate_calledid"></span>**LINECALLINFOSTATE\_CALLEDID**
</dt> <dd> <dl> <dt>



One of the calledID-related fields of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_CALLERID"></span><span id="linecallinfostate_callerid"></span>**LINECALLINFOSTATE\_CALLERID**
</dt> <dd> <dl> <dt>



One of the callerID-related fields of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_CALLID"></span><span id="linecallinfostate_callid"></span>**LINECALLINFOSTATE\_CALLID**
</dt> <dd> <dl> <dt>



The call ID field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_CHARGINGINFO"></span><span id="linecallinfostate_charginginfo"></span>**LINECALLINFOSTATE\_CHARGINGINFO**
</dt> <dd> <dl> <dt>



The charging information of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_COMPLETIONID"></span><span id="linecallinfostate_completionid"></span>**LINECALLINFOSTATE\_COMPLETIONID**
</dt> <dd> <dl> <dt>



The completion identifier field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_CONNECTEDID"></span><span id="linecallinfostate_connectedid"></span>**LINECALLINFOSTATE\_CONNECTEDID**
</dt> <dd> <dl> <dt>



One of the connectedID-related fields of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_DEVSPECIFIC"></span><span id="linecallinfostate_devspecific"></span>**LINECALLINFOSTATE\_DEVSPECIFIC**
</dt> <dd> <dl> <dt>



The device-specific field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_DIALPARAMS"></span><span id="linecallinfostate_dialparams"></span>**LINECALLINFOSTATE\_DIALPARAMS**
</dt> <dd> <dl> <dt>



The dial parameters of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_DISPLAY"></span><span id="linecallinfostate_display"></span>**LINECALLINFOSTATE\_DISPLAY**
</dt> <dd> <dl> <dt>



The display field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_HIGHLEVELCOMP"></span><span id="linecallinfostate_highlevelcomp"></span>**LINECALLINFOSTATE\_HIGHLEVELCOMP**
</dt> <dd> <dl> <dt>



The high level compatibility field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_LOWLEVELCOMP"></span><span id="linecallinfostate_lowlevelcomp"></span>**LINECALLINFOSTATE\_LOWLEVELCOMP**
</dt> <dd> <dl> <dt>



The low level compatibility field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_MEDIAMODE"></span><span id="linecallinfostate_mediamode"></span>**LINECALLINFOSTATE\_MEDIAMODE**
</dt> <dd> <dl> <dt>



The media type field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_MONITORMODES"></span><span id="linecallinfostate_monitormodes"></span>**LINECALLINFOSTATE\_MONITORMODES**
</dt> <dd> <dl> <dt>



One or more of the digit, tone, or media monitoring fields in the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_NUMMONITORS"></span><span id="linecallinfostate_nummonitors"></span>**LINECALLINFOSTATE\_NUMMONITORS**
</dt> <dd> <dl> <dt>



The number of monitors field in the call-information record has changed.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_NUMOWNERDECR"></span><span id="linecallinfostate_numownerdecr"></span>**LINECALLINFOSTATE\_NUMOWNERDECR**
</dt> <dd> <dl> <dt>



The number of owner field in the call-information record was decreased.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_NUMOWNERINCR"></span><span id="linecallinfostate_numownerincr"></span>**LINECALLINFOSTATE\_NUMOWNERINCR**
</dt> <dd> <dl> <dt>



The number of owner field in the call-information record was increased.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_ORIGIN"></span><span id="linecallinfostate_origin"></span>**LINECALLINFOSTATE\_ORIGIN**
</dt> <dd> <dl> <dt>



The origin field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_OTHER"></span><span id="linecallinfostate_other"></span>**LINECALLINFOSTATE\_OTHER**
</dt> <dd> <dl> <dt>



Call information items other than those listed below have changed. The application should check the current call information to determine which items have changed.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_QOS"></span><span id="linecallinfostate_qos"></span>**LINECALLINFOSTATE\_QOS**
</dt> <dd> <dl> <dt>



One or more of the **QOS** members in [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) has been updated.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_RATE"></span><span id="linecallinfostate_rate"></span>**LINECALLINFOSTATE\_RATE**
</dt> <dd> <dl> <dt>



The rate field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_REASON"></span><span id="linecallinfostate_reason"></span>**LINECALLINFOSTATE\_REASON**
</dt> <dd> <dl> <dt>



The reason field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_REDIRECTINGID"></span><span id="linecallinfostate_redirectingid"></span>**LINECALLINFOSTATE\_REDIRECTINGID**
</dt> <dd> <dl> <dt>



The address identifier of the location that redirected a call.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_REDIRECTIONID"></span><span id="linecallinfostate_redirectionid"></span>**LINECALLINFOSTATE\_REDIRECTIONID**
</dt> <dd> <dl> <dt>



The address identifier of the location to which a call has been redirected.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_RELATEDCALLID"></span><span id="linecallinfostate_relatedcallid"></span>**LINECALLINFOSTATE\_RELATEDCALLID**
</dt> <dd> <dl> <dt>



The related call ID field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_TERMINAL"></span><span id="linecallinfostate_terminal"></span>**LINECALLINFOSTATE\_TERMINAL**
</dt> <dd> <dl> <dt>



The terminal mode information of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_TREATMENT"></span><span id="linecallinfostate_treatment"></span>**LINECALLINFOSTATE\_TREATMENT**
</dt> <dd> <dl> <dt>



The **CallTreatment** member in [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) has been updated. This can occur in response to a [**lineSetCallTreatment**](/windows/desktop/api/Tapi/nf-tapi-linesetcalltreatment) function, a call state change, a call "vector" or other script controlling the call, or upon completion of playback of a recorded message (ordinarily, indicating a change to "silence" or "music").


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_TRUNK"></span><span id="linecallinfostate_trunk"></span>**LINECALLINFOSTATE\_TRUNK**
</dt> <dd> <dl> <dt>



The trunk field of the call-information record.


</dt> </dl> </dd> <dt>

<span id="LINECALLINFOSTATE_USERUSERINFO"></span><span id="linecallinfostate_useruserinfo"></span>**LINECALLINFOSTATE\_USERUSERINFO**
</dt> <dd> <dl> <dt>



The user-user information of the call-information record.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

When changes occur in this data structure, a [**LINE\_CALLINFO**](line-callinfo.md) message is sent to the application. The parameters to this message are a handle to the call and an indication of the information item that has changed. The [**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps) data structure also indicates which of these call information elements are valid for every call on the address.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_CALLINFO**](line-callinfo.md)
</dt> <dt>

[**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps)
</dt> <dt>

[**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo)
</dt> <dt>

[**lineSetCallTreatment**](/windows/desktop/api/Tapi/nf-tapi-linesetcalltreatment)
</dt> </dl>

 

 




