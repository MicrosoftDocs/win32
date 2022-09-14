---
title: Syntax
description: Here is the syntax for calling FXC.exe, the effect-compiler tool. For an example, see Offline Compiling.
ms.assetid: 3aee89bd-02e1-4de1-8552-ba36814f8464
keywords:
- fxc, syntax
ms.topic: article
ms.date: 05/31/2018
---

# Syntax

Here is the syntax for calling FXC.exe, the effect-compiler tool. For an example, see [Offline Compiling](dx-graphics-tools-fxc-using.md).

-   [Usage](#usage)
-   [Arguments](#arguments)
-   [Remarks](#remarks)
-   [Profiles](#profiles)
-   [Version notes](#version-notes)
-   [Related topics](#related-topics)

## Usage

**fxc** *SwitchOptions* *Filenames*

## Arguments
Separate each switch option with a space or a colon.

### *SwitchOptions*
\[in\] Compile options. There is just one required option, and many more that are optional. Separate each with a space or colon.

#### Required option
##### /T <*profile*>
Shader model (see [Profiles](#profiles)).

#### Optional options
##### /?, /help
Print help for `FXC.exe`.

##### @<*command.option.file*>
File that contains additional compile options. This option can be mixed with other command line compile options. The *command.option.file* must contain only one option per line. The *command.option.file* cannot contain any blank lines. Options specified in the file must not contain any leading or trailing spaces.

##### /all_resources_bound
Enable aggressive flattening in SM5.1+. New for Direct3D 12.

##### /Cc
Output color-coded assembly.

##### /compress
Compress DX10 shader bytecode from files.

##### /D <*id*>=<*text*>
Define macro.

##### /decompress
Decompress DX10 shader bytecode from first file. Output files should be listed in the order they were in during compression.

##### /dumpbin
Loads a binary file rather than compiling a shader.

##### /E &lt;name&gt;
Shader entry point. If no entry point is given, **main** is considered to be the shader entry name.

##### /enable_unbounded_descriptor_tables
Enables unbounded descriptor tables. New for Direct3D 12.

##### /extractrootsignature <*file*>
Extract root signature from shader bytecode. New for Direct3D 12.

##### /Fc <*file*>
Output assembly code listing file.

##### /Fd <*file*>
Extract shader program database (PDB) info and write to the given file.When you compile the shader, use /Fd to generate a PDB file with shader debugging info.

##### /Fe <*file*>
Output warnings and errors to the given file.

##### /Fh <*file*>
Output header file containing object code.

##### /Fl <*file*
Output a library. Requires the D3dcompiler\_47.dll or a later version of the DLL.

##### /Fo <*file*>
Output object file. Often given the extension &quot;.fxc&quot;, though other extensions are used, such as &quot;.o&quot;, &quot;.obj&quot; or &quot;.dxbc&quot;.

##### /Fx <*file*>
Output assembly code and hex listing file.

##### /Gch
Compile as a child effect for fx_4_x profiles.

> [!NOTE]
> Support for legacy Effects profiles is deprecated.

##### /Gdp
Disable effect performance mode.

##### /Gec
Enable backward compatibility mode.

##### /Ges
Enable strict mode.

##### /getprivate <*file*>
Save private data from the shader blob (compiled shader binary) to the given file. Extracts private data, previously embedded by /setprivate, from the shader blob.

You must specify the /dumpbin option with /getprivate. For example:

```console
fxc /getprivate ps01.private.data 
    /dumpbin ps01.with.private.obj
```
	
##### /Gfa
Avoid flow control constructs.

##### /Gfp
Prefer flow control constructs.

##### /Gis
Force IEEE strictness.

##### /Gpp
Force partial precision.
	
##### /I <*include*>
Additional include path.

##### /Lx
Output hexadecimal literals. Requires the D3dcompiler\_47.dll or a later version of the DLL.

##### /matchUAVs
Match template shader UAV slot allocations in the current shader. For more info, see <a href="#remarks">Remarks</a>.

##### /mergeUAVs
Merge UAV slot allocations of template shader and the current shader. For more info, see <a href=""></a><a href="#remarks">Remarks</a>.

##### /Ni
Output instruction numbers in assembly listings.

##### /No
Output instruction byte offset in assembly listings. When you produce assembly, use /No to annotate it with the byte offset for each instruction.

##### /nologo
Suppress copyright message.

##### /Od
Disable optimizations. /Od implies /Gfp, though output may not be identical to /Od /Gfp.

##### /Op
Disable preshaders (deprecated).

##### /O0 /O1, /O2, /O3
Optimization levels. O1 is the default setting.
- O0 - Disables instruction reordering. This helps reduce register load and enables faster loop simulation.
- O1 - Disables instruction reordering for ps_3_0 and up.
- O2 - Same as O1. Reserved for future use.
- O3 - Same as O1. Reserved for future use.

##### /P <*file*>
Preprocess to file (must be used alone).

##### /Qstrip_debug
Strip debug data from shader bytecode for 4_0+ profiles.

##### /Qstrip_priv
Strip the private data from 4_0+ shader bytecode. Removes private data (arbitrary sequence of bytes) from the shader blob (compiled shader binary) that you previously embedded with the `/setprivate <file>` option.

You must specify the /dumpbin option with /Qstrip_priv. For example:

```console
fxc /Qstrip_priv /dumpbin /Fo ps01.no.private.obj 
    ps01.with.private.obj
```

##### /Qstrip_reflect
Strip reflection data from shader bytecode for 4_0+ profiles.

##### /Qstrip_rootsignature
Strip root signature from shader bytecode. New for Direct3D 12.

##### /res_may_alias
Assume that UAVs/SRVs may alias for cs_5_0+. Requires the D3dcompiler\_47.dll or a later version of the DLL.

##### /setprivate <*file*>
Add private data in the given file to the compiled shader blob. Embeds the given file, which is treated as a raw buffer, to the shader blob. Use /setprivate to add private data when you compile a shader. Or, use the /dumpbin option with /setprivate to load an existing shader object, and then after the object is in memory, to add the private data blob. For example, use either a single command with /setprivate to add private data to a compiled shader blob:

```console
fxc /T ps_4_0 /Fo ps01.with.private.obj ps01.fx 
    /setprivate ps01.private.data
```
	
Or, use two commands where the second command loads a shader object and then adds private data:

```console
fxc /T ps_4_0 /Fo ps01.no.private.obj ps01.fx
fxc /dumpbin /Fo ps01.with.private.obj ps01.no.private.obj 
    /setprivate ps01.private.data
```
	
##### /setrootsignature <*file*>
Attach root signature to shader bytecode. New for Direct3D 12.

##### /shtemplate <*file*>
Use given template shader file for merging (/mergeUAVs) and matching (/matchUAVs) resources. For more info, see <a href="#remarks">Remarks</a>.

##### /Vd
Disable validation.

##### /verifyrootsignature <*file*>
Verify shader bytecode against root signature. New for Direct3D 12.

##### /Vi
Display details about the include process.

##### /Vn <*name*>
Use name as variable name in header file.

##### /WX
Treat warnings as errors.

##### /Zi
Enable debugging information.

##### /Zpc
Pack matrices in column-major order.

##### /Zpr
Pack matrices in row-major order.

### *Filenames*

\[in\] The files that contains the shader(s) and/or the effect(s).

## Remarks

Use the `/mergeUAVs`, `/matchUAVs`, and `/shtemplate` options to align the UAV binding slots for a chain of shaders.

Suppose you have shaders A.fx, B.fx, and C.fx. To align the UAV binding slots for this chain of shaders, you need two passes of compilation:

**To align the UAV binding slots for a chain of shaders**

1.  Use /mergeUAVs to compile shaders, and specify a previously-compiled shader blob with /shtemplate. For example:
    ```
    fxc.exe /T cs_5_0 C.fx /Fo C.o /mergeUAVs /shtemplate Btmp.o
    ```
2.  Use /matchUAVs to compile shaders, and specify the last shader blob from the first pass with /shtemplate. You can compile in any order. For example:
    ```
    fxc.exe /T cs_5_0 A.fx /Fo A.o /matchUAVs /shtemplate C.o
    ```
You don't have to recompile C.fx in the second pass.

After you perform the preceding two compilation passes, you can use A.o, B.o, and C.o as final shader blobs with aligned UAV slots.

## Profiles

Each shader model is labeled with an HLSL profile. To compile a shader against a particular shader model, choose the appropriate shader profile from the following table.

<table><thead><tr class="header"><th>Shader Type</th><th>Profiles</th></tr></thead><tbody><tr class="odd"><td>Compute Shader</td><td><dl> cs_4_0<br />
cs_4_1<br />
cs_5_0<br />
cs_5_1<br />
</dl></td></tr><tr class="even"><td>Domain Shader</td><td><dl> ds_5_0<br />
ds_5_1<br />
</dl></td></tr><tr class="odd"><td>Geometry Shader</td><td><dl> gs_4_0<br />
gs_4_1<br />
gs_5_0<br />
gs_5_1<br />
</dl></td></tr><tr class="even"><td>HLSL shader linking </td><td><dl> lib_4_0<br />
lib_4_1<br />
lib_4_0_level_9_1<br />
lib_4_0_level_9_1_vs_only<br />
lib_4_0_level_9_1_ps_only<br />
lib_4_0_level_9_3<br />
lib_4_0_level_9_3_vs_only<br />
lib_4_0_level_9_3_ps_only<br />
lib_5_0<br />
</dl> For more info about shader linking, see <a href="/windows/desktop/api/d3d11shader/nn-d3d11shader-id3d11linker"><strong>ID3D11Linker</strong></a> and <a href="/windows/desktop/api/d3d11shader/nn-d3d11shader-id3d11functionlinkinggraph"><strong>ID3D11FunctionLinkingGraph</strong></a>. <br/></td></tr><tr class="odd"><td>Hull Shader</td><td><dl> hs_5_0<br />
hs_5_1<br />
</dl></td></tr><tr class="even"><td>Pixel Shader</td><td><dl> ps_2_0<br />
ps_2_a<br />
ps_2_b<br />
ps_2_sw<br />
ps_3_0<br />
ps_3_sw<br />
ps_4_0<br />
ps_4_0_level_9_0<br />
ps_4_0_level_9_1<br />
ps_4_0_level_9_3<br />
ps_4_1<br />
ps_5_0<br />
ps_5_1<br />
</dl></td></tr><tr class="odd"><td>Root Signature</td><td><dl> rootsig_1_0<br />
</dl></td></tr><tr class="even"><td>Texture Shader</td><td><dl> tx_1_0<br />
</dl></td></tr><tr class="odd"><td>Vertex Shader</td><td><dl> vs_1_1<br />
vs_2_0<br />
vs_2_a<br />
vs_2_sw<br />
vs_3_0<br />
vs_3_sw<br />
vs_4_0<br />
vs_4_0_level_9_0<br />
vs_4_0_level_9_1<br />
vs_4_0_level_9_3<br />
vs_4_1<br />
vs_5_0<br />
vs_5_1<br />
</dl></td></tr></tbody></table>

## Version notes

For Direct3D 12 refer to [Specifying Root Signatures in HLSL](/windows/desktop/direct3d12/specifying-root-signatures-in-hlsl), [Resource Binding in HLSL](/windows/desktop/direct3d12/resource-binding-in-hlsl) and [Dynamic Indexing using HLSL 5.1](/windows/desktop/direct3d12/dynamic-indexing-using-hlsl-5-1).

In Direct3D 10 use the API to get the vertex, geometry, and pixel-shader profile best suited to a given device by calling these functions: [**D3D10GetVertexShaderProfile**](/windows/desktop/api/d3d10shader/nf-d3d10shader-d3d10getvertexshaderprofile), [**D3D10GetPixelShaderProfile**](/windows/desktop/api/d3d10shader/nf-d3d10shader-d3d10getpixelshaderprofile), and [**D3D10GetGeometryShaderProfile**](/windows/desktop/api/d3d10shader/nf-d3d10shader-d3d10getgeometryshaderprofile).

In Direct3D 9 use the [**GetDeviceCaps**](/windows/desktop/api/d3d9/nf-d3d9-idirect3d9-getdevicecaps) or [**GetDeviceCaps**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-getdevicecaps) methods to retrieve the vertex and pixel-shader profiles supported by a device. The [**D3DCAPS9**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dcaps9) structure returned by those methods indicates the vertex and pixel-shader profiles supported by a device in its **VertexShaderVersion** and **PixelShaderVersion** members.

For examples, see [Compiling with the Current Compiler](dx-graphics-tools-fxc-using.md).

## Related topics

* [Effect-Compiler Tool](fxc.md)
