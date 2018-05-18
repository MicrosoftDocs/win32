---
title: Default RSVP Filter Style Settings
description: The RSVP SP sets RSVP reservation style (also referred to as a filter style) based on the type of socket on which the reservation request is based.
ms.assetid: 'b56162bd-6375-4b37-9ce8-307d35ff1b36'
---

# Default RSVP Filter Style Settings

The RSVP SP sets RSVP reservation style (also referred to as a **filter style**) based on the type of socket on which the reservation request is based. Default settings are applied to their corresponding connection types when the RSVP SP makes RSVP signaling requests on behalf of an application when there is no reservation, and when RSVP\_DEFAULT\_STYLE is specified in the Style member of the [**RSVP\_RESERVE\_INFO**](rsvp-reserve-info.md) object.

Note that these default settings can be overridden by setting the **Style** member of the [**RSVP\_RESERVE\_INFO**](rsvp-reserve-info.md) object to one of the other available RSVP filter styles.

## Unicast Receivers

Applications that request QOS service provisions for unicast sessions are assumed to require the Fixed Filter (FF) RSVP reservation style. While TCP receivers are always assumed to be unicast receivers, only UDP unicast receivers that use the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function are provided with the Fixed Filter RSVP reservation style; otherwise, UDP unicast receivers are provided with the Wildcard Filter (WF) RSVP reservation style.

## Multicast Receivers

Applications that request QOS service provisions for multicast sessions are assumed to require the Wildcard Filter (WF) RSVP reservation style.

## Use of the RSVP\_DEFAULT\_STYLE Filter Style

The RSVP\_DEFAULT\_STYLE filter style enables an application developer to specify parameters in other members of the [**RSVP\_RESERVE\_INFO**](rsvp-reserve-info.md) object without having to explicitly indicate (or override) the RSVP filter style applied by the RSVP SP.

When the connection is TCP or connected UDP, specifying RSVP\_DEFAULT\_STYLE implements the Fixed Filter (FF) style.

When the connection is multicast or unconnected UDP, specifying RSVP\_DEFAULT\_STYLE implements the Wildcard Filter (WF) style.

 

 




