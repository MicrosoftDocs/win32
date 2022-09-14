---
description: A line device can represent a pool of homogeneous resources (channels) that are used to establish calls. In a client computer, a TSP typically provides access to one or more line devices.
ms.assetid: cb599a4d-80dd-40fe-b448-f9ea58f01124
title: Line Configurations
ms.topic: article
ms.date: 05/31/2018
---

# Line Configurations

A line device can represent a pool of homogeneous resources (channels) that are used to establish calls. In a client computer, a TSP typically provides access to one or more line devices.

Here are some examples of how a service provider might model various configurations:

**Example 1:** A single POTS line in the computer-centric or phone-centric connection models. The most straightforward model is a single line device with one channel.

**Example 2:** A single BRI-ISDN line in the computer-centric or phone-centric connection models. The service provider has a number of options as to how it may want to model this, for example:

-   Model the BRI line as a single line device with a pool of two B channels that allows both channels to be combined for establishing 128 kbps calls.
-   Model each B-channel as a separate line device and disallow both channels to be combined into a single 128 kbps channel.
-   Model the BRI connection as two separate line devices, each drawing up to two channels from a shared pool of two B-channels.
-   Model as three line devices, one for each B-channel, and one for the combination. Clearly in the latter two models, resources may be assigned to different line devices at different times.

**Example 3:** In client/server systems, a pool of telephone ports attached to a server can be shared among multiple client computers over a local area network. The pool can be administered to assign a maximum number of line devices (quota) to each client workstation. It is not unusual for the sum of all quotas to exceed the total number of lines. Furthermore, a given client with a quota equal to 2 may be satisfied by using ports 1 and 2 at one time and ports 7 and 11 at a later time. The service provider for the pool can model this arrangement by giving each client workstation access to two line devices.

Suppose that the configuration of service providers for a given computer is such that this particular service provider gets a **DeviceIDBase** of 3. This implies that the (fixed) device identifiers for this client are 3 and 4. If the application later calls the TAPI 2 function [**lineGetDevCaps**](/windows/win32/api/tapi/nf-tapi-linegetdevcaps) for device 3 and again for device 4, it should be able to assume that the device capabilities for each of these devices are constant, because that is the device model. As long as the given computer's service-provider configuration remains constant, the device identifiers that appear at the TSPI level remain constant, even if the server changes port allocations. For server-based devices that are pooled as described in Example 3, this holds only for line devices that have identical device capabilities. Of course, if the given computer's service-provider configuration is changed, such that this service provider gets a different **DeviceIDBase**, device identifiers change correspondingly.

**Example 4:** Switch-to-host link:

-   To provide personal telephony to each desktop, the service provider could model the PBX line paired with the computer as a single line device with one channel. Each client computer would have one line device available.
-   Each third-party station could be modeled as a separate line device. This enables the application to control calls on other stations. This solution requires that the application open each line it wants to manipulate or monitor, which may be fine if only a small number of lines is of interest, but may generate a lot of overhead if a large number of lines is involved.
-   The set of all third-party stations could be modeled as a single line device with one address (phone number) assigned to it per station. Only a single device is to be opened, providing monitoring and control of all addresses on the line (all stations). To originate a call on any of these stations, the application only needs to specify the station's address to the operation that makes the call. No extra open operations are required. This modeling does imply that all stations have the same line device capabilities, although their address capabilities could be different.

> [!Note]  
> All of these examples are simply different ways that a service provider may choose to implement the mapping of line device behavior onto some physical realization.

 

 

 
