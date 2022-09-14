---
description: The Basic Telephony functions are listed by category in the following tables.
ms.assetid: 09d10789-bc36-47c7-b77d-8698ae75541a
title: Basic Telephony Services Reference
ms.topic: article
ms.date: 05/31/2018
---

# Basic Telephony Services Reference

The Basic Telephony functions are listed by category in the following tables. A function is identified as [*asynchronous*](a-tapgloss.md) if it indicates completion in a REPLY message to the application. If the function always returns its result to the application immediately, the function is considered [*synchronous*](s-tapgloss.md).

Following is a functional grouping of the basic telephony service functions:

-   [Address Formats](#address-formats)
-   [Addresses](#addresses)
-   [Answering Incoming Calls](#answering-incoming-calls)
-   [Call Drop Functions](#call-drop-functions)
-   [Call Handle Manipulation](#call-handle-manipulation)
-   [Call Privilege Control](#call-privilege-control)
-   [Call States and Events](#call-states-and-events)
-   [Line Status and Capabilities](#line-status-and-capabilities)
-   [Line Version Negotiation](#line-version-negotiation)
-   [Location and Country/Region Information](#location-and-countryregion-information)
-   [Making Calls](#making-calls)
-   [Opening and Closing Line Devices](#opening-and-closing-line-devices)
-   [Request Recipient Services](#request-recipient-services)
-   [TAPI Initialization and Shutdown](#tapi-initialization-and-shutdown)
-   [Toll Saver Support](#toll-saver-support)

## TAPI Initialization and Shutdown



| Function                                     | Description                                                                             |
|----------------------------------------------|-----------------------------------------------------------------------------------------|
| [**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa) | Initializes the TAPI line abstraction for use by the invoking application. Synchronous. |
| [**lineShutdown**](/windows/desktop/api/Tapi/nf-tapi-lineshutdown)         | Shuts down the application's use of TAPI's line abstraction. Synchronous.               |



 

## Line Version Negotiation



| Function                                                   | Description                                                            |
|------------------------------------------------------------|------------------------------------------------------------------------|
| [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion) | Allows an application to negotiate a TAPI version to use. Synchronous. |



 

## Line Status and Capabilities



| Function                                               | Description                                                                                                                                                    |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**lineGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetdevcaps)               | Returns the capabilities of a given line device. Synchronous.                                                                                                  |
| [**lineGetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig)           | Returns configuration of a media stream device. Synchronous.                                                                                                   |
| [**lineGetLineDevStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetlinedevstatus)   | Returns current status of the specified open line device. Synchronous.                                                                                         |
| [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig)           | Sets the configuration of the specified media stream device. Synchronous.                                                                                      |
| [**lineSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-linesetstatusmessages) | Specifies the status changes for which the application needs to be notified. Synchronous.                                                                      |
| [**lineGetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-linegetstatusmessages) | Returns the application's current line and address status message settings. Synchronous.                                                                       |
| [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid)                         | Retrieves a device ID associated with the specified open line, address, or call. Synchronous.                                                                  |
| [**lineGetIcon**](/windows/desktop/api/Tapi/nf-tapi-linegeticon)                     | Allows an application to retrieve an icon for display to the user. Synchronous.                                                                                |
| [**lineConfigDialog**](/windows/desktop/api/Tapi/nf-tapi-lineconfigdialog)           | Causes the provider of the specified line device to display a dialog box that allows the user to configure parameters related to the line device. Synchronous. |
| [**lineConfigDialogEdit**](/windows/desktop/api/Tapi/nf-tapi-lineconfigdialogedit)   | Displays a dialog box allowing the user to change configuration information for a line device. Synchronous.                                                    |



 

## Addresses



| Function                                             | Description                                                                              |
|------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**lineGetAddressCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetaddresscaps)     | Returns the telephony capabilities of an address. Synchronous.                           |
| [**lineGetAddressStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus) | Returns current status of a specified address. Synchronous.                              |
| [**lineGetAddressID**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressid)         | Retrieves the address ID of an address specified using an alternate format. Synchronous. |



 

## Opening and Closing Line Devices



| Function                       | Description                                                                                                |
|--------------------------------|------------------------------------------------------------------------------------------------------------|
| [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen)   | Opens a specified line device for providing subsequent monitoring and/or control of the line. Synchronous. |
| [**lineClose**](/windows/desktop/api/Tapi/nf-tapi-lineclose) | Closes a specified opened line device. Synchronous.                                                        |



 

## Address Formats



| Function                                                 | Description                                                                                       |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**lineTranslateAddress**](/windows/desktop/api/Tapi/nf-tapi-linetranslateaddress)     | Translates between an address in canonical format and an address in dialable format. Synchronous. |
| [**lineSetCurrentLocation**](/windows/desktop/api/Tapi/nf-tapi-linesetcurrentlocation) | Sets the location used as the context for address translation. Synchronous.                       |
| [**lineSetTollList**](/windows/desktop/api/Tapi/nf-tapi-linesettolllist)               | Manipulates the toll list. Synchronous.                                                           |
| [**lineGetTranslateCaps**](/windows/desktop/api/Tapi/nf-tapi-linegettranslatecaps)     | Returns address translation capabilities. Synchronous.                                            |



 

## Call States and Events



| Function                                         | Description                                                                         |
|--------------------------------------------------|-------------------------------------------------------------------------------------|
| [**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo)       | Returns fixed information about a call. Synchronous.                                |
| [**lineGetCallStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetcallstatus)   | Returns complete call status information for the specified call. Synchronous.       |
| [**lineSetAppSpecific**](/windows/desktop/api/Tapi/nf-tapi-linesetappspecific) | Sets the application-specific field of a call's information structure. Synchronous. |



 

## Making Calls



| Function                             | Description                                                            |
|--------------------------------------|------------------------------------------------------------------------|
| [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall) | Makes an outbound call and returns a call handle for it. Asynchronous. |
| [**lineDial**](/windows/desktop/api/Tapi/nf-tapi-linedial)         | Dials (parts of one or more) dialable addresses. Asynchronous.         |



 

## Answering Incoming Calls



| Function                         | Description                             |
|----------------------------------|-----------------------------------------|
| [**lineAnswer**](/windows/desktop/api/Tapi/nf-tapi-lineanswer) | Answers an incoming call. Asynchronous. |



 

## Toll Saver Support



| Function                                   | Description                                                                                                 |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**lineSetNumRings**](/windows/desktop/api/Tapi/nf-tapi-linesetnumrings) | Indicates the number of rings after which incoming calls are to be answered. Synchronous.                   |
| [**lineGetNumRings**](/windows/desktop/api/Tapi/nf-tapi-linegetnumrings) | Returns the minimum number of rings requested with [**lineSetNumRings**](/windows/desktop/api/Tapi/nf-tapi-linesetnumrings). Synchronous. |



 

## Call Privilege Control



| Function                                             | Description                                                               |
|------------------------------------------------------|---------------------------------------------------------------------------|
| [**lineSetCallPrivilege**](/windows/desktop/api/Tapi/nf-tapi-linesetcallprivilege) | Sets the application's privilege to the privilege specified. Synchronous. |



 

## Call Drop Functions



| Function                                         | Description                                                               |
|--------------------------------------------------|---------------------------------------------------------------------------|
| [**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop)                     | Disconnects a call, or abandons a call attempt in progress. Asynchronous. |
| [**lineDeallocateCall**](/windows/desktop/api/Tapi/nf-tapi-linedeallocatecall) | Deallocates the specified call handle. Synchronous.                       |



 

## Call Handle Manipulation



| Function                                                   | Description                                                                                                                    |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**lineHandoff**](/windows/desktop/api/Tapi/nf-tapi-linehandoff)                         | Hands off call ownership and/or changes an application's privileges to a call. Synchronous.                                    |
| [**lineGetNewCalls**](/windows/desktop/api/Tapi/nf-tapi-linegetnewcalls)                 | Returns call handles to calls on a specified line or address for which the application does not yet have handles. Synchronous. |
| [**lineGetConfRelatedCalls**](/windows/desktop/api/Tapi/nf-tapi-linegetconfrelatedcalls) | Returns a list of call handles that are part of the same conference call as the call specified as a parameter. Synchronous.    |



 

## Location and Country/Region Information



| Function                                           | Description                                                                                           |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**lineTranslateDialog**](/windows/desktop/api/Tapi/nf-tapi-linetranslatedialog) | Displays a dialog box allowing the user to change location and calling card information. Synchronous. |
| [**lineGetCountry**](/windows/desktop/api/Tapi/nf-tapi-linegetcountry)           | Retrieves dialing rules and other information about a given country/region. Synchronous.              |



 

## Request Recipient Services

The following two functions are used only in support of Assisted Telephony.



| Function                                                             | Description                                                                                                  |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**lineRegisterRequestRecipient**](/windows/desktop/api/Tapi/nf-tapi-lineregisterrequestrecipient) | Registers or deregisters the application as a request recipient for the specified request mode. Synchronous. |
| [**lineGetRequest**](/windows/desktop/api/Tapi/nf-tapi-linegetrequest)                             | Gets the next request from the Telephony dynamic link library. Synchronous.                                  |



 

 

 



