---
title: Writing HLSL Shaders in Direct3D 9
description: Writing HLSL Shaders in Direct3D 9
ms.assetid: 7db6b264-c96c-4298-9b8a-d0c488390e4e
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Writing HLSL Shaders in Direct3D 9

-   [Vertex-Shader Basics](#vertex-shader-basics)
-   [Pixel-Shader Basics](#pixel-shader-basics)
    -   [Texture Stage and Sampler States](#texture-stage-and-sampler-states)
    -   [Pixel Shader Inputs](#pixel-shader-inputs)
    -   [Pixel Shader Outputs](#pixel-shader-outputs)
-   [Shader Inputs and Shader Variables](#shader-inputs-and-shader-variables)
    -   [Declaring Shader Variables](#declaring-shader-variables)
    -   [Uniform Shader Inputs](#uniform-shader-inputs)
    -   [Varying Shader Inputs and Semantics](#varying-shader-inputs-and-semantics)
    -   [Samplers and Texture Objects](#samplers-and-texture-objects)
-   [Writing Functions](#writing-functions)
-   [Flow Control](#flow-control)
-   [Related topics](#related-topics)

## Vertex-Shader Basics

When in operation, a programmable vertex shader replaces the vertex processing done by the Microsoft Direct3D graphics pipeline. While using a vertex shader, state information regarding transformation and lighting operations is ignored by the fixed function pipeline. When the vertex shader is disabled and fixed function processing is returned, all current state settings apply.

Tessellation of high-order primitives should be done before the vertex shader executes. Implementations that perform surface tessellation after the shader processing must do so in a way that is not apparent to the application and shader code.

As a minimum, a vertex shader must output vertex position in homogeneous clip space. Optionally, the vertex shader can output texture coordinates, vertex color, vertex lighting, fog factors, and so on.

## Pixel-Shader Basics

Pixel processing is performed by pixel shaders on individual pixels. Pixel shaders work in concert with vertex shaders; the output of a vertex shader provides the inputs for a pixel shader. Other pixel operations (fog blending, stencil operations, and render-target blending) occur after execution of the shader.

### Texture Stage and Sampler States

A pixel shader completely replaces the pixel-blending functionality specified by the multi-texture blender including operations previously defined by the texture stage states. Texture sampling and filtering operations which were controlled by the standard texture stage states for minification, magnification, mip filtering, and the wrap addressing modes, can be initialized in shaders. The application is free to change these states without requiring the regeneration of the currently bound shader. Setting state can be made even easier if your shaders are designed within an effect.

### Pixel Shader Inputs

For pixel shader versions ps\_1\_1 - ps\_2\_0, diffuse and specular colors are saturated (clamped) in the range 0 to 1 before use by the shader.

Color values input to the pixel shader are assumed to be perspective correct, but this is not guaranteed (for all hardware). Colors sampled from texture coordinates are iterated in a perspective correct manner, and are clamped to the 0 to 1 range during iteration.

### Pixel Shader Outputs

For pixel shader versions ps\_1\_1 - ps\_1\_4, the result emitted by the pixel shader is the contents of register r0. Whatever it contains when the shader completes processing is sent to the fog stage and render-target blender.

For pixel shader versions ps\_2\_0 and above, output color is emitted from oC0 - oC4.

## Shader Inputs and Shader Variables

-   [Declaring Shader Variables](#declaring-shader-variables)
-   [Uniform Shader Inputs](#uniform-shader-inputs)
-   [Varying Shader Inputs and Semantics](#varying-shader-inputs-and-semantics)
-   [Samplers and Texture Objects](#samplers-and-texture-objects)

### Declaring Shader Variables

The simplest variable declaration includes a type and a variable name, such as this floating-point declaration:


```
float fVar;
```



You can initialize a variable in the same statement.


```
float fVar = 3.1f;
```



An array of variables can be declared,


```
int iVar[3];
```



or declared and initialized in the same statement.


```
int iVar[3] = {1,2,3};
```



Here are a few declarations that demonstrate many of the characteristics of high-level shader language (HLSL) variables:


```
float4 color;
uniform float4 position : POSITION; 
const float4 lightDirection = {0,0,1};
```



Data declarations can use any valid type including:

-   [Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
-   [Vector Type (DirectX HLSL)](dx-graphics-hlsl-vector.md)
-   [Matrix Type (DirectX HLSL)](dx-graphics-hlsl-matrix.md)
-   [Shader Type (DirectX HLSL)](dx-graphics-hlsl-shader.md)
-   [Sampler Type (DirectX HLSL)](dx-graphics-hlsl-sampler.md)
-   [User-Defined Type (DirectX HLSL)](dx-graphics-hlsl-user-defined.md)

A shader can have top-level variables, arguments, and functions.


```
// top-level variable
float globalShaderVariable; 

// top-level function
void function(
in float4 position: POSITION0 // top-level argument
              )
{
  float localShaderVariable; // local variable
  function2(...)
}

void function2()
{
  ...
}
```



Top-level variables are declared outside of all functions. Top-level arguments are parameters to a top-level function. A top-level function is any function called by the application (as opposed to a function that is called by another function).

### Uniform Shader Inputs

Vertex and pixel shaders accept two kinds of input data: varying and uniform. The varying input is the data that is unique to each execution of the shader. For a vertex shader, the varying data (for example: position, normal, etc.) comes from the vertex streams. The uniform data (for example: material color, world transform, etc.) is constant for multiple executions of a shader. For those familiar with the assembly shader models, uniform data is specified by constant registers and varying data by the v and t registers.

Uniform data can be specified by two methods. The most common method is to declare global variables and use them within a shader. Any use of global variables within a shader will result in adding that variable to the list of uniform variables required by that shader. The second method is to mark an input parameter of the top-level shader function as uniform. This marking specifies that the given variable should be added to the list of uniform variables.

Uniform variables used by a shader are communicated back to the application via the constant table. The constant table is the name for the symbol table that defines how the uniform variables used by a shader fit into the constant registers. The uniform function parameters appear in the constant table prepended with a dollar sign ($), unlike the global variables. The dollar sign is required to avoid name collisions between local uniform inputs and global variables of the same name.

The constant table contains the constant register locations of all uniform variables used by the shader. The table also includes the type information and the default value, if specified.

### Varying Shader Inputs and Semantics

Varying input parameters (of a top-level shader function) must be marked either with a semantic or uniform keyword indicating the value is constant for the execution of the shader. If a top-level shader input is not marked with a semantic or uniform keyword, then the shader will fail to compile.

The input semantic is a name used to link the given input to an output of the previous part of the graphics pipeline. For example, the input semantic POSITION0 is used by the vertex shaders to specify where the position data from the vertex buffer should be linked.

Pixel and vertex shaders have different sets of input semantics due to the different parts of the graphics pipeline that feed into each shader unit. Vertex shader input semantics describe the per-vertex information (for example: position, normal, texture coordinates, color, tangent, binormal, etc.) to be loaded from a vertex buffer into a form that can be consumed by the vertex shader. The input semantics directly map to the vertex declaration usage and the usage index.

Pixel shader input semantics describe the information that is provided per pixel by the rasterization unit. The data is generated by interpolating between outputs of the vertex shader for each vertex of the current primitive. The basic pixel shader input semantics link the output color and texture coordinate information to input parameters.

Input semantics can be assigned to shader input by two methods:

-   Appending a colon and the semantic name to the parameter declaration.
-   Defining an input structure with input semantics assigned to each structure member.

Vertex and pixel shaders provide output data to the subsequent graphics pipeline stage. Output semantics are used to specify how data generated by the shader should be linked to the inputs of the next stage. For example, the output semantics for a vertex shader are used to link the outputs of the interpolators in the rasterizer to generate the input data for the pixel shader. The pixel shader outputs are the values provided to the alpha blending unit for each of the render targets or the depth value written to the depth buffer.

Vertex shader output semantics are used to link the shader both to the pixel shader and to the rasterizer stage. A vertex shader that is consumed by the rasterizer and not exposed to the pixel shader must generate position data as a minimum. Vertex shaders that generate texture coordinate and color data provide that data to a pixel shader after interpolation is done.

Pixel shader output semantics bind the output colors of a pixel shader with the correct render target. The pixel shader output color is linked to the alpha blend stage, which determines how the destination render targets are modified. The pixel shader depth output can be used to change the destination depth values at the current raster location. The depth output and multiple render targets are only supported with some shader models.

The syntax for output semantics is identical to the syntax for specifying input semantics. The semantics can be either specified directly on parameters declared as "out" parameters or assigned during the definition of a structure that either returned as an "out" parameter or the return value of a function.

Semantics identify where data comes from. Semantics are optional identifiers that identify shader inputs and outputs. Semantics appear in one of three places:

-   After a structure member.
-   After an argument in a function's input argument list.
-   After the function's input argument list.

This example uses a structure to provide one or more vertex shader inputs, and another structure to provide one or more vertex shader outputs. Each of the structure members uses a semantic.


```
vector vClr;

struct VS_INPUT
{
    float4 vPosition : POSITION;
    float3 vNormal : NORMAL;
    float4 vBlendWeights : BLENDWEIGHT;
};

struct VS_OUTPUT
{
    float4  vPosition : POSITION;
    float4  vDiffuse : COLOR;

};

float4x4 mWld1;
float4x4 mWld2;
float4x4 mWld3;
float4x4 mWld4;

float Len;
float4 vLight;

float4x4 mTot;

VS_OUTPUT VS_Skinning_Example(const VS_INPUT v, uniform float len=100)
{
    VS_OUTPUT out;

    // Skin position (to world space)
    float3 vPosition = 
        mul(v.vPosition, (float4x3) mWld1) * v.vBlendWeights.x +
        mul(v.vPosition, (float4x3) mWld2) * v.vBlendWeights.y +
        mul(v.vPosition, (float4x3) mWld3) * v.vBlendWeights.z +
        mul(v.vPosition, (float4x3) mWld4) * v.vBlendWeights.w;
    // Skin normal (to world space)
    float3 vNormal =
        mul(v.vNormal, (float3x3) mWld1) * v.vBlendWeights.x + 
        mul(v.vNormal, (float3x3) mWld2) * v.vBlendWeights.y + 
        mul(v.vNormal, (float3x3) mWld3) * v.vBlendWeights.z + 
        mul(v.vNormal, (float3x3) mWld4) * v.vBlendWeights.w;
    
    // Output stuff
    out.vPosition    = mul(float4(vPosition + vNormal * Len, 1), mTot);
    out.vDiffuse  = dot(vLight,vNormal);

    return out;
}
```



The input structure identifies the data from the vertex buffer that will provide the shader inputs. This shader maps the data from the position, normal, and blendweight elements of the vertex buffer into vertex shader registers. The input data type does not have to exactly match the vertex declaration data type. If it doesn't exactly match, the vertex data will automatically be converted into the HLSL's data type when it is written into the shader registers. For instance, if the normal data were defined to be of type UINT by the application, it would be converted into a float3 when read by the shader.

If the data in the vertex stream contains fewer components than the corresponding shader data type, the missing components will be initialized to 0 (except for w, which is initialized to 1).

Input semantics are similar to the values in the [**D3DDECLUSAGE**](/windows/desktop/direct3d9/d3ddeclusage).

The output structure identifies the vertex shader output parameters of position and color. These outputs will be used by the pipeline for triangle rasterization (in primitive processing). The output marked as position data denotes the position of a vertex in homogeneous space. As a minimum, a vertex shader must generate position data. The screen space position is computed after the vertex shader completes by dividing the (x, y, z) coordinate by w. In screen space, -1 and 1 are the minimum and maximum x and y values of the boundaries of the viewport, while z is used for z-buffer testing.

Output semantics are also similar to the values in [**D3DDECLUSAGE**](/windows/desktop/direct3d9/d3ddeclusage). In general, an output structure for a vertex shader can also be used as the input structure for a pixel shader, provided the pixel shader does not read from any variable marked with the position, point size, or fog semantics. These semantics are associated with per-vertex scalar values that are not used by a pixel shader. If these values are needed for the pixel shader, they can be copied into another output variable that uses a pixel shader semantic.

Global variables are assigned to registers automatically by the compiler. Global variables are also called uniform parameters because the contents of the variable is the same for all pixels processed each time the shader is called. The registers are contained in the constant table, which can be read using the [**ID3DXConstantTable**](/windows/desktop/direct3d9/id3dxconstanttable) interface.

Input semantics for pixel shaders map values into specific hardware registers for transport between vertex shaders and pixel shaders. Each register type has specific properties. Because there are currently only two semantics for color and texture coordinates, it is common for most data to be marked as a texture coordinate even when it is not.

Notice that the vertex shader output structure used an input with position data, which is not used by the pixel shader. HLSL allows valid output data of a vertex shader that is not valid input data for a pixel shader, provided that it is not referenced in the pixel shader.

Input arguments can also be arrays. Semantics are automatically incremented by the compiler for each element of the array. For instance, consider the following explicit declaration:


```
struct VS_OUTPUT
{
    float4 Position   : POSITION;
    float3 Diffuse    : COLOR0;
    float3 Specular   : COLOR1;               
    float3 HalfVector : TEXCOORD3;
    float3 Fresnel    : TEXCOORD2;               
    float3 Reflection : TEXCOORD0;               
    float3 NoiseCoord : TEXCOORD1;               
};

float4 Sparkle(VS_OUTPUT In) : COLOR
```



The explicit declaration given above is equivalent to the following declaration that will have semantics automatically incremented by the compiler:


```
float4 Sparkle(float4 Position : POSITION,
                 float3 Col[2] : COLOR0,
                 float3 Tex[4] : TEXCOORD0) : COLOR0
{
   // shader statements
   ...
```



Just like input semantics, output semantics identify data usage for pixel shader output data. Many pixel shaders write to only one output color. Pixel shaders can also write out a depth value into one or more multiple render targets at the same time (up to four). Like vertex shaders, pixel shaders use a structure to return more than one output. This shader writes 0 to the color components, as well as to the depth component.


```
struct PS_OUTPUT
{
    float4 Color[4] : COLOR0;
    float  Depth  : DEPTH;
};

PS_OUTPUT main(void)
{
    PS_OUTPUT out;

   // Shader statements
   ...

  // Write up to four pixel shader output colors
  out.Color[0] =  ...
  out.Color[1] =  ...
  out.Color[2] =  ...
  out.Color[3] =  ...

  // Write pixel depth 
  out.Depth =  ...

    return out;
}
```



Pixel shader output colors must be of type float4. When writing multiple colors, all output colors must be used contiguously. In other words, [COLOR1](dx-graphics-hlsl-semantics.md) cannot be an output unless [COLOR0](dx-graphics-hlsl-semantics.md) has already been written. Pixel shader depth output must be of type float1.

### Samplers and Texture Objects

A sampler contains sampler state. Sampler state specifies the texture to be sampled, and controls the filtering that is done during sampling. Three things are required to sample a texture:

-   A texture
-   A sampler (with sampler state)
-   A sampling instruction

Samplers can be initialized with textures and sampler state as shown here:


```
sampler s = sampler_state 
{ 
  texture = NULL; 
  mipfilter = LINEAR; 
};
```



Here's an example of the code to sample a 2D texture:


```
texture tex0;
sampler2D s_2D;

float2 sample_2D(float2 tex : TEXCOORD0) : COLOR
{
  return tex2D(s_2D, tex);
}
```



The texture is declared with a texture variable tex0.

In this example, a sampler variable named s\_2D is declared. The sampler contains the sampler state inside of curly braces. This includes the texture that will be sampled and, optionally, the filter state (that is, wrap modes, filter modes, etc.). If the sampler state is omitted, a default sampler state is applied specifying linear filtering and a wrap mode for the texture coordinates. The sampler function takes a two-component floating-point texture coordinate, and returns a two-component color. This is represented with the float2 return type and represents data in the red and green components.

Four types of samplers are defined (see [Keywords](dx-graphics-hlsl-appendix.md)) and texture lookups are performed by the intrinsic functions: [**tex1D(s, t) (DirectX HLSL)**](dx-graphics-hlsl-tex1d.md), [**tex2D(s, t) (DirectX HLSL)**](dx-graphics-hlsl-tex2d.md), [**tex3D(s, t) (DirectX HLSL)**](dx-graphics-hlsl-tex3d.md), [**texCUBE(s, t) (DirectX HLSL)**](dx-graphics-hlsl-texcube.md). Here is an example of 3D sampling:


```
texture tex0;
sampler3D s_3D;

float3 sample_3D(float3 tex : TEXCOORD0) : COLOR
{
  return tex3D(s_3D, tex);
}
```



This sampler declaration uses default sampler state for the filter settings and address mode.

Here is the corresponding cube sampling example:


```
texture tex0;
samplerCUBE s_CUBE;

float3 sample_CUBE(float3 tex : TEXCOORD0) : COLOR
{
  return texCUBE(s_CUBE, tex);
}
```



And finally, here is the 1D sampling example:


```
texture tex0;
sampler1D s_1D;

float sample_1D(float tex : TEXCOORD0) : COLOR
{
  return tex1D(s_1D, tex);
}
```



Because the runtime does not support 1D textures, the compiler will use a 2D texture with the knowledge that the y-coordinate is unimportant. Since [**tex1D(s, t) (DirectX HLSL)**](dx-graphics-hlsl-tex1d.md) is implemented as a 2D texture lookup, the compiler is free to choose the y-component in an efficient manner. In some rare scenarios, the compiler cannot choose an efficient y-component, in which case it will issue a warning.


```
texture tex0;
sampler s_1D_float;

float4 main(float texCoords : TEXCOORD) : COLOR
{
    return tex1D(s_1D_float, texCoords);
}
```



This particular example is inefficient because the compiler must move the input coordinate into another register (because a 1D lookup is implemented as a 2D lookup and the texture coordinate is declared as a float1). If the code is rewritten using a float2 input instead of a float1, the compiler can use the input texture coordinate because it knows that y is initialized to something.


```
texture tex0;
sampler s_1D_float2;

float4 main(float2 texCoords : TEXCOORD) : COLOR
{
    return tex1D(s_1D_float2, texCoords);
}
```



All texture lookups can be appended with "bias" or "proj" (that is, [**tex2Dbias (DirectX HLSL)**](dx-graphics-hlsl-tex2dbias.md), [**texCUBEproj (DirectX HLSL)**](dx-graphics-hlsl-texcubeproj.md)). With the "proj" suffix, the texture coordinate is divided by the w-component. With "bias," the mip level is shifted by the w-component. Thus, all texture lookups with a suffix always take a float4 input. [**tex1D(s, t) (DirectX HLSL)**](dx-graphics-hlsl-tex1d.md) and [**tex2D(s, t) (DirectX HLSL)**](dx-graphics-hlsl-tex2d.md) ignore the yz- and z-components respectively.

Samplers may also be used in array, although no back end currently supports dynamic array access of samplers. Therefore, the following is valid because it can be resolved at compile time:


```
tex2D(s[0],tex)
```



However, this example is not valid.


```
tex2D(s[a],tex)
```



Dynamic access of samplers is primarily useful for writing programs with literal loops. The following code illustrates sampler array accessing:


```
sampler sm[4];

float4 main(float4 tex[4] : TEXCOORD) : COLOR
{
    float4 retColor = 1;

    for(int i = 0; i < 4;i++)
    {
        retColor *= tex2D(sm[i],tex[i]);
    }

    return retColor;
}
```



> [!Note]
>
> Using the Microsoft Direct3D debug runtime can help you catch mismatches between the number of components in a texture and a sampler.

 

## Writing Functions

Functions break large tasks into smaller ones. Small tasks are easier to debug and can be reused, once proven. Functions can be used to hide details of other functions, which makes a program composed of functions easier to follow.

HLSL functions are similar to C functions in several ways: They both contain a definition and a function body and they both declare return types and argument lists. Like C functions, HLSL validation does type checking on the arguments, argument types, and the return value during shader compilation.

Unlike C functions, HLSL entry point functions use semantics to bind function arguments to shader inputs and outputs (HLSL functions called internally ignore semantics). This makes it easier to bind buffer data to a shader, and bind shader outputs to shader inputs.

A function contains a declaration and a body, and the declaration must precede the body.


```
float4 VertexShader_Tutorial_1(float4 inPos : POSITION ) : POSITION
{
    return mul(inPos, WorldViewProj );
};
```



The function declaration includes everything in front of the curly braces:


```
float4 VertexShader_Tutorial_1(float4 inPos : POSITION ) : POSITION
```



A function declaration contains:

-   A return type
-   A function name
-   An argument list (optional)
-   An output semantic (optional)
-   An annotation (optional)

The return type can be any of the HLSL basic data types such as a float4:


```
float4 VertexShader_Tutorial_1(float4 inPos : POSITION ) : POSITION
{
   ...
}
```



The return type can be a structure that has already been defined:


```
struct VS_OUTPUT
{
    float4  vPosition        : POSITION;
    float4  vDiffuse         : COLOR;
}; 

VS_OUTPUT VertexShader_Tutorial_1(float4 inPos : POSITION )
{
   ...
}
```



If the function does not return a value, void can be used as the return type.


```
void VertexShader_Tutorial_1(float4 inPos : POSITION )
{
   ...
}
```



The return type always appears first in a function declaration.


```
float4 VertexShader_Tutorial_1(float4 inPos : POSITION ) : POSITION
```



An argument list declares the input arguments to a function. It may also declare values that will be returned. Some arguments are both input and output arguments. Here is an example of a shader that takes four input arguments.


```
float4 Light(float3 LightDir : TEXCOORD1, 
             uniform float4 LightColor,  
             float2 texcrd : TEXCOORD0, 
             uniform sampler samp) : COLOR 
{
    float3 Normal = tex2D(samp,texcrd);

    return dot((Normal*2 - 1), LightDir)*LightColor;
}
```



This function returns a final color, that is a blend of a texture sample and the light color. The function takes four inputs. Two inputs have semantics: LightDir has the [TEXCOORD1](dx-graphics-hlsl-semantics.md) semantic, and texcrd has the [TEXCOORD0](dx-graphics-hlsl-semantics.md) semantic. The semantics mean that the data for these variables will come from the vertex buffer. Even though the LightDir variable has a [TEXCOORD1](dx-graphics-hlsl-semantics.md) semantic, the parameter is probably not a texture coordinate. The TEXCOORDn semantic type is often used to supply a semantic for a type that is not predefined (there is no vertex shader input semantic for a light direction).

The other two inputs LightColor and samp are labeled with the [uniform](dx-graphics-hlsl-appendix.md) keyword. These are uniform constants that will not change between draw calls. The values for these parameters come from shader global variables.

Arguments can be labeled as inputs with the in keyword, and output arguments with the out keyword. Arguments cannot be passed by reference; however, an argument can be both an input and an output if it is declared with the inout keyword. Arguments passed to a function that are marked with the inout keyword are considered copies of the original until the function returns, and they are copied back. Here's an example using inout:


```
void Increment_ByVal(inout float A, inout float B) 
{ 
    A++; B++;
}
```



This function increments the values in A and B and returns them.

The function body is all of the code after the function declaration.


```
float4 VertexShader_Tutorial_1(float4 inPos : POSITION ) : POSITION
{
    return mul(inPos, WorldViewProj );
};
```



The body consists of statements which are surrounded by curly braces. The function body implements all of the functionality using variables, literals, expressions, and statements.

The shader body does two things: it performs a matrix multiply and returns a float4 result. The matrix multiply is accomplished with the [**mul (DirectX HLSL)**](dx-graphics-hlsl-mul.md) function, which performs a 4x4 matrix multiply. **mul (DirectX HLSL)** is called an intrinsic function because it is already built into the HLSL library of functions. Intrinsic functions will be covered in more detail in the next section.

The matrix multiply combines an input vector Pos and a composite matrix WorldViewProj. The result is position data transformed into screen space. This is the minimum vertex shader processing we can do. If we were using the fixed function pipeline instead of a vertex shader, the vertex data could be drawn after doing this transform.

The last statement in a function body is a return statement. Just like C, this statement returns control from the function to the statement that called the function.

Function return types can be any of the simple data types defined in HLSL, including bool, int half, float, and double. Return types can be one of the complex data types such as vectors and matrices. HLSL types that refer to objects cannot be used as return types. This includes pixelshader, vertexshader, texture, and sampler.

Here is an example of a function that uses a structure for a return type.


```
float4x4 WorldViewProj : WORLDVIEWPROJ;

struct VS_OUTPUT
{
    float4 Pos  : POSITION;
};

VS_OUTPUT VS_HLL_Example(float4 inPos : POSITION )
{
    VS_OUTPUT Out;

    Out.Pos = mul(inPos,  WorldViewProj );

    return Out;
};
```



The float4 return type has been replaced with the structure VS\_OUTPUT, which now contains a single float4 member.

A return statement signals the end of a function. This is the simplest return statement. It returns control from the function to the calling program. It returns no value.


```
void main()
{
    return ;
}
```



A return statement can return one or more values. This example returns a literal value:


```
float main( float input : COLOR0) : COLOR0
{
    return 0;
}
```



This example returns the scalar result of an expression:


```
return  light.enabled;
```



This example returns a float4 constructed from a local variable and a literal:


```
return  float4(color.rgb, 1) ;
```



This example returns a float4 that is constructed from the result returned from an intrinsic function, and a few literal values:


```
float4 func(float2 a: POSITION): COLOR
{
    return float4(sin(length(a) * 100.0) * 0.5 + 0.5, sin(a.y * 50.0), 0, 1);
}
```



This example returns a structure that contains one or more members:


```
float4x4 WorldViewProj;

struct VS_OUTPUT
{
    float4 Pos  : POSITION;
};

VS_OUTPUT VertexShader_Tutorial_1(float4 inPos : POSITION )
{
    VS_OUTPUT out;
    out.Pos = mul(inPos, WorldViewProj );
    return out;
};
```



## Flow Control

Most current vertex and pixel shader hardware is designed to run a shader line by line, executing each instruction once. HLSL supports flow control, which includes static branching, predicated instructions, static looping, dynamic branching, and dynamic looping.

Previously, using an if statement resulted in assembly-language shader code that implements both the if side and the else side of the code flow. Here is an example of the in HLSL code that was compiled for vs\_1\_1:


```
if (Value > 0)
    oPos = Value1; 
else
    oPos = Value2; 
```



And here is the resulting assembly code:


```
// Calculate linear interpolation value in r0.w
mov r1.w, c2.x               
slt r0.w, c3.x, r1.w         
// Linear interpolation between value1 and value2
mov r7, -c1                      
add r2, r7, c0                   
mad oPos, r0.w, r2, c1  
```



Some hardware allows for either static or dynamic looping, but most require linear execution. On the models that do not support looping, all loops must be unrolled. An example is the [DepthOfField Sample](https://msdn.microsoft.com/library/Ee416592(v=VS.85).aspx) sample that uses unrolled loops even for ps\_1\_1 shaders.

HLSL now includes support for each of these types of flow control:

-   static branching
-   predicated instructions
-   static looping
-   dynamic branching
-   dynamic looping

Static branching allows blocks of shader code to be switched on or off based on a Boolean shader constant. This is a convenient method for enabling or disabling code paths based on the type of object currently being rendered. Between draw calls, you can decide which features you want to support with the current shader and then set the Boolean flags required to get that behavior. Any statements that are disabled by a Boolean constant are skipped during shader execution.

The most familiar branching support is dynamic branching. With dynamic branching, the comparison condition resides in a variable, which means that the comparison is done for each vertex or each pixel at run time (as opposed to the comparison occurring at compile time, or between two draw calls). The performance hit is the cost of the branch plus the cost of the instructions on the side of the branch taken. Dynamic branching is implemented in shader model 3 or higher. Optimizing shaders that work with these models is similar to optimizing code that runs on a CPU.

## Related topics

<dl> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> </dl>

 

 
