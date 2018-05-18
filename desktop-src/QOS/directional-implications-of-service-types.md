---
title: Directional Implications of Service Types
description: The impact of specifying each of these service types differs depending on whether is it sent in the SendingFlowspec or the ReceivingFlowspecparameter.
ms.assetid: '895efcac-1b59-4f4c-a180-df26222ad212'
---

# Directional Implications of Service Types

The impact of specifying each of these service types differs depending on whether is it sent in the SendingFlowspec or the ReceivingFlowspecparameter. To illustrate the impact of specifying any of these service types, the following table explains the implications of each, depending on whether the service type is specified in SendingFlowspec or ReceivingFlowspec.



| Service Types                   | In SendingFlowspec                                                                                                                                                                                                                                                                           | In ReceivingFlowspec                                                                                                                                                                                                                                                       |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BESTEFFORT                      | Indicates that only best-effort service is supported for this traffic flow.                                                                                                                                                                                                                  | Requests best-effort service (no RSVP signaling treatment).                                                                                                                                                                                                                |
| NOTRAFFIC                       | Indicates that there will be no traffic in this direction.                                                                                                                                                                                                                                   | Indicates that there will be no traffic in this direction.                                                                                                                                                                                                                 |
| CONTROLLEDLOAD                  | Indicates that only controlled load service is supported for this traffic flow.                                                                                                                                                                                                              | Asks the network for a controlled load reservation.                                                                                                                                                                                                                        |
| GUARANTEED                      | Indicates that only guaranteed service is supported for this traffic flow.                                                                                                                                                                                                                   | Asks the network for a guaranteed reservation.                                                                                                                                                                                                                             |
| QUALITATIVE                     | Indicates that only qualitative service is requested for this traffic flow.                                                                                                                                                                                                                  | Indicates that qualitative service is being requested for the traffic flow.                                                                                                                                                                                                |
| GENERAL\_INFORMATION<br/> | Indicates that all service types are supported or this traffic flow.                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                                                        |
| NO\_CHANGE                      | Allows an application to modify quality of service in the receiving direction, while leaving the sending unchanged, or to provide [ProviderSpecific](the-providerspecific-buffer.md) parameters without altering values previously specified in the [**FLOWSPEC**](flowspec.md) structure. | Allows an application to modify quality of service in the sending direction, while leaving the receiving direction unchanged, or to provide ProviderSpecific buffer parameters without altering values previously specified in the [**FLOWSPEC**](flowspec.md) structure. |



 

 

Note that a sending application can specify a ServiceType parameter in the SendingFlowspec set to CONTROLLED\_LOAD or GUARANTEED if it wants to limit the service type options presented to the receiver to just one service type. If the SendingFlowspecypes will be advertised as available from the sender (although intervening routers may indicate that they do not support one or both service types).

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

 

 





