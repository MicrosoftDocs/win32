---
title: LPM Byte Reordering
description: The RSVP protocol submits policy information in network-byte order.
ms.assetid: '5477ebe9-7e1b-4e07-ae1c-9be4d627f910'
---

# LPM Byte Reordering

The RSVP protocol submits policy information in network-byte order, as illustrated in the following example:

``` syntax
0 1 2 3 4 5 6 7
```

As you can see from the example, in network-byte ordering, the bits in any given byte are ordered such that the first bit (base zero) is bit zero, and the following bits are ordered sequentially through the last bit (bit position seven, base zero).

The Microsoft LPM, Msidlpm.dll, reorders these bits in host-byte order. This is an important distinction because bit-based flags can be used to designate certain values in the PCM-LPM interaction. The following example illustrates host-byte ordering:

``` syntax
7 6 5 4 3 2 1 0
```

Host-byte ordering begins with the last bit in the byte (bit position seven, base zero) and progresses sequentially through the byte to bit position zero.

 

 




