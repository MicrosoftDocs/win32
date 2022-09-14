---
title: Variable Syntax
description: Use the following syntax rules to declare HLSL variables.
ms.assetid: 684c42d1-2dd4-42e1-9cff-580edb5c6bcd
keywords:
- extern, Variable Syntax (DirectX HLSL)
- nointerpolation, Variable Syntax (DirectX HLSL)
- shared, Variable Syntax (DirectX HLSL)
- groupshared, Variable Syntax (DirectX HLSL)
- static, Variable Syntax (DirectX HLSL)
- uniform, Variable Syntax (DirectX HLSL)
- volatile, Variable Syntax (DirectX HLSL)
- precise, Variable Syntax (DirectX HLSL)
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Variable Syntax

Use the following syntax rules to declare HLSL variables.

\[*Storage\_Class*\] \[*Type\_Modifier*\] *Type Name*\[*Index*\]     \[*: Semantic*\]     \[*: Packoffset*\]     \[*: Register*\];    \[*Annotations*\]     \[*= Initial\_Value*\]



 

## Parameters

<dl> <dt>

<span id="Storage_Class_"></span><span id="storage_class_"></span><span id="STORAGE_CLASS_"></span>*Storage\_Class* 
</dt> <dd>

Optional storage-class modifiers that give the compiler hints about variable scope and lifetime; the modifiers can be specified in any order.




| Value | Description | 
|-------|-------------|
| <strong>extern</strong> | Mark a global variable as an external input to the shader; this is the default marking for all global variables. Cannot be combined with <strong>static</strong>. | 
| <strong>nointerpolation</strong> | Do not interpolate the outputs of a vertex shader before passing them to a pixel shader. | 
| <strong>precise</strong> | The <strong>precise</strong> keyword when applied to a variable will restrict any calculations used to produce the value assigned to that variable in the following ways:*	Separate operations are kept separate. For example, where a mul and add operation might have been fused into a mad operation, <strong>precise</strong> forces the operations to remain separate. Instead, you must explicitly use the mad intrinsic function.*	Order of operations are maintained. Where the order of instructions might have been shuffled to improve performance, <strong>precise</strong> ensures that the compiler preserves the order as written.*	IEEE unsafe operations are restricted. Where the compiler might have used fast math operations that don't account for NaN (not a number) and INF (infinite) values, <strong>precise</strong> forces IEEE requirements concerning NaN and INF values to be respected. Without <strong>precise</strong>, these optimizations and mathematical operations are not IEEE safe.*	Qualifying a variable <strong>precise</strong> doesn't make operations that use the variable <strong>precise</strong>. Since <strong>precise</strong> propagates only to operations that contribute to the values that are assigned to the <strong>precise</strong>-qualified variable, correctly making desired calculations <strong>precise</strong> can be tricky, so we recommended that you mark the shader outputs <strong>precise</strong> directly where you declare them, whether that's on a structure field, or on an output parameter, or the return type of the entry function.The ability to control optimizations in this way maintains result invariance for the modified output variable by disabling optimizations that might affect final results due to differences in accumulated precision differences. It is useful when you want shaders for tessellation to maintain water-tight patch seams or match depth values over multiple passes.[Sample code](https://github.com/microsoft/DirectXShaderCompiler/blob/master/tools/clang/test/HLSLFileCheck/hlsl/types/modifiers/precise/precise4.hlsl): ```HLSLmatrix g_mWorldViewProjection;void main(in float3 InPos : Position, out precise float4 OutPos : SV_Position){  // operation is precise because it contributes to the precise parameter OutPos  OutPos = mul( float4( InPos, 1.0 ), g_mWorldViewProjection );}``` | 
| <strong>shared</strong> | Mark a variable for sharing between effects; this is a hint to the compiler. | 
| <strong>groupshared</strong> | Mark a variable for thread-group-shared memory for compute shaders. In D3D10 the maximum total size of all variables with the groupshared storage class is 16kb, in D3D11 the maximum size is 32kb. See examples. | 
| <strong>static</strong> | Mark a local variable so that it is initialized one time and persists between function calls. If the declaration does not include an initializer, the value is set to zero. A global variable marked <strong>static</strong> is not visible to an application. | 
| <strong>uniform</strong> | Mark a variable whose data is constant throughout the execution of a shader (such as a material color in a vertex shader); global variables are considered <strong>uniform</strong> by default. | 
| <strong>volatile</strong> | Mark a variable that changes frequently; this is a hint to the compiler. This storage class modifier only applies to a local variable.<br /><blockquote>[!Note]<br />The HLSL compiler currently ignores this storage class modifier.</blockquote><br /> | 




 

</dd> <dt>

<span id="Type_Modifier"></span><span id="type_modifier"></span><span id="TYPE_MODIFIER"></span>*Type\_Modifier*
</dt> <dd>

Optional variable-type modifier.



| Value             | Description                                                                                                                                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **const**         | Mark a variable that cannot be changed by a shader, therefore, it must be initialized in the variable declaration. Global variables are considered **const** by default (suppress this behavior by supplying the /Gec flag to the compiler). |
| **row\_major**    | Mark a variable that stores four components in a single row so they can be stored in a single constant register.                                                                                                                             |
| **column\_major** | Mark a variable that stores 4 components in a single column to optimize matrix math.                                                                                                                                                         |



 

> [!Note]  
> If you do not specify a type-modifier value, the compiler uses **column\_major** as the default value.

 

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>*Type*
</dt> <dd>

Any HLSL type listed in [Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md).

</dd> <dt>

<span id="Name_Index_"></span><span id="name_index_"></span><span id="NAME_INDEX_"></span>*Name*\[*Index*\]
</dt> <dd>

ASCII string that uniquely identifies a shader variable. To define an optional array, use **index** for the array size, which is a positive integer = 1.

</dd> <dt>

<span id="Semantic"></span><span id="semantic"></span><span id="SEMANTIC"></span>*Semantic*
</dt> <dd>

Optional parameter-usage information, used by the compiler to link shader inputs and outputs. There are several predefined [semantics](dx-graphics-hlsl-semantics.md) for vertex and pixel shaders. The compiler ignores semantics unless they are declared on a global variable, or a parameter passed into a shader.

</dd> <dt>

<span id="Packoffset"></span><span id="packoffset"></span><span id="PACKOFFSET"></span>*Packoffset*
</dt> <dd>

Optional keyword for manually packing shader constants. See [packoffset (DirectX HLSL)](dx-graphics-hlsl-variable-packoffset.md).

</dd> <dt>

<span id="Register"></span><span id="register"></span><span id="REGISTER"></span>*Register*
</dt> <dd>

Optional keyword for manually assigning a shader variable to a particular register. See [register (DirectX HLSL)](dx-graphics-hlsl-variable-register.md).

</dd> <dt>

<span id="Annotation_s_"></span><span id="annotation_s_"></span><span id="ANNOTATION_S_"></span>*Annotation(s)*
</dt> <dd>

Optional metadata, in the form of a string, attached to a global variable. An annotation is used by the effect framework and ignored by HLSL; to see more detailed syntax, see [annotation syntax](/windows/desktop/direct3d10/d3d10-effect-annotation-syntax).

</dd> <dt>

<span id="Initial_Value"></span><span id="initial_value"></span><span id="INITIAL_VALUE"></span>*Initial\_Value*
</dt> <dd>

Optional initial value(s); the number of values should match the number of components in *Type*. Each global variable marked **extern** must be initialized with a literal value; each variable marked **static** must be initialized with a constant.

