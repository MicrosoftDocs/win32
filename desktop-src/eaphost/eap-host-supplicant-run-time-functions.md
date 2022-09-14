---
title: EAPHost Supplicant Run-Time Functions
description: Learn about EAPHost Supplicant run-time functions, like EapHostPeerBeginSession and EapHostPeerGetResult. 
ms.assetid: b1c473ba-9a12-4929-b4d0-27262117e9c0
ms.topic: article
ms.date: 05/31/2018
---

# EAPHost Supplicant Run-Time Functions

The EAP Supplicant API run-time functions are as follows.



| Function                                                                     | Description                                                                                                                                                                                                          |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapHostPeerBeginSession**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerbeginsession)                   | Starts an EAP authentication session.                                                                                                                                                                                |
| [**EapHostPeerClearConnection**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerclearconnection)             | Halts all future callbacks to the [**NotificationHandler**](/previous-versions/windows/desktop/api) provided by the calling supplicant to EAPHost in a previous call to [**EapHostPeerBeginSession**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerbeginsession). |
| [**EapHostPeerEndSession**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerendsession)                       | Terminates a current EAP authentication session between EAPHost and the calling supplicant.                                                                                                                          |
| [**EapHostPeerFreeEapError**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerfreeeaperror)                   | Frees all EAP error-specific memory returned by EAPHost APIs.                                                                                                                                                        |
| [**EapHostFreeRuntimeMemory**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerfreememory)                    | Releases memory space used by run-time APIs.                                                                                                                                                                         |
| [**EapHostPeerGetAuthStatus**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetauthstatus)                 | Obtains the supplicant's current EAP authentication status from EAPHost.                                                                                                                                             |
| [**EapHostPeerGetIdentity**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetidentity)                     | Requests identity information from the inner methods.                                                                                                                                                                |
| [**EapHostPeerGetResponseAttributes**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetresponseattributes) | Obtains an array of EAP authentication attributes from EAPHost.                                                                                                                                                      |
| [**EapHostPeerGetResult**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetresult)                         | Obtains the authentication result for the specified EAP authentication session.                                                                                                                                      |
| [**EapHostPeerGetSendPacket**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetsendpacket)                 | Obtains a packet from EAPHost to send to the authenticator.                                                                                                                                                          |
| [**EapHostPeerGetUIContext**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeergetuicontext)                   | Obtains the user interface context for the supplicant from EAPHost that is used in the [**EapHostPeerInvokeInteractiveUI**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeinteractiveui) APIs for the supplicant.                             |
| [**EapHostPeerInitialize**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerinitialize)                       | Initializes EAPHost for the supplicant. [**EapHostInitialize**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerinitialize) and [**EapHostUninitialize**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeeruninitialize) must be called as a pair.                                      |
| [**EapHostPeerProcessReceivedPacket**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerprocessreceivedpacket) | Transfers the EAP packet to EAPHost after having received an EAP packet from the server.                                                                                                                             |
| [**EapHostPeerSetResponseAttributes**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeersetresponseattributes) | Provides updated EAP authentication attributes to EAPHost.                                                                                                                                                           |
| [**EapHostPeerSetUIContext**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeersetuicontext)                   | Provides a new or updated user interface context to the EAP peer method loaded on EAPHost.                                                                                                                           |
| [**EapHostPeerUninitialize**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeeruninitialize)                   | Unitializes EapHost for the supplicant. [**EapHostInitialize**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerinitialize) and [**EapHostUninitialize**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeeruninitialize) must be called as a pair.                                      |



 

 

 




