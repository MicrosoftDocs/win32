---
title: Differences in the Binding Model from Direct3D 11
description: One of the main design decisions behind DirectX12 binding is to separate it from other management tasks. This places some requirements on the app to manage certain potential hazards.
ms.assetid: 3EE7E9AE-203D-40D4-9F12-4313ED179035
ms.topic: article
ms.date: 05/31/2018
---

# Differences in the Binding Model from Direct3D 11

One of the main design decisions behind DirectX12 binding is to separate it from other management tasks. This places some requirements on the app to manage certain potential hazards.

The main advantage of the D3D12 Binding Model is that it enables apps to change texture bindings frequently, without a huge CPU performance cost. Other benefits are that shaders have access to a very large number of resources, shaders need not know in advance how many resources will be bound, and that a unified resource binding model can be used regardless of hardware or the apps content flow.

To improve performance, the binding model does not require the system to keep track of what bindings an app has requested the GPU to use, and there is a clean integration between binding and multi-threaded command lists.

The following sections list some of the changes to the resource binding model since D3D11.

-   [Memory Residency Management Separated From Binding](#memory-residency-management-separated-from-binding)
-   [Object Lifetime Management Separated From Binding](#object-lifetime-management-separated-from-binding)
-   [Driver Resource State Tracking Separated From Binding](#driver-resource-state-tracking-separated-from-binding)
-   [CPU GPU Mapped Memory Synchronization Separated From Binding](#cpu-gpu-mapped-memory-synchronization-separated-from-binding)
-   [Related topics](#related-topics)

## Memory Residency Management Separated From Binding

Applications have explicit control over which surfaces they need to be available for the GPU to use directly (called being "resident"). Conversely, they can apply other states on resources such as explicitly making them not resident, or letting the OS choose for certain classes of applications that require a minimal memory footprint. The important point here is that the application's management of what is resident is completely decoupled from how it gives access to resources to shaders.

The decoupling of residency management from the mechanism for giving shaders access to resources reduces the system/hardware cost for rendering since the OS doesn't have to constantly inspect the local binding state to know what to make resident. Furthermore, shaders no longer have to know which exact surfaces they may need to reference, as long as the entire set of possibly accessible resources has been made resident ahead of time.

## Object Lifetime Management Separated From Binding

Unlike previous APIs, the system no longer tracks bindings of resources to the pipeline. This used to enable the system to keep alive resources that the application has released because they are still referenced by outstanding GPU work.

Before freeing any resource, such as a texture, applications now must make sure the GPU has completed referencing it. This means before an application can safely free a resource the GPU must have completed execution of the command list referencing the resource.

## Driver Resource State Tracking Separated From Binding

The system no longer inspects resource bindings to understand when resource transitions have occurred which require additional driver or GPU work. A common example for many GPUs and drivers is having to know when a surface transitions from being used as a Render Target View (RTV) to Shader Resource View (SRV). Applications themselves must now identify when any resource transitions that the system might care about are happening via dedicated APIs.

## CPU GPU Mapped Memory Synchronization Separated From Binding

The system no longer inspects resource bindings to understand if rendering needs to be delayed because it depends on a resource that has been mapped for CPU access but has not been unmapped yet. Applications now have the responsibility to synchronize CPU and GPU memory accesses. To help with this, the system provides mechanisms for the application to request the sleeping of a CPU thread until work completes. Polling could also be done, but can be less efficient.

## Related topics

<dl> <dt>

[Resource Binding](resource-binding.md)
</dt> </dl>

 

 




