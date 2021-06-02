---
description: The media type (or mode) of a device describes the type of information that can be exchanged, such as interactive voice. A given device might be able to handle only one media type, or it might be able to deal with a range of types.
ms.assetid: fccf85e9-3889-4ebc-b1bf-a60e27ab4586
title: Media Type
ms.topic: article
ms.date: 05/31/2018
---

# Media Type

The *media type* (or mode) of a device describes the type of information that can be exchanged, such as interactive voice. A given device might be able to handle only one media type, or it might be able to deal with a range of types.

Service providers expose the media type or types supported by the devices they control. Applications query for media type and then use this information to select an appropriate address on which to initiate a session. Application response to a session offered may also be predicated on media type.

A given communications session, or call, can involve several media types. For further information, see Media type for a session.

**TAPI 2.x:** See [**lineGetAddressCaps**](/windows/win32/api/tapi/nf-tapi-linegetaddresscaps), **dwAvailableMediaModes** member of [**LINEADDRESSCAPS**](/windows/win32/api/tapi/ns-tapi-lineaddresscaps) structure pointed to by *lpAddressCaps*, [LINEMEDIAMODE\_ Constants](./linemediamode--constants.md).

**TAPI 3.x:** See [**ITTerminal::get\_MediaType**](/windows/win32/api/tapi3if/nf-tapi3if-itterminal-get_mediatype), [TAPIMEDIATYPE\_ Constants](tapimediatype--constants.md).
