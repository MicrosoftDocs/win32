---
title: RaytracingAccelerationStructure 
description: A resource type that can be declared in HLSL and passed into TraceRay to indicate the top-level acceleration resource built using BuildRaytracingAccelerationStructure.
ms.assetid: 
ms.topic: language-reference
ms.date: 05/31/2018
---

# RaytracingAccelerationStructure

A resource type that can be declared in HLSL and passed into [**TraceRay**](traceray-function.md) to indicate the top-level acceleration resource built using **BuildRaytracingAccelerationStructure**. It is bound as a raw buffer SRV in a descriptor table or root descriptor SRV.  The declaration in HLSL is as follows:


```
RaytracingAccelerationStructure MyScene[] : register(t3,space1);
```

This example shows an unbounded size array of acceleration structures, which implies coming from a descriptor heap since root descriptors can’t be indexed.

**RaytracingAccelerationStructure** is an opaque resource with no methods available to shaders.


 

 




