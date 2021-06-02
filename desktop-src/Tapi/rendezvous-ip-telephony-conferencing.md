---
description: The TAPI 3 Rendezvous controls enable a programmer to create applications that can create and discover multimedia multicast IP conferences.
ms.assetid: '4da2046c-00fd-46a8-805f-503729cfa531'
title: Rendezvous IP Telephony Conferencing
ms.topic: article
ms.date: 05/31/2018
---

# Rendezvous IP Telephony Conferencing

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The TAPI 3 Rendezvous controls enable a programmer to create applications that can create and discover multimedia multicast IP conferences.

The key components of Rendezvous:

[Directory Controls](directory-controls.md) are an abstraction of conference listings on an ILS or NTDS server.

[Conference Blob Controls](conference-blob-controls.md) represent conference-specific information such as start and stop time. Special interfaces are provided for SDP protocol blobs. For detailed information, see RFC 2327 entitled "SDP: Session Description Protocol." A current copy of this RFC can be located using an Internet search engine.

[Multicast COM Interfaces](multicast-com-interfaces.md) are COM wrappers for the MADCAP functions, formerly know as MDHCP. These interfaces allow an application to get multicast addresses from a multicast address allocation server.

The following material provides a general overview and some usage examples of the Rendezvous controls for IP telephony and conferencing.

 

 



