---
title: Devices (Direct3D 11 Graphics)
description: This section describes Direct3D 11 device and device-context objects.
ms.assetid: 61d1ea92-e657-4931-8475-74a3123c72f7
ms.topic: article
ms.date: 05/31/2018
---

# Devices (Direct3D 11 Graphics)

A Direct3D device allocates and destroys objects, renders primitives, and communicates with a graphics driver and the hardware. In Direct3D 11, a device is separated into a device object for creating resources and a device-context object, which performs rendering. This section describes Direct3D 11 device and device-context objects.

Objects created from one device cannot be used directly with other devices. Use a shared resource to share data between multiple devices, with the constraint that a shared object can be used only by the device that created it.


## In this section



| Topic                                                                                                                                                         | Description                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Introduction to a Device in Direct3D 11](overviews-direct3d-11-devices-intro.md)<br/>                                                                 | The Direct3D 11 object model separates resource creation and rendering functionality into a device and one or more contexts; this separation is designed to facilitate multithreading.<br/>                                                  |
| [Software Layers](overviews-direct3d-11-devices-layers.md)<br/>                                                                                        | The Direct3D 11 runtime is constructed with layers, starting with the basic functionality at the core and building optional and developer-assist functionality in outer layers. This section describes the functionality of each layer.<br/> |
| [Limitations Creating WARP and Reference Devices](overviews-direct3d-11-devices-limitations.md)<br/>                                                   | Some limitations exist for creating WARP and Reference devices in Direct3D 10.1 and Direct3D 11.0. This topic discusses those limitations.<br/>                                                                                              |
| [Direct3D 11 on Downlevel Hardware](overviews-direct3d-11-devices-downlevel.md)<br/>                                                                   | This section discusses how Direct3D 11 is designed to support both new and existing hardware, from DirectX 9 to DirectX 11.<br/>                                                                                                             |
| [Using Direct3D 11 feature data to supplement Direct3D feature levels](using-direct3d-optional-features-to-supplement-direct3d-feature-levels.md)<br/> | Find out how to check device support for optional features, including features that were added in recent versions of Windows.<br/>                                                                                                           |



 

## How to topics about devices



| Topic                                                                                                                                                                                                                                                                                                    | Description                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <span id="How_To__Create_a_Reference_Device"></span><span id="how_to__create_a_reference_device"></span><span id="HOW_TO__CREATE_A_REFERENCE_DEVICE"></span>[How To: Create a Reference Device](overviews-direct3d-11-devices-create-ref.md)<br/>                                                 | Describes how to create a reference device.<br/>                            |
| <span id="How_To__Create_a_WARP_Device"></span><span id="how_to__create_a_warp_device"></span><span id="HOW_TO__CREATE_A_WARP_DEVICE"></span>[How To: Create a WARP Device](overviews-direct3d-11-devices-create-warp.md)<br/>                                                                    | Describes how to create a WARP device.<br/>                                 |
| <span id="How_To__Create_a_Swap_Chain"></span><span id="how_to__create_a_swap_chain"></span><span id="HOW_TO__CREATE_A_SWAP_CHAIN"></span>[How To: Create a Swap Chain](overviews-direct3d-11-devices-create-swap-chain.md)<br/>                                                                  | Describes how to create a swap chain.<br/>                                  |
| <span id="How_To__Enumerate_Adapters"></span><span id="how_to__enumerate_adapters"></span><span id="HOW_TO__ENUMERATE_ADAPTERS"></span>[How To: Enumerate Adapters](overviews-direct3d-11-devices-enum.md)<br/>                                                                                   | Describes how to enumerate the physical display adapters.<br/>              |
| <span id="How_To__Get_Adapter_Display_Modes"></span><span id="how_to__get_adapter_display_modes"></span><span id="HOW_TO__GET_ADAPTER_DISPLAY_MODES"></span>[How To: Get Adapter Display Modes](overviews-direct3d-11-devices-get-adapter-info.md)<br/>                                           | Describes how to get the supported display capabilities of an adapter.<br/> |
| <span id="How_To__Create_a_Device_and_Immediate_Context"></span><span id="how_to__create_a_device_and_immediate_context"></span><span id="HOW_TO__CREATE_A_DEVICE_AND_IMMEDIATE_CONTEXT"></span>[How To: Create a Device and Immediate Context](overviews-direct3d-11-devices-initialize.md)<br/> | Describes how to initialize a device.<br/>                                  |



 

## Related topics

<dl> <dt>

[Programming Guide for Direct3D 11](dx-graphics-overviews.md)
</dt> </dl>

 

 





