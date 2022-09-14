---
description: TAPI 3 defines five main ACD objects the Agent Handler the Queue the ACD Group the Agent and the Agent Session. It also extends the TAPI object with an additional interface ITTAPICallCenter.
ms.assetid: 6b24e8aa-fef4-44aa-8d2b-33b9be3d6ea7
title: About Call Center Controls
ms.topic: article
ms.date: 05/31/2018
---

# About Call Center Controls

TAPI 3 defines five main ACD objects: the Agent Handler, the Queue, the ACD Group, the Agent, and the Agent Session. It also extends the TAPI object with an additional interface— [**ITTAPICallCenter**](/windows/win32/api/tapi3cc/nn-tapi3cc-ittapicallcenter).

## Agent Object

The Agent object represents an agent capable of handling calls. This is usually a person but may be an IVR or some other combination of software and hardware. Agents are key to a call center; they are responsible for receiving and processing incoming calls and, at times, making outgoing calls to customers or prospects.

In TAPI, the Agent object directly relates to a user account, to provide compatibility with existing legacy switching systems. Additionally, to provide compatibility with existing legacy switching systems, the Agent may also be related to a switch agent ID.

The Agent object exposes the [**ITAgent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagent) interface. This interface implements methods that can create an Agent Session and retrieve statistics such as total calls handled. Applications can use the Agent object to manipulate Agent State and determine global agent statistics.

## Agent Handler Object

An Agent Handler represents software or hardware capable of passing calls to a group of agents. Typically, this is a proprietary switch connecting outside lines to telephones at agent stations. Most ACD systems have only one such switch, but large operations may have more. In the case where an agent has devices on more than one ACD system, the agent will see a corresponding number of Agent Handler objects. There will also be an instance of the Agent object relating to the agent's appearance on each ACD system.

The Agent Handler object exposes the [**ITAgentHandler**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagenthandler) interface. This interface implements methods that provide information on the [ACD Groups](#acd-group-object) associated with the Agent Handler and the addresses that it can use.

## Agent Session Object

An Agent Session represents an agent who has logged in and is qualified to handle calls for a particular [ACD Group](#acd-group-object). An Agent Session is a dynamically created object, which relates an agent to an ACD group, for which they will provide service, and also to the address, where they will receive calls (turret, station, phone, etc.). Applications can use the Agent Session object to track the agent activity within a particular ACD group.

The Agent Session object exposes the [**ITAgentSession**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagentsession) interface. This interface implements methods that can retrieve information such as average talk time for a call.

## ACD Group Object

An ACD Group represents a class of calls that requires a particular type of handling. For example, some incoming calls for a bank's call center may concern existing accounts and others may relate to new accounts. Some agents may have expertise in both areas but most will specialize in one. ACD Groups will be created to handle each type of call. An ACD group services one or more queues. As incoming calls are classified, they will be passed to queues associated with the relevant ACD Group. A call coming off the queue is passed to an agent who has created an [Agent Session Object](#agent-session-object) indicating they are able to handle calls from that ACD Group.

The ACD Group Object exposes the [**ITACDGroup**](/windows/win32/api/tapi3cc/nn-tapi3cc-itacdgroup) interface. This interface implements methods that provide access to the queues associated with the current ACD Group.

## Queue Object

The Queue object represents a point within the ACD system where calls are temporarily held pending action. The Queue object exposes the [**ITQueue**](/windows/win32/api/tapi3cc/nn-tapi3cc-itqueue) interface. This interface implements methods that gather statistics on a queue, such the number of calls currently queued. The [ACD Proxy](acd-proxy.md) uses this information to distribute calls to Agents and to produce administrative reports.

Access to a Queue object allows an application to read a variety of standard statistics relating to queue usage, but does not give it the ability to control calls on the queue. Only applications with access to the associated addresses and lines (typically the ACD proxy application) would be able to control the calls on the queue.

Most queues relate directly to an [ACD Group Object](#acd-group-object), and will hold a call until an agent can handle it. Other queues may exist to allow for complex call guides (the defined path an unanswered call will take through a switch). For example, calls may be placed in holding queues before being routed to a queue serviced by an ACD group.

 

 
