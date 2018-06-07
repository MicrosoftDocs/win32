---
title: D3DX Functions
description: This section contains information about the D3DX 11 functions.
ms.assetid: 7548c02e-c8c2-4629-95ac-d21ca7a39f0a
keywords:
- functions, DirectX 11 D3DX
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DX Functions

This section contains information about the D3DX 11 functions.

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

## 

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
<td>[<strong>D3DX11CompileFromFile</strong>](d3dx11compilefromfile.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you compile offline by using the Fxc.exe command-line compiler or use one of the HLSL compile APIs, like the [<strong>D3DCompileFromFile</strong>](https://msdn.microsoft.com/library/windows/desktop/hh446872) API.
</blockquote>
<br/> Compile a shader or an effect from a file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11CompileFromMemory</strong>](d3dx11compilefrommemory.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you compile offline by using the Fxc.exe command-line compiler or use one of the HLSL compile APIs, like the [<strong>D3DCompile</strong>](https://msdn.microsoft.com/library/windows/desktop/dd607324) API.
</blockquote>
<br/> Compile a shader or an effect that is loaded in memory.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11CompileFromResource</strong>](d3dx11compilefromresource.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use [resource functions](https://msdn.microsoft.com/library/windows/desktop/ff468902), then compile offline by using the Fxc.exe command-line compiler or use one of the HLSL compile APIs, like the [<strong>D3DCompile</strong>](https://msdn.microsoft.com/library/windows/desktop/dd607324) API.
</blockquote>
<br/> Compile a shader or an effect from a resource.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11ComputeNormalMap</strong>](d3dx11computenormalmap.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, <strong>ComputeNormalMap</strong>.
</blockquote>
<br/> Converts a height map into a normal map. The (x,y,z) components of each normal are mapped to the (r,g,b) channels of the output texture.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11CreateAsyncCompilerProcessor</strong>](d3dx11createasynccompilerprocessor.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create an asynchronous-data processor for a shader.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11CreateAsyncFileLoader</strong>](d3dx11createasyncfileloader.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create an asynchronous-file loader.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11CreateAsyncMemoryLoader</strong>](d3dx11createasyncmemoryloader.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create an asynchronous-memory loader.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11CreateAsyncResourceLoader</strong>](d3dx11createasyncresourceloader.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create an asynchronous-resource loader.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11CreateAsyncShaderPreprocessProcessor</strong>](d3dx11createasyncshaderpreprocessprocessor.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a data processor for a shader asynchronously.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11CreateAsyncTextureInfoProcessor</strong>](d3dx11createasynctextureinfoprocessor.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a data processor to be used with a [<strong>thread pump</strong>](id3dx11threadpump.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11CreateAsyncTextureProcessor</strong>](d3dx11createasynctextureprocessor.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a data processor to be used with a [<strong>thread pump</strong>](id3dx11threadpump.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11CreateAsyncShaderResourceViewProcessor</strong>](d3dx11createasyncshaderresourceviewprocessor.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a data processor that will load a resource and then create a shader-resource view for it. Data processors are a component of the asynchronous data loading feature in D3DX11 that uses [<strong>thread pumps</strong>](id3dx11threadpump.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11CreateShaderResourceViewFromFile</strong>](d3dx11createshaderresourceviewfromfile.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use these:</p>
<ul>
<li>[DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library (runtime), <strong>CreateXXXTextureFromFile</strong> (where XXX is DDS or WIC)</li>
<li>[DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library (tools), <strong>LoadFromXXXFile</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateShaderResourceView</strong></li>
</ul>
</blockquote>
<br/> Create a shader-resource view from a file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11CreateShaderResourceViewFromMemory</strong>](d3dx11createshaderresourceviewfrommemory.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use these:</p>
<ul>
<li>[DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library (runtime), <strong>CreateXXXTextureFromMemory</strong> (where XXX is DDS or WIC)</li>
<li>[DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateShaderResourceView</strong></li>
</ul>
</blockquote>
<br/> Create a shader-resource view from a file in memory.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11CreateShaderResourceViewFromResource</strong>](d3dx11createshaderresourceviewfromresource.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use [resource functions](https://msdn.microsoft.com/library/windows/desktop/ff468902), then these:</p>
<ul>
<li>[DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library (runtime), <strong>CreateXXXTextureFromMemory</strong> (where XXX is DDS or WIC)</li>
<li>[DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateShaderResourceView</strong></li>
</ul>
</blockquote>
<br/> Create a shader-resource view from a resource.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11CreateTextureFromFile</strong>](d3dx11createtexturefromfile.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use these:</p>
<ul>
<li>[DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library (runtime), <strong>CreateXXXTextureFromFile</strong> (where XXX is DDS or WIC)</li>
<li>[DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library (tools), <strong>LoadFromXXXFile</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateTexture</strong></li>
</ul>
</blockquote>
<br/> Create a texture resource from a file.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11CreateTextureFromMemory</strong>](d3dx11createtexturefrommemory.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use these:</p>
<ul>
<li>[DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library (runtime), <strong>CreateXXXTextureFromMemory</strong> (where XXX is DDS or WIC)</li>
<li>[DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateTexture</strong></li>
</ul>
</blockquote>
<br/> Create a texture resource from a file residing in system memory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11CreateTextureFromResource</strong>](d3dx11createtexturefromresource.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
<p>[!Note]<br />
Instead of using this function, we recommend that you use [resource functions](https://msdn.microsoft.com/library/windows/desktop/ff468902), then these:</p>
<ul>
<li>[DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library (runtime), <strong>CreateXXXTextureFromMemory</strong> (where XXX is DDS or WIC)</li>
<li>[DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games) then <strong>CreateTexture</strong></li>
</ul>
</blockquote>
<br/> Create a texture from another resource.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11CreateThreadPump</strong>](d3dx11createthreadpump.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.
</blockquote>
<br/> Create a thread pump.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11FilterTexture</strong>](d3dx11filtertexture.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, <strong>GenerateMipMaps</strong> and <strong>GenerateMipMaps3D</strong>.
</blockquote>
<br/> Generates mipmap chain using a particular texture filter.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11GetImageInfoFromFile</strong>](d3dx11getimageinfofromfile.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, <strong>GetMetadataFromXXXFile</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games).
</blockquote>
<br/> Retrieves information about a given image file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11GetImageInfoFromMemory</strong>](d3dx11getimageinfofrommemory.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, <strong>GetMetadataFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games).
</blockquote>
<br/> Get information about an image already loaded into memory.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11GetImageInfoFromResource</strong>](d3dx11getimageinfofromresource.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use [resource functions](https://msdn.microsoft.com/library/windows/desktop/ff468902), then use [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library (tools), <strong>LoadFromXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games).
</blockquote>
<br/> Retrieves information about a given image in a resource.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11LoadTextureFromTexture</strong>](d3dx11loadtexturefromtexture.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, <strong>Resize</strong>, <strong>Convert</strong>, <strong>Compress</strong>, <strong>Decompress</strong>, and/or <strong>CopyRectangle</strong>.
</blockquote>
<br/> Load a texture from a texture.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11PreprocessShaderFromFile</strong>](d3dx11preprocessshaderfromfile.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [<strong>D3DPreprocess</strong>](https://msdn.microsoft.com/library/windows/desktop/dd607332) API.
</blockquote>
<br/> Create a shader from a file without compiling it.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11PreprocessShaderFromMemory</strong>](d3dx11preprocessshaderfrommemory.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [<strong>D3DPreprocess</strong>](https://msdn.microsoft.com/library/windows/desktop/dd607332) API.
</blockquote>
<br/> Create a shader from memory without compiling it.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11PreprocessShaderFromResource</strong>](d3dx11preprocessshaderfromresource.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [<strong>D3DPreprocess</strong>](https://msdn.microsoft.com/library/windows/desktop/dd607332) API.
</blockquote>
<br/> Create a shader from a resource without compiling it.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11SaveTextureToFile</strong>](d3dx11savetexturetofile.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, <strong>CaptureTexture</strong> then <strong>SaveToXXXFile</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games). For the simplified scenario of creating a screen shot from a render target texture, we recommend that you use the [DirectXTK](http://go.microsoft.com/fwlink/p/?linkid=248929) library, <strong>SaveDDSTextureToFile</strong> or <strong>SaveWICTextureToFile</strong>.
</blockquote>
<br/> Save a texture to a file.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11SaveTextureToMemory</strong>](d3dx11savetexturetomemory.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [DirectXTex](http://go.microsoft.com/fwlink/p/?linkid=248926) library, <strong>CaptureTexture</strong> then <strong>SaveToXXXMemory</strong> (where XXX is WIC, DDS, or TGA; WIC doesn't support DDS and TGA; D3DX 9 supported TGA as a common art source format for games).
</blockquote>
<br/> Save a texture to memory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DX11SHProjectCubeMap</strong>](d3dx11shprojectcubemap.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [Spherical Harmonics Math](http://go.microsoft.com/fwlink/p/?LinkId=262885) library, <strong>SHProjectCubeMap</strong>.
</blockquote>
<br/> Projects a function represented in a cube map into spherical harmonics.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DX11UnsetAllDeviceObjects</strong>](d3dx11unsetalldeviceobjects.md)<br/></td>
<td><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
Instead of using this function, we recommend that you use the [<strong>ID3D11DeviceContext::ClearState</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-clearstate) method.
</blockquote>
<br/> Removes all resources from the device by setting their pointers to <strong>NULL</strong>. This should be called during shutdown of your application. It helps ensure that when one is releasing all of their resources that none of them are bound to the device.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[D3DX 11 Reference](d3d11-graphics-reference-d3dx11.md)
</dt> </dl>

 

 





