---
description: The primary pieces of information an application supplies to initiate a communications session are the address type, the media type or types, and the destination address.
ms.assetid: 65e53587-0e40-411b-8d6c-d6adfc9d1e6c
title: Initiate a Session
ms.topic: article
ms.date: 05/31/2018
---

# Initiate a Session

The primary pieces of information an application supplies to initiate a communications session are the [address type](address-type-ovr.md), the [media type](media-type-ovr.md) or types, and the destination [address](address-ovr.md).

The destination address may require [address translation](#address-translation) to put the information entered by a user into the proper format for a given address type. For example, a phone number that was in an electronic address book in [canonical](address-ovr.md) format will require translation to [dialable](address-ovr.md) format.

Some sessions may require special setup parameters, if supported by the service provider. For example, an ISDN TSP can transmit user-user information, and some MSPs require information about media stream direction. Please see [Session Information](session-information-ovr.md) for a review of data that may be set or obtained concerning a session.

Once a session has been initiated, TAPI will inform the application of call progress using the event notification mechanism set up during initialization.

**TAPI 2.x:** Applications initiate a session using the [**lineMakeCall**](/windows/win32/api/tapi/nf-tapi-linemakecall) function. The [**lineTranslateAddress**](/windows/win32/api/tapi/nf-tapi-linetranslateaddress) function is used to perform address translation, if required.

Call setup parameters can be stored in the [**LINECALLPARAMS**](/windows/win32/api/tapi/ns-tapi-linecallparams) data structure, and a pointer to this structure is then used as a parameter of [**lineMakeCall**](/windows/win32/api/tapi/nf-tapi-linemakecall). If no **LINECALLPARAMS** structure is supplied to **lineMakeCall**, a default POTS voice-grade call is requested with a set of default values.

If the session is set up successfully, a call handle with *owner* [privileges](privilege-ovr.md) is returned to the application and TAPI sends the application [**LINE\_CALLSTATE**](./line-callstate.md) messages with information concerning the call's progress. Applications typically use these messages to display status reports to the user.

**TAPI 3.x:** Applications initiate a communications session by invoking the [**ITAddress::CreateCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddress-createcall) method on an address capable of handling the address type and media type required. If the address exposes the [**ITTerminalSupport**](/windows/win32/api/tapi3if/nn-tapi3if-itterminalsupport) interface, terminals are selected onto the media streams of the call object. See the [Make a Call](make-a-call.md) code example for an illustration of this process.

Call setup parameters can be stored or changed using methods exposed by the [**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo) interface.

If the session is set up successfully, TAPI returns an [**ITBasicCallControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasiccallcontrol) interface pointer that can be used for further session operations, or to obtain an [**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo) interface pointer that can be used to acquire additional session information. The [**ITCallStateEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallstateevent) interface processes TAPI call state events.

> [!Note]  
> TAPI should not be used for fax transmissions. Instead, use the functions available through MAPI, the Microsoft Messaging API.

 

## Address Translation

An end-user or server application may store addresses in a format that is not compatible with the needs of a given service provider. For example, a phone number may be stored in an electronic address book in [canonical format](address-ovr.md), but most service providers that handle phone numbers require the [dialable format](address-ovr.md).

TAPI supplies address translation operations that assist an application in presenting the correct address type to a TSP. The service provider specifies to TAPI which address types it supports, and need not include any form of address translation.

**TAPI 2.x:** See [**lineTranslateAddress**](/windows/win32/api/tapi/nf-tapi-linetranslateaddress).

**TAPI 3:** See [**ITAddressTranslation**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresstranslation), [**ITAddressTranslationInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresstranslationinfo).

## Toll Lists

In some locations in North America, all telephone calls placed to the local area code are local calls. In other locations, some calls placed to the local area code are long distance, and need a "1" prefix to be dialed. The first three digits of the address (the prefix) determine whether or not a call within the local area code is a toll call.

A *toll list* is a list of prefixes in the local area code whose addresses must be dialed as long-distance addresses, and are assessed long-distance charges.

Toll lists are not relevant to service providers, or to applications that do not access a telephone network.

**TAPI 2.x:** See [**lineTranslateAddress**](/windows/win32/api/tapi/nf-tapi-linetranslateaddress) (LINETRANSLATERESULT\_INTOLLLIST and LINETRANSLATERESULT\_NOTINTOLLLIST bits in the [**LINETRANSLATEOUTPUT**](/windows/win32/api/tapi/ns-tapi-linetranslateoutput) structure), [**lineSetTollList**](/windows/win32/api/tapi/nf-tapi-linesettolllist).

**TAPI 3:** See [**ITAddressTranslation::TranslateAddress**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddresstranslation-translateaddress), [**ITAddressTranslationInfo::get\_TranslationResults**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddresstranslationinfo-get_translationresults).

 

 
