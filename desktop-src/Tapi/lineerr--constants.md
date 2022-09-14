---
description: The following is a list of error codes that TAPI can return when invoking operations on lines, addresses, or calls.
ms.assetid: bdaf60d1-6ff2-4bd6-b246-8556d6cae644
title: LINEERR_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEERR\_ Constants

The following is a list of error codes that TAPI can return when invoking operations on lines, addresses, or calls. For more information about how to determine which of these error codes a particular function can return, see the individual function descriptions.

<dl> <dt>

<span id="LINEERR_ADDRESSBLOCKED"></span><span id="lineerr_addressblocked"></span>**LINEERR\_ADDRESSBLOCKED**
</dt> <dd> <dl> <dt>



The specified address is blocked from being dialed on the specified call.


</dt> </dl> </dd> <dt>

<span id="LINEERR_ADDRESSBLOCKED"></span><span id="lineerr_addressblocked"></span>**LINEERR\_ADDRESSBLOCKED**
</dt> <dd> <dl> <dt>



The target call address has call blocking enabled.


</dt> </dl> </dd> <dt>

<span id="LINEERR_ALLOCATED"></span><span id="lineerr_allocated"></span>**LINEERR\_ALLOCATED**
</dt> <dd> <dl> <dt>



The line cannot be opened due to a persistent condition, such as that of a serial port being exclusively opened by another process.


</dt> </dl> </dd> <dt>

<span id="LINEERR_BADDEVICEID"></span><span id="lineerr_baddeviceid"></span>**LINEERR\_BADDEVICEID**
</dt> <dd> <dl> <dt>



The specified device identifier or line device identifier, such as in a *dwDeviceID* parameter, is invalid or out of range.


</dt> </dl> </dd> <dt>

<span id="LINEERR_BEARERMODEUNAVAIL"></span><span id="lineerr_bearermodeunavail"></span>**LINEERR\_BEARERMODEUNAVAIL**
</dt> <dd> <dl> <dt>



The bearer mode member in [**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams) is invalid, the bearer mode specified in **LINECALLPARAMS** is not available, or the call bearer mode cannot be changed to the specified bearer mode.


</dt> </dl> </dd> <dt>

<span id="LINEERR_BILLINGREJECTED"></span><span id="lineerr_billingrejected"></span>**LINEERR\_BILLINGREJECTED**
</dt> <dd> <dl> <dt>



The billing mode of the call was rejected.


</dt> </dl> </dd> <dt>

<span id="LINEERR_CALLUNAVAIL"></span><span id="lineerr_callunavail"></span>**LINEERR\_CALLUNAVAIL**
</dt> <dd> <dl> <dt>



All call appearances on the specified address are currently in use.


</dt> </dl> </dd> <dt>

<span id="LINEERR_COMPLETIONOVERRUN"></span><span id="lineerr_completionoverrun"></span>**LINEERR\_COMPLETIONOVERRUN**
</dt> <dd> <dl> <dt>



The maximum number of outstanding call completions has been exceeded.


</dt> </dl> </dd> <dt>

<span id="LINEERR_CONFERENCEFULL"></span><span id="lineerr_conferencefull"></span>**LINEERR\_CONFERENCEFULL**
</dt> <dd> <dl> <dt>



The maximum number of parties for a conference has been reached, or the requested number of parties cannot be satisfied.


</dt> </dl> </dd> <dt>

<span id="LINEERR_DIALBILLING"></span><span id="lineerr_dialbilling"></span>**LINEERR\_DIALBILLING**
</dt> <dd> <dl> <dt>



The dialable address parameter contains dialing control characters not processed by the service provider.


</dt> </dl> </dd> <dt>

<span id="LINEERR_DIALDIALTONE"></span><span id="lineerr_dialdialtone"></span>**LINEERR\_DIALDIALTONE**
</dt> <dd> <dl> <dt>



The dialable address parameter contains dialing control characters not processed by the service provider.


</dt> </dl> </dd> <dt>

<span id="LINEERR_DIALPROMPT"></span><span id="lineerr_dialprompt"></span>**LINEERR\_DIALPROMPT**
</dt> <dd> <dl> <dt>



The dialable address parameter contains dialing control characters not processed by the service provider.


</dt> </dl> </dd> <dt>

<span id="LINEERR_DIALQUIET"></span><span id="lineerr_dialquiet"></span>**LINEERR\_DIALQUIET**
</dt> <dd> <dl> <dt>



The dialable address parameter contains dialing control characters not processed by the service provider.


</dt> </dl> </dd> <dt>

<span id="LINEERR_DIALVOICEDETECT"></span><span id="lineerr_dialvoicedetect"></span>**LINEERR\_DIALVOICEDETECT**
</dt> <dd> <dl> <dt>



Use of the dial modifier (:) is not supported. This value is exposed only to applications that negotiate a TAPI version of 2.0 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_DISCONNECTED"></span><span id="lineerr_disconnected"></span>**LINEERR\_DISCONNECTED**
</dt> <dd> <dl> <dt>



The call has been disconnected. This value is exposed only to applications that negotiate a TAPI version of 2.2 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INCOMPATIBLEAPIVERSION"></span><span id="lineerr_incompatibleapiversion"></span>**LINEERR\_INCOMPATIBLEAPIVERSION**
</dt> <dd> <dl> <dt>



The application requested a TAPI version or version range that is either incompatible with, or cannot be supported by, the Telephony API implementation and the corresponding service provider.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INCOMPATIBLEEXTVERSION"></span><span id="lineerr_incompatibleextversion"></span>**LINEERR\_INCOMPATIBLEEXTVERSION**
</dt> <dd> <dl> <dt>



The application requested an extension version range that is either invalid or cannot be supported by the corresponding service provider.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INIFILECORRUPT"></span><span id="lineerr_inifilecorrupt"></span>**LINEERR\_INIFILECORRUPT**
</dt> <dd> <dl> <dt>



The Telephon.ini file cannot be read or understood properly by TAPI because of internal inconsistencies or formatting problems. For example, the \[Locations\], \[Cards\], or \[Countries\] section of the Telephon.ini file may be corrupted or inconsistent.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INUSE"></span><span id="lineerr_inuse"></span>**LINEERR\_INUSE**
</dt> <dd> <dl> <dt>



The line device is in use and cannot currently be configured, allow a party to be added, allow a call to be answered, allow a call to be placed, or allow a call to be transferred.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALADDRESS"></span><span id="lineerr_invaladdress"></span>**LINEERR\_INVALADDRESS**
</dt> <dd> <dl> <dt>



A specified address is either invalid or not allowed. If invalid, the address contains invalid characters or digits, or the destination address contains dialing control characters (W, @, $, or ?) that are not supported by the service provider. If not allowed, the specified address is either not assigned to the specified line or is not valid for address redirection.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALADDRESSID"></span><span id="lineerr_invaladdressid"></span>**LINEERR\_INVALADDRESSID**
</dt> <dd> <dl> <dt>



The specified address identifier is either invalid or out of range.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALADDRESSMODE"></span><span id="lineerr_invaladdressmode"></span>**LINEERR\_INVALADDRESSMODE**
</dt> <dd> <dl> <dt>



The specified address mode is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALADDRESSSTATE"></span><span id="lineerr_invaladdressstate"></span>**LINEERR\_INVALADDRESSSTATE**
</dt> <dd> <dl> <dt>



The specified address state contains one or more bits that are not [**LINEADDRESSSTATE\_ constants**](lineaddressstate--constants.md).


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALADDRESSTYPE"></span><span id="lineerr_invaladdresstype"></span>**LINEERR\_INVALADDRESSTYPE**
</dt> <dd> <dl> <dt>



