---
description: Service providers can expose each resource on the PBX as a line device and possibly an associated phone device.
ms.assetid: 25394b19-bf75-4adc-b07d-41bc781931b6
title: Modeling of a Call Center
ms.topic: article
ms.date: 05/31/2018
---

# Modeling of a Call Center

Service providers can expose each resource on the PBX as a line device and possibly an associated phone device. Terminals that support multiple call appearances would do so through multiple addresses, just as in first-party call control. In fact, the third-party view of a device is identical to the first-party view; applications on the server can see and control all of the first-party devices, whereas an individual client PC connected to the server can only see those devices that are made visible to it through access controls administered by TAPISRV on the server. Resources other than terminals can also be modeled as line devices. For example, an ACD queue or route point would be modeled as a line device that could have many active calls; an IVR server, voice mail server, or set of predictive dialing ports could also be modeled as a line device that supports multiple calls.

Within this model, the status of the addressed device and calls associated with it can be monitored though existing TAPI messages such as [**LINE\_LINEDEVSTATE**](line-linedevstate.md), [**LINE\_ADDRESSSTATE**](line-addressstate.md), [**LINE\_CALLSTATE**](line-callstate.md), and [**LINE\_CALLINFO**](line-callinfo.md), and details obtained through functions such as [**lineGetLineDevStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetlinedevstatus), [**lineGetAddressStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus), [**lineGetCallStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetcallstatus), and [**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo). Whenever a TAPI object is operated upon through a third-party application running on the server, the result is identical to what would have occurred if the same object had been similarly operated on by a first-party application running on a client PC associated with that device. Status indications sent by the server service provider controlling the switching fabric (or switch) are delivered both to applications running on the server and to those running on associated, authorized clients.

 

 



