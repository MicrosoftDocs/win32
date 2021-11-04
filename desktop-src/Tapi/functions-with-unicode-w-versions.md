---
description: "Learn more about: Functions with Unicode (W) Versions"
ms.assetid: 3457cfb6-3891-4e15-a4e0-53ad43adcc2d
title: Functions with Unicode (W) Versions
ms.topic: article
ms.date: 05/31/2018
---

# Functions with Unicode (W) Versions

The following TAPI functions are implemented in Unicode (W) and ANSI (A) versions. In general, the implementation of the ANSI version calls the Unicode version and performs necessary conversions of ANSI parameters and structure fields to and from Unicode; the following table indicates the parameters that are converted.

Applications that explicitly call the generic (neither "W" or "A" suffix) version of a function will execute the ANSI version, for compatibility with previous versions of TAPI.

> [!Note]  
> The entire Telephony Service Provider Interface (TSPI) is Unicode for version 2.0.

 

Listed in the following table are references to string fields in TAPI structures that consist of a portion of the field names. For example, the "Caller Address" in the [**LINEFORWARD**](/windows/desktop/api/Tapi/ns-tapi-lineforward) structure is pointed to by the **dwCallerAddressOffset** field and delimited by the **dwCallerAddressSize** field; in the table, this string is identified simply as **CallerAddress**.




| TAPI function | Parameters and structure fields converted in ANSI version of function | 
|---------------|-----------------------------------------------------------------------|
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineaddprovider"><strong>lineAddProvider</strong></a> | <em>lpszProviderName</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineblindtransfer"><strong>lineBlindTransfer</strong></a> | <em>lpszDestAddress</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineconfigdialog"><strong>lineConfigDialog</strong></a> | <em>lpszDeviceClass</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineconfigdialogedit"><strong>lineConfigDialogEdit</strong></a> | <em>lpszDeviceClass</em><blockquote>[!Note]<br />Application must handle conversion of strings in <em>lpDeviceConfigIn</em> and <em>lpDeviceConfigOut</em>, if directly manipulated.</blockquote><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linedial"><strong>lineDial</strong></a> | <em>lpszDestAddress</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineforward"><strong>lineForward</strong></a> | <em>lpForwardList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineforwardlist"><strong>LINEFORWARDLIST</strong></a>)<ul><li><em>ForwardList</em> ( <a href="/windows/desktop/api/Tapi/ns-tapi-lineforward"><strong>LINEFORWARD</strong></a>)<ul><li><em>CallerAddress</em></li><li><em>DestAddress</em></li></ul></li></ul><em>lpCallParams</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecallparams"><strong>LINECALLPARAMS</strong></a>)<br /><ul><li><em>OrigAddress</em></li><li><em>DisplayableAddress</em></li><li><em>CalledParty</em></li><li><em>Comment</em></li><li><em>TargetAddress</em></li><li><em>DeviceClass</em></li><li><em>CallingPartyID</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegatherdigits"><strong>lineGatherDigits</strong></a> | <em>lpsDigitslpszTerminationDigits</em><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegeneratedigits"><strong>lineGenerateDigits</strong></a> | <em>lpszDigits</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetaddresscaps"><strong>lineGetAddressCaps</strong></a> | <em>lpAddressCaps</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineaddresscaps"><strong>LINEADDRESSCAPS</strong></a>)<ul><li><em>Address</em></li><li><em>CompletionMsgText</em></li><li><em>DeviceClasses</em></li><li><em>CallTreatmentList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecalltreatmententry"><strong>LINECALLTREATMENTENTRY</strong></a>)</li><li><em>CallTreatmentName</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetaddressid"><strong>lineGetAddressID</strong></a> | <em>lpsAddress</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus"><strong>lineGetAddressStatus</strong></a> | <em>lpAddressStatus</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineaddressstatus"><strong>LINEADDRESSSTATUS</strong></a>)<ul><li><em>Forward</em> ( <a href="/windows/desktop/api/Tapi/ns-tapi-lineforward"><strong>LINEFORWARD</strong></a>)</li><li><em>CallerAddress</em></li><li><em>DestAddress</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetagentactivitylista"><strong>lineGetAgentActivityList</strong></a> | <em>lpAgentActivityList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineagentactivitylist"><strong>LINEAGENTACTIVITYLIST</strong></a>)<ul><li><em>List</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineagentactivityentry"><strong>LINEAGENTACTIVITYENTRY</strong></a>)</li><li><em>Name</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetagentcapsa"><strong>lineGetAgentCaps</strong></a> | <em>lpAgentCaps</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineagentcaps"><strong>LINEAGENTCAPS</strong></a>)<ul><li><em>AgentHandlerInfo</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetagentgrouplista"><strong>lineGetAgentGroupList</strong></a> | <em>lpAgentGroupListI</em>( <a href="/windows/win32/api/tapi/ns-tapi-lineagentgrouplist"><strong>LINEAGENTGROUPLIST</strong></a>)<ul><li><em>List</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineagentgroupentry"><strong>LINEAGENTGROUPENTRY</strong></a>)</li><li><em>Name</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetagentstatusa"><strong>lineGetAgentStatus</strong></a> | <em>lpAgentStatus</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineagentstatus"><strong>LINEAGENTSTATUS</strong></a>)<ul><li><em>Activity</em></li><li><em>GroupList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineagentgroupentry"><strong>LINEAGENTGROUPENTRY</strong></a>)</li><li><em>Name</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetapppriority"><strong>lineGetAppPriority</strong></a> | <em>lpszAppFilenamelpExtensionName</em><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo"><strong>lineGetCallInfo</strong></a> | <em>lpCallInfo</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecallinfo"><strong>LINECALLINFO</strong></a>)<ul><li><em>CallerID</em></li><li><em>CallerIDName</em></li><li><em>CalledID</em></li><li><em>CalledIDName</em></li><li><em>ConnectID</em></li><li><em>ConnectedIDName</em></li><li><em>RedirectionID</em></li><li><em>RedirectionIDName</em></li><li><em>RedirectingID</em></li><li><em>RedirectingIDName</em></li><li><em>AppName</em></li><li><em>DisplayableAddress</em></li><li><em>CalledParty</em></li><li><em>Comment</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetcountry"><strong>lineGetCountry</strong></a> | <em>lpLineCountryList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecountrylist"><strong>LINECOUNTRYLIST</strong></a>)<ul><li><em>CountryList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecountryentry"><strong>LINECOUNTRYENTRY</strong></a>)</li><li><em>CountryName</em></li><li><em>SameAreaRule</em></li><li><em>LongDistanceRule</em></li><li><em>InternationalRule</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetdevcaps"><strong>lineGetDevCaps</strong></a> | <em>lpLineDevCaps</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linedevcaps"><strong>LINEDEVCAPS</strong></a>)<ul><li><em>ProviderInfo</em></li><li><em>SwitchInfo</em></li><li><em>LineName</em></li><li><em>TerminalText</em></li><li><em>DeviceClasses</em></li></ul><blockquote>[!Note]<br /><em>dwStringFormat</em> is obsolete.</blockquote><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig"><strong>LineGetDevConfig</strong></a> | <em>lpszDeviceClass</em><blockquote>[!Note]<br />Application must handle conversion of strings in <em>lpDeviceConfig</em>, if these are directly manipulated.</blockquote><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegeticon"><strong>LineGetIcon</strong></a> | <em>lpszDeviceClass</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetid"><strong>lineGetID</strong></a> | <em>lpszDeviceClass</em><blockquote>[!Note]<br />Application must handle conversion of strings in <em>lpDeviceID</em>, if these are directly manipulated.</blockquote><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetlinedevstatus"><strong>LineGetLineDevStatus</strong></a> | <em>lpLineDevStatus</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linedevstatus"><strong>LINEDEVSTATUS</strong></a>)<ul><li><em>AppInfo</em> (LINEAPPINFO)</li><li><em>MachineName</em></li><li><em>UserName</em></li><li><em>ModuleFilename</em></li><li><em>FriendlyName</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetproviderlist"><strong>lineGetProviderList</strong></a> | <em>lpProviderList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineproviderlist"><strong>LINEPROVIDERLIST</strong></a>)<ul><li><em>ProviderList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-lineproviderentry"><strong>LINEPROVIDERENTRY</strong></a>)</li><li><em>ProviderFilename</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegetrequest"><strong>lineGetRequest</strong></a> | <em>lpRequestBuffer</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linereqmakecall"><strong>LINEREQMAKECALL</strong></a><ul><li><em>szDestAddress</em></li><li><em>szAppName</em></li><li><em>szCalledParty</em></li><li><em>szComment</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linegettranslatecaps"><strong>lineGetTranslateCaps</strong></a> | <em>lpTranslateCaps</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linetranslatecaps"><strong>LINETRANSLATECAPS</strong></a>)<ul><li><em>CardList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecardentry"><strong>LINECARDENTRY</strong></a>)</li><li><em>CardName</em></li><li><em>SameAreaRule</em></li><li><em>LongDistanceRule</em></li><li><em>InternationalRule</em></li><li><em>LocationList</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linelocationentry"><strong>LINELOCATIONENTRY</strong></a></li><li><em>LocationName</em></li><li><em>CityCode</em></li><li><em>LocalAccessCode</em></li><li><em>LongDistanceAccessCode</em></li><li><em>TollPrefixList</em></li><li><em>celCallWaiting</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linehandoff"><strong>lineHandoff</strong></a> | <em>lpszFileName</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa"><strong>lineInitializeEx</strong></a> | <em>lpszFriendlyAppName</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linemakecall"><strong>lineMakeCall</strong></a> | <em>lpszDestAddresslpCallParams</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecallparams"><strong>LINECALLPARAMS</strong></a>)<br /><ul><li><em>OrigAddress</em></li><li><em>DisplayableAddress</em></li><li><em>CalledParty</em></li><li><em>Comment</em></li><li><em>TargetAddress</em></li><li><em>DeviceClass</em></li><li><em>CallingPartyID</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineopen"><strong>lineOpen</strong></a> | <em>lpCallParams</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecallparams"><strong>LINECALLPARAMS</strong></a>)<ul><li><em>OrigAddress</em></li><li><em>DisplayableAddress</em></li><li><em>CalledParty</em></li><li><em>Comment</em></li><li><em>TargetAddress</em></li><li><em>DeviceClass</em></li><li><em>CallingPartyID</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linepark"><strong>linePark</strong></a> | <em>lpszDirAddresslpNonDirAddress</em> ( <a href="/windows/win32/api/tapi/ns-tapi-varstring"><strong>VARSTRING</strong></a>)<br /><ul><li><em>String</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linepickup"><strong>linePickup</strong></a> | <em>lpszDestAddresslpszGroupID</em><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineprepareaddtoconference"><strong>linePrepareAddToConference</strong></a> | <em>lpCallParams</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecallparams"><strong>LINECALLPARAMS</strong></a>)<ul><li><em>OrigAddress</em></li><li><em>DisplayableAddress</em></li><li><em>CalledParty</em></li><li><em>Comment</em></li><li><em>TargetAddress</em></li><li><em>DeviceClass</em></li><li><em>CallingPartyID</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineredirect"><strong>lineRedirect</strong></a> | <em>lpszDestAddress</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linesetapppriority"><strong>lineSetAppPriority</strong></a> | <em>lpszAppFilenamelpszExtensionName</em><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig"><strong>lineSetDevConfig</strong></a> | <em>lpszDeviceClass</em><blockquote>[!Note]<br />Application must handle conversion of strings in <em>lpDeviceConfig</em>, if these are directly manipulated.</blockquote><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linesettolllist"><strong>lineSetTollList</strong></a> | <em>lpszAddressIn</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linesetupconference"><strong>lineSetupConference</strong></a> | <em>lpCallParams</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecallparams"><strong>LINECALLPARAMS</strong></a>)<ul><li><em>OrigAddress</em></li><li><em>DisplayableAddress</em></li><li><em>CalledParty</em></li><li><em>Comment</em></li><li><em>TargetAddress</em></li><li><em>DeviceClass</em></li><li><em>CallingPartyID</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linesetuptransfer"><strong>lineSetupTransfer</strong></a> | <em>lpCallParams</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linecallparams"><strong>LINECALLPARAMS</strong></a>)<ul><li><em>OrigAddress</em></li><li><em>DisplayableAddress</em></li><li><em>CalledParty</em></li><li><em>Comment</em></li><li><em>TargetAddress</em></li><li><em>DeviceClass</em></li><li><em>CallingPartyID</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linetranslateaddress"><strong>lineTranslateAddress</strong></a> | <em>lpszAddressInlpTranslateOutput</em> ( <a href="/windows/win32/api/tapi/ns-tapi-linetranslateoutput"><strong>LINETRANSLATEOUTPUT</strong></a>)<br /><ul><li><em>DialableString</em></li><li><em>DisplayableString</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-linetranslatedialog"><strong>lineTranslateDialog</strong></a> | <em>lpszAddressIn</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-lineunpark"><strong>lineUnpark</strong></a> | <em>lpszDestAddress</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-phoneconfigdialog"><strong>phoneConfigDialog</strong></a> | <em>lpszDeviceClass</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-phonegetbuttoninfo"><strong>phoneGetButtonInfo</strong></a> | <em>lpButtonInfo</em> ( <a href="/windows/win32/api/tapi/ns-tapi-phonebuttoninfo"><strong>PHONEBUTTONINFO</strong></a>)<ul><li><em>ButtonText</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps"><strong>phoneGetDevCaps</strong></a> | <em>lpPhoneCaps</em> ( <a href="/windows/win32/api/tapi/ns-tapi-phonecaps"><strong>PHONECAPS</strong></a>)<ul><li><em>ProviderInfo</em></li><li><em>PhoneInfo</em></li><li><em>PhoneName</em></li><li><em>Device Classes</em></li></ul><blockquote>[!Note]<br /><em>dwStringFormat</em> is obsolete.</blockquote><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-phonegeticon"><strong>phoneGetIcon</strong></a> | <em>lpszDeviceClass</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-phonegetid"><strong>phoneGetID</strong></a> | <em>lpszDeviceClass</em><blockquote>[!Note]<br />Application must handle conversion of strings in <em>lpDeviceID</em>, if these are directly manipulated.</blockquote><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-phonegetstatus"><strong>phoneGetStatus</strong></a> | <em>lpPhoneStatus</em> ( <a href="/windows/win32/api/tapi/ns-tapi-phonestatus"><strong>PHONESTATUS</strong></a>)<ul><li><em>OwnerName</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa"><strong>phoneInitializeEx</strong></a> | <em>lpszFriendlyAppName</em> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-phonesetbuttoninfo"><strong>phoneSetButtonInfo</strong></a> | <em>lpButtonInfo</em> ( <a href="/windows/win32/api/tapi/ns-tapi-phonebuttoninfo"><strong>PHONEBUTTONINFO</strong></a>)<ul><li><em>ButtonTest</em></li></ul> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-tapigetlocationinfo"><strong>tapiGetLocationInfo</strong></a> | <em>lpszCountryCodelpszCityCode</em><br /> | 
| <a href="/windows/desktop/api/Tapi/nf-tapi-tapirequestmakecall"><strong>tapiRequestMakeCall</strong></a> | <em>lpszDestAddresslpszAppName</em><br /><em>lpszCalledParty</em><br /><em>lpszComment</em><br /> | 




 

 

 




