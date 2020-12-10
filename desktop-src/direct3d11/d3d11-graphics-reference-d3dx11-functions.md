---
title: D3DX Functions (Direct3D 11 Graphics)
description: This section contains information about the D3DX 11 functions.
ms.assetid: 7548c02e-c8c2-4629-95ac-d21ca7a39f0a
keywords:
- functions, DirectX 11 D3DX
ms.topic: article
ms.date: 05/31/2018
---

# D3DX Functions (Direct3D 11 Graphics)

This section contains information about the D3DX 11 functions.

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 


## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="d3dx11compilefromfile.md"><strong>D3DX11CompileFromFile</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you compile offline by using the Fxc.exe command-line compiler or use one of the HLSL compile APIs, like the <a href="/windows/desktop/direct3dhlsl/d3dcompilefromfile"><strong>D3DCompileFromFile</strong></a> API.
</blockquote>
<br/> Compile a shader or an effect from a file.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11compilefrommemory.md"><strong>D3DX11CompileFromMemory</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you compile offline by using the Fxc.exe command-line compiler or use one of the HLSL compile APIs, like the <a href="/windows/desktop/direct3dhlsl/d3dcompile"><strong>D3DCompile</strong></a> API.
</blockquote>
<br/> Compile a shader or an effect that is loaded in memory.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11compilefromresource.md"><strong>D3DX11CompileFromResource</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use <a href="/windows/desktop/menurc/resources-functions">resource functions</a>, then compile offline by using the Fxc.exe command-line compiler or use one of the HLSL compile APIs, like the <a href="/windows/desktop/direct3dhlsl/d3dcompile"><strong>D3DCompile</strong></a> API.
</blockquote>
<br/> Compile a shader or an effect from a resource.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11computenormalmap.md"><strong>D3DX11ComputeNormalMap</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library, <strong>ComputeNormalMap</strong>.
</blockquote>
<br/> Converts a height map into a normal map. The (x,y,z) components of each normal are mapped to the (r,g,b) channels of the output texture.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11createasynccompilerprocessor.md"><strong>D3DX11CreateAsyncCompilerProcessor</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create an asynchronous-data processor for a shader.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11createasyncfileloader.md"><strong>D3DX11CreateAsyncFileLoader</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create an asynchronous-file loader.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11createasyncmemoryloader.md"><strong>D3DX11CreateAsyncMemoryLoader</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create an asynchronous-memory loader.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11createasyncresourceloader.md"><strong>D3DX11CreateAsyncResourceLoader</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create an asynchronous-resource loader.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11createasyncshaderpreprocessprocessor.md"><strong>D3DX11CreateAsyncShaderPreprocessProcessor</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a data processor for a shader asynchronously.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11createasynctextureinfoprocessor.md"><strong>D3DX11CreateAsyncTextureInfoProcessor</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a data processor to be used with a <a href="id3dx11threadpump.md"><strong>thread pump</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11createasynctextureprocessor.md"><strong>D3DX11CreateAsyncTextureProcessor</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a data processor to be used with a <a href="id3dx11threadpump.md"><strong>thread pump</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11createasyncshaderresourceviewprocessor.md"><strong>D3DX11CreateAsyncShaderResourceViewProcessor</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a data processor that will load a resource and then create a shader-resource view for it. Data processors are a component of the asynchronous data loading feature in D3DX11 that uses <a href="id3dx11threadpump.md"><strong>thread pumps</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11createshaderresourceviewfromfile.md"><strong>D3DX11CreateShaderResourceViewFromFile</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use these:</p>
<ul>
<li><a href="https://github.com/Microsoft/DirectXTK">DirectXTK</a> library (runtime), <strong>CreateXXXTextureFromFile</strong> (where XXX is DDS or WIC)</li>
<li><a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library (tools), <strong>LoadFromXXXFile</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateShaderResourceView</strong></li>
</ul>
</blockquote>
<br/> Create a shader-resource view from a file.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11createshaderresourceviewfrommemory.md"><strong>D3DX11CreateShaderResourceViewFromMemory</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use these:</p>
<ul>
<li><a href="https://github.com/Microsoft/DirectXTK">DirectXTK</a> library (runtime), <strong>CreateXXXTextureFromMemory</strong> (where XXX is DDS or WIC)</li>
<li><a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateShaderResourceView</strong></li>
</ul>
</blockquote>
<br/> Create a shader-resource view from a file in memory.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11createshaderresourceviewfromresource.md"><strong>D3DX11CreateShaderResourceViewFromResource</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use <a href="/windows/desktop/menurc/resources-functions">resource functions</a>, then these:</p>
<ul>
<li><a href="https://github.com/Microsoft/DirectXTK">DirectXTK</a> library (runtime), <strong>CreateXXXTextureFromMemory</strong> (where XXX is DDS or WIC)</li>
<li><a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateShaderResourceView</strong></li>
</ul>
</blockquote>
<br/> Create a shader-resource view from a resource.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11createtexturefromfile.md"><strong>D3DX11CreateTextureFromFile</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use these:</p>
<ul>
<li><a href="https://github.com/Microsoft/DirectXTK">DirectXTK</a> library (runtime), <strong>CreateXXXTextureFromFile</strong> (where XXX is DDS or WIC)</li>
<li><a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library (tools), <strong>LoadFromXXXFile</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateTexture</strong></li>
</ul>
</blockquote>
<br/> Create a texture resource from a file.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11createtexturefrommemory.md"><strong>D3DX11CreateTextureFromMemory</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use these:</p>
<ul>
<li><a href="https://github.com/Microsoft/DirectXTK">DirectXTK</a> library (runtime), <strong>CreateXXXTextureFromMemory</strong> (where XXX is DDS or WIC)</li>
<li><a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateTexture</strong></li>
</ul>
</blockquote>
<br/> Create a texture resource from a file residing in system memory.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11createtexturefromresource.md"><strong>D3DX11CreateTextureFromResource</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use <a href="/windows/desktop/menurc/resources-functions">resource functions</a>, then these:</p>
<ul>
<li><a href="https://github.com/Microsoft/DirectXTK">DirectXTK</a> library (runtime), <strong>CreateXXXTextureFromMemory</strong> (where XXX is DDS or WIC)</li>
<li><a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateTexture</strong></li>
</ul>
</blockquote>
<br/> Create a texture from another resource.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11createthreadpump.md"><strong>D3DX11CreateThreadPump</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a thread pump.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11filtertexture.md"><strong>D3DX11FilterTexture</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library, <strong>GenerateMipMaps</strong> and <strong>GenerateMipMaps3D</strong>.
</blockquote>
<br/> Generates mipmap chain using a particular texture filter.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11getimageinfofromfile.md"><strong>D3DX11GetImageInfoFromFile</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library, <strong>GetMetadataFromXXXFile</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games).
</blockquote>
<br/> Retrieves information about a given image file.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11getimageinfofrommemory.md"><strong>D3DX11GetImageInfoFromMemory</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library, <strong>GetMetadataFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games).
</blockquote>
<br/> Get information about an image already loaded into memory.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11getimageinfofromresource.md"><strong>D3DX11GetImageInfoFromResource</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use <a href="/windows/desktop/menurc/resources-functions">resource functions</a>, then use <a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games).
</blockquote>
<br/> Retrieves information about a given image in a resource.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11loadtexturefromtexture.md"><strong>D3DX11LoadTextureFromTexture</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library, <strong>Resize</strong>, <strong>Convert</strong>, <strong>Compress</strong>, <strong>Decompress</strong>, and/or <strong>CopyRectangle</strong>.
</blockquote>
<br/> Load a texture from a texture.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11preprocessshaderfromfile.md"><strong>D3DX11PreprocessShaderFromFile</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="/windows/desktop/direct3dhlsl/d3dpreprocess"><strong>D3DPreprocess</strong></a> API.
</blockquote>
<br/> Create a shader from a file without compiling it.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11preprocessshaderfrommemory.md"><strong>D3DX11PreprocessShaderFromMemory</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="/windows/desktop/direct3dhlsl/d3dpreprocess"><strong>D3DPreprocess</strong></a> API.
</blockquote>
<br/> Create a shader from memory without compiling it.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11preprocessshaderfromresource.md"><strong>D3DX11PreprocessShaderFromResource</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="/windows/desktop/direct3dhlsl/d3dpreprocess"><strong>D3DPreprocess</strong></a> API.
</blockquote>
<br/> Create a shader from a resource without compiling it.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11savetexturetofile.md"><strong>D3DX11SaveTextureToFile</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library, <strong>CaptureTexture</strong> then <strong>SaveToXXXFile</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games). For the simplified scenario of creating a screen shot from a render target texture, we recommend that you use the <a href="https://github.com/Microsoft/DirectXTK">DirectXTK</a> library, <strong>SaveDDSTextureToFile</strong> or <strong>SaveWICTextureToFile</strong>.
</blockquote>
<br/> Save a texture to a file.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11savetexturetomemory.md"><strong>D3DX11SaveTextureToMemory</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="https://github.com/Microsoft/DirectXTex">DirectXTex</a> library, <strong>CaptureTexture</strong> then <strong>SaveToXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games).
</blockquote>
<br/> Save a texture to memory.<br/></td>
</tr>
<tr class="even">
<td><a href="d3dx11shprojectcubemap.md"><strong>D3DX11SHProjectCubeMap</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="https://github.com/Microsoft/DirectXMath/tree/master/SHMath">Spherical Harmonics Math</a> library, <strong>SHProjectCubeMap</strong>.
</blockquote>
<br/> Projects a function represented in a cube map into spherical harmonics.<br/></td>
</tr>
<tr class="odd">
<td><a href="d3dx11unsetalldeviceobjects.md"><strong>D3DX11UnsetAllDeviceObjects</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-clearstate"><strong>ID3D11DeviceContext::ClearState</strong></a> method.
</blockquote>
<br/> Removes all resources from the device by setting their pointers to <strong>NULL</strong>. This should be called during shutdown of your application. It helps ensure that when one is releasing all of their resources that none of them are bound to the device.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[D3DX 11 Reference](d3d11-graphics-reference-d3dx11.md)
</dt> </dl>

 

