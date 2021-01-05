---
description: The following page provides a basic outline of key differences between Direct3D 9 and Direct3D 10. The outline below provides some insight to assist developers with Direct3D 9 experience to explore and relate to Direct3D 10.
ms.assetid: 283b54e0-94cb-47a8-8cfc-5798e0538b9f
title: Direct3D 9 to Direct3D 10 Considerations (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 9 to Direct3D 10 Considerations (Direct3D 10)

The following page provides a basic outline of key differences between Direct3D 9 and Direct3D 10. The outline below provides some insight to assist developers with Direct3D 9 experience to explore and relate to Direct3D 10.

Although the info in this topic compares Direct3D 9 with Direct3D 10, because Direct3D 11 builds on the improvements made in Direct3D 10 and 10.1, you also need this info to migrate from Direct3D 9 to Direct3D 11. For info about moving beyond Direct3D 10 to Direct3D 11, see [Migrating to Direct3D 11](../direct3d11/d3d11-programming-guide-migrating.md).

-   [Overview of the Major Structural Changes in Direct3D 10](#overview-of-the-major-structural-changes-in-direct3d-10)
    -   [Removal of Fixed Function](#removal-of-fixed-function)
    -   [Device Object Creation Time Validation](#device-object-creation-time-validation)
-   [Engine Abstractions / Separation](/windows)
    -   [Direct Removal of Direct3D 9 Dependencies](#direct-removal-of-direct3d-9-dependencies)
-   [Tricks for Quickly Resolving Application Build Issues](#tricks-for-quickly-resolving-application-build-issues)
    -   [Overriding Direct3D 9 Types](#overriding-direct3d-9-types)
    -   [Resolving Link Issues](#resolving-link-issues)
    -   [Simulating Device CAPs](#simulating-device-caps)
-   [Driving the Direct3D 10 API](#driving-the-direct3d-10-api)
    -   [Resource Creation](#resource-creation)
    -   [Views](#views)
    -   [Static versus Dynamic Resource Access](#static-versus-dynamic-resource-access)
    -   [Direct3D 10 Effects](#direct3d-10-effects)
    -   [HLSL without Effects](#hlsl-without-effects)
    -   [Shader Compilation](#shader-compilation)
    -   [Creation of Shader Resources](#creation-of-shader-resources)
    -   [Shader Reflection Layer Interface](#shader-reflection-layer-interface)
    -   [Input Assembler Layouts - Vertex Shader / Input Stream Linkage](/windows)
    -   [Impact of Shader Dead Code Removal](#impact-of-shader-dead-code-removal)
    -   [Vertex Shader Input Structure Example](#vertex-shader-input-structure-example)
    -   [State Object Creation](#state-object-creation)
-   [Porting Textures](#porting-textures)
    -   [File Formats Supported](#file-formats-supported)
    -   [Mapping Texture Formats](#mapping-texture-formats)
-   [Porting Shaders](#porting-shaders)
    -   [Direct3D 10 Shaders are Authored in HLSL](#direct3d-10-shaders-are-authored-in-hlsl)
    -   [Shader Signatures and Linkage](#shader-signatures-and-linkage)
    -   [HLSL Shader Stage linkages](#hlsl-shader-stage-linkages)
    -   [Constant Buffers](#constant-buffers)
    -   [User clip planes in HLSL on feature level 9 and higher](#user-clip-planes-in-hlsl-on-feature-level-9-and-higher)
-   [Additional Direct3D 10 Differences to Watch For](#additional-direct3d-10-differences-to-watch-for)
    -   [Integers as Input](#integers-as-input)
    -   [Mouse Cursors](#mouse-cursors)
    -   [Mapping Texels to Pixels in Direct3D 10](#mapping-texels-to-pixels-in-direct3d-10)
    -   [Reference Counting Behavior Changes](#reference-counting-behavior-changes)
    -   [Test Cooperative Level](#test-cooperative-level)
    -   [StretchRect](#stretchrect)
-   [Additional Direct3D 10.1 Differences](#additional-direct3d-101-differences)
-   [Related topics](#related-topics)

## Overview of the Major Structural Changes in Direct3D 10

-   [Removal of Fixed Function](#removal-of-fixed-function)
-   [Device Object Creation Time Validation](#device-object-creation-time-validation)

The process of rendering using the Direct3D 10 device is structurally similar to Direct3D 9.

-   Set a vertex stream source
-   Set input layout in Direct3D 10 (set vertex stream declaration in Direct3D 9)
-   Declare primitive topology
-   Set textures
-   Set state objects
-   Set shaders
-   Draw

The [**Draw**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-draw) call ties the operations together; the ordering of calls prior to the Draw call is arbitrary. The major differences in the Direct3D 10 API design are as follows:

-   Removal of Fixed Function
-   Removal of CAPS bits - Direct3D 10's base feature set is guaranteed
-   Stricter management of: resource access, device state, shader constants, shader linkage (inputs and outputs to shaders) between stages
-   API entry point name changes reflect the use of virtual GPU memory (Map() instead of Lock()).
-   A debug layer can be added to the device at creation time
-   The primitive topology is now an explicit state (separated from the [**Draw**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-draw) call)
-   Explicit shader constants are now stored in constant buffers
-   Shader authoring is done entirely in HLSL. The HLSL compiler now resides in the primary Direct3D 10 DLL.
-   New programmable stage - the geometry shader
-   Removal of BeginScene()/EndScene()
-   Common 2D, focus and adapter-management functionality implemented in a new component: DXGI

### Removal of Fixed Function

It is sometimes surprising that even in a Direct3D 9 engine that fully exploits the programmable pipeline, there remains a number of areas that depend on the fixed-function (FF) pipeline. The most common areas are usually related to screen-space aligned rendering for UI. It is for this reason that you are likely to need to build a FF emulation shader or set of shaders which provide the necessary replacement behaviors.

This documentation contains a white paper containing replacement shader sources for the most common FF behaviors (see [Fixed Function EMU Sample](https://msdn.microsoft.com/library/Ee416406(v=VS.85).aspx)). Some fixed-function pixel behavior including alpha test has been moved into shaders.

### Device Object Creation Time Validation

The Direct3D 10 pipeline has been redesigned from the ground up in hardware and software with a primary intention to reduce CPU overhead (at Draw time). To reduce costs, all types of device data have been assigned an object with explicit creation methods provided by the device itself. This enables strict data validation at object creation time instead of during the Draw call as it often does with Direct3D 9.

## Engine Abstractions / Separation

Applications, including Games, that wish to support both Direct3D 9 and Direct3D 10 need to have the rendering layers abstracted from the rest of the code base. There are many ways to achieve this but key to all of them is the design of the abstraction layer for the lower-level Direct3D device. All systems should communicate to the hardware through the common layer which is designed to provide GPU resource and low-level type management.

### Direct Removal of Direct3D 9 Dependencies

When porting large, previously tested code bases, it is important to minimize the amount of code changes to those which are absolutely necessary to preserve previously tested behaviors in the code. Best practices include clearly documenting where items change using comments. It's often useful to have a commenting standard for this work which enables quick navigation through the code base.

The following is an example list of standard single line / start block comments which could be used for this work.



| Item                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="___Direct3D_10_REMOVED"></span><span id="___direct3d_10_removed"></span><span id="___DIRECT3D_10_REMOVED"></span>// Direct3D 10 REMOVED<br/>                     | Use this where lines / blocks of code are removed<br/>                                                                                                                                                                                                                                                                   |
| <span id="___Direct3D_10_NEEDS_UPDATE"></span><span id="___direct3d_10_needs_update"></span><span id="___DIRECT3D_10_NEEDS_UPDATE"></span>// Direct3D 10 NEEDS UPDATE<br/> | It helps to added additional notes to the NEED UPDATE comment that suggests what work / new API should be used for later visits to the code for behavior conversion. Heavy use of assert(**false**) should also be used where \\\\ Direct3D 10 NEEDS UPDATE occurs to ensure you do not unknowingly run errant code<br/> |
| <span id="___Direct3D_10_CHANGED"></span><span id="___direct3d_10_changed"></span><span id="___DIRECT3D_10_CHANGED"></span>// Direct3D 10 CHANGED<br/>                     | Areas where major changes have occurred should be kept for future reference but commented out<br/>                                                                                                                                                                                                                       |
| <span id="___Direct3D_10_END"></span><span id="___direct3d_10_end"></span><span id="___DIRECT3D_10_END"></span>// Direct3D 10 END<br/>                                     | End code block qualifier<br/>                                                                                                                                                                                                                                                                                            |



 

For multiple lines of source you should use the C style /\* \*/ comments too but add the relevant start / end comments around these areas.

## Tricks for Quickly Resolving Application Build Issues

-   [Overriding Direct3D 9 Types](#overriding-direct3d-9-types)
-   [Resolving Link Issues](#resolving-link-issues)
-   [Simulating Device CAPs](#simulating-device-caps)

### Overriding Direct3D 9 Types

It may be useful to insert a high level header file containing type definitions / overrides for Direct3D 9 base types which are no longer supported by the Direct3D 10 headers. This will help you minimize the amount of changes in the code and interfaces where there is a direct mapping from a Direct3D 9 type to the newly defined Direct3D 10 type. This approach is also useful for keeping code behaviors together in one source file. In this case, it is a good idea to define version neutral / generally named types which describe common constructs used for rendering yet span both Direct3D 9 and Direct3D 10 APIs. For example:


```
#if defined(D3D9)
typedef IDirect3DIndexBuffer9   IDirect3DIndexBuffer;
typedef IDirect3DVertexBuffer9  IDirect3DVertexBuffer;
#else //D3D10
typedef ID3D10Buffer            IDirect3DIndexBuffer;
typedef ID3D10Buffer            IDirect3DVertexBuffer
#endif
```



Other Direct3D 10 specific examples of this include:


```
typedef ID3D10TextureCube   IDirect3DCubeTexture;
typedef ID3D10Texture3D     IDirect3DVolumeTexture;
typedef D3D10_VIEWPORT      D3DVIEWPORT;
typedef ID3D10VertexShader  IDirect3DVertexShader;
typedef ID3D10PixelShader   IDirect3DPixelShader;
```



### Resolving Link Issues

It is advisable to develop Direct3D 10 and Windows Vista applications using the latest version of Microsoft Visual Studio. However, it is possible to build a Windows Vista application which depends on Direct3D 10 using the earlier 2003 version of Visual Studio. Direct3D 10 is a Windows Vista platform component which has dependencies (as with the Server 2003 SP1 platform SDK) on the following lib: BufferOverflowU.lib is needed to solve any buffer\_security check linker issues.

### Simulating Device CAPs

Many applications contain areas of code which depend on device CAPS data being available. Work around this by overriding device enumeration and forcing device CAPS to sensible values. Plan to re-visit areas where there are dependencies on CAPS later for full removal of CAPS where possible.

## Driving the Direct3D 10 API

This section focuses on the behavior changes caused by the Direct3D 10 API.

-   [Resource Creation](#resource-creation)
-   [Views](#views)
-   [Static versus Dynamic Resource Access](#static-versus-dynamic-resource-access)
-   [Direct3D 10 Effects](#direct3d-10-effects)
-   [HLSL without Effects](#hlsl-without-effects)
-   [Shader Compilation](#shader-compilation)
-   [Creation of Shader Resources](#creation-of-shader-resources)
-   [Shader Reflection Layer Interface](#shader-reflection-layer-interface)
-   [Input Assembler Layouts - Vertex Shader / Input Stream Linkage](/windows)
-   [Impact of Shader Dead Code Removal](#impact-of-shader-dead-code-removal)
-   [Vertex Shader Input Structure Example](#vertex-shader-input-structure-example)
-   [State Object Creation](#state-object-creation)

### Resource Creation

The Direct3D 10 API has designed resources as generic buffer types which have specific bind flags according to the planned usage. This design point was chosen to facilitate near ubiquitous access of resources in the Pipeline for scenarios such as rendering to a vertex buffer then instantly drawing the results without interrupting the CPU. The following example demonstrates allocation of vertex buffers and index buffer where you can see that the resource description only differs by the GPU resource bind flags.

The Direct3D 10 API has provided texture helper methods for explicitly creating texture type resources but as you can imagine, these are really helper functions.

-   CreateTexture2D()
-   CreateTextureCube()
-   CreateTexture3D()

When targeting Direct3D 10, you are likely to want to allocate more items during resource creation time than you are used to with Direct3D 9. This will become most apparent with the creation of Render Target buffers and Textures where you need to also create a view for accessing the buffer and setting the resource on the device.

[Tutorial 1: Direct3D 10 Basics](https://msdn.microsoft.com/library/Ee416436(v=VS.85).aspx)

> [!Note]  
> Direct3D 10 and later versions of Direct3D extend the DDS file format to support new DXGI formats, texture arrays, and cube-map arrays. For more information about the DDS file format extension, see the [Programming Guide for DDS](../direct3ddds/dx-graphics-dds-pguide.md).

 

### Views

A view is a specifically typed, interface to data stored in a pixel buffer. A resource can have several views allocated on it at once and this feature is highlighted in the Single Pass Render to Cubemap sample contained in this SDK.

[Programmers Guide page on Resource Access](d3d10-graphics-programming-guide-resources-access-views.md)

[CubeMap Sample](https://msdn.microsoft.com/library/Ee416398(v=VS.85).aspx)

### Static versus Dynamic Resource Access

For best performance, applications should partition their data use in terms of the static vs dynamic nature of the data. Direct3D 10 has been designed to take advantage of this approach and as such, the access rules for resources have been significantly tightened up over Direct3D 9. For static resources you should ideally populate the resource with its data during creation time. If your engine has been designed around the Create, Lock, Fill, Unlock design point of Direct3D 9, you may defer population from Create time by using a staging resource and the UpdateSubResource method on the resource interface.

### Direct3D 10 Effects

Use of the Direct3D 10 Effects system is outside the scope of this article. The system has been written to take full advantage of the architectural benefits that Direct3D 10 provides. See the [Effects (Direct3D 10)](d3d10-graphics-programming-guide-effects.md) section for more detail on its use.

### HLSL without Effects

The Direct3D 10 Shader pipeline may be driven without the use of the Direct3D 10 Effects system. Note that in this instance, all constant buffer, shader, sampler and texture binding must be managed by the application itself. See the sample link and following sections of this document for more detail:

[HLSL without Effects sample](https://msdn.microsoft.com/library/Ee416414(v=VS.85).aspx)

### Shader Compilation

The Direct3D 10 HLSL compiler brings enhancements to the HLSL language definition and therefore has the ability to operate in 2 modes. For complete support of Direct3D 9 style intrinsic functions and semantics, compilation should be invoked using the COMPATIBILITY MODE flag which can be specified on a per compile basis.

The shader model 4.0 specific HLSL language semantics and intrinsic functions for Direct3D 10 can be found at [HLSL](../direct3dhlsl/dx-graphics-hlsl.md). Major changes in syntax from Direct3D 9 HLSL to take the most notice of are in the area of texture access. The new syntax is the only form supported by the compiler outside of compatibility mode.

> [!Note]  
> The Direct3D 10 compiler-type APIs ([**D3D10CompileShader**](/windows/desktop/api/D3D10Shader/nf-d3d10shader-d3d10compileshader) and [**D3D10CompileEffectFromMemory**](/windows/desktop/api/D3D10Effect/nf-d3d10effect-d3d10compileeffectfrommemory)) are supplied by the Direct3D 10, 10.1, and 11 runtimes that run in Windows Vista and later. The Direct3D 10 compiler-type APIs have the same functionality as the HLSL compiler that is shipped in the DirectX SDK (December 2006). This HLSL compiler does not support the Direct3D 10.1 profiles (vs\_4\_1, ps\_4\_1, gs\_4\_1, fx\_4\_1), and is missing a number of optimizations and improvements. You can get an HLSL compiler that supports the Direct3D 10.1 profiles from the latest legacy [DirectX SDK release](/previous-versions/windows/apps/hh452744(v=win.10)). For info about the legacy DirectX SDK, see [Where is the DirectX SDK?](../directx-sdk--august-2009-.md). You can get the latest HLSL Fxc.exe command-line compiler and [D3DCompiler](../direct3dhlsl/dx-graphics-d3dcompiler-reference.md) APIs from the Windows SDK.

 

### Creation of Shader Resources

The creation of compiled shader instances outside of the Direct3D 10 Effects system is done in a very similar manner to Direct3D 9 however, in Direct3D 10, it is important to keep the Shader Input signature around for later use. The signature is returned by default as part of the shader blob but may be extracted to reduce the memory requirements if needed. For more details, see [Using Shaders in Direct3D 10](../direct3dhlsl/dx-graphics-hlsl-using-shaders-10.md).

### Shader Reflection Layer Interface

The shader reflection layer is the interface by which information about the shader requirements may be obtained. This is particularly useful when creating Input Assembly linkages (see below) where you may need to traverse the shader input requirements to ensure you are supplying the correct input structure to the shader. You can create an instance of the reflection layer interface at the same time as creating an instance of a compiled shader.

The shader reflection layer replaces D3DX9 methods that provide similar functionality. For example [**IsParameterUsed**](../direct3d9/id3dxeffect--isparameterused.md) is replaced by the [**GetDesc**](/windows/desktop/api/D3D10Shader/nf-d3d10shader-id3d10shaderreflectionvariable-getdesc) method.

### Input Assembler Layouts - Vertex Shader / Input Stream Linkage

The Input Assembler (IA) replaces the Direct3D 9 style Vertex Stream Declaration and it's description structure is very similar in form. The main difference that the IA brings is that the IA layout object created must directly map to a specific format of shader input signature. The mapping object created to link the input stream to shader may be used across any number of shaders where the shader input signature matches that of the shader used to create the Input Layout.

To best drive the pipeline with static data, you should consider the permutations of input stream format to possible shader input signatures and create the IA layout object instances as early as is possible and reuse them where possible.

### Impact of Shader Dead Code Removal

The following section details a significant difference between Direct3D 9 and Direct3D 10 that is likely to require careful handling in your engine code. Shaders which contain conditional expressions often have certain code paths removed as part of the compilation process. In Direct3D 9, two kinds of inputs may be removed (marked for removal) when unused: signature inputs (like the example below) and constant inputs. If the end of the constant buffer contains unused entries, the size declaration in the shader will reflect the size of the constant buffer without the unused entries at the end. Both of these kinds of inputs remain in signatures or constant buffers Direct3D 10 with a special exception in the case of unused constant inputs at the end of a constant buffer. This may have an impact on the engine when handling large shaders and creating input layouts. Elements which are removed by dead code optimizations in the compiler must still be declared in the input structure. The following example demonstrates this:

### Vertex Shader Input Structure Example


```
struct VS_INPUT
{
float4 pos: SV_Position;
float2 uv1 : Texcoord1;
float2 uv2 : Texcoord2; *
};
```



\* Direct3D 9 dead code removal would remove the declaration in the shader due to conditional dead code removal


```
float4x4  g_WorldViewProjMtx;
static const bool g_bLightMapped = false; // define a compile time constant

VS_INPUT main(VS_INPUT i) 
{
    VS_INPUT o;
    o.pos = mul( i.pos, g_WorldViewProjMtx);
    o.uv1 = i.uv1;
    if ( g_bLightMapped )
    {
        o.uv2 = i.uv2;
    }
    return o;
}
```



Or, you could make it even more obvious that the constant is a compile time constant with the following declaration:


```
#define LIGHT_MAPPED false
```



In the above example, under Direct3D 9, the uv2 element would be removed due to dead code optimizations in the compiler. Under Direct3D 10, the dead code will still be removed but the shader input assembler layout requires the definition of the input data to exist. The shader reflection layer provides the means to handle this situation in a generic manner whereby you can traverse the shader input requirements and ensure that you provide a full description of the Input Stream to shader signature mapping.

Here's an example function to detect the existence of a semantic name/index in a function signature:


```
// Returns true if the SemanticName / SemanticIndex is used in the input signature.
// pReflector is a previously acquired shader reflection interface.
bool IsSignatureElementExpected(ID3D10ShaderReflection *pReflector, const LPCSTR SemanticName, UINT SemanticIndex)
{
    D3D10_SHADER_DESC               shaderDesc;
    D3D10_SIGNATURE_PARAMETER_DESC  paramDesc;

    Assert(pReflector);
    Assert(SemanticName);

    pReflector->GetDesc(&shaderDesc);

    for (UINT k=0; k<shaderDesc.InputParameters; k++)
    {
        pReflector->GetInputParameterDesc( k, &paramDesc);
        if (wcscmp( SemanticName, paramDesc.SemanticName)==0 && paramDesc.SemanticIndex == SemanticIndex) 
            return true;
    }

    return false;
}
```



### State Object Creation

When porting engine code, it may help to initially use a default set of state objects and disable all Direct3D 9 device render state / texture state setting. This will cause rendering artifacts but is the quickest way to get things up and running. You can later construct a state object management system which can use a compound key to enable maximum reuse of the number of state objects being used.

## Porting Textures

### File Formats Supported

The **D3DXxxCreateXXX** and **D3DXxxSaveXXX** functions that create or save a texture from or to a graphics file (for example, [**D3DX10CreateTextureFromFile**](d3dx10createtexturefromfile.md)) support a different set of file formats in Direct3D 10 than they did in Direct3D 9:



| File Format | Direct3D 9 | Direct3D 10 |
|-------------|------------|-------------|
| .bmp        | x          | x           |
| .jpg        | x          | x           |
| .tga        | x          |             |
| .png        | x          | x           |
| .dds        | x          | x           |
| .ppm        | x          |             |
| .dib        | x          |             |
| .hdr        | x          |             |
| .pfm        | x          |             |
| .tiff       |            | x           |
| .gif        |            | x           |
| .tif        |            | x           |



 

For details, compare the Direct3D 9 [**D3DXIMAGE\_FILEFORMAT**](../direct3d9/d3dximage-fileformat.md) enumerations with the [**D3DX10\_IMAGE\_FILE\_FORMAT**](d3dx10-image-file-format.md) enumerations for Direct3D 10.

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8. For texture file processing, we recommend that you use [DirectXTex](https://github.com/Microsoft/DirectXTex).

 

### Mapping Texture Formats

The following table shows the mapping of texture formats from Direct3D 9 to Direct3D 10. Any content in formats not available in DXGI will need to be converted by utility routines.



| Direct3D 9 Format                   | Direct3D 10 Format                                                                                                                                                                                                                                   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DFMT\_UNKNOWN                     | DXGI\_FORMAT\_UNKNOWN                                                                                                                                                                                                                                |
| D3DFMT\_R8G8B8                      | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_A8R8G8B8                    | DXGI\_FORMAT\_B8G8R8A8\_UNORM & DXGI\_FORMAT\_B8G8R8A8\_UNORM\_SRGB¹                                                                                                                                                                                 |
| D3DFMT\_X8R8G8B8                    | DXGI\_FORMAT\_B8G8R8X8\_UNORM & DXGI\_FORMAT\_B8G8R8X8\_UNORM\_SRGB¹                                                                                                                                                                                 |
| D3DFMT\_R5G6B5                      | DXGI\_FORMAT\_B5G6R5\_UNORM²                                                                                                                                                                                                                         |
| D3DFMT\_X1R5G5B5                    | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_A1R5G5B5                    | DXGI\_FORMAT\_B5G5R5A1\_UNORM²                                                                                                                                                                                                                       |
| D3DFMT\_A4R4G4B4                    | DXGI\_FORMAT\_B4G4R4A4\_UNORM³                                                                                                                                                                                                                       |
| D3DFMT\_R3G3B2                      | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_A8                          | DXGI\_FORMAT\_A8\_UNORM                                                                                                                                                                                                                              |
| D3DFMT\_A8R3G3B2                    | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_X4R4G4B4                    | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_A2B10G10R10                 | DXGI\_FORMAT\_R10G10B10A2                                                                                                                                                                                                                            |
| D3DFMT\_A8B8G8R8                    | DXGI\_FORMAT\_R8G8B8A8\_UNORM & DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB                                                                                                                                                                                  |
| D3DFMT\_X8B8G8R8                    | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_G16R16                      | DXGI\_FORMAT\_R16G16\_UNORM                                                                                                                                                                                                                          |
| D3DFMT\_A2R10G10B10                 | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_A16B16G16R16                | DXGI\_FORMAT\_R16G16B16A16\_UNORM                                                                                                                                                                                                                    |
| D3DFMT\_A8P8                        | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_P8                          | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_L8                          | DXGI\_FORMAT\_R8\_UNORM Note: Use .r swizzle in shader to duplicate red to other components to get D3D9 behavior.                                                                                                                                    |
| D3DFMT\_A8L8                        | DXGI\_FORMAT\_R8G8\_UNORM Note: Use swizzle .rrrg in shader to duplicate red and move green to the alpha components to get D3D9 behavior.                                                                                                            |
| D3DFMT\_A4L4                        | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_V8U8                        | DXGI\_FORMAT\_R8G8\_SNORM                                                                                                                                                                                                                            |
| D3DFMT\_L6V5U5                      | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_X8L8V8U8                    | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_Q8W8V8U8                    | DXGI\_FORMAT\_R8G8B8A8\_SNORM                                                                                                                                                                                                                        |
| D3DFMT\_V16U16                      | DXGI\_FORMAT\_R16G16\_SNORM                                                                                                                                                                                                                          |
| D3DFMT\_W11V11U10                   | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_A2W10V10U10                 | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_UYVY                        | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_R8G8\_B8G8                  | DXGI\_FORMAT\_G8R8\_G8B8\_UNORM (in DX9 the data was scaled up by 255.0f, but this can be handled in shader code).                                                                                                                                   |
| D3DFMT\_YUY2                        | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_G8R8\_G8B8                  | DXGI\_FORMAT\_R8G8\_B8G8\_UNORM (in DX9 the data was scaled up by 255.0f, but this can be handled in shader code).                                                                                                                                   |
| D3DFMT\_DXT1                        | DXGI\_FORMAT\_BC1\_UNORM & DXGI\_FORMAT\_BC1\_UNORM\_SRGB                                                                                                                                                                                            |
| D3DFMT\_DXT2                        | DXGI\_FORMAT\_BC1\_UNORM & DXGI\_FORMAT\_BC1\_UNORM\_SRGB Note: DXT1 and DXT2 are the same from an API/hardware perspective... only difference was 'premultiplied alpha', which can be tracked by an application and doesn't need a separate format. |
| D3DFMT\_DXT3                        | DXGI\_FORMAT\_BC2\_UNORM & DXGI\_FORMAT\_BC2\_UNORM\_SRGB                                                                                                                                                                                            |
| D3DFMT\_DXT4                        | DXGI\_FORMAT\_BC2\_UNORM & DXGI\_FORMAT\_BC2\_UNORM\_SRGB Note: DXT3 and DXT4 are the same from an API/hardware perspective... only difference was 'premultiplied alpha', which can be tracked by an application and doesn't need a separate format. |
| D3DFMT\_DXT5                        | DXGI\_FORMAT\_BC3\_UNORM & DXGI\_FORMAT\_BC3\_UNORM\_SRGB                                                                                                                                                                                            |
| D3DFMT\_D16 & D3DFMT\_D16\_LOCKABLE | DXGI\_FORMAT\_D16\_UNORM                                                                                                                                                                                                                             |
| D3DFMT\_D32                         | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_D15S1                       | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_D24S8                       | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_D24X8                       | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_D24X4S4                     | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_D16                         | DXGI\_FORMAT\_D16\_UNORM                                                                                                                                                                                                                             |
| D3DFMT\_D32F\_LOCKABLE              | DXGI\_FORMAT\_D32\_FLOAT                                                                                                                                                                                                                             |
| D3DFMT\_D24FS8                      | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_S1D15                       | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_S8D24                       | DXGI\_FORMAT\_D24\_UNORM\_S8\_UINT                                                                                                                                                                                                                   |
| D3DFMT\_X8D24                       | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_X4S4D24                     | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_L16                         | DXGI\_FORMAT\_R16\_UNORM Note: Use .r swizzle in shader to duplicate red to other components to get D3D9 behavior.                                                                                                                                   |
| D3DFMT\_INDEX16                     | DXGI\_FORMAT\_R16\_UINT                                                                                                                                                                                                                              |
| D3DFMT\_INDEX32                     | DXGI\_FORMAT\_R32\_UINT                                                                                                                                                                                                                              |
| D3DFMT\_Q16W16V16U16                | DXGI\_FORMAT\_R16G16B16A16\_SNORM                                                                                                                                                                                                                    |
| D3DFMT\_MULTI2\_ARGB8               | Not available                                                                                                                                                                                                                                        |
| D3DFMT\_R16F                        | DXGI\_FORMAT\_R16\_FLOAT                                                                                                                                                                                                                             |
| D3DFMT\_G16R16F                     | DXGI\_FORMAT\_R16G16\_FLOAT                                                                                                                                                                                                                          |
| D3DFMT\_A16B16G16R16F               | DXGI\_FORMAT\_R16G16B16A16\_FLOAT                                                                                                                                                                                                                    |
| D3DFMT\_R32F                        | DXGI\_FORMAT\_R32\_FLOAT                                                                                                                                                                                                                             |
| D3DFMT\_G32R32F                     | DXGI\_FORMAT\_R32G32\_FLOAT                                                                                                                                                                                                                          |
| D3DFMT\_A32B32G32R32F               | DXGI\_FORMAT\_R32G32B32A32\_FLOAT                                                                                                                                                                                                                    |
| D3DFMT\_CxV8U8                      | Not available                                                                                                                                                                                                                                        |
| D3DDECLTYPE\_FLOAT1                 | DXGI\_FORMAT\_R32\_FLOAT                                                                                                                                                                                                                             |
| D3DDECLTYPE\_FLOAT2                 | DXGI\_FORMAT\_R32G32\_FLOAT                                                                                                                                                                                                                          |
| D3DDECLTYPE\_FLOAT3                 | DXGI\_FORMAT\_R32G32B32\_FLOAT                                                                                                                                                                                                                       |
| D3DDECLTYPE\_FLOAT4                 | DXGI\_FORMAT\_R32G32B32A32\_FLOAT                                                                                                                                                                                                                    |
| D3DDECLTYPED3DCOLOR                 | Not available                                                                                                                                                                                                                                        |
| D3DDECLTYPE\_UBYTE4                 | DXGI\_FORMAT\_R8G8B8A8\_UINT Note: Shader gets UINT values, but if Direct3D 9 style integral floats are needed (0.0f, 1.0f... 255.f), UINT can just be converted to float32 in shader.                                                               |
| D3DDECLTYPE\_SHORT2                 | DXGI\_FORMAT\_R16G16\_SINT Note: Shader gets SINT values, but if Direct3D 9 style integral floats are needed, SINT can just be converted to float32 in shader.                                                                                       |
| D3DDECLTYPE\_SHORT4                 | DXGI\_FORMAT\_R16G16B16A16\_SINT Note: Shader gets SINT values, but if Direct3D 9 style integral floats are needed, SINT can just be converted to float32 in shader.                                                                                 |
| D3DDECLTYPE\_UBYTE4N                | DXGI\_FORMAT\_R8G8B8A8\_UNORM                                                                                                                                                                                                                        |
| D3DDECLTYPE\_SHORT2N                | DXGI\_FORMAT\_R16G16\_SNORM                                                                                                                                                                                                                          |
| D3DDECLTYPE\_SHORT4N                | DXGI\_FORMAT\_R16G16B16A16\_SNORM                                                                                                                                                                                                                    |
| D3DDECLTYPE\_USHORT2N               | DXGI\_FORMAT\_R16G16\_UNORM                                                                                                                                                                                                                          |
| D3DDECLTYPE\_USHORT4N               | DXGI\_FORMAT\_R16G16B16A16\_UNORM                                                                                                                                                                                                                    |
| D3DDECLTYPE\_UDEC3                  | Not available                                                                                                                                                                                                                                        |
| D3DDECLTYPE\_DEC3N                  | Not available                                                                                                                                                                                                                                        |
| D3DDECLTYPE\_FLOAT16\_2             | DXGI\_FORMAT\_R16G16\_FLOAT                                                                                                                                                                                                                          |
| D3DDECLTYPE\_FLOAT16\_4             | DXGI\_FORMAT\_R16G16B16A16\_FLOAT                                                                                                                                                                                                                    |
| FourCC 'ATI1'                       | DXGI\_FORMAT\_BC4\_UNORM                                                                                                                                                                                                                             |
| FourCC 'ATI2'                       | DXGI\_FORMAT\_BC5\_UNORM                                                                                                                                                                                                                             |



 

¹DXGI 1.1, which is included in the Direct3D 11 runtime, includes BGRA formats. However, support for these formats is optional for Direct3D 10 and 10.1 devices with drivers that are implemented to the Windows Display Driver Model (WDDM) for Windows Vista (WDDM 1.0). Consider using DXGI\_FORMAT\_R8G8B8A8\_UNORM instead. Alternatively, you can create your device with [**D3D10\_CREATE\_DEVICE\_BGRA\_SUPPORT**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_create_device_flag) to ensure that you only support computers with the Direct3D 11.0 runtime and a WDDM 1.1 driver or higher installed.

²DXGI 1.0 defined 5:6:5 and 5:5:5:1 formats, but they were not supported by the Direct3D 10.x or Direct3D 11.0 runtime. These formats are optionally supported with DXGI 1.2 in the DirectX 11.1 runtime, which is required for feature level 11.1 video adapters and WDDM 1.2 (display driver model starting with Windows 8) drivers and already supported on 10level9 feature levels.

³DXGI 1.2 introduced the 4:4:4:4 format. This format is optionally supported in the DirectX 11.1 runtime, which is required for feature level 11.1 video adapters and WDDM 1.2 drivers and already supported on 10level9 feature levels.

For uncompressed formats, DXGI has limited the support for arbitrary pixel format patterns; all uncompressed formats must be of type RGBA. This might require swizzling of existing assets pixel formats, which we recommend that you compute as an offline pre-process pass where possible.

## Porting Shaders

### Direct3D 10 Shaders are Authored in HLSL

Direct3D 10 limits the use of assembly language to that of debugging purposes only, therefore any hand written assembly shaders used in Direct3D 9 will need to be converted to HLSL.

### Shader Signatures and Linkage

We discussed the requirements for Input Assembly linkage to Vertex shader input signatures earlier in this document (see above). Note that the Direct3D 10 runtime has also tightened the requirements for stage to stage linkage between shaders. This change will affect shader sources where the binding between stages may not have been fully described under Direct3D 9. For example:


```
VS_OUTPUT                       PS_INPUT
float4   pos : SV_POSITION;     float4 pos : SV_POSITION;
float4   uv1 : TEXCOORD1;       float4 uv1 : TEXCOORD1;
float4x3 tangentSp : TEXCOORD2; float4 tangent : TEXCOORD2; *
float4   Color : TEXCOORD6;     float4 color : TEXCOORD6;
```



\* Broken VS - PS Linkage - even though the pixel shader may not be interested in the full matrix, the linkage must specify the full float4x3.

Note, the linkage semantics between stages must match exactly however, the target stages inputs may be a prefix of the values being output. In the example above, the pixel shader could have position and texcoord1 as the only inputs, but it could not have the position and texcoord2 as the only inputs due to the ordering constraints.

### HLSL Shader Stage linkages

Linkage between shaders may occur at any of the following points in the pipeline:

-   Input Assembler to Vertex Shader
-   Vertex Shader to Pixel Shader
-   Vertex Shader to Geometry Shader
-   Vertex Shader to Stream Output
-   Geometry Shader to Pixel Shader
-   Geometry Shader to Stream Out

### Constant Buffers

For ease of porting content from Direct3D 9 an initial approach to constant management outside of the Effects system might involve the creation of a single constant buffer containing all the required constants. It is important for performance to order constants into buffers by the expected frequency of update. This organization will reduce the amount of redundant constant sets to a minimum.

### User clip planes in HLSL on feature level 9 and higher

Starting with Windows 8, you can use the **clipplanes** function attribute in an HLSL [function declaration](../direct3dhlsl/dx-graphics-hlsl-function-syntax.md) rather than [SV\_ClipDistance](../direct3dhlsl/dx-graphics-hlsl-semantics.md) to make your shader work on [feature level](../direct3d11/overviews-direct3d-11-devices-downlevel-intro.md) 9\_x as well as feature level 10 and higher. For more info, see [User clip planes on feature level 9 hardware](../direct3dhlsl/user-clip-planes-on-10level9.md).

## Additional Direct3D 10 Differences to Watch For

### Integers as Input

In Direct3D 9, there was no real hardware support for integer data types, however Direct3D 10 hardware supports explicit integer types. If you have floating-point data in your vertex buffer, then you must have a float input. Otherwise an integer type will be the bit pattern representation of the floating-point value. An integer type is not allowed for a pixel shader input unless the value is marked for no interpolation (see [Interpolation Modifiers](../direct3dhlsl/dx-graphics-hlsl-struct.md)).

### Mouse Cursors

On previous versions of Windows, the standard GDI mouse cursor routines did not operate correctly on all full-screen exclusive devices. The [**SetCursorProperties**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setcursorproperties), [**ShowCursor**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-showcursor), and [**SetCursorPosition**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setcursorposition) APIs were added to handle these cases. Since Windows Vista's version of GDI fully understands [DXGI](../direct3ddxgi/d3d10-graphics-programming-guide-dxgi.md) surfaces, there is no need for this specialized mouse cursor API so there is no Direct3D 10 equivalent. Direct3D 10 applications should instead use the standard [GDI mouse cursor routines](../menurc/cursors.md) for mouse cursors.

### Mapping Texels to Pixels in Direct3D 10

In Direct3D 9, texel centers and pixel centers were a half unit apart (see [Directly Mapping Texels to Pixels (Direct3D 9)](../direct3d9/directly-mapping-texels-to-pixels.md)). In Direct3D 10, texel centers are already at half-units, so there is no need to shift vertex coordinates at all.

Rendering full-screen quads is more straight-forward with Direct3D 10. Full-screen quads should be defined in clipspace (-1,1) and simply passed through the vertex shader with no changes. This way, there is no need to reload your vertex buffer every time the screen resolution changes, and there's no extra work in the pixel shader to manipulate the texture coordinates.

### Reference Counting Behavior Changes

Unlike previous Direct3D versions, the various Set functions will not hold a reference to the devices objects. This means that the application must ensure that it holds a reference on the object for as long as it would like that object to be bound to the pipeline. When the ref count of the object drops to zero, then the object will be unbound from the pipeline as it is destroyed. This style of reference holding is also known as weak-reference holding, so therefore each bind location on the Device object holds a weak-reference to the interface/ object. Unless explicitly mentioned otherwise, this behavior should be assumed for all Set methods. Whenever destruction of an object causes a bind point to be set to **NULL** out, the Debug Layer will issue a warning. Note, calls to device Get methods such as [**OMGetRenderTargets**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-omgetrendertargets) will increase the reference count of objects being returned.

### Test Cooperative Level

The functionality of the Direct3D 9 API [**TestCooperativeLevel**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-testcooperativelevel) is analogous to setting the [DXGI\_PRESENT\_TEST](../direct3ddxgi/dxgi-present.md) when calling [**Present**](/windows/win32/api/dxgi/nf-dxgi-idxgiswapchain-present).

### StretchRect

A function similar to the Direct3D 9 [**IDirect3DDevice9::StretchRect**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-stretchrect) method is not available in Direct3D 10 and 10.1. To copy resource surfaces, use [**ID3D10Device::CopySubresourceRegion**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copysubresourceregion). For resizing operations, render to a texture by using texture filtering. For converting MSAA surfaces to non-MSAA surfaces, use [**ID3D10Device::ResolveSubresource**](/windows/desktop/api/d3d10/nf-d3d10-id3d10device-resolvesubresource).

## Additional Direct3D 10.1 Differences

Windows Vista with Service Pack 1 (SP1) included a minor update to Direct3D 10 and Direct3D 10.1, which exposed the following additional hardware features:

-   MSAA per-sample shaders
-   MSAA depth read-back
-   Independent blend modes per render target
-   Cube map arrays
-   Render to block-compressed (BC) formats

The Direct3D 10.1 update added support for the following new interfaces, which are derived from existing interfaces:

-   [**ID3D10Device1**](/windows/desktop/api/D3D10_1/nn-d3d10_1-id3d10device1)
-   [**ID3D10BlendState1**](/windows/desktop/api/D3D10_1/nn-d3d10_1-id3d10blendstate1)
-   [**ID3D10ShaderResourceView1**](/windows/desktop/api/d3d10_1/nn-d3d10_1-id3d10shaderresourceview1)

The Direct3D 10.1 update also included the following additional structures:

-   [**D3D10\_RENDER\_TARGET\_BLEND\_DESC1**](/windows/desktop/api/d3d10_1/ns-d3d10_1-d3d10_render_target_blend_desc1)
-   [**D3D10\_BLEND\_DESC1**](/windows/desktop/api/D3D10_1/ns-d3d10_1-d3d10_blend_desc1)
-   [**D3D10\_SHADER\_RESOURCE\_VIEW\_DESC1**](/windows/desktop/api/d3d10_1/ns-d3d10_1-d3d10_shader_resource_view_desc1)

The Direct3D 10.1 API includes a new concept named feature level. This concept means that you can use the Direct3D 10.1 API to drive Direct3D 10.0 ([**D3D10\_FEATURE\_LEVEL\_10\_0**](/windows/desktop/api/D3D10_1/ne-d3d10_1-d3d10_feature_level1)) or Direct3D 10.1 ([**D3D10\_FEATURE\_LEVEL\_10\_1**](/windows/desktop/api/D3D10_1/ne-d3d10_1-d3d10_feature_level1)) hardware. Because the Direct3D 10.1 API is derived from the Direct3D 10 interfaces, applications can create a Direct3D 10.1 device, then use it as a Direct3D 10.0 device except where new 10.1-specific features are needed (provided that the **D3D10\_FEATURE\_LEVEL\_10\_1** feature-level is present and supports these features).

> [!Note]  
> Direct3D 10.1 devices can use the existing 10.0 HLSL shader profiles (vs\_4\_0, ps\_4\_0, gs\_4\_0) and the new 10.1 profiles (vs\_4\_1, ps\_4\_1, gs\_4\_1) with additional HLSL instructions and capabilities.

 

Windows 7 contained a minor update to the Direct3D 10.1 API that is included in the Direct3D 11 runtime. This update adds support for the following feature levels:

-   [**D3D10\_FEATURE\_LEVEL\_9\_1**](/windows/desktop/api/D3D10_1/ne-d3d10_1-d3d10_feature_level1)
-   [**D3D10\_FEATURE\_LEVEL\_9\_2**](/windows/desktop/api/D3D10_1/ne-d3d10_1-d3d10_feature_level1)
-   [**D3D10\_FEATURE\_LEVEL\_9\_3**](/windows/desktop/api/D3D10_1/ne-d3d10_1-d3d10_feature_level1)

Windows 7 also added support to Direct3D 10.1 for [Windows Advanced Rasterization Platform (WARP)](../direct3darticles/directx-warp.md). You can specify a WARP driver by using [**D3D10\_DRIVER\_TYPE\_WARP**](/windows/desktop/api/D3D10misc/ne-d3d10misc-d3d10_driver_type).

For more information about Direct3D 10.1, see [Direct3D 10.1 Features](d3d10-graphics-programming-guide-10-1.md) and the [**D3D10\_FEATURE\_LEVEL1**](/windows/desktop/api/D3D10_1/ne-d3d10_1-d3d10_feature_level1) enumeration.

## Related topics

<dl> <dt>

[Programming Guide for Direct3D 10](d3d10-graphics-programming-guide.md)
</dt> </dl>

 

 
