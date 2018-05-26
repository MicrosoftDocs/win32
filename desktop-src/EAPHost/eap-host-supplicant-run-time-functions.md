---
title: EAPHost Supplicant Run-Time Functions
description: EAPHost Supplicant Run-Time Functions
ms.assetid: b1c473ba-9a12-4929-b4d0-27262117e9c0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EAPHost Supplicant Run-Time Functions

The EAP Supplicant API run-time functions are as follows.



| Function                                                                     | Description                                                                                                                                                                                                          |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapHostPeerBeginSession**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerbeginsession?branch=master)                   | Starts an EAP authentication session.                                                                                                                                                                                |
| [**EapHostPeerClearConnection**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerclearconnection?branch=master)             | Halts all future callbacks to the [**NotificationHandler**](/windows/previous-versions/eappapis/nc-eappapis-notificationhandler?branch=master) provided by the calling supplicant to EAPHost in a previous call to [**EapHostPeerBeginSession**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerbeginsession?branch=master). |
| [**EapHostPeerEndSession**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerendsession?branch=master)                       | Terminates a current EAP authentication session between EAPHost and the calling supplicant.                                                                                                                          |
| [**EapHostPeerFreeEapError**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerfreeeaperror?branch=master)                   | Frees all EAP error-specific memory returned by EAPHost APIs.                                                                                                                                                        |
| [**EapHostFreeRuntimeMemory**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerfreememory?branch=master)                    | Releases memory space used by run-time APIs.                                                                                                                                                                         |
| [**EapHostPeerGetAuthStatus**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeergetauthstatus?branch=master)                 | Obtains the supplicant's current EAP authentication status from EAPHost.                                                                                                                                             |
| [**EapHostPeerGetIdentity**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeergetidentity?branch=master)                     | Requests identity information from the inner methods.                                                                                                                                                                |
| [**EapHostPeerGetResponseAttributes**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeergetresponseattributes?branch=master) | Obtains an array of EAP authentication attributes from EAPHost.                                                                                                                                                      |
| [**EapHostPeerGetResult**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeergetresult?branch=master)                         | Obtains the authentication result for the specified EAP authentication session.                                                                                                                                      |
| [**EapHostPeerGetSendPacket**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeergetsendpacket?branch=master)                 | Obtains a packet from EAPHost to send to the authenticator.                                                                                                                                                          |
| [**EapHostPeerGetUIContext**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeergetuicontext?branch=master)                   | Obtains the user interface context for the supplicant from EAPHost that is used in the [**EapHostPeerInvokeInteractiveUI**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeinteractiveui?branch=master) APIs for the supplicant.                             |
| [**EapHostPeerInitialize**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerinitialize?branch=master)                       | Initializes EAPHost for the supplicant. [**EapHostInitialize**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerinitialize?branch=master) and [**EapHostUninitialize**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeeruninitialize?branch=master) must be called as a pair.                                      |
| [**EapHostPeerProcessReceivedPacket**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerprocessreceivedpacket?branch=master) | Transfers the EAP packet to EAPHost after having received an EAP packet from the server.                                                                                                                             |
| [**EapHostPeerSetResponseAttributes**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeersetresponseattributes?branch=master) | Provides updated EAP authentication attributes to EAPHost.                                                                                                                                                           |
| [**EapHostPeerSetUIContext**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeersetuicontext?branch=master)                   | Provides a new or updated user interface context to the EAP peer method loaded on EAPHost.                                                                                                                           |
| [**EapHostPeerUninitialize**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeeruninitialize?branch=master)                   | Unitializes EapHost for the supplicant. [**EapHostInitialize**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerinitialize?branch=master) and [**EapHostUninitialize**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeeruninitialize?branch=master) must be called as a pair.                                      |



 

 

 




