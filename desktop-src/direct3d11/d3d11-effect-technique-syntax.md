---
title: Effect Technique Syntax (Direct3D 11)
description: An effect technique is declared with the syntax described in this section.
ms.assetid: 54a6ebd1-a6b4-473b-bf53-a3323445de71
keywords:
- technique11, Direct3D 11 Effect
- pass, Direct3D 11 Effect
- CompileShader, Direct3D 11 Effect
- SetStateGroup, Direct3D 11 Effect
- SetBlendState, Direct3D 11 Effect
- SetDepthStencilState, Direct3D 11 Effect
- SetRasterizerState, Direct3D 11 Effect
- SetVertexShader, Direct3D 11 Effect
- SetGeometryShader, Direct3D 11 Effect
- SetPixelShader, Direct3D 11 Effect
ms.topic: reference
ms.date: 05/31/2018
---

# Effect Technique Syntax (Direct3D 11)

An effect technique is declared with the syntax described in this section.

TechniqueVersion *TechniqueName* \[ <*Annotations* > \]

{

<dl> pass *PassName* \[ <*Annotations* > \]  
{  
<dl> \[ *SetStateGroup*; \] \[ *SetStateGroup*; \]  
...  
\[ *SetStateGroup*; \]  
</dl> </dd> }  
</dl>

}

## Parameters



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="TechniqueVersion"></span><span id="techniqueversion"></span><span id="TECHNIQUEVERSION"></span>TechniqueVersion<br/></td>
<td>Either technique10 or technique11. Techniques which use functionality new to Direct3D 11 (5_0 shaders, BindInterfaces, etc) must use technique11.<br/></td>
</tr>
<tr class="even">
<td><span id="TechniqueName"></span><span id="techniquename"></span><span id="TECHNIQUENAME"></span><em>TechniqueName</em><br/></td>
<td>Optional. An ASCII string that uniquely identifies the name of the effect technique.<br/></td>
</tr>
<tr class="odd">
<td><span id="______________Annotations__"></span><span id="______________annotations__"></span><span id="______________ANNOTATIONS__"></span> <<em>Annotations</em> ><br/></td>
<td>[in] Optional. One or more pieces of user-supplied information (metadata) that is ignored by the effect system. For syntax, see <a href="d3d11-effect-annotation-syntax.md">Annotation Syntax (Direct3D 11)</a>.<br/></td>
</tr>
<tr class="even">
<td><span id="pass"></span><span id="PASS"></span>pass<br/></td>
<td>Required keyword.<br/></td>
</tr>
<tr class="odd">
<td><span id="PassName"></span><span id="passname"></span><span id="PASSNAME"></span><em>PassName</em><br/></td>
<td>[in] Optional. An ASCII string that uniquely identifies the name of the pass.<br/></td>
</tr>
<tr class="even">
<td><span id="SetStateGroup"></span><span id="setstategroup"></span><span id="SETSTATEGROUP"></span><em>SetStateGroup</em><br/></td>
<td>[in] Set one or more state groups such as: <br/> 
<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>StateGroup</th>
<th>Syntax</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Blend State</td>
<td><span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetBlendState( arguments ); </code></pre></td>
</tr>
</tbody>
</table>

<p>See [<strong>ID3D11DeviceContext::OMSetBlendState</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-omsetblendstate) for the argument list.</p></td>
</tr>
<tr class="even">
<td>Depth-stencil State</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetDepthStencilState( arguments ); </code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>See <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-omsetdepthstencilstate"><strong>ID3D11DeviceContext::OMSetDepthStencilState</strong></a> for the argument list.</p></td>
</tr>
<tr class="odd">
<td>Rasterizer State</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetRasterizerState( arguments ); </code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>See [<strong>ID3D11DeviceContext::RSSetState</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-rssetstate) for the argument list.</p></td>
</tr>
<tr class="even">
<td>Shader State</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetXXXShader( Shader );</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>SetXXXShader is one of SetVertexShader, SetDomainShader, SetHullShader, SetGeometryShader, SetPixelShader or SetComputeShader (which are similar to the API methods <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-vssetshader"><strong>ID3D11DeviceContext::VSSetShader</strong></a>, <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-dssetshader"><strong>ID3D11DeviceContext::DSSetShader</strong></a>, <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-hssetshader"><strong>ID3D11DeviceContext::HSSetShader</strong></a>, <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-gssetshader"><strong>ID3D11DeviceContext::GSSetShader</strong></a>, <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-pssetshader"><strong>ID3D11DeviceContext::PSSetShader</strong></a> and <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-cssetshader"><strong>ID3D11DeviceContext::CSSetShader</strong></a>).</p>
<p>Shader is a shader variable, which can be obtained in many ways:</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetXXXShader( CompileShader( shader_profile, ShaderFunction( args ) ) );
SetXXXShader( CompileShader( NULL ) );
SetXXXShader( NULL );
SetXXXShader( myShaderVar );
SetXXXShader( myShaderArray[2] );
SetXXXShader( myShaderArray[uIndex] );
SetGeometryShader( ConstructGSWithSO( Shader, strStream0 ) );
SetGeometryShader( ConstructGSWithSO( Shader, strStream0, strStream1, strStream2, strStream3, RastStream ) );</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>Render Target State</td>
<td>One of:
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetRenderTargets( RTV0, DSV );
SetRenderTargets( RTV0, RTV1, DSV );
...
SetRenderTargets( RTV0, RTV1, RTV2, RTV3, RTV4, RTV5, RTV6, RTV7, DSV );</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>Similar to <a href="/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-omsetrendertargets"><strong>ID3D11DeviceContext::OMSetRenderTargets</strong></a>.</p></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

## Examples

This example sets blending state.


```
BlendState NoBlend
{ 
    BlendEnable[0] = False;
};

...

technique10
{
    pass p2 
    {
        ...
        SetBlendState( NoBlend, float4( 0.0f, 0.0f, 0.0f, 0.0f ), 0xFFFFFFFF );
    }
}
```



This example sets up the rasterizer state to render an object in wireframe.


```
RasterizerState rsWireframe { FillMode = WireFrame; };

...

technique10
{
    pass p1 
    {
        ....
        SetRasterizerState( rsWireframe );
    }
}
```



This example sets shader state.


```
technique10 RenderSceneWithTexture1Light
{
    pass P0
    {
        SetVertexShader( CompileShader( vs_4_0, RenderSceneVS( 1, true, true ) ) );
        SetGeometryShader( NULL );
        SetPixelShader( CompileShader( ps_4_0, RenderScenePS( true ) ) );
    }
}
```



## Related topics

<dl> <dt>

[Effect Format](d3d11-effect-format.md)
</dt> <dt>

[Effect Group Syntax (Direct3D 11)](d3d11-effect-group-syntax.md)
</dt> <dt>

[Effect State Groups](d3d11-effect-states.md)
</dt> </dl>

 

 





