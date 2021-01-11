---
description: TAPI supports line device functions to configure line devices and perform telephony functions such hold and forward.
ms.assetid: 74e6300f-0d72-4b0f-8b95-fc1c8d0d0293
title: Line Device Functions
ms.topic: article
ms.date: 05/31/2018
---

# Line Device Functions

TAPI supports the following line device functions:

-   [**lineAccept**](/windows/desktop/api/Tapi/nf-tapi-lineaccept)
-   [**lineAddProvider**](/windows/desktop/api/Tapi/nf-tapi-lineaddprovider)
-   [**lineAddToConference**](/windows/desktop/api/Tapi/nf-tapi-lineaddtoconference)
-   [**lineAnswer**](/windows/desktop/api/Tapi/nf-tapi-lineanswer)
-   [**lineBlindTransfer**](/windows/desktop/api/Tapi/nf-tapi-lineblindtransfer)
-   [**lineCallbackFunc**](/windows/desktop/api/Tapi/nc-tapi-linecallback)
-   [**lineClose**](/windows/desktop/api/Tapi/nf-tapi-lineclose)
-   [**lineCompleteCall**](/windows/desktop/api/Tapi/nf-tapi-linecompletecall)
-   [**lineCompleteTransfer**](/windows/desktop/api/Tapi/nf-tapi-linecompletetransfer)
-   [**lineConfigDialog**](/windows/desktop/api/Tapi/nf-tapi-lineconfigdialog)
-   [**lineConfigDialogEdit**](/windows/desktop/api/Tapi/nf-tapi-lineconfigdialogedit)
-   [**lineConfigProvider**](/windows/desktop/api/Tapi/nf-tapi-lineconfigprovider)
-   [**lineDeallocateCall**](/windows/desktop/api/Tapi/nf-tapi-linedeallocatecall)
-   [**lineDevSpecific**](/windows/desktop/api/Tapi/nf-tapi-linedevspecific)
-   [**lineDevSpecificFeature**](/windows/desktop/api/Tapi/nf-tapi-linedevspecificfeature)
-   [**lineDial**](/windows/desktop/api/Tapi/nf-tapi-linedial)
-   [**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop)
-   [**lineForward**](/windows/desktop/api/Tapi/nf-tapi-lineforward)
-   [**lineGatherDigits**](/windows/desktop/api/Tapi/nf-tapi-linegatherdigits)
-   [**lineGenerateDigits**](/windows/desktop/api/Tapi/nf-tapi-linegeneratedigits)
-   [**lineGenerateTone**](/windows/desktop/api/Tapi/nf-tapi-linegeneratetone)
-   [**lineGetAddressCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetaddresscaps)
-   [**lineGetAddressID**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressid)
-   [**lineGetAddressStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus)
-   [**lineGetAppPriority**](/windows/desktop/api/Tapi/nf-tapi-linegetapppriority)
-   [**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo)
-   [**lineGetCallStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetcallstatus)
-   [**lineGetConfRelatedCalls**](/windows/desktop/api/Tapi/nf-tapi-linegetconfrelatedcalls)
-   [**lineGetCountry**](/windows/desktop/api/Tapi/nf-tapi-linegetcountry)
-   [**lineGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetdevcaps)
-   [**lineGetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig)
-   [**lineGetIcon**](/windows/desktop/api/Tapi/nf-tapi-linegeticon)
-   [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid)
-   [**lineGetLineDevStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetlinedevstatus)
-   [**lineGetMessage**](/windows/desktop/api/Tapi/nf-tapi-linegetmessage)
-   [**lineGetNewCalls**](/windows/desktop/api/Tapi/nf-tapi-linegetnewcalls)
-   [**lineGetNumRings**](/windows/desktop/api/Tapi/nf-tapi-linegetnumrings)
-   [**lineGetProviderList**](/windows/desktop/api/Tapi/nf-tapi-linegetproviderlist)
-   [**lineGetRequest**](/windows/desktop/api/Tapi/nf-tapi-linegetrequest)
-   [**lineGetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-linegetstatusmessages)
-   [**lineGetTranslateCaps**](/windows/desktop/api/Tapi/nf-tapi-linegettranslatecaps)
-   [**lineHandoff**](/windows/desktop/api/Tapi/nf-tapi-linehandoff)
-   [**lineHold**](/windows/desktop/api/Tapi/nf-tapi-linehold)
-   [**lineInitialize**](/windows/desktop/api/Tapi/nf-tapi-lineinitialize)
-   [**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa)
-   [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall)
-   [**lineMonitorDigits**](/windows/desktop/api/Tapi/nf-tapi-linemonitordigits)
-   [**lineMonitorMedia**](/windows/desktop/api/Tapi/nf-tapi-linemonitormedia)
-   [**lineMonitorTones**](/windows/desktop/api/Tapi/nf-tapi-linemonitortones)
-   [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion)
-   [**lineNegotiateExtVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateextversion)
-   [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen)
-   [**linePark**](/windows/desktop/api/Tapi/nf-tapi-linepark)
-   [**linePickup**](/windows/desktop/api/Tapi/nf-tapi-linepickup)
-   [**linePrepareAddToConference**](/windows/desktop/api/Tapi/nf-tapi-lineprepareaddtoconference)
-   [**lineRedirect**](/windows/desktop/api/Tapi/nf-tapi-lineredirect)
-   [**lineRegisterRequestRecipient**](/windows/desktop/api/Tapi/nf-tapi-lineregisterrequestrecipient)
-   [**lineReleaseUserUserInfo**](/windows/desktop/api/Tapi/nf-tapi-linereleaseuseruserinfo)
-   [**lineRemoveFromConference**](/windows/desktop/api/Tapi/nf-tapi-lineremovefromconference)
-   [**lineRemoveProvider**](/windows/desktop/api/Tapi/nf-tapi-lineremoveprovider)
-   [**lineSecureCall**](/windows/desktop/api/Tapi/nf-tapi-linesecurecall)
-   [**lineSendUserUserInfo**](/windows/desktop/api/Tapi/nf-tapi-linesenduseruserinfo)
-   [**lineSetAppPriority**](/windows/desktop/api/Tapi/nf-tapi-linesetapppriority)
-   [**lineSetAppSpecific**](/windows/desktop/api/Tapi/nf-tapi-linesetappspecific)
-   [**lineSetCallData**](/windows/desktop/api/Tapi/nf-tapi-linesetcalldata)
-   [**lineSetCallParams**](/windows/desktop/api/Tapi/nf-tapi-linesetcallparams)
-   [**lineSetCallPrivilege**](/windows/desktop/api/Tapi/nf-tapi-linesetcallprivilege)
-   [**lineSetCallQualityOfService**](/windows/desktop/api/Tapi/nf-tapi-linesetcallqualityofservice)
-   [**lineSetCallTreatment**](/windows/desktop/api/Tapi/nf-tapi-linesetcalltreatment)
-   [**lineSetCurrentLocation**](/windows/desktop/api/Tapi/nf-tapi-linesetcurrentlocation)
-   [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig)
-   [**lineSetLineDevStatus**](/windows/desktop/api/Tapi/nf-tapi-linesetlinedevstatus)
-   [**lineSetMediaControl**](/windows/desktop/api/Tapi/nf-tapi-linesetmediacontrol)
-   [**lineSetMediaMode**](/windows/desktop/api/Tapi/nf-tapi-linesetmediamode)
-   [**lineSetNumRings**](/windows/desktop/api/Tapi/nf-tapi-linesetnumrings)
-   [**lineSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-linesetstatusmessages)
-   [**lineSetTerminal**](/windows/desktop/api/Tapi/nf-tapi-linesetterminal)
-   [**lineSetTollList**](/windows/desktop/api/Tapi/nf-tapi-linesettolllist)
-   [**lineSetupConference**](/windows/desktop/api/Tapi/nf-tapi-linesetupconference)
-   [**lineSetupTransfer**](/windows/desktop/api/Tapi/nf-tapi-linesetuptransfer)
-   [**lineShutdown**](/windows/desktop/api/Tapi/nf-tapi-lineshutdown)
-   [**lineSwapHold**](/windows/desktop/api/Tapi/nf-tapi-lineswaphold)
-   [**lineTranslateAddress**](/windows/desktop/api/Tapi/nf-tapi-linetranslateaddress)
-   [**lineTranslateDialog**](/windows/desktop/api/Tapi/nf-tapi-linetranslatedialog)
-   [**lineUncompleteCall**](/windows/desktop/api/Tapi/nf-tapi-lineuncompletecall)
-   [**lineUnhold**](/windows/desktop/api/Tapi/nf-tapi-lineunhold)
-   [**lineUnpark**](/windows/desktop/api/Tapi/nf-tapi-lineunpark)

For a categorization of TAPI functions by service level and task, see [TAPI Quick Function Reference](tapi-quick-function-reference.md).

 

 