Global variables that are not marked **static** or **extern** are not compiled into the shader. The compiler does not automatically set default values for global variables and cannot use them in optimizations. To initialize this type of global variable, use reflection to get its value and then copy the value to a constant buffer. For example, you can use the [**ID3D11ShaderReflection::GetVariableByName**](/windows/desktop/api/d3d11shader/nf-d3d11shader-id3d11shaderreflection-getvariablebyname) method to get the variable, use the [**ID3D11ShaderReflectionVariable::GetDesc**](/windows/desktop/api/d3d11shader/nf-d3d11shader-id3d11shaderreflectionvariable-getdesc) method to get the shader-variable description, and get the initial value from the **DefaultValue** member of the [**D3D11\_SHADER\_VARIABLE\_DESC**](/windows/desktop/api/d3d11shader/ns-d3d11shader-d3d11_shader_variable_desc) structure. To copy the value to the constant buffer, you must ensure that the buffer was created with CPU write access ([**D3D11\_CPU\_ACCESS\_WRITE**](/windows/desktop/api/d3d11/ne-d3d11-d3d11_cpu_access_flag)). For more information about how to create a constant buffer, see [How to: Create a Constant Buffer](/windows/desktop/direct3d11/overviews-direct3d-11-resources-buffers-constant-how-to).

You can also use the [effects framework](../direct3d11/d3d11-graphics-programming-guide-effects.md) to automatically process the reflecting and setting the initial value. For example, you can use the [**ID3DX11EffectPass::Apply**](/windows/desktop/direct3d11/id3dx11effectpass-apply) method.

</dd> </dl>

## Examples

Here are several examples of shader-variable declarations.


```
float fVar;
```




```
float4 color;
float fVar = 3.1f;

int iVar[3];

int iVar[3] = {1,2,3};

uniform float4 position : SV_POSITION; 
const float4 lightDirection = {0,0,1};
      
```



### Group Shared

HLSL enables threads of a compute shader to exchange values via shared memory. HLSL provides barrier primitives such as [**GroupMemoryBarrierWithGroupSync**](groupmemorybarrierwithgroupsync.md), and so on to ensure the correct ordering of reads and writes to shared memory in the shader and to avoid data races.

> [!Note]  
> Hardware executes threads in groups (warps or wave-fronts), and barrier synchronization can sometimes be omitted to increase performance when only synchronizing threads that belong to the same group is correct. But we highly discourage this omission for these reasons:
>
> -   This omission results in non-portable code, which might not work on some hardware and doesn't work on software rasterizers that typically execute threads in smaller groups.
> -   The performance improvements that you might achieve with this omission will be minor compared to using all-thread barrier.

 

In Direct3D 10 there is no synchronization of threads when writing to **groupshared**, so this means that each thread is limited to a single location in an array for writing. Use the [SV\_GroupIndex](dx-graphics-hlsl-semantics.md) system value to index into this array when writing to ensure that no two threads can collide. In terms of reading, all threads have access to the entire array for reading.


```
struct GSData
{
    float4 Color;
    float Factor;
}

groupshared GSData data[5*5*1];

[numthreads(5,5,1)]
void main( uint index : SV_GroupIndex )
{
    data[index].Color = (float4)0;
    data[index].Factor = 2.0f;
    GroupMemoryBarrierWithGroupSync();
    ...
}
```



### Packing

Pack subcomponents of vectors and scalars whose size is large enough to prevent crossing register boundarys. For example, these are all valid:


```
cbuffer MyBuffer
{
    float4 Element1 : packoffset(c0);
    float1 Element2 : packoffset(c1);
    float1 Element3 : packoffset(c1.y);
}
        
```



Cannot mix packing types.

Like the register keyword, a packoffset can be target specific. Subcomponent packing is only available with the packoffset keyword, not the register keyword. Inside a cbuffer declaration, the register keyword is ignored for Direct3D 10 targets as it is assumed to be for cross-platform compatibility.

Packed elements may overlap and the compiler will give no error or warning. In this example, Element2 and Element3 will overlap with Element1.x and Element1.y.


```
cbuffer MyBuffer
{
    float4 Element1 : packoffset(c0);
    float1 Element2 : packoffset(c0);
    float1 Element3 : packoffset(c0.y);
}
        
```



A sample that uses packoffset is: [HLSLWithoutFX10 Sample](https://msdn.microsoft.com/library/Ee416414(v=VS.85).aspx).

## Related topics

<dl> <dt>

[Variables (DirectX HLSL)](dx-graphics-hlsl-variables.md)
</dt> </dl>

 

