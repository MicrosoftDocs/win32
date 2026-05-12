---
title: How secure is my RPC server now
description: Following the security outlined in this section, provided elsewhere in the RPC SDK, and generally accepted as proper security practices, will result in a server that is very secure. Such servers are protected from penetration attacks or privacy breaches.
ms.assetid: 528ff35c-f37c-43d8-8cc1-dbc36a9a826c
ms.topic: concept-article
ms.date: 05/31/2024
---

# How secure is my RPC server now?

Following the security outlined in this section, and provided elsewhere in the RPC SDK, and generally accepted as proper security practices, will result in a server that has increased security. Such servers are compararively more protected from penetration attacks and privacy breaches.

If state is kept between RPC calls, then make sure that a single client doesn't cause the allocation of excessive resources. Allocating excessive resources could potentially deny service to other clients.
