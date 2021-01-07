---
description: The supplementary line service functions are listed by category in the following topics.
ms.assetid: d4338b3c-cd84-4abb-b74e-9df895c8355b
title: Supplementary Line Service Functions
ms.topic: article
ms.date: 05/31/2018
---

# Supplementary Line Service Functions

The supplementary line service functions are listed by category in the following topics. A function is identified as [*asynchronous*](a-tapgloss.md) if it will indicate completion in a REPLY message to the application. If the function always returns its result to the application immediately, the function is considered [*synchronous*](s-tapgloss.md).

Following is a functional grouping of the supplementary line service functions:

-   [Agents](#agents)
-   [Application priority](#application-priority)
-   [Bearer mode and rate](#bearer-mode-and-rate)
-   [Call accept and redirect](#call-accept-and-redirect)
-   [Call completion](#call-completion)
-   [Call conference](#call-conference)
-   [Call forwarding](#call-forwarding)
-   [Call hold](#call-hold)
-   [Call park](#call-park)
-   [Call pickup](#call-pickup)
-   [Call reject](#call-reject)
-   [Call transfer](#call-transfer)
-   [Digit monitoring and gathering](#digit-monitoring-and-gathering)
-   [Generating inband digits and tones](#generating-inband-digits-and-tones)
-   [Making calls](basic-telephony-services-reference.md)
-   [Media control](#media-control)
-   [Media monitoring](#media-monitoring)
-   [Proxies](#proxies)
-   [Quality of Service](#quality-of-service)
-   [Sending information to remote party](#sending-information-to-remote-party)
-   [Service provider management](#service-provider-management)
-   [Setting a terminal for phone conversations](#setting-a-terminal-for-phone-conversations)
-   [Tone monitoring](#tone-monitoring)

There are also [miscellaneous](#miscellaneous) supplementary line service functions.

## Bearer Mode and Rate



| Function                                       | Description                                                                |
|------------------------------------------------|----------------------------------------------------------------------------|
| [**lineSetCallParams**](/windows/desktop/api/Tapi/nf-tapi-linesetcallparams) | Requests a change in the call parameters of an existing call. Synchronous. |



 

## Media Monitoring



| Function                                     | Description                                                                   |
|----------------------------------------------|-------------------------------------------------------------------------------|
| [**lineMonitorMedia**](/windows/desktop/api/Tapi/nf-tapi-linemonitormedia) | Enables or disables media mode notification on a specified call. Synchronous. |



 

## Digit Monitoring and Gathering



| Function                                       | Description                                                                        |
|------------------------------------------------|------------------------------------------------------------------------------------|
| [**lineMonitorDigits**](/windows/desktop/api/Tapi/nf-tapi-linemonitordigits) | Enables or disables digit detection notification on a specified call. Synchronous. |
| [**lineGatherDigits**](/windows/desktop/api/Tapi/nf-tapi-linegatherdigits)   | Performs the buffered gathering of digits on a call. Synchronous.                  |



 

## Tone Monitoring



| Function                                     | Description                                                       |
|----------------------------------------------|-------------------------------------------------------------------|
| [**lineMonitorTones**](/windows/desktop/api/Tapi/nf-tapi-linemonitortones) | Specifies which tones to detect on a specified call. Synchronous. |



 

## Media Control



| Function                                           | Description                                                                                                          |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**lineSetMediaControl**](/windows/desktop/api/Tapi/nf-tapi-linesetmediacontrol) | Sets up a call's media stream for media control. Synchronous.                                                        |
| [**lineSetMediaMode**](/windows/desktop/api/Tapi/nf-tapi-linesetmediamode)       | Sets the media mode(s) of the specified call in its [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) structure. Synchronous. |



 

## Generating Inband Digits and Tones



| Function                                         | Description                                                   |
|--------------------------------------------------|---------------------------------------------------------------|
| [**lineGenerateDigits**](/windows/desktop/api/Tapi/nf-tapi-linegeneratedigits) | Generates inband digits on a call. Synchronous.               |
| [**lineGenerateTone**](/windows/desktop/api/Tapi/nf-tapi-linegeneratetone)     | Generates a given set of tones inband on a call. Synchronous. |



 

## Call Accept and Redirect



| Function                             | Description                                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**lineAccept**](/windows/desktop/api/Tapi/nf-tapi-lineaccept)     | Accepts an offered call and starts alerting both caller (ringback) and called party (ring). Asynchronous. |
| [**lineRedirect**](/windows/desktop/api/Tapi/nf-tapi-lineredirect) | Redirects an offering call to another address. Asynchronous.                                              |



 

## Call Reject



| Function                     | Description                                                               |
|------------------------------|---------------------------------------------------------------------------|
| [**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop) | Disconnects a call, or abandons a call attempt in progress. Asynchronous. |



 

## Call Hold



| Function                         | Description                                           |
|----------------------------------|-------------------------------------------------------|
| [**lineHold**](/windows/desktop/api/Tapi/nf-tapi-linehold)     | Places the specified call on hard hold. Asynchronous. |
| [**lineUnhold**](/windows/desktop/api/Tapi/nf-tapi-lineunhold) | Retrieves a held call. Asynchronous.                  |



 

## Securing Calls



| Function                                 | Description                                                                                                              |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**lineSecureCall**](/windows/desktop/api/Tapi/nf-tapi-linesecurecall) | Secures an existing call from interference by other events such as call-waiting beeps on data connections. Asynchronous. |



 

## Call Transfer



| Function                                             | Description                                                                                                    |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**lineSetupTransfer**](/windows/desktop/api/Tapi/nf-tapi-linesetuptransfer)       | Prepares a specified call for transfer to another address. Asynchronous.                                       |
| [**lineCompleteTransfer**](/windows/desktop/api/Tapi/nf-tapi-linecompletetransfer) | Transfers a call that was set up for transfer to another call, or enters a three-way conference. Asynchronous. |
| [**lineBlindTransfer**](/windows/desktop/api/Tapi/nf-tapi-lineblindtransfer)       | Transfers a call to another party. Asynchronous.                                                               |
| [**lineSwapHold**](/windows/desktop/api/Tapi/nf-tapi-lineswaphold)                 | Swaps the active call with the call currently on consultation hold. Asynchronous.                              |



 

## Call Conference



| Function                                                         | Description                                                                                                                                                                                          |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**lineSetupConference**](/windows/desktop/api/Tapi/nf-tapi-linesetupconference)               | Prepares a given call for the addition of another party. Asynchronous.                                                                                                                               |
| [**linePrepareAddToConference**](/windows/desktop/api/Tapi/nf-tapi-lineprepareaddtoconference) | Prepares to add a party to an existing conference call by placing the conference call in a hold state and creating a consultation call that can be added later to the conference call. Asynchronous. |
| [**lineAddToConference**](/windows/desktop/api/Tapi/nf-tapi-lineaddtoconference)               | Adds a consultation call to an existing conference call. Asynchronous.                                                                                                                               |
| [**lineRemoveFromConference**](/windows/desktop/api/Tapi/nf-tapi-lineremovefromconference)     | Removes a party from a conference call. Asynchronous.                                                                                                                                                |



 

## Call Park



| Function                         | Description                                          |
|----------------------------------|------------------------------------------------------|
| [**linePark**](/windows/desktop/api/Tapi/nf-tapi-linepark)     | Parks a given call at another address. Asynchronous. |
| [**lineUnpark**](/windows/desktop/api/Tapi/nf-tapi-lineunpark) | Retrieves a parked call. Asynchronous.               |



 

## Call Forwarding



| Function                           | Description                                             |
|------------------------------------|---------------------------------------------------------|
| [**lineForward**](/windows/desktop/api/Tapi/nf-tapi-lineforward) | Sets or cancels call forwarding requests. Asynchronous. |



 

## Call Pickup



| Function                         | Description                                                                                                                                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**linePickup**](/windows/desktop/api/Tapi/nf-tapi-linepickup) | Picks up a call alerting at a specified destination address and returns a call handle for the picked-up call ([**linePickup**](/windows/desktop/api/Tapi/nf-tapi-linepickup) can also be used for call waiting). Asynchronous. |



 

## Sending Information to Remote Party



| Function                                                   | Description                                                                                                         |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**lineReleaseUserUserInfo**](/windows/desktop/api/Tapi/nf-tapi-linereleaseuseruserinfo) | Releases user-user information, permitting the system to overwrite this storage with new information. Asynchronous. |
| [**lineSendUserUserInfo**](/windows/desktop/api/Tapi/nf-tapi-linesenduseruserinfo)       | Sends user-user information to the remote party on the specified call. Asynchronous.                                |



 

## Call Completion



| Function                                         | Description                                      |
|--------------------------------------------------|--------------------------------------------------|
| [**lineCompleteCall**](/windows/desktop/api/Tapi/nf-tapi-linecompletecall)     | Places a call completion request. Asynchronous.  |
| [**lineUncompleteCall**](/windows/desktop/api/Tapi/nf-tapi-lineuncompletecall) | Cancels a call completion request. Asynchronous. |



 

## Setting a Terminal for Phone Conversations



| Function                                   | Description                                                                                                                      |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**lineSetTerminal**](/windows/desktop/api/Tapi/nf-tapi-linesetterminal) | Specifies the terminal device to which the specified line, address events, or call media stream events are routed. Asynchronous. |



 

## Application Priority



| Function                                         | Description                                                                                       |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**lineGetAppPriority**](/windows/desktop/api/Tapi/nf-tapi-linegetapppriority) | Retrieves handoff and/or Assisted Telephony priority information for an application. Synchronous. |
| [**lineSetAppPriority**](/windows/desktop/api/Tapi/nf-tapi-linesetapppriority) | Sets the handoff and/or Assisted Telephony priority for an application. Synchronous.              |



 

## Service Provider Management



| Function                                           | Description                                                           |
|----------------------------------------------------|-----------------------------------------------------------------------|
| [**lineAddProvider**](/windows/desktop/api/Tapi/nf-tapi-lineaddprovider)         | Installs a telephony service provider. Synchronous.                   |
| [**lineConfigProvider**](/windows/desktop/api/Tapi/nf-tapi-lineconfigprovider)   | Displays configuration dialog box of a service provider. Synchronous. |
| [**lineRemoveProvider**](/windows/desktop/api/Tapi/nf-tapi-lineremoveprovider)   | Removes an existing telephony service provider. Synchronous.          |
| [**lineGetProviderList**](/windows/desktop/api/Tapi/nf-tapi-linegetproviderlist) | Retrieves a list of installed service providers. Synchronous.         |



 

## Agents



| Function                                                     | Description                                                                                                                             |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**lineAgentSpecific**](/windows/desktop/api/Tapi/nf-tapi-lineagentspecific)               | Allows the application to access proprietary handler-specific functions of the agent handler associated with the address. Asynchronous. |
| [**lineGetAgentActivityList**](/windows/desktop/api/Tapi/nf-tapi-linegetagentactivitylista) | Obtains the list of activities from which an application selects the functions an agent is performing. Asynchronous.                    |
| [**lineGetAgentCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetagentcapsa)                 | Obtains the agent-related capabilities supported on the specified line device. Asynchronous.                                            |
| [**lineGetAgentGroupList**](/windows/desktop/api/Tapi/nf-tapi-linegetagentgrouplista)       | Obtains the list of agent groups into which an agent can log into on the automatic call distributor. Asynchronous.                      |
| [**lineGetAgentStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetagentstatusa)             | Obtains the agent-related status on the specified address. Asynchronous.                                                                |
| [**lineSetAgentActivity**](/windows/desktop/api/Tapi/nf-tapi-linesetagentactivity)         | Sets the agent activity code associated with a particular address. Asynchronous.                                                        |
| [**lineSetAgentGroup**](/windows/desktop/api/Tapi/nf-tapi-linesetagentgroup)               | Sets the agent groups that the agent is logged into on a particular address. Asynchronous.                                              |
| [**lineSetAgentState**](/windows/desktop/api/Tapi/nf-tapi-linesetagentstate)               | Sets the agent state associated with a particular address. Asynchronous.                                                                |



 

## Proxies



| Function                                       | Description                                                                         |
|------------------------------------------------|-------------------------------------------------------------------------------------|
| [**lineProxyMessage**](/windows/desktop/api/Tapi/nf-tapi-lineproxymessage)   | Used by a registered proxy request handler to generate TAPI messages. Synchronous.  |
| [**lineProxyResponse**](/windows/desktop/api/Tapi/nf-tapi-lineproxyresponse) | Indicates completion of a proxy request by a registered proxy handler. Synchronous. |



 

## Quality of Service



| Function                                                           | Description                                                                                |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**lineSetCallQualityOfService**](/windows/desktop/api/Tapi/nf-tapi-linesetcallqualityofservice) | Requests a change of the quality of service parameters for an existing call. Asynchronous. |



 

## Miscellaneous



| Function                                             | Description                                                                                           |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**lineSetCallData**](/windows/desktop/api/Tapi/nf-tapi-linesetcalldata)           | Sets the **CallData** member of the [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) structure. Asynchronous. |
| [**lineSetCallTreatment**](/windows/desktop/api/Tapi/nf-tapi-linesetcalltreatment) | Sets the sounds that the user hears when a call is unanswered or on hold. Asynchronous.               |
| [**lineSetLineDevStatus**](/windows/desktop/api/Tapi/nf-tapi-linesetlinedevstatus) | Sets the line device status. Asynchronous.                                                            |



 

 

 