The application referenced an address type that is not valid. This value is exposed only to applications that negotiate a TAPI version of 3.0 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAGENTACTIVITY"></span><span id="lineerr_invalagentactivity"></span>**LINEERR\_INVALAGENTACTIVITY**
</dt> <dd> <dl> <dt>



The specified agent activity is not valid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAGENTACTIVITY"></span><span id="lineerr_invalagentactivity"></span>**LINEERR\_INVALAGENTACTIVITY**
</dt> <dd> <dl> <dt>



The application invoking this operation is the target of the indirect handoff. That is, TAPI has determined that the calling application is also the highest priority application for the given media type. This value is exposed only to applications that negotiate a TAPI version of 2.0 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAGENTGROUP"></span><span id="lineerr_invalagentgroup"></span>**LINEERR\_INVALAGENTGROUP**
</dt> <dd> <dl> <dt>



The specified agent group information is not valid or contains errors. The requested action has not been performed.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAGENTGROUP"></span><span id="lineerr_invalagentgroup"></span>**LINEERR\_INVALAGENTGROUP**
</dt> <dd> <dl> <dt>



The application referenced an agent group that is not valid. This value is exposed only to applications that negotiate a TAPI version of 2.0 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAGENTID"></span><span id="lineerr_invalagentid"></span>**LINEERR\_INVALAGENTID**
</dt> <dd> <dl> <dt>



The specified agent identifier is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAGENTID"></span><span id="lineerr_invalagentid"></span>**LINEERR\_INVALAGENTID**
</dt> <dd> <dl> <dt>



An invalid agent identifier was used. This value is exposed only to applications that negotiate a TAPI version of 2.0 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAGENTSESSIONSTATE"></span><span id="lineerr_invalagentsessionstate"></span>**LINEERR\_INVALAGENTSESSIONSTATE**
</dt> <dd> <dl> <dt>



The agent session state is invalid. This value is exposed only to applications that negotiate a TAPI version of 2.2 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAGENTSTATE"></span><span id="lineerr_invalagentstate"></span>**LINEERR\_INVALAGENTSTATE**
</dt> <dd> <dl> <dt>



The specified agent state is not valid or contains errors. No changes have been made to the agent state of the specified address.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAGENTSTATE"></span><span id="lineerr_invalagentstate"></span>**LINEERR\_INVALAGENTSTATE**
</dt> <dd> <dl> <dt>



The application referenced an agent state that is not valid. This value is exposed only to applications that negotiate a TAPI version of 2.0 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAPPHANDLE"></span><span id="lineerr_invalapphandle"></span>**LINEERR\_INVALAPPHANDLE**
</dt> <dd> <dl> <dt>



The application handle (such as specified by a *hLineApp* parameter) or the application registration handle is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALAPPNAME"></span><span id="lineerr_invalappname"></span>**LINEERR\_INVALAPPNAME**
</dt> <dd> <dl> <dt>



The specified application name is invalid. If an application name is specified by the application, it is assumed that the string does not contain any non-displayable characters, and is zero-terminated.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALBEARERMODE"></span><span id="lineerr_invalbearermode"></span>**LINEERR\_INVALBEARERMODE**
</dt> <dd> <dl> <dt>



The specified bearer mode is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCALLCOMPLMODE"></span><span id="lineerr_invalcallcomplmode"></span>**LINEERR\_INVALCALLCOMPLMODE**
</dt> <dd> <dl> <dt>



The specified completion is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCALLHANDLE"></span><span id="lineerr_invalcallhandle"></span>**LINEERR\_INVALCALLHANDLE**
</dt> <dd> <dl> <dt>



The specified call handle is not valid. For example, the handle is not **NULL** but does not belong to the given line. In some cases, the specified call device handle is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCALLPARAMS"></span><span id="lineerr_invalcallparams"></span>**LINEERR\_INVALCALLPARAMS**
</dt> <dd> <dl> <dt>



