---
title: Root Signatures
description: The root signature defines what types of resources are bound to the graphics pipeline.
ms.assetid: 'ee32a222-8469-4af5-b688-afa70cf77c6a'
ms.topic: article
ms.date: 05/31/2018
---

# Root Signatures

The root signature defines what types of resources are bound to the graphics pipeline.

## In this section



| Topic                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Root Signatures Overview](root-signatures-overview.md)<br/>                                                 | A root signature is configured by the app and links command lists to the resources the shaders require. The graphics command list has both a graphics and compute root signature. A compute command list will simply have one compute root signature. These root signatures are independent of each other.<br/>                                                                                             |
| [Using a Root Signature](using-a-root-signature.md)<br/>                                                     | The root signature is the definition of an arbitrarily arranged collection of descriptor tables (including their layout), root constants and root descriptors. Each entry has a cost towards a maximum limit, so the application can trade off the balance between how many of each type of entry the root signature will contain.<br/>                                                                     |
| [Creating a Root Signature](creating-a-root-signature.md)<br/>                                               | Root signatures are a complex data structure containing nested structures. These can be defined programmatically using the data structure definition below (which includes methods to help initialize members). Alternatively, they can be authored in High Level Shading Language (HLSL)   giving the advantage that the compiler will validate early that the layout is compatible with the shader. <br/> |
| [Root Signature Limits](root-signature-limits.md)<br/>                                                       | The root signature is prime real estate, and there are strict limits and costs to consider.<br/>                                                                                                                                                                                                                                                                                                            |
| [Using Constants Directly in the Root Signature](using-constants-directly-in-the-root-signature.md)<br/>     | Applications can define root constants in the root signature, each as a set of 32-bit values. They appear in High Level Shading Language (HLSL) as a constant buffer. Note that constant buffers for historical reasons are viewed as sets of 4x32-bit values. <br/>                                                                                                                                        |
| [Using Descriptors Directly in the Root Signature](using-descriptors-directly-in-the-root-signature.md)<br/> | Applications can put descriptors directly in the root signature to avoid having to go through a descriptor heap. These descriptors take a lot of space in the root signature (see the root signature limits section), so applications have to use them sparingly. <br/>                                                                                                                                     |
| [Example Root Signatures](example-root-signatures.md)<br/>                                                   | The following section shows root signatures varying in complexity from empty to completely full.<br/>                                                                                                                                                                                                                                                                                                       |
| [Specifying Root Signatures in HLSL](specifying-root-signatures-in-hlsl.md)<br/>                             | Specifying root signatures in HLSL Shader Model 5.1 is an alternative to specifying them in C++ code.<br/>                                                                                                                                                                                                                                                                                                  |
| [Root Signature Version 1.1](root-signature-version-1-1.md)<br/>                                             | The purpose of Root Signature version 1.1 is to enable applications to indicate to drivers when descriptors in a descriptor heap won t change or the data descriptors point to won t change. This allows the option for drivers to make optimizations that might be possible knowing that a descriptor or the memory it points to is static for some period of time. <br/>                                  |



 

## Related topics

<dl> <dt>

[**ID3D12RootSignature**](/windows/win32/api/d3d12/nn-d3d12-id3d12rootsignature)
</dt> <dt>

[**ID3D12RootSignatureDeserializer**](/windows/desktop/api/d3d12/nn-d3d12-id3d12rootsignaturedeserializer)
</dt> <dt>

[Resource Binding](resource-binding.md)
</dt> </dl>

 

