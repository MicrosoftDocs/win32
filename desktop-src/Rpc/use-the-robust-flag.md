---
title: Use the /robust Flag
description: Always compile .idl files using the /robust switch.
ms.assetid: bb2fd026-3ad8-4bb5-b05e-4835b874882f
ms.topic: article
ms.date: 05/31/2018
---

# Use the /robust Flag

Always compile .idl files using the [**/robust**](/windows/desktop/Midl/-robust) switch. Using the **/robust** switch generates additional information that enables the Network Data Representation (NDR) engine to perform run-time error checking on correlated arguments in dynamic arrays, unions, and in out interface pointers in COM and RPC applications. If software fails to compile with this flag, the software is so exposed to attacks that no efforts in any other area can protect it.

 

 