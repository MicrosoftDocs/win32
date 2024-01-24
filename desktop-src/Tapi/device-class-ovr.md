---
description: Device classes simplify development by letting programmers treat devices that have similar properties in a similar manner.
ms.assetid: 061f3037-1c71-4da1-88d7-29906c136d7b
title: Device Class (TAPI)
ms.topic: article
ms.date: 05/31/2018
---

# Device Class

Device classes simplify development by letting programmers treat devices that have similar properties in a similar manner. For example, a digital phone in an office typically has more capabilities than a standard handset in a home, but both respond in much the same way to a basic set of functions, and both belong to a phone device class. Device classes help make TAPI extensible by providing a framework from which to classify and support new equipment.

See [TAPI Device Classes](./tapi-device-classes.md) for classes that TAPI has predefined. A service provider may implement and define additional device classes for the equipment it supports. An application never needs to know which service provider controls which device, but may require information on the control of new device classes.

A service provider implements a device class by mapping requests into actual device commands. For example, when the service provider for a Hayes-compatible modem receives a command passed through TAPISVR to make a call, it sends classic AT commands to the modem.

The service provider interface can be mapped to a wide range of environments, including those not traditionally thought of as belonging to telephony. An example is multimedia conferencing over an IP-based network such as the Internet.

Application developers should keep in mind the existence of other applications that may share telephony services.

 

 