The specified call parameters are invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCALLPRIVILEGE"></span><span id="lineerr_invalcallprivilege"></span>**LINEERR\_INVALCALLPRIVILEGE**
</dt> <dd> <dl> <dt>



The specified call privilege parameter is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCALLSELECT"></span><span id="lineerr_invalcallselect"></span>**LINEERR\_INVALCALLSELECT**
</dt> <dd> <dl> <dt>



The specified select parameter is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCALLSTATE"></span><span id="lineerr_invalcallstate"></span>**LINEERR\_INVALCALLSTATE**
</dt> <dd> <dl> <dt>



The current state of a call is not in a valid state for the requested operation.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCALLSTATELIST"></span><span id="lineerr_invalcallstatelist"></span>**LINEERR\_INVALCALLSTATELIST**
</dt> <dd> <dl> <dt>



The specified call state list is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCARD"></span><span id="lineerr_invalcard"></span>**LINEERR\_INVALCARD**
</dt> <dd> <dl> <dt>



The permanent card identifier specified in *dwCard* could not be found in any entry in the \[Cards\] section in the registry.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCOMPLETIONID"></span><span id="lineerr_invalcompletionid"></span>**LINEERR\_INVALCOMPLETIONID**
</dt> <dd> <dl> <dt>



The completion identifier is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCONFCALLHANDLE"></span><span id="lineerr_invalconfcallhandle"></span>**LINEERR\_INVALCONFCALLHANDLE**
</dt> <dd> <dl> <dt>



The specified call handle for the conference call is invalid or is not a handle for a conference call.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCONSULTCALLHANDLE"></span><span id="lineerr_invalconsultcallhandle"></span>**LINEERR\_INVALCONSULTCALLHANDLE**
</dt> <dd> <dl> <dt>



The specified consultation call handle is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALCOUNTRYCODE"></span><span id="lineerr_invalcountrycode"></span>**LINEERR\_INVALCOUNTRYCODE**
</dt> <dd> <dl> <dt>



The specified country or region code is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALDEVICECLASS"></span><span id="lineerr_invaldeviceclass"></span>**LINEERR\_INVALDEVICECLASS**
</dt> <dd> <dl> <dt>



The line device has no associated device for the given device class, or the specified line does not support the indicated device class.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALDEVICEHANDLE"></span><span id="lineerr_invaldevicehandle"></span>**LINEERR\_INVALDEVICEHANDLE**
</dt> <dd> <dl> <dt>



The line device handle is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALDIALPARAMS"></span><span id="lineerr_invaldialparams"></span>**LINEERR\_INVALDIALPARAMS**
</dt> <dd> <dl> <dt>



The dialing parameters are invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALDIGITLIST"></span><span id="lineerr_invaldigitlist"></span>**LINEERR\_INVALDIGITLIST**
</dt> <dd> <dl> <dt>



The specified digit list is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALDIGITMODE"></span><span id="lineerr_invaldigitmode"></span>**LINEERR\_INVALDIGITMODE**
</dt> <dd> <dl> <dt>



The specified digit mode is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALDIGITS"></span><span id="lineerr_invaldigits"></span>**LINEERR\_INVALDIGITS**
</dt> <dd> <dl> <dt>



The specified termination digits are not valid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALEXTVERSION"></span><span id="lineerr_invalextversion"></span>**LINEERR\_INVALEXTVERSION**
</dt> <dd> <dl> <dt>



The service provider extension version number is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALFEATURE"></span><span id="lineerr_invalfeature"></span>**LINEERR\_INVALFEATURE**
</dt> <dd> <dl> <dt>



The *dwFeature* parameter is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALFEATURE"></span><span id="lineerr_invalfeature"></span>**LINEERR\_INVALFEATURE**
</dt> <dd> <dl> <dt>



The application invoked a feature that is not available on this line.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALGROUPID"></span><span id="lineerr_invalgroupid"></span>**LINEERR\_INVALGROUPID**
</dt> <dd> <dl> <dt>



