---
description: The Media Service Provider Interface (MSPI) is a set of interfaces and methods implemented by an MSP to allow a TAPI 3 application control over media transport during a communications session.
ms.assetid: 53b7bcbd-571a-44da-a6db-10d4c3e5d30a
title: Media Service Provider Interface (MSPI)
ms.topic: article
ms.date: 05/31/2018
---

# Media Service Provider Interface (MSPI)

The Media Service Provider Interface (MSPI) is a set of interfaces and methods implemented by an MSP to allow a TAPI 3 application control over media transport during a communications session. An MSP handles the device-specific and protocol-specific mechanisms needed to enact these controls, and communicates with its paired TSP or an application through use of the methods provided in the MSPI.

The following section ( [Media Service Provider Interface (MSPI) Reference](media-service-provider-interface-mspi-reference.md)) details the interfaces an MSP exposes in order to interact with the Microsoft Telephony environment.

In addition, an MSP may expose provider-specific private interfaces and methods to further assist in media control. For example, the [IP Conference MSP](ipconf-msp.md) exposes interfaces that provide participant control. See [Provider-Specific Interfaces](provider-specific-interfaces.md) for information on how private objects work and [IPConf MSP Interfaces](ipconf-msp-interfaces.md) for a reference listing of IPConf.

The majority of the programming effort in creating an MSP is highly specific to a given platform, device, and transport protocol, and is outside the scope of this document. However, Microsoft supplies a set of MSP base classes, which will be useful to most MSP authors. See [TAPI 3 MSP Base Classes](tapi-3-msp-base-classes.md) for information on using these classes.

The [**ITMSPAddress**](/windows/desktop/api/msp/nn-msp-itmspaddress) interface represents a media service provider to the TAPI DLL. This interface is not used by or exposed to an end-user application. The TAPI 3 DLL calls **CoCreateInstance** on this interface to create the main MSP object. Methods on this object allow an application to load and unload the MSP, receive information from a TSP, and create the [**ITStreamControl**](/windows/win32/api/tapi3if/nn-tapi3if-itstreamcontrol) interface, which is exposed on the call object.

The [**ITSubStreamControl**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstreamcontrol) and [**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream) interfaces provide parallel methods with respect to substreams. Substream support is optional. All other interfaces must be implemented by an MSP.

> [!Note]  
> Operations implemented by a TSP/MSP pair must be located in one DLL to allow a user to update the service provider without rebooting his or her system.

 

 

 
