---
Description: 'An effect technique is declared with the following syntax.'
ms.assetid: '84f9b74d-8397-4cd5-91a0-7f910ba7b19e'
title: 'Effect Technique Syntax (Direct3D 10)'
---

# Effect Technique Syntax (Direct3D 10)

An effect technique is declared with the following syntax.

technique10 *TechniqueName* \[ &lt;*Annotations* &gt; \]

{

<dl> pass *PassName* \[ &lt;*Annotations* &gt; \]  
{  
<dl> \[ *SetStateGroup*; \] \[ *SetStateGroup*; \]  
...  
\[ *SetStateGroup*; \]  
</dl> </dd> }  
</dl>

}

## Parameters

<dl> <dt>

<span id="technique10"></span><span id="TECHNIQUE10"></span>technique10
</dt> <dd>

Required keyword.

</dd> <dt>

<span id="TechniqueName"></span><span id="techniquename"></span><span id="TECHNIQUENAME"></span>*TechniqueName*
</dt> <dd>

Optional. An ASCII string that uniquely identifies the name of the effect technique.

</dd> <dt>

<span id="Annotations"></span><span id="annotations"></span><span id="ANNOTATIONS"></span>*Annotations*
</dt> <dd>

\[in\] Optional. One or more pieces of user-supplied information (metadata) that is ignored by the effect system. For syntax, see [Annotation Syntax (Direct3D 10)](d3d10-effect-annotation-syntax.md).

</dd> <dt>

<span id="pass"></span><span id="PASS"></span>pass
</dt> <dd>

Required keyword.

</dd> <dt>

<span id="PassName"></span><span id="passname"></span><span id="PASSNAME"></span>*PassName*
</dt> <dd>

\[in\] Optional. An ASCII string that uniquely identifies the name of the pass.

</dd> <dt>

<span id="SetStateGroup"></span><span id="setstategroup"></span><span id="SETSTATEGROUP"></span>*SetStateGroup*
</dt> <dd>

\[in\] Set one or more state groups such as:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
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
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetBlendState( arguments ); </code></pre></td>
</tr>
</tbody>
</table>

<p>See [<strong>OMSetBlendState</strong>](id3d10device-omsetblendstate.md) for the argument list.</p></td>
</tr>
<tr class="even">
<td>Depth-stencil State</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetDepthStencilState( arguments ); </code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>See [<strong>OMSetDepthStencilState</strong>](id3d10device-omsetdepthstencilstate.md) for the argument list.</p></td>
</tr>
<tr class="odd">
<td>Rasterizer State</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetRasterizerState( arguments ); </code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>See [<strong>RSSetState</strong>](id3d10device-rssetstate.md) for the argument list.</p></td>
</tr>
<tr class="even">
<td>Shader State</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetXXXShader( CompileShader( shader_profile, ShaderFunction( args ) ) );</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>or</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetXXXShader( CompileShader( NULL ) );</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>or</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SetXXXShader( NULL );</code></pre></td>
</tr>
</tbody>
</table>

</div>
<p>SetXXXShader is one of <strong>SetVertexShader</strong>, <strong>SetGeometryShader</strong>, or <strong>SetPixelShader</strong> (which are similar to the API methods [<strong>VSSetShader</strong>](id3d10device-vssetshader.md), [<strong>GSSetShader</strong>](id3d10device-gssetshader.md), and [<strong>PSSetShader</strong>](id3d10device-pssetshader.md)).</p></td>
</tr>
</tbody>
</table>



 

</dd> </dl>

Effect state groups are listed in [effect state](d3d10-effect-states.md).

## Examples

This example (from [CubeMapGS sample](7bb33415-9ed7-1a13-637b-df3669cae2fa)) sets blending state.


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



This example sets shader state (from [BasicHLSL10 sample](e749975d-211e-f7ed-5dd1-b9c29681c71b)); which uses a vertex and pixel shader.


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

[Effect Format](d3d10-effect-format.md)
</dt> </dl>

 

 