The specified group identifier is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALLINEHANDLE"></span><span id="lineerr_invallinehandle"></span>**LINEERR\_INVALLINEHANDLE**
</dt> <dd> <dl> <dt>



The specified call, device, line device, or line handle is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALLINESTATE"></span><span id="lineerr_invallinestate"></span>**LINEERR\_INVALLINESTATE**
</dt> <dd> <dl> <dt>



The device configuration may not be changed in the current line state. The line may be in use by another application or a *dwLineStates* parameter contains one or more bits that are not [LINEDEVSTATE\_ constants](linedevstate--constants.md). The **LINEERR\_INVALLINESTATE** value can also indicate that the device is disconnected or out of service. These states are indicated by setting the bits corresponding to the *LINEDEVSTATUSFLAGS\_CONNECTED* and *LINEDEVSTATUSFLAGS\_INSERVICE* values to 0 in the **dwDevStatusFlags** member of the [**LINEDEVSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linedevstatus) structure returned by the [**lineGetLineDevStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetlinedevstatus) function.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALLOCATION"></span><span id="lineerr_invallocation"></span>**LINEERR\_INVALLOCATION**
</dt> <dd> <dl> <dt>



The permanent location identifier specified in *dwLocation* could not be found in any entry in the \[Locations\] section in the registry.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALMEDIALIST"></span><span id="lineerr_invalmedialist"></span>**LINEERR\_INVALMEDIALIST**
</dt> <dd> <dl> <dt>



The specified media list is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALMEDIAMODE"></span><span id="lineerr_invalmediamode"></span>**LINEERR\_INVALMEDIAMODE**
</dt> <dd> <dl> <dt>



The list of media types (modes) to be monitored contains invalid information, the specified media type parameter is invalid, or the service provider does not support the specified media type. The media types supported on the line are listed in the **dwMediaModes** member in the [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps) structure.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALMESSAGEID"></span><span id="lineerr_invalmessageid"></span>**LINEERR\_INVALMESSAGEID**
</dt> <dd> <dl> <dt>



The number given in *dwMessageID* is outside the range specified by the **dwNumCompletionMessages** member in the [**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps) structure.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALPARAM"></span><span id="lineerr_invalparam"></span>**LINEERR\_INVALPARAM**
</dt> <dd> <dl> <dt>



A parameter or structure that a parameter points to contains invalid information, a country or region code is invalid, a window handle is invalid, or the specified forward list parameter contains invalid information.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALPARKID"></span><span id="lineerr_invalparkid"></span>**LINEERR\_INVALPARKID**
</dt> <dd> <dl> <dt>



The park identifier is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALPARKMODE"></span><span id="lineerr_invalparkmode"></span>**LINEERR\_INVALPARKMODE**
</dt> <dd> <dl> <dt>



The specified park mode is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALPASSWORD"></span><span id="lineerr_invalpassword"></span>**LINEERR\_INVALPASSWORD**
</dt> <dd> <dl> <dt>



The specified password is not correct and the requested action has not been carried out.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALPASSWORD"></span><span id="lineerr_invalpassword"></span>**LINEERR\_INVALPASSWORD**
</dt> <dd> <dl> <dt>



The application used an invalid password. This value is exposed only to applications that negotiate a TAPI version of 2.0 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALPOINTER"></span><span id="lineerr_invalpointer"></span>**LINEERR\_INVALPOINTER**
</dt> <dd> <dl> <dt>



One or more of the specified pointer parameters (such as *lpCallList*, *lpdwAPIVersion*, *lpExtensionID*, *lpdwExtVersion*, *lphIcon*, *lpLineDevCaps*, and *lpToneList*) are invalid, or a required pointer to an output parameter is **NULL**.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALPRIVSELECT"></span><span id="lineerr_invalprivselect"></span>**LINEERR\_INVALPRIVSELECT**
</dt> <dd> <dl> <dt>



