---
title: Development vs. Deployment in the Network
description: Most developers write and test their software on a fast reliable LAN.
ms.assetid: 9458162c-1046-4554-bafa-b455f2957d58
ms.topic: article
ms.date: 05/31/2018
---

# Development vs. Deployment in the Network

Most developers write and test their software on a fast reliable LAN. Their client and server are often on the same network segment. In such circumstances the network is rarely unresponsive, and connectivity rarely lost. When deployed in a customer environment however, client and server are often on different network segments, possibly geographically remote, and the server is heavily loaded with other clients. In other words: network responsiveness cannot be assumed.

This article explains how to construct robust client/server architectures in the face of uncertainty introduced by an intrinsically unreliable network and potentially unavailable servers.

 

 




