---
title: Root Signature Version 1.1
description: The purpose of Root Signature version 1.1 is to enable applications to indicate to drivers when descriptors in a descriptor heap won’t change or the data descriptors point to won’t change.
ms.assetid: 8FE42C1C-7F1D-4E70-A7EE-D5EC67237327
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Root Signature Version 1.1

The purpose of Root Signature version 1.1 is to enable applications to indicate to drivers when descriptors in a descriptor heap won’t change or the data descriptors point to won’t change. This allows the option for drivers to make optimizations that might be possible knowing that a descriptor or the memory it points to is static for some period of time.

-   [Overview](#overview)
-   [Static and Volatile Flags](#static-and-volatile-flags)
    -   [DESCRIPTORS\_VOLATILE](#descriptors_volatile)
    -   [DATA\_VOLATILE](#data_volatile)
    -   [DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE](#data_static_while_set_at_execute)
    -   [DATA\_STATIC](#data_static)
    -   [Combining Flags](#combining-flags)
    -   [Flag Summary](#flag-summary)
-   [Version 1.1 API Summary](#version-11-api-summary)
    -   [Enums](#enums)
    -   [Structures](#helper-structures)
    -   [Functions](#functions)
    -   [Methods](#methods)
    -   [Helper structures](#helper-structures)
-   [Consequences of violating static-ness flags](#consequences-of-violating-static-ness-flags)
-   [Version management](#version-management)
-   [Related topics](#related-topics)

## Overview

Root Signature version 1.0 allows the contents of descriptor heaps and the memory they point at to be freely changed by applications any time that command lists / bundles referencing them are potentially in flight on the GPU. Very often, however, applications don’t actually need the flexibility to change descriptors or memory after commands that reference them have been recorded.

Applications are often trivially able to:

-   Set up descriptors (and possible the memory they point to) before binding descriptor tables or root descriptors on a command list or bundle.
-   Ensure that these descriptors will not change until the command list /bundles referencing them have finished executing for the last time.
-   Ensure the data the descriptors point to does not change for the same full duration.

Alternatively, an application may only be able to honor that data doesn’t change for a shorter duration in time. In particular data might be static for the window in time during command list execution that a root parameter binding (descriptor table or root descriptor) currently points to the data. In other words, an application may wish to perform execution on the GPU timeline that updates some data in between time periods where it is set via a root parameter, knowing that when it is set it will be static.

If descriptors, or the data descriptors point to, will not change, then the specific optimizations drivers might do are hardware vendor specific, and importantly they do not change behavior other than possibly improving performance. Preserving as much knowledge about application intent as possible does not put a burden on applications.

One optimization is that many drivers can produce more efficient memory accesses by shaders if they know the promises an application can make about the static-ness of descriptors and data. For example, drivers could remove a level of indirection for accessing a descriptor in a heap by converting it into a root descriptor if the particular hardware is not sensitive to root argument size.

The additional task for developer using Version 1.1 is to make promises about the volatility and static-ness of data wherever possible, so that drivers can make the optimizations that make sense. Developers do not have to make any promises about static-ness.

Root Signature version 1.0 continues to function unchanged, though applications that recompile root signatures will default to Root Signature 1.1 now (with an option to force version 1.0 if desired).

## Static and Volatile Flags

The following flags are part of the root signature to allow drivers to choose a strategy for how to best handle individual root arguments when they are set, and also embed the same assumptions into Pipeline State Objects (PSOs) when they are originally compiled - since the root signature is part of a PSO.

The following flags are set by the app and apply to descriptors or data.

``` syntax
typedef enum D3D12_DESCRIPTOR_RANGE_FLAGS
{
    D3D12_DESCRIPTOR_RANGE_FLAG_NONE    = 0,
    D3D12_DESCRIPTOR_RANGE_FLAG_DESCRIPTORS_VOLATILE    = 0x1,
    D3D12_DESCRIPTOR_RANGE_FLAG_DATA_VOLATILE   = 0x2,
    D3D12_DESCRIPTOR_RANGE_FLAG_DATA_STATIC_WHILE_SET_AT_EXECUTE    = 0x4,
    D3D12_DESCRIPTOR_RANGE_FLAG_DATA_STATIC = 0x8
} D3D12_DESCRIPTOR_RANGE_FLAGS;

typedef enum D3D12_ROOT_DESCRIPTOR_FLAGS
{
    D3D12_ROOT_DESCRIPTOR_FLAG_NONE = 0,
    D3D12_ROOT_DESCRIPTOR_FLAG_DATA_VOLATILE    = 0x2,
    D3D12_ROOT_DESCRIPTOR_FLAG_DATA_STATIC_WHILE_SET_AT_EXECUTE = 0x4,
    D3D12_ROOT_DESCRIPTOR_FLAG_DATA_STATIC  = 0x8
} D3D12_ROOT_DESCRIPTOR_FLAGS;
```

### DESCRIPTORS\_VOLATILE

With this flag set, the descriptors in a descriptor heap pointed to by a root descriptor table can be changed by the application any time except while the command list / bundles that bind the descriptor table have been submitted and have not finished executing. For instance, recording a command list and subsequently changing descriptors in a descriptor heap it refers to *before* submitting the command list for execution is valid. This is the only supported behavior of Root Signature version 1.0.

If the DESCRIPTORS\_VOLATILE flag is *not* set then descriptors are static. There is no flag for this mode. Static descriptors mean the descriptors in a descriptor heap pointed to by a root descriptor table have been initialized by the time the descriptor table is set on a command list / bundle (during recording), and the descriptors cannot be changed until the command list / bundle has finished executing for the last time. *For Root Signature version 1.1, static descriptors are the default assumption*, and the application has to specify the DESCRIPTORS\_VOLATILE flag when needed.

For bundles using descriptor tables with static descriptors, the descriptors have to be ready starting at the time the bundle is recorded (as opposed to when the bundle is called), and not change until the bundle has finished executing for the last time. Descriptor tables pointing to static descriptors have to be set during bundle recording and not inherited into the bundle. It is valid for a command list to use a descriptor table with static descriptors that has been set in a bundle and returned back to the command list.

When descriptors are static there is another change in behavior that requires the DESCRIPTORS\_VOLATILE flag to be set. Out of bounds accesses to any Buffer views (as opposed to Texture1D/2D/3D/Cube views) are invalid and produce undefined results, including possible device reset, rather than returning default values for reads or dropping writes. The purpose for removing the ability for applications to depend on hardware out of bounds access checking is to allow drivers to choose to promote static descriptor accesses to root descriptor accesses if they deem that more efficient. Root descriptors don’t support any out of bounds checking.

If applications depend on safe out of bounds memory access behavior when accessing descriptors, they need to mark the descriptor ranges that access those descriptors as DESCRIPTORS\_VOLATILE.

### DATA\_VOLATILE

With this flag set, the data pointed to by descriptors can be changed by the CPU any time except while the command list / bundles that bind the descriptor table have been submitted and have not finished executing. This is the only supported behavior of Root Signature version 1.0.

The flag is available in both descriptor range flags and root descriptor flags.

### DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE

With this flag set, the data pointed to by descriptors cannot change starting from when the underlying root descriptor or descriptor table is set on a command list / bundle during execution on the GPU timeline, and ending when subsequent draws/dispatches will no longer reference the data.

Before a root descriptor or descriptor table has been set on the GPU, this data *can* be changed even by the same command list / bundle. The data can also be changed while a root descriptor or descriptor table pointing to it is still set on the command list / bundle, as long as draw/dispatches referencing it have completed. However, doing so requires the descriptor table be rebound to the command list again before the next time the root descriptor or descriptor table is dereferenced. This allows the driver to know that data pointed to by a root descriptor or descriptor table has changed.

The essential difference between DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE and DATA\_VOLATILE is with DATA\_VOLATILE a driver can’t tell whether data copies in a command list have changed the data pointed to by a descriptor, without doing extra state tracking. So if, for instance, a driver can insert any sort of data pre-fetching commands into their command list (to make shader access to known data more efficient, for example), DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE lets the driver know it only needs to perform data pre-fetching at the moment it is set via [**SetGraphicsRootDescriptorTable**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsrootdescriptortable), [**SetComputeRootDescriptorTable**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootdescriptortable) or one of the methods to set the constant buffer view, shader resource view, or unordered access view.

For bundles, the promise that data is static while set at execute applies uniquely to each execution of the bundle.

The flag is available in both descriptor range flags and root descriptor flags.

### DATA\_STATIC

If this flag is set, the data pointed to by descriptors has been initialized by the time a root descriptor or descriptor table referencing the memory has been set on a command list / bundle during recording, and the data cannot be changed until the command list / bundle has finished executing for the last time.

For bundles, the static duration starts at root descriptor or descriptor table setting during the recording of the bundle, as opposed to recording of a calling command list. In addition, a descriptor table pointing to static data must be set in the bundle and not inherited. It is valid for a command list to use a descriptor table pointing to static data that has been set in a bundle and returned back to the command list.

The flag is available in both descriptor range flags and root descriptor flags.

### Combining Flags

At most one of the DATA flags can be specified at a time, except for Sampler descriptor ranges which do not support DATA flags at all since samplers do not point to data.

The absence of any DATA flags for SRV and CBV descriptor ranges means a default of DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE behavior is assumed. The reason this default is chosen rather than DATA\_STATIC is that DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE is much more likely to be a safe default for a majority of cases, while still yielding some optimization opportunity better than defaulting to DATA\_VOLATILE.

The absence of DATA flags for UAV descriptor ranges means a default of DATA\_VOLATILE behavior is assumed, given typically UAVs are written to.

DESCRIPTORS\_VOLATILE *cannot* be combined with DATA\_STATIC, but *can* be combined with the other DATA flags. The reason DESCRIPTORS\_VOLATILE can be combined with DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE is that volatile descriptors still require the descriptors be ready during command list / bundle execution, and DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE is only making promises about the static-ness within a subset of command list / bundle execution.

### Flag Summary

The following tables summarize the flag combinations that might be employed.



| Valid D3D12\_DESCRIPTOR\_RANGE\_FLAGS settings                                                               | Description                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No flags set                                                   | Descriptors are static (the default). Default assumptions for data: for SRV/CBV: DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE, and for UAV: DATA\_VOLATILE. These defaults for SRV/CBV will safely fit the usage patterns for the majority of root signatures.                                                                                              |
| DATA\_STATIC                                                   | Both descriptors and data are static. This maximizes the potential for driver optimization.                                                                                                                                                                                                                                                          |
| DATA\_VOLATILE                                                 | Descriptors are static and the data is volatile.                                                                                                                                                                                                                                                                                                     |
| DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE                          | Descriptors are static and data is static while set at execute.                                                                                                                                                                                                                                                                                      |
| DESCRIPTORS\_VOLATILE                                          | Descriptors are volatile, and default assumptions are made about data: for SRV/CBV: DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE, and for UAV: DATA\_VOLATILE.                                                                                                                                                                                              |
| DESCRIPTORS\_VOLATILE \| DATA\_VOLATILE                        | Both descriptors and data are volatile, equivalent to Root Signature 1.0.                                                                                                                                                                                                                                                                            |
| DESCRIPTORS\_VOLATILE \| DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE | Descriptors are volatile, but note that still doesn’t allow them to change during command list execution. So it is valid to combine the additional declaration that data is static while set via root descriptor table during execution – the underlying descriptors are effectively static for longer than the data is being promised to be static. |



 



| Valid D3D12\_ROOT\_DESCRIPTOR\_FLAGS settings                                                  |  Description                                                                                                                                                                                                                 |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No flags set                                      | Default assumptions for data: for SRV/CBV: DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE, and for UAV: DATA\_VOLATILE. These defaults for SRV/CBV will safely fit the usage patterns for the majority of root signatures. |
| DATA\_STATIC                                      | Data is static, the best potential for driver optimization.                                                                                                                                                       |
| DATA\_STATIC\_WHILE\_SET\_AT\_EXECUTE             | Data is static while set at execute.                                                                                                                                                                              |
| DATA\_VOLATILE                                    | Equivalent to Root Signature 1.0.                                                                                                                                                                                 |



 

## Version 1.1 API Summary

The following API calls enable version 1.1.

### Enums

These enumerations contain the key flags to specify descriptor and data volatility.

-   [**D3D\_ROOT\_SIGNATURE\_VERSION**](/windows/desktop/api/d3d12/ne-d3d12-d3d_root_signature_version) : version ids.
-   [**D3D12\_DESCRIPTOR\_RANGE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_descriptor_range_flags) : a range of flags determining if descriptors or data are volatile or static.
-   [**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_root_descriptor_flags) : a similar range of flags to [**D3D12\_DESCRIPTOR\_RANGE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_descriptor_range_flags), except that only data flags apply to root descriptors.

### Structures

Updated structures (from version 1.0) contain references to the volatility/static flags.

-   [**D3D12\_FEATURE\_DATA\_ROOT\_SIGNATURE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_feature_data_root_signature) : pass this structure to [**CheckFeatureSupport**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport) to check for Root Signature Version 1.1 support.
-   [**D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc) : can hold any version of a root signature description, and is designed to be used with the serialization/deserialization functions listed below.
-   These structures are equivalent to those used in version 1.0, with the addition of new flags fields for descriptor ranges and root descriptors:

    -   [**D3D12\_ROOT\_SIGNATURE\_DESC1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_signature_desc1)
    -   [**D3D12\_DESCRIPTOR\_RANGE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range1)
    -   [**D3D12\_ROOT\_DESCRIPTOR\_TABLE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor_table1)
    -   [**D3D12\_ROOT\_DESCRIPTOR1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor1)
    -   [**D3D12\_ROOT\_PARAMETER1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_parameter1)

### Functions

The methods listed here supersede the original [**D3D12SerializeRootSignature**](/windows/desktop/api/d3d12/nf-d3d12-d3d12serializerootsignature) and [**D3D12CreateRootSignatureDeserializer**](/windows/desktop/api/d3d12/nf-d3d12-d3d12createrootsignaturedeserializer) functions, as they are designed to work on any version of root signature. The serialized form is what is passed into the [**CreateRootSignature**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createrootsignature) API. If a shader has been authored with a root signature in it, the compiled shader will contain a serialized root signature in it already.

-   [**D3D12SerializeVersionedRootSignature**](/windows/desktop/api/d3d12/nf-d3d12-d3d12serializeversionedrootsignature) : if an application procedurally generates the [**D3D12\_VERSIONED\_ROOT\_SIGNATURE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc) data structure, it must make the serialized form using this function.
-   [**D3D12CreateVersionedRootSignatureDeserializer**](/windows/desktop/api/d3d12/nf-d3d12-d3d12createversionedrootsignaturedeserializer) : generates an interface that can return the deserialized data structure, via [**GetUnconvertedRootSignatureDesc**](/windows/desktop/api/d3d12/nf-d3d12-id3d12versionedrootsignaturedeserializer-getunconvertedrootsignaturedesc).

### Methods

The [**ID3D12VersionedRootSignatureDeserializer**](/windows/desktop/api/d3d12/nn-d3d12-id3d12versionedrootsignaturedeserializer) interface is created to deserialize the root signature data structure.

-   [**GetRootSignatureDescAtVersion**](/windows/desktop/api/d3d12/nf-d3d12-id3d12versionedrootsignaturedeserializer-getrootsignaturedescatversion) : converts root signature description structures to a requested version.
-   [**GetUnconvertedRootSignatureDesc**](/windows/desktop/api/d3d12/nf-d3d12-id3d12versionedrootsignaturedeserializer-getunconvertedrootsignaturedesc) : returns a pointer to a [**D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc) structure.

### Helper structures

Helper structures have been added to aid in the initialization of some of the version 1.1 structures.

-   CD3DX12\_DESCRIPTOR\_RANGE1
-   CD3DX12\_ROOT\_PARAMETER1
-   CD3DX12\_STATIC\_SAMPLER1
-   CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC

Refer to [Helper Structures and Functions for D3D12](helper-structures-and-functions-for-d3d12.md).

## Consequences of violating static-ness flags

The descriptor and data flags described above (as well as the defaults implied by the absence of particular flags) define a promise by the application to the driver about how it is going to behave. If an application violates the promise, this is invalid behavior: results are undefined and might be different across different drivers and hardware.

The debug layer has options for validating that applications honor their promises, including the default promises that come with using Root Signature version 1.1 without setting any flags.

## Version management

When compiling root signatures attached to shaders, newer HLSL compilers will default to compiling the root signature at version 1.1, whereas old HLSL compilers only support 1.0. Note that 1.1 root signatures will not work on OS’s that don’t support root signature 1.1.

The root signature version compiled with a shader can be forced to a particular version using `/force_rootsig_ver <version>`. Forcing the version will succeed if the compiler can preserve the behavior of the root signature being compiled at the forced version, for example by dropping unsupported flags in the root signature that serve only for optimization purposes but do not affect behavior.

This way an application can, for instance, compile a 1.1 root signature to both 1.0 and 1.1 when building the application and select the appropriate version at runtime depending on the level of OS support. It would be most space efficient, however, for an application to compile root signatures individually (particularly if multiple versions are needed), separately from shaders. Even if shaders aren’t initially compiled with a root signature attached, the benefit of compiler validation of root signature compatibility with a shader can be preserved by using the `/verifyrootsignature` compiler option. Later at runtime, PSOs can be created using shaders that don’t have root signatures in them while passing the desired root signature (perhaps the appropriate version supported by the OS) as a separate parameter.

## Related topics

<dl> <dt>

[Creating a Root Signature](creating-a-root-signature.md)
</dt> <dt>

[Root Signatures](root-signatures.md)
</dt> <dt>

[Specifying Root Signatures in HLSL](specifying-root-signatures-in-hlsl.md)
</dt> </dl>

 

 