An invalid flag or combination of flags was set for the *dwPrivileges* parameter.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALRATE"></span><span id="lineerr_invalrate"></span>**LINEERR\_INVALRATE**
</dt> <dd> <dl> <dt>



The specified rate is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALREQUESTMODE"></span><span id="lineerr_invalrequestmode"></span>**LINEERR\_INVALREQUESTMODE**
</dt> <dd> <dl> <dt>



The [**LINEREQUESTMODE**](linerequestmode--constants.md) indicator is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALTERMINALID"></span><span id="lineerr_invalterminalid"></span>**LINEERR\_INVALTERMINALID**
</dt> <dd> <dl> <dt>



The specified terminal identifier is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALTERMINALMODE"></span><span id="lineerr_invalterminalmode"></span>**LINEERR\_INVALTERMINALMODE**
</dt> <dd> <dl> <dt>



The specified terminal modes parameter is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALTIMEOUT"></span><span id="lineerr_invaltimeout"></span>**LINEERR\_INVALTIMEOUT**
</dt> <dd> <dl> <dt>



Timeouts are not supported or a value falls outside the valid range specified in [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps).


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALTONE"></span><span id="lineerr_invaltone"></span>**LINEERR\_INVALTONE**
</dt> <dd> <dl> <dt>



The specified custom tone does not represent a valid tone or is made up of too many frequencies or the specified tone structure does not describe a valid tone.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALTONELIST"></span><span id="lineerr_invaltonelist"></span>**LINEERR\_INVALTONELIST**
</dt> <dd> <dl> <dt>



The specified tone list is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALTONEMODE"></span><span id="lineerr_invaltonemode"></span>**LINEERR\_INVALTONEMODE**
</dt> <dd> <dl> <dt>



The specified tone mode parameter is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_INVALTRANSFERMODE"></span><span id="lineerr_invaltransfermode"></span>**LINEERR\_INVALTRANSFERMODE**
</dt> <dd> <dl> <dt>



The specified transfer mode parameter is invalid.


</dt> </dl> </dd> <dt>

<span id="LINEERR_LINEMAPPERFAILED"></span><span id="lineerr_linemapperfailed"></span>**LINEERR\_LINEMAPPERFAILED**
</dt> <dd> <dl> <dt>



LINEMAPPER was the value passed in the *dwDeviceID* parameter, but no lines were found that match the requirements specified in the *lpCallParams* parameter.


</dt> </dl> </dd> <dt>

<span id="LINEERR_NOCONFERENCE"></span><span id="lineerr_noconference"></span>**LINEERR\_NOCONFERENCE**
</dt> <dd> <dl> <dt>



The specified call is not a conference call handle or a participant call.


</dt> </dl> </dd> <dt>

<span id="LINEERR_NODEVICE"></span><span id="lineerr_nodevice"></span>**LINEERR\_NODEVICE**
</dt> <dd> <dl> <dt>



The specified device identifier, which was previously valid, is no longer accepted because the associated device has been removed from the system since TAPI was last initialized. Alternately, the line device has no associated device for the given device class.


</dt> </dl> </dd> <dt>

<span id="LINEERR_NODRIVER"></span><span id="lineerr_nodriver"></span>**LINEERR\_NODRIVER**
</dt> <dd> <dl> <dt>



Either Tapiaddr.dll could not be located or the telephone service provider for the specified device found that one of its components is missing or corrupt in a way that was not detected at initialization time. The user should be advised to use the Telephony Control Panel to correct the problem.


</dt> </dl> </dd> <dt>

<span id="LINEERR_NOMEM"></span><span id="lineerr_nomem"></span>**LINEERR\_NOMEM**
</dt> <dd> <dl> <dt>



Insufficient memory to perform the operation, or unable to lock memory.


</dt> </dl> </dd> <dt>

