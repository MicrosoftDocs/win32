---
title: Root Signature Limits
description: The root signature is prime real estate, and there are strict limits and costs to consider.
ms.assetid: 01121D3A-1926-4246-9C20-5E11F2E0B092
ms.topic: article
ms.date: 05/31/2018
---

# Root Signature Limits

The root signature is prime real estate, and there are strict limits and costs to consider.

-   [Memory limits and costs](#memory-limits-and-costs)
-   [Performance costs](#performance-costs)
-   [Static samplers](#static-samplers)
-   [Related topics](#related-topics)

## Memory limits and costs

The maximum size of a root signature is 64 DWORDs.

This maximum size is chosen to prevent abuse of the root signature as a way of storing bulk data. Each entry in the root signature has a cost towards this 64 DWORD limit:

-   Descriptor tables cost 1 DWORD each.
-   Root constants cost 1 DWORD each, since they are 32-bit values.
-   Root descriptors (64-bit GPU virtual addresses) cost 2 DWORDs each.

Static samplers do not have any cost in the size of the root signature.

## Performance costs

The performance cost (in terms of levels of indirection) are zero for a root constant, 1 for a root descriptor, and 2 for a descriptor table. If a root signature is large and overflows out of the fastest memory into slightly slower memory (which can happen on some hardware), then add 1 to the performance cost for the overflowing items at the end of the root signature.

An overflow can occur on hardware that might have, for example, a fixed size of 16 DWORDs for root argument space. This limit might be further reduced by one if the Input Assembler is used. In this case there is overflow into slightly slower memory if the root signature is too large for the 15 or 16 DWORD native memory. In other hardware there is no fixed native root argument memory (so the overflow situation never occurs).

For all hardware, if any root argument changes, the driver must maintain a version of all the root arguments (unlike other storage such as descriptor heaps and buffer resources, which are not versioned by the driver). In hardware that an overflow situation occurs, only the native or overflow area needs to be versioned, depending on where the change occurred. The amount of versioning should obviously be kept to the necessary minimum.

Generally, consider the following guidelines:

-   Use a small a root signature as necessary, though balance this with the flexibility of a larger root signature.
-   Arrange parameters in a large root signature so that the parameters most likely to change often, or if low access latency for a given parameter is important, occur first.
-   If convenient, use root constants or root constant buffer views over putting constant buffer views in a descriptor heap.

## Static samplers

Static samplers (samplers where the state is fully defined and immutable) are part of root signatures, but do not count towards the 64 DWORD limit. If a sampler can be defined as static, there is no need for the sampler to be part of a descriptor heap.

There is no performance cost to using static samplers, and a root signature can contain a mix of static samplers (stored in the root signature, or in reserved space on some hardware) and dynamic samplers (stored in a sampler descriptor heap). Samplers in a descriptor heap can be dynamically assigned and indexed, which static samplers cannot.

Static samplers can be written as part of the root signature in HLSL shaders (refer to [Specifying Root Signatures in HLSL](specifying-root-signatures-in-hlsl.md)).

## Related topics

<dl> <dt>

[Root Signatures](root-signatures.md)
</dt> </dl>

 

 




