---
title: Transfer Syntax and NDR64
description: The NDR wire protocol, also referred to as transfer syntax, enables RPC calls to traverse the network.
ms.assetid: 30b3843a-172c-4d08-beed-c68bcb68daaf
ms.topic: article
ms.date: 05/31/2018
---

# Transfer Syntax and NDR64

The NDR wire protocol, also referred to as transfer syntax, enables RPC calls to traverse the network. The wire protocol defines the wire representation of an RPC call, such as the order in which data members are marshaled, alignment of data on the wire, additional information included with the data, and other issues. The NDR64 protocol is an extension to the 32-bit based NDR transfer syntax, created specifically to enable developers targeting 64-bit systems to achieve optimized performance.

The differences between the NDR wire format and the NDR64 wire format addresses the different size of pointers in a 64-bit environment, as well as other issues. The mechanics of NDR64 is handled by RPC. Developers need only use the /[**protocol**](/windows/desktop/Midl/-protocol)**all** MIDL command line switch to obtain the benefits of NDR64 on 64-bit platforms. NDR64 is available only on 64-bit platforms.

 

 