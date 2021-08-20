---
title: Sampler Type
description: Use the following syntax to declare sampler state as well as sampler-comparison state.
ms.assetid: 6534d343-d724-46e5-b300-2a29124a1a28
keywords:
- Sampler Type HLSL
topic_type:
- apiref
api_name:
- Sampler Type
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Sampler Type

Use the following syntax to declare sampler state as well as sampler-comparison state.



<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>Differences between Direct3D 9 and Direct3D 10 and later:<br/> Here is the syntax for a sampler in Direct3D 9.<br/> 
<table>
<tbody>
<tr class="odd">
<td>sampler <em>Name</em> = <em>SamplerType</em>{   Texture = <<em>texture_variable</em>>;   [<em>state_name = state_value;</em>]   ... };</td>
</tr>
</tbody>
</table>

<p> </p>
<p>The syntax for a sampler in Direct3D 10 and later is changed slightly to support texture objects and sampler arrays.</p>

<table>
<tbody>
<tr class="odd">
<td><em>SamplerType Name[Index]</em>{   [<em>state_name = state_value;</em>]   ... };</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

## Parameters

<dl> <dt>

<span id="sampler"></span><span id="SAMPLER"></span>sampler
</dt> <dd>

Direct3D 9 only. Required keyword.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>*Name*
</dt> <dd>

ASCII string that uniquely identifies the sampler variable name.

</dd> <dt>

<span id="_Index_"></span><span id="_index_"></span><span id="_INDEX_"></span>*\[Index\]*
</dt> <dd>

Direct3D 10 and later only. Optional array size; a positive integer greater than or equal to 1.

</dd> <dt>

<span id="SamplerType"></span><span id="samplertype"></span><span id="SAMPLERTYPE"></span>*SamplerType*
</dt> <dd>

\[in\] The sampler type, which is one of the following: *sampler*, *sampler1D*, *sampler2D*, *sampler3D*, *samplerCUBE*, *sampler\_state*, *SamplerState*.

Differences between Direct3D 9 and Direct3D 10 and later:

- Direct3D 10 and later supports one additional sampler type: *SamplerComparisonState*.



 

</dd> <dt>

<span id="Texture____texture_variable__"></span><span id="texture____texture_variable__"></span><span id="TEXTURE____TEXTURE_VARIABLE__"></span>*Texture* = <*texture\_variable*>;
</dt> <dd>

Direct3D 9 only. A texture variable. The *Texture* keyword is required on the left-hand side; the variable name belongs on the right-hand side of the expression within the angle brackets.

</dd> <dt>

<span id="state_name___state_value"></span><span id="STATE_NAME___STATE_VALUE"></span>*state\_name = state\_value*
</dt> <dd>

\[in\] Optional state assignment(s). The left hand side of an assignment is a state name, the right hand side is the state value. All state assignments must appear within a statement block (in curly brackets). Each statement is separated with a semicolon. The following table lists the possible state names.


```
// sampler state
AddressU
AddressV
AddressW
BorderColor
Filter
MaxAnisotropy
MaxLOD
MinLOD
MipLODBias

// sampler-comparison state
ComparisonFunc
```



The right side of each expression is the value assigned to each state. See the [**D3D11\_SAMPLER\_DESC**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_sampler_desc) structure for the possible state values for Direct3D 11. There is a 1 to 1 relationship between the state names and the members of the structure. See the following example.

</dd> </dl>

## Remarks

When you implement an effect, sampler state is one of several types of state that you might need to set up in the pipeline for rendering. For a list of all the possible states that you can set in an effect, see:

-   Direct3D 10 uses [state groups](/windows/desktop/direct3d10/d3d10-effect-states).
-   Direct3D 9 uses individual [states](/windows/desktop/direct3d9/effect-states).

## Example



<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>Differences between Direct3D 9 and Direct3D 10:<br/> Here is a partial example of a Direct3D 9 sampler from <a href="https://msdn.microsoft.com/library/Ee416223(v=VS.85).aspx">BasicHLSL Sample</a>.<br/> <span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>sampler MeshTextureSampler = 
sampler_state
{
    Texture = <g_MeshTexture>;
    MipFilter = LINEAR;
    MinFilter = LINEAR;
    MagFilter = LINEAR;
};</code></pre></td>
</tr>
</tbody>
</table>

<p>Here is a partial example of a Direct3D 10 sampler from <a href="https://msdn.microsoft.com/library/Ee416395(v=VS.85).aspx">BasicHLSL10 Sample</a>.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SamplerState MeshTextureSampler
{
    Filter = MIN_MAG_MIP_LINEAR;
    AddressU = Wrap;
    AddressV = Wrap;
};</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>



 

Here is a partial example of declaring sampler-comparison state, and calling a comparison sampler in Direct3D 10.


```
SamplerComparisonState ShadowSampler
{
   // sampler state
   Filter = COMPARISON_MIN_MAG_LINEAR_MIP_POINT;
   AddressU = MIRROR;
   AddressV = MIRROR;

   // sampler comparison state
   ComparisonFunc = LESS;
};
        
float3 vModProjUV;
  ...
float fShadow = g_ShadowMap.SampleCmpLevelZero( ShadowSampler, vModProjUV.xy, vModProjUV.z);
```



## See also

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

