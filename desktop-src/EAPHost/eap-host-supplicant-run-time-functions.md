---
title: EAPHost Supplicant Run-Time Functions
description: EAPHost Supplicant Run-Time Functions
ms.assetid: 'b1c473ba-9a12-4929-b4d0-27262117e9c0'
---

# EAPHost Supplicant Run-Time Functions

The EAP Supplicant API run-time functions are as follows.



| Function                                                                     | Description                                                                                                                                                                                                          |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EapHostPeerBeginSession**](eaphostpeerbeginsession.md)                   | Starts an EAP authentication session.                                                                                                                                                                                |
| [**EapHostPeerClearConnection**](eaphostpeerclearconnection.md)             | Halts all future callbacks to the [**NotificationHandler**](notificationhandler.md) provided by the calling supplicant to EAPHost in a previous call to [**EapHostPeerBeginSession**](eaphostpeerbeginsession.md). |
| [**EapHostPeerEndSession**](eaphostpeerendsession.md)                       | Terminates a current EAP authentication session between EAPHost and the calling supplicant.                                                                                                                          |
| [**EapHostPeerFreeEapError**](eaphostpeerfreeeaperror.md)                   | Frees all EAP error-specific memory returned by EAPHost APIs.                                                                                                                                                        |
| [**EapHostFreeRuntimeMemory**](eaphostpeerfreememory.md)                    | Releases memory space used by run-time APIs.                                                                                                                                                                         |
| [**EapHostPeerGetAuthStatus**](eaphostpeergetauthstatus.md)                 | Obtains the supplicant's current EAP authentication status from EAPHost.                                                                                                                                             |
| [**EapHostPeerGetIdentity**](eaphostpeergetidentity.md)                     | Requests identity information from the inner methods.                                                                                                                                                                |
| [**EapHostPeerGetResponseAttributes**](eaphostpeergetresponseattributes.md) | Obtains an array of EAP authentication attributes from EAPHost.                                                                                                                                                      |
| [**EapHostPeerGetResult**](eaphostpeergetresult.md)                         | Obtains the authentication result for the specified EAP authentication session.                                                                                                                                      |
| [**EapHostPeerGetSendPacket**](eaphostpeergetsendpacket.md)                 | Obtains a packet from EAPHost to send to the authenticator.                                                                                                                                                          |
| [**EapHostPeerGetUIContext**](eaphostpeergetuicontext.md)                   | Obtains the user interface context for the supplicant from EAPHost that is used in the [**EapHostPeerInvokeInteractiveUI**](eaphostpeerinvokeinteractiveui.md) APIs for the supplicant.                             |
| [**EapHostPeerInitialize**](eaphostpeerinitialize.md)                       | Initializes EAPHost for the supplicant. [**EapHostInitialize**](eaphostpeerinitialize.md) and [**EapHostUninitialize**](eaphostpeeruninitialize.md) must be called as a pair.                                      |
| [**EapHostPeerProcessReceivedPacket**](eaphostpeerprocessreceivedpacket.md) | Transfers the EAP packet to EAPHost after having received an EAP packet from the server.                                                                                                                             |
| [**EapHostPeerSetResponseAttributes**](eaphostpeersetresponseattributes.md) | Provides updated EAP authentication attributes to EAPHost.                                                                                                                                                           |
| [**EapHostPeerSetUIContext**](eaphostpeersetuicontext.md)                   | Provides a new or updated user interface context to the EAP peer method loaded on EAPHost.                                                                                                                           |
| [**EapHostPeerUninitialize**](eaphostpeeruninitialize.md)                   | Unitializes EapHost for the supplicant. [**EapHostInitialize**](eaphostpeerinitialize.md) and [**EapHostUninitialize**](eaphostpeeruninitialize.md) must be called as a pair.                                      |



 

 

 




