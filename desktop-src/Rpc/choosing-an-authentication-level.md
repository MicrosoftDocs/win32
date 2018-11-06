---
title: Choosing an Authentication Level
description: When choosing an authentication level, use the following guideline.
ms.assetid: 6efb4162-5884-4bcb-86da-4809f89f0c26
ms.topic: article
ms.date: 05/31/2018
---

# Choosing an Authentication Level

When choosing an authentication level, use the following guideline. If it does not matter whether the data being sent can be intercepted and modified, and the data received can be intercepted or modified, use RPC\_C\_AUTHN\_LEVEL\_NONE, which is the default. If the data should not be modified, and private data is not being sent or received, use RPC\_C\_AUTHN\_LEVEL\_PKT\_INTEGRITY. In all other cases, use RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY.

Do not use RPC\_C\_AUTHN\_LEVEL\_DEFAULT, RPC\_C\_AUTHN\_LEVEL\_CONNECT, RPC\_C\_AUTHN\_LEVEL\_CALL or RPC\_C\_AUTHN\_LEVEL\_PKT. A sophisticated attacker can break these authentication levels and render them ineffective. Each of these levels does make it slightly more difficult for an attacker to intercept and modify data, and to impersonate, but security is not really achieved. Since the sophistication level of an attacker is rarely known, these are not wise choices.

 

 




