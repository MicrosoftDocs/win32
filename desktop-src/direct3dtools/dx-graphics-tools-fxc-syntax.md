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

<dl> <dt>

<span id="SwitchOptions"></span><span id="switchoptions"></span><span id="SWITCHOPTIONS"></span>*SwitchOptions*
</dt> <dd>

\[in\] Compile options. There is just one required option, and many more that are optional. Separate each with a space or colon.



| Required SwitchOptions | Description                               |
|------------------------|-------------------------------------------|
| /T <*profile*>   | Shader model (see [Profiles](#profiles)). |



 



<table><colgroup><col style="width: 33%" /><col style="width: 33%" /><col style="width: 33%" /></colgroup><thead><tr class="header"><th>New for Direct3D 12</th><th>Optional SwitchOptions</th><th>Description</th></tr></thead><tbody><tr class="odd"><td>/?, /help</td><td>Print help for FXC.exe.</td></tr><tr class="even"><td>@<<em>command.option.file</em>></td><td>File that contains additional compile options.<ul><li>This option can be mixed with other command line compile options.</li><li>The <em>command.option.file</em> must contain only one option per line.</li><li>The <em>command.option.file</em> cannot contain any blank lines.</li><li>Options specified in the file must not contain any leading or trailing spaces.</li></ul></td></tr><tr class="odd"><td>Yes</td><td>/all_resources_bound</td><td>Enable aggressive flattening in SM5.1+.</td></tr><tr class="even"><td>/Cc</td><td>Output color-coded assembly.</td></tr><tr class="odd"><td>/compress</td><td>Compress DX10 shader bytecode from files.</td></tr><tr class="even"><td>/D <<em>id</em>>=<<em>text</em>></td><td>Define macro.</td></tr><tr class="odd"><td>/decompress</td><td>Decompress DX10 shader bytecode from first file. Output files should be listed in the order they were in during compression.</td></tr><tr class="even"><td>/dumpbin</td><td>Loads a binary file rather than compiling a shader.</td></tr><tr class="odd"><td>/E <name></td><td>Shader entry point. If no entry point is given, <strong>main</strong> is considered to be the shader entry name.</td></tr><tr class="even"><td>Yes</td><td>/enable_unbounded_descriptor_tables</td><td>Enables unbounded descriptor tables.</td></tr><tr class="odd"><td>Yes</td><td>/extractrootsignature <<em>file</em>></td><td>Extract root signature from shader bytecode.</td></tr><tr class="even"><td>/Fc <<em>file</em>></td><td>Output assembly code listing file.</td></tr><tr class="odd"><td>/Fd <<em>file</em>></td><td>Extract shader program database (PDB) info and write to the given file.When you compile the shader, use /Fd to generate a PDB file with shader debugging info.</td></tr><tr class="even"><td>/Fe <<em>file</em>></td><td>Output warnings and errors to the given file.</td></tr><tr class="odd"><td>/Fh <<em>file</em>></td><td>Output header file containing object code.</td></tr><tr class="even"><td>/Fl <<em>file</em>></td><td>Output a library .</td></tr><tr class="odd"><td>/Fo <<em>file</em>></td><td>Output object file. Often given the extension &quot;.fxc&quot;, though other extensions are used, such as &quot;.o&quot;, &quot;.obj&quot; or &quot;.dxbc&quot;.</td></tr><tr class="even"><td>/Fx <<em>file</em>></td><td>Output assembly code and hex listing file.</td></tr><tr class="odd"><td>/Gch</td><td>Compile as a child effect for fx_4_x profiles.<blockquote>[!Note]<br />
Support for legacy Effects profiles is deprecated.</blockquote><br/></td></tr><tr class="even"><td>/Gdp</td><td>Disable effect performance mode.</td></tr><tr class="odd"><td>/Gec</td><td>Enable backwards compatibility mode.</td></tr><tr class="even"><td>/Ges</td><td>Enable strict mode.</td></tr><tr class="odd"><td>/getprivate <<em>file</em>></td><td>Save private data from the shader blob (compiled shader binary) to the given file. Extracts private data, previously embedded by /setprivate, from the shader blob. <br/> You must specify the /dumpbin option with /getprivate. For example:<span data-codelanguage=""></span><table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td><pre><code>fxc /getprivate ps01.private.data 
    /dumpbin ps01.with.private.obj</code></pre></td></tr></tbody></table></td></tr><tr class="even"><td>/Gfa</td><td>Avoid flow control constructs.</td></tr><tr class="odd"><td>/Gfp</td><td>Prefer flow control constructs.</td></tr><tr class="even"><td>/Gis</td><td>Force IEEE strictness.</td></tr><tr class="odd"><td>/Gpp</td><td>Force partial precision.</td></tr><tr class="even"><td>/I <<em>include</em>></td><td>Additional include path.</td></tr><tr class="odd"><td>/Lx</td><td>Output hexadecimal literals .</td></tr><tr class="even"><td>/matchUAVs</td><td>Match template shader UAV slot allocations in the current shader. For more info, see <a href="#remarks">Remarks</a>.</td></tr><tr class="odd"><td>/mergeUAVs</td><td>Merge UAV slot allocations of template shader and the current shader. For more info, see <a href=""></a><a href="#remarks">Remarks</a>.</td></tr><tr class="even"><td>/Ni</td><td>Output instruction numbers in assembly listings.</td></tr><tr class="odd"><td>/No</td><td>Output instruction byte offset in assembly listings. When you produce assembly, use /No to annotate it with the byte offset for each instruction.</td></tr><tr class="even"><td>/nologo</td><td>Suppress copyright message.</td></tr><tr class="odd"><td>/Od</td><td>Disable optimizations. /Od implies /Gfp though output may not be identical to /Od /Gfp.</td></tr><tr class="even"><td>/Op</td><td>Disable preshaders (deprecated).</td></tr><tr class="odd"><td>/O0 /O1, /O2, /O3</td><td>Optimization levels. O1 is the default setting.<ul><li>O0 - Disables instruction reordering. This helps reduce register load and enables faster loop simulation.</li><li>O1 - Disables instruction reordering for ps_3_0 and up.</li><li>O2 - Same as O1. Reserved for future use.</li><li>O3 - Same as O1. Reserved for future use.</li></ul></td></tr><tr class="even"><td>/P <<em>file</em>></td><td>Preprocess to file (must be used alone).</td></tr><tr class="odd"><td>/Qstrip_debug</td><td>Strip debug data from shader bytecode for 4_0+ profiles.</td></tr><tr class="even"><td>/Qstrip_priv</td><td><p>Strip the private data from 4_0+ shader bytecode. Removes private data (arbitrary sequence of bytes) from the shader blob (compiled shader binary) that you previously embedded with the /setprivate <file> option.</p><p>You must specify the /dumpbin option with /Qstrip_priv. For example:</p><div class="code"><span data-codelanguage=""></span><table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td><pre><code>fxc /Qstrip_priv /dumpbin /Fo ps01.no.private.obj 
    ps01.with.private.obj</code></pre></td></tr></tbody></table></div></td></tr><tr class="odd"><td>/Qstrip_reflect</td><td>Strip reflection data from shader bytecode for 4_0+ profiles.</td></tr><tr class="even"><td>Yes</td><td>/Qstrip_rootsignature</td><td>Strip root signature from shader bytecode.</td></tr><tr class="odd"><td>/res_may_alias</td><td>Assume that UAVs/SRVs may alias for cs_5_0+ .</td></tr><tr class="even"><td>/setprivate <<em>file</em>></td><td>Add private data in the given file to the compiled shader blob. Embeds the given file, which is treated as a raw buffer, to the shader blob. Use /setprivate to add private data when you compile a shader. Or, use the /dumpbin option with /setprivate to load an existing shader object, and then after the object is in memory, to add the private data blob. For example, use either a single command with /setprivate to add private data to a compiled shader blob:<div class="code"><span data-codelanguage=""></span><table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td><pre><code>fxc /T ps_4_0 /Fo ps01.with.private.obj ps01.fx 
    /setprivate ps01.private.data</code></pre></td></tr></tbody></table></div>Or, use two commands where the second command loads a shader object and then adds private data:<div class="code"><span data-codelanguage=""></span><table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td><pre><code>fxc /T ps_4_0 /Fo ps01.no.private.obj ps01.fx
fxc /dumpbin /Fo ps01.with.private.obj ps01.no.private.obj 
    /setprivate ps01.private.data</code></pre></td></tr></tbody></table></div></td></tr><tr class="odd"><td>Yes</td><td>/setrootsignature <<em>file</em>></td><td>Attach root signature to shader bytecode.</td></tr><tr class="even"><td>/shtemplate <<em>file</em>></td><td>Use given template shader file for merging (/mergeUAVs) and matching (/matchUAVs) resources. For more info, see <a href="#remarks">Remarks</a>.</td></tr><tr class="odd"><td>/Vd</td><td>Disable validation.</td></tr><tr class="even"><td>Yes</td><td>/verifyrootsignature <<em>file</em>></td><td>Verify shader bytecode against root signature.</td></tr><tr class="odd"><td>/Vi</td><td>Display details about the include process.</td></tr><tr class="even"><td>/Vn <<em>name</em>></td><td>Use name as variable name in header file.</td></tr><tr class="odd"><td>/WX</td><td>Treat warnings as errors.</td></tr><tr class="even"><td>/Zi</td><td>Enable debugging information.</td></tr><tr class="odd"><td>/Zpc</td><td>Pack matrices in column-major order.</td></tr><tr class="even"><td>/Zpr</td><td>Pack matrices in row-major order.</td></tr></tbody></table>



 

</dd> <dt>

<span id="Filenames"></span><span id="filenames"></span><span id="FILENAMES"></span>*Filenames*
</dt> <dd>

\[in\] The files that contains the shader(s) and/or the effect(s).

</dd> </dl>

## Remarks

Use the /mergeUAVs, /matchUAVs, and /shtemplate options to align the UAV binding slots for a chain of shaders.

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

    

    Note that you don't have to recompile C.fx in the second pass.

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
</dl> For more info about shader linking, see <a href="https://msdn.microsoft.com/library/windows/desktop/dn280558"><strong>ID3D11Linker</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dn280535"><strong>ID3D11FunctionLinkingGraph</strong></a>. <br/></td></tr><tr class="odd"><td>Hull Shader</td><td><dl> hs_5_0<br />
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

  : this option requires the D3dcompiler\_47.dll or a later version of the DLL.

For Direct3D 12 refer to [Specifying Root Signatures in HLSL](https://msdn.microsoft.com/library/windows/desktop/dn913202), [Resource Binding in HLSL](https://msdn.microsoft.com/library/windows/desktop/dn899207) and [Dynamic Indexing using HLSL 5.1](https://msdn.microsoft.com/library/windows/desktop/mt186614).

In Direct3D 10 use the API to get the vertex, geometry, and pixel-shader profile best suited to a given device by calling these functions: [**D3D10GetVertexShaderProfile**](https://msdn.microsoft.com/library/windows/desktop/bb205099), [**D3D10GetPixelShaderProfile**](https://msdn.microsoft.com/library/windows/desktop/bb205097), and [**D3D10GetGeometryShaderProfile**](https://msdn.microsoft.com/library/windows/desktop/bb205093).

In Direct3D 9 use the [**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/bb174320) or [**GetDeviceCaps**](https://msdn.microsoft.com/library/windows/desktop/bb174385) methods to retrieve the vertex and pixel-shader profiles supported by a device. The [**D3DCAPS9**](https://msdn.microsoft.com/library/windows/desktop/bb172513) structure returned by those methods indicates the vertex and pixel-shader profiles supported by a device in its **VertexShaderVersion** and **PixelShaderVersion** members.

For examples, see [Compiling with the Current Compiler](dx-graphics-tools-fxc-using.md).

## Related topics

<dl> <dt>

[Effect-Compiler Tool](fxc.md)
</dt> </dl>

 

 





