---
description: Before a socket can be used to set up a connection or receive a connection request, it needs to be bound to a local address.
ms.assetid: 8767a209-e293-47cd-b503-ff4cffbf6fb4
title: Binding to a Local Address
ms.topic: article
ms.date: 05/31/2018
---

# Binding to a Local Address

Before a socket can be used to set up a connection or receive a connection request, it needs to be bound to a local address. This could be done explicitly by calling [**WSPBind**](/previous-versions/windows/hardware/network/ff566268(v=vs.85)), or implicitly by [**WSPConnect**](/previous-versions/windows/hardware/network/ff566275(v=vs.85)) if the socket is unbound when this function is called.

 

 