<span id="LINEERR_NOMULTIPLEINSTANCE"></span><span id="lineerr_nomultipleinstance"></span>**LINEERR\_NOMULTIPLEINSTANCE**
</dt> <dd> <dl> <dt>



A telephony service provider that does not support multiple instances is listed more than once in the \[Providers\] section in the registry. The application should advise the user to use the Telephony Control Panel to remove the duplicated driver.


</dt> </dl> </dd> <dt>

<span id="LINEERR_NOMULTIPLEINSTANCE"></span><span id="lineerr_nomultipleinstance"></span>**LINEERR\_NOMULTIPLEINSTANCE**
</dt> <dd> <dl> <dt>



Multiple instances of this service provider are not allowed.


</dt> </dl> </dd> <dt>

<span id="LINEERR_NOREQUEST"></span><span id="lineerr_norequest"></span>**LINEERR\_NOREQUEST**
</dt> <dd> <dl> <dt>



There currently is no request pending of the indicated mode, or the application is no longer the highest-priority application for the specified request mode.


</dt> </dl> </dd> <dt>

<span id="LINEERR_NOTOWNER"></span><span id="lineerr_notowner"></span>**LINEERR\_NOTOWNER**
</dt> <dd> <dl> <dt>



The application does not have owner privilege to the specified call.


</dt> </dl> </dd> <dt>

<span id="LINEERR_NOTREGISTERED"></span><span id="lineerr_notregistered"></span>**LINEERR\_NOTREGISTERED**
</dt> <dd> <dl> <dt>



The application is not registered as a request recipient for the indicated request mode.


</dt> </dl> </dd> <dt>

<span id="LINEERR_OPERATIONFAILED"></span><span id="lineerr_operationfailed"></span>**LINEERR\_OPERATIONFAILED**
</dt> <dd> <dl> <dt>



The operation failed for an unspecified or unknown reason.


</dt> </dl> </dd> <dt>

<span id="LINEERR_OPERATIONUNAVAIL"></span><span id="lineerr_operationunavail"></span>**LINEERR\_OPERATIONUNAVAIL**
</dt> <dd> <dl> <dt>



The operation is not available, such as for the given device or specified line.


</dt> </dl> </dd> <dt>

<span id="LINEERR_RATEUNAVAIL"></span><span id="lineerr_rateunavail"></span>**LINEERR\_RATEUNAVAIL**
</dt> <dd> <dl> <dt>



The service provider currently does not have enough bandwidth available for the specified rate.


</dt> </dl> </dd> <dt>

<span id="LINEERR_REINIT"></span><span id="lineerr_reinit"></span>**LINEERR\_REINIT**
</dt> <dd> <dl> <dt>



If TAPI reinitialization has been requested, for example as a result of adding or removing a telephony service provider, then [**lineInitialize**](/windows/desktop/api/Tapi/nf-tapi-lineinitialize), [**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa), or [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen) requests are rejected with this error until the last application shuts down its usage of the API (using [**lineShutdown**](/windows/desktop/api/Tapi/nf-tapi-lineshutdown)), at which time the new configuration becomes effective and applications are once again permitted to call **lineInitialize** or **lineInitializeEx**.


</dt> </dl> </dd> <dt>

<span id="LINEERR_REINIT"></span><span id="lineerr_reinit"></span>**LINEERR\_REINIT**
</dt> <dd> <dl> <dt>



The application attempted to initialize TAPI twice.


</dt> </dl> </dd> <dt>

<span id="LINEERR_REQUESTOVERRUN"></span><span id="lineerr_requestoverrun"></span>**LINEERR\_REQUESTOVERRUN**
</dt> <dd> <dl> <dt>



More requests are pending than the device can handle.


</dt> </dl> </dd> <dt>

<span id="LINEERR_RESOURCEUNAVAIL"></span><span id="lineerr_resourceunavail"></span>**LINEERR\_RESOURCEUNAVAIL**
</dt> <dd> <dl> <dt>



