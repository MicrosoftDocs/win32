---
description: Normally, a media service provider (MSP) implements terminal creation.
ms.assetid: 203fccc0-aa5a-4ec3-97d3-546c36018d52
title: Writing a Pluggable Terminal
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Pluggable Terminal

Normally, a media service provider (MSP) implements terminal creation. Starting with Windows 2000 SP1, TAPI 3 includes pluggable terminals to allow an application to implement terminal creation. Please see the overview on [implementing pluggable terminals](implementing-pluggable-terminals.md) for additional information on using these terminals.

You should not use pluggable terminals routinely because the full capabilities of a terminal will only be available when an MSP is fully aware of it. Further, you should not attempt to implement pluggable terminals unless you are already familiar with writing media service providers. The techniques and potential problems involved are quite similar.

Provision for a special case of pluggable terminal currently exists for the situation of a conferencing server that needs to add non-Windows 2000 SP1 or nonmulticast H.323 clients to TAPI 3 multiparty SDP/IP multicast conferences.

 

 



