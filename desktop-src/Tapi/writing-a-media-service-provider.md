---
description: A media service provider must implement a minimum subset of MSPI interfaces ITMSPAddress ITTerminalSupport ITStreamControl and ITStream.
ms.assetid: 59560bdf-953e-48e8-b565-46c3e0123c7e
title: Writing a Media Service Provider
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Media Service Provider

A media service provider must implement a minimum subset of MSPI interfaces: [**ITMSPAddress**](/windows/desktop/api/msp/nn-msp-itmspaddress), [**ITTerminalSupport**](/windows/win32/api/tapi3if/nn-tapi3if-itterminalsupport), [**ITStreamControl**](/windows/win32/api/tapi3if/nn-tapi3if-itstreamcontrol), and [**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream). SubStream support is optional. In addition, a given MSP may implement additional methods, such as controls required for specialized hardware.

The following material documents:

-   The [TAPI 3 MSP Base Classes](tapi-3-msp-base-classes.md), which are a set of C++ classes designed to simplify the task of building a DirectShow-based MSP. The base classes implement all the MSPI interfaces in a generic manner. Different MSPs can override MSP-specific functions and provide their own implementations.
-   The [TAPI 3 Terminal Manager](tapi-3-terminal-manager.md), which provides interfaces and methods used by an MSP to control terminals.
-   [Pluggable Terminals](writing-a-pluggable-terminal.md), which allow an application instead of an MSP to create terminals. Developers who are already experienced at writing service providers will be the primary creators of pluggable terminals. The initial version implemented for this release is aimed at conferencing server applications that need to add non-Windows 2000 or non-multicast clients to TAPI 3 multi-party SDP/IP multicast conferences.

 

 
