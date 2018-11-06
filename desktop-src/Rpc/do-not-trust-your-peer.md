---
title: Do Not Trust Your Peer
description: '\ 0034;Do not trust your peer \ 0034; is a basic security rule, but it is often overlooked.'
ms.assetid: 776c1c99-feb1-415c-9a18-e9bf581bc3ff
ms.topic: article
ms.date: 05/31/2018
---

# Do Not Trust Your Peer

"Do not trust your peer" is a basic security rule, but it is often overlooked. Do not assume the other party in a communication will behave properly, and do not assume your peer will pass the data you expect. MIDL and RPC perform some checks on your behalf, but not all checks.

Know which aspect of the parameters are verified by MIDL or RPC, and which aspects you must verify yourself. For example, for in/out context handles, RPC verifies the context handle is not an invalid non-null value. It allows null values and valid values, but many developers are not aware that null values are let through. This is something to check for.

Even if you generally trust your peer, be sure not to introduce new paths by which a compromised machine or principal account can attack other machines. Imagine that a user chooses his birthday as his password, and it is guessed by an attacker. Even after requests from the user are authenticated and access to his data is allowed, make sure exploitable vulnerabilities do not exist, such stack overruns that may allow an attacker to take control of your server and extend the security breach.

 

 