Insufficient resources to complete the operation. For example, a line cannot be opened due to a dynamic resource overcommitment.


</dt> </dl> </dd> <dt>

<span id="LINEERR_STRUCTURETOOSMALL"></span><span id="lineerr_structuretoosmall"></span>**LINEERR\_STRUCTURETOOSMALL**
</dt> <dd> <dl> <dt>



The **dwTotalSize** member of a structure does not specify enough memory to contain the fixed portion of the specified structure.


</dt> </dl> </dd> <dt>

<span id="LINEERR_TARGETNOTFOUND"></span><span id="lineerr_targetnotfound"></span>**LINEERR\_TARGETNOTFOUND**
</dt> <dd> <dl> <dt>



A target for the call handoff was not found. This can occur if the named application did not open the same line with the LINECALLPRIVILEGE\_OWNER bit in the *dwPrivileges* parameter of [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen). Or, in the case of media-mode handoff, no application has opened the same line with the LINECALLPRIVILEGE\_OWNER bit in the *dwPrivileges* parameter of [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen) and with the media type specified in the *dwMediaMode* parameter having been specified in the *dwMediaModes* parameter of [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen).


</dt> </dl> </dd> <dt>

<span id="LINEERR_TARGETSELF"></span><span id="lineerr_targetself"></span>**LINEERR\_TARGETSELF**
</dt> <dd> <dl> <dt>



The application invoking this operation is the target of the indirect handoff. That is, TAPI has determined that the calling application is also the highest priority application for the given media type.


</dt> </dl> </dd> <dt>

<span id="LINEERR_UNINITIALIZED"></span><span id="lineerr_uninitialized"></span>**LINEERR\_UNINITIALIZED**
</dt> <dd> <dl> <dt>



The operation was invoked before any application called [**lineInitialize**](/windows/desktop/api/Tapi/nf-tapi-lineinitialize) or [**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa).


</dt> </dl> </dd> <dt>

<span id="LINEERR_USERCANCELLED"></span><span id="lineerr_usercancelled"></span>**LINEERR\_USERCANCELLED**
</dt> <dd> <dl> <dt>



The user cancelled the call. This value is exposed only to applications that negotiate a TAPI version of 2.2 or later.


</dt> </dl> </dd> <dt>

<span id="LINEERR_USERUSERINFOTOOBIG"></span><span id="lineerr_useruserinfotoobig"></span>**LINEERR\_USERUSERINFOTOOBIG**
</dt> <dd> <dl> <dt>



The string containing user-user information exceeds the maximum number of bytes specified in the **dwUUIAcceptSize**, **dwUUIAnswerSize**, **dwUUIDropSize**, **dwUUIMakeCallSize**, or **dwUUISendUserUserInfoSize** member of [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps), or the string containing user-user information is too long.


</dt> </dl> </dd> </dl>

## Remarks

The values 0xC0000000 through 0xFFFFFFFF are available for device-specific extensions. The values 0x80000000 through 0xBFFFFFFF are reserved, while 0x00000000 through 0x7FFFFFFF are used as request identifiers.

If an application gets an error return that it does not specifically handle (such as an error defined by a device-specific extension), it should treat the error as a LINEERR\_OPERATIONFAILED (for an unspecified reason).

When invoking the LINEERR\_constants which are new with TAPI 3.0, the Tapierr.mc file must be updated with new messages.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps)
</dt> <dt>

[**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps)
</dt> <dt>

[**LINEDEVSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linedevstatus)
</dt> <dt>

[**lineGetLineDevStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetlinedevstatus)
</dt> <dt>

[**lineInitialize**](/windows/desktop/api/Tapi/nf-tapi-lineinitialize)
</dt> <dt>

[**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa)
</dt> <dt>

[**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen)
</dt> <dt>

[**lineShutdown**](/windows/desktop/api/Tapi/nf-tapi-lineshutdown)
</dt> </dl>

 

 




