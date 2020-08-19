---
title: Work with shaders and shader resources
description: It's time to learn how to work with shaders and shader resources in developing your Microsoft DirectX game for Windows 8.
ms.assetid: 25a11983-e3f6-4bd3-86f1-d660edc4cd4b
ms.topic: article
ms.date: 05/31/2018
---

# Work with shaders and shader resources

It's time to learn how to work with shaders and shader resources in developing your Microsoft DirectX game for Windows 8. We've seen how to set up the graphics device and resources, and perhaps you've even started modifying its pipeline. So now let's look at pixel and vertex shaders.

If you aren't familiar with shader languages, a quick discussion is in order. Shaders are small, low-level programs that are compiled and run at specific stages in the graphics pipeline. Their specialty is very fast floating-point mathematical operations. The most common shader programs are:

-   **Vertex shader**—Executed for each vertex in a scene. This shader operates on vertex buffer elements provided to it by the calling app, and minimally results in a 4-component position vector that will be rasterized into a pixel position.
-   **Pixel shader**—Executed for each pixel in a render target. This shader receives rasterized coordinates from previous shader stages (in the simplest pipelines, this would be the vertex shader) and returns a color (or other 4-component value) for that pixel position, which is then written into a render target.

This example includes very basic vertex and pixel shaders that only draw geometry, and more complex shaders that add basic lighting calculations.

Shader programs are written in Microsoft High Level Shader Language (HLSL). HLSL syntax looks a lot like C, but without the pointers. Shader programs must be very compact and efficient. If your shader compiles to too many instructions, it cannot be run and an error is returned. (Note that the exact number of instructions allowed is part of the [Direct3D feature level](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro).)

In Direct3D, shaders are not compiled at run time; they are compiled when the rest of the program is compiled. When you compile your app with Microsoft Visual Studio 2013, the HLSL files are compiled to CSO (.cso) files that your app must load and place in GPU memory prior to drawing. Make sure you include these CSO files with your app when you package it; they are assets just like meshes and textures.

## Understand HLSL semantics

It's important to take a moment to discuss HLSL semantics before we continue, because they are often a point of confusion for new Direct3D developers. HLSL semantics are strings that identify a value passed between the app and a shader program. Although they can be any of a variety of possible strings, the best practice is to use a string like `POSITION` or `COLOR` that indicates the usage. You assign these semantics when you are constructing a constant buffer or input layout. You can also append a number between 0 and 7 to the semantic so that you use separate registers for similar values. For example: COLOR0, COLOR1, COLOR2...

Semantics that are prefixed with "SV\_" are *system value* semantics that are written to by your shader program; your game itself (running on the CPU) cannot modify them. Typically, these semantics contain values that are inputs or outputs from another shader stage in the graphics pipeline, or that are generated entirely by the GPU.

Additionally, `SV_` semantics have different behaviors when they are used to specify input to or output from a shader stage. For example, `SV_POSITION` (output) contains the vertex data transformed during the vertex shader stage, and `SV_POSITION` (*input*) contains the pixel position values that were interpolated by the GPU during the rasterization stage.

Here are a few common HLSL semantics:

-   `POSITION`(*n*) for vertex buffer data. `SV_POSITION` provides a pixel position to the pixel shader and cannot be written by your game.
-   `NORMAL`(*n*) for normal data provided by the vertex buffer.
-   `TEXCOORD`(*n*) for texture UV coordinate data supplied to a shader.
-   `COLOR`(n) for RGBA color data supplied to a shader. Note that it is treated identically to coordinate data, including interpolating the value during rasterization; the semantic simply helps you identify that it is color data.
-   `SV_Target`\[n\] for writing from a pixel shader to a target texture or other pixel buffer.

We'll see some examples of HLSL semantics as we review the example.

## Read from the constant buffers

Any shader can read from a constant buffer if that buffer is attached to its stage as a resource. In this example, only the vertex shader is assigned a constant buffer.

The constant buffer is declared in two places: in the C++ code, and in the corresponding HLSL files that will access it.

Here's how the constant buffer struct is declared in the C++ code.


```C++
typedef struct _constantBufferStruct {
    DirectX::XMFLOAT4X4 world;
    DirectX::XMFLOAT4X4 view;
    DirectX::XMFLOAT4X4 projection;
} ConstantBufferStruct;
```



When declaring the structure for the constant buffer in your C++ code, ensure that all of the data is correctly aligned along 16-byte boundaries. The easiest way to do this is to use [DirectXMath](/windows/desktop/dxmath/directxmath-portal) types, like **XMFLOAT4** or **XMFLOAT4X4**, as seen in the example code. You can also guard against misaligned buffers by declaring a static assert:


```C++
// Assert that the constant buffer remains 16-byte aligned.
static_assert((sizeof(ConstantBufferStruct) % 16) == 0, "Constant Buffer size must be 16-byte aligned");
```



This line of code will cause an error at compile time if **ConstantBufferStruct** is not 16-byte aligned. For more information about constant buffer alignment and packing, see [Packing Rules for Constant Variables](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-packing-rules).

Now, here's how the constant buffer is declared in the vertex shader HLSL.


```C++
cbuffer ModelViewProjectionConstantBuffer : register(b0)
{
    matrix mWorld;      // world matrix for object
    matrix View;        // view matrix
    matrix Projection;  // projection matrix
};
```



All buffers—constant, texture, sampler, or other—must have a register defined so the GPU can access them. Each shader stage allows up to 15 constant buffers, and each buffer can hold up to 4,096 constant variables. The register-usage declaration syntax is as follows:

-   **b***\#*: A register for a constant buffer (**cbuffer**).
-   **t***\#*: A register for a texture buffer (**tbuffer**).
-   **s***\#*: A register for a sampler. (A sampler defines the lookup behavior for texels in the texture resource.)

For example, the HLSL for a pixel shader might take a texture and a sampler as input with a declaration like this.

``` syntax
Texture2D simpleTexture : register(t0);
SamplerState simpleSampler : register(s0);
```

It's up to you to assign constant buffers to registers—when you set up the pipeline, you attach a constant buffer to the same slot you assigned it to in the HLSL file. For example, in the previous topic the call to [**VSSetConstantBuffers**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-vssetconstantbuffers) indicates '0' for the first parameter. That tells Direct3D to attach the constant buffer resource to register 0, which matches the buffer's assignment to **register(b0)** in the HLSL file.

## Read from the vertex buffers

The vertex buffer supplies the triangle data for the scene objects to the vertex shader(s). As with the constant buffer, the vertex buffer struct is declared in the C++ code, using similar packing rules.


```C++
typedef struct _vertexPositionColor
{
    DirectX::XMFLOAT3 pos;
    DirectX::XMFLOAT3 color;
} VertexPositionColor;
```



There is no standard format for vertex data in Direct3D 11. Instead, we define our own vertex data layout using a descriptor; the data fields are defined using an array of [**D3D11\_INPUT\_ELEMENT\_DESC**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_input_element_desc) structures. Here, we show a simple input layout that describes the same vertex format as the preceding struct:


```C++
D3D11_INPUT_ELEMENT_DESC iaDesc [] =
{
    { "POSITION", 0, DXGI_FORMAT_R32G32B32_FLOAT,
    0, 0, D3D11_INPUT_PER_VERTEX_DATA, 0 },

    { "COLOR", 0, DXGI_FORMAT_R32G32B32_FLOAT,
    0, 12, D3D11_INPUT_PER_VERTEX_DATA, 0 },
};

hr = device->CreateInputLayout(
    iaDesc,
    ARRAYSIZE(iaDesc),
    bytes,
    bytesRead,
    &m_pInputLayout
    );
```



If you add data to the vertex format when modifying the example code, be sure to update the input layout as well, or the shader will not be able to interpret it. You might modify the vertex layout like this:


```C++
typedef struct _vertexPositionColorTangent
{
    DirectX::XMFLOAT3 pos;
    DirectX::XMFLOAT3 normal;
    DirectX::XMFLOAT3 tangent;
} VertexPositionColorTangent;
```



In that case, you'd modify the input-layout definition as follows.


```C++
D3D11_INPUT_ELEMENT_DESC iaDescExtended[] =
{
    { "POSITION", 0, DXGI_FORMAT_R32G32B32_FLOAT,
    0, 0, D3D11_INPUT_PER_VERTEX_DATA, 0 },

    { "NORMAL", 0, DXGI_FORMAT_R32G32B32_FLOAT,
    0, 12, D3D11_INPUT_PER_VERTEX_DATA, 0 },

    { "TANGENT", 0, DXGI_FORMAT_R32G32B32_FLOAT,
    0, 12, D3D11_INPUT_PER_VERTEX_DATA, 0 },
};

hr = device->CreateInputLayout(
    iaDesc,
    ARRAYSIZE(iaDesc),
    bytes,
    bytesRead,
    &m_pInputLayoutExtended
    );
```



Each of the input-layout element definitions is prefixed with a string, like "POSITION" or "NORMAL"—that is the semantic we discussed earlier in this topic. It's like a handle that helps the GPU identify that element when processing the vertex. Choose common, meaningful names for your vertex elements.

Just as with the constant buffer, the vertex shader has a corresponding buffer definition for incoming vertex elements. (That's why we provided a reference to the vertex shader resource when creating the input layout - Direct3D validates the per-vertex data layout with the shader's input struct.) Note how the semantics match between the input layout definition and this HLSL buffer declaration. However, `COLOR` has a "0" appended to it. It isn't necessary to add the 0 if you have only one `COLOR` element declared in the layout, but it's a good practice to append it in case you you choose to add more color elements in the future.


```C++
struct VS_INPUT
{
    float3 vPos   : POSITION;
    float3 vColor : COLOR0;
};
```



## Pass data between shaders

Shaders take input types and return output types from their main functions upon execution. For the vertex shader defined in the previous section, the input type was the VS\_INPUT structure, and we defined a matching input layout and C++ struct. An array of this struct is used to create a vertex buffer in the **CreateCube** method.

The vertex shader returns a PS\_INPUT structure, which must minimally contain the 4-component (float4) final vertex position. This position value must have the system value semantic, `SV_POSITION`, declared for it so the GPU has the data it needs to perform the next drawing step. Notice that there is not a 1:1 correspondence between vertex shader output and pixel shader input; the vertex shader returns one structure for each vertex it is given, but the pixel shader runs once for each pixel. That's because the per-vertex data first passes through the rasterization stage. This stage decides which pixels "cover" the geometry you're drawing, computes interpolated per-vertex data for each pixel, and then calls the pixel shader once for each of those pixels. Interpolation is the default behavior when rasterizing output values, and is essential in particular for the correct processing of output vector data (light vectors, per-vertex normals and tangents, and others).


```C++
struct PS_INPUT
{
    float4 Position : SV_POSITION;  // interpolated vertex position (system value)
    float4 Color    : COLOR0;       // interpolated diffuse color
};
```



## Review the vertex shader

The example vertex shader is very simple: take in a vertex (position and color), transform the position from model coordinates into perspective projected coordinates, and return it (along with the color) to the rasterizer. Notice that the color value is interpolated right along with the position data, providing a different value for each pixel even though the vertex shader didn't perform any calculations on the color value.


```C++
VS_OUTPUT main(VS_INPUT input) // main is the default function name
{
    VS_OUTPUT Output;

    float4 pos = float4(input.vPos, 1.0f);

    // Transform the position from object space to homogeneous projection space
    pos = mul(pos, mWorld);
    pos = mul(pos, View);
    pos = mul(pos, Projection);
    Output.Position = pos;

    // Just pass through the color data
    Output.Color = float4(input.vColor, 1.0f);

    return Output;
}
```



A more complex vertex shader, such as one that sets up an object's vertices for Phong shading, might look more like this. In this case, we're taking advantage of the fact that the vectors and normals are interpolated to approximate a smooth-looking surface.

``` syntax
// A constant buffer that stores the three basic column-major matrices for composing geometry.
cbuffer ModelViewProjectionConstantBuffer : register(b0)
{
    matrix model;
    matrix view;
    matrix projection;
};

cbuffer LightConstantBuffer : register(b1)
{
    float4 lightPos;
};

struct VertexShaderInput
{
    float3 pos : POSITION;
    float3 normal : NORMAL;
};

// Per-pixel color data passed through the pixel shader.

struct PixelShaderInput
{
    float4 position : SV_POSITION; 
    float3 outVec : POSITION0;
    float3 outNormal : NORMAL0;
    float3 outLightVec : POSITION1;
};

PixelShaderInput main(VertexShaderInput input)
{
    // Inefficient -- doing this only for instruction. Normally, you would
 // premultiply them on the CPU and place them in the cbuffer.
    matrix mvMatrix = mul(model, view);
    matrix mvpMatrix = mul(mvMatrix, projection);

    PixelShaderInput output;

    float4 pos = float4(input.pos, 1.0f);
    float4 normal = float4(input.normal, 1.0f);
    float4 light = float4(lightPos.xyz, 1.0f);

    // 
    float4 eye = float4(0.0f, 0.0f, -2.0f, 1.0f);

    // Transform the vertex position into projected space.
    output.gl_Position = mul(pos, mvpMatrix);
    output.outNormal = mul(normal, mvMatrix).xyz;
    output.outVec = -(eye - mul(pos, mvMatrix)).xyz;
    output.outLightVec = mul(light, mvMatrix).xyz;

    return output;
}
```

## Review the pixel shader

This pixel shader in this example is quite possibly the absolute minimum amount of code you can have in a pixel shader. It takes the interpolated pixel color data generated during rasterization and returns it as output, where it will be written to a render target. How boring!


```C++
PS_OUTPUT main(PS_INPUT In)
{
    PS_OUTPUT Output;

    Output.RGBColor = In.Color;

    return Output;
}
```



The important part is the `SV_TARGET` system-value semantic on the return value. It indicates that the output is to be written to the primary render target, which is the texture buffer supplied to the swap chain for display. This is required for pixel shaders - without the color data from the pixel shader, Direct3D wouldn't have anything to display!

An example of a more complex pixel shader to perform Phong shading might look like this. Since the vectors and normals were interpolated, we don't have to compute them on a per-pixel basis. However, we do have to re-normalize them because of how interpolation works; conceptually, we need to gradually "spin" the vector from direction at vertex A to direction at vertex B, maintaining its length—wheras interpolation instead cuts across a straight line between the two vector endpoints.

``` syntax
cbuffer MaterialConstantBuffer : register(b2)
{
    float4 lightColor;
    float4 Ka;
    float4 Kd;
    float4 Ks;
    float4 shininess;
};

struct PixelShaderInput
{
    float4 position : SV_POSITION;
    float3 outVec : POSITION0;
    float3 normal : NORMAL0;
    float3 light : POSITION1;
};

float4 main(PixelShaderInput input) : SV_TARGET
{
    float3 L = normalize(input.light);
    float3 V = normalize(input.outVec);
    float3 R = normalize(reflect(L, input.normal));

    float4 diffuse = Ka + (lightColor * Kd * max(dot(input.normal, L), 0.0f));
    diffuse = saturate(diffuse);

    float4 specular = Ks * pow(max(dot(R, V), 0.0f), shininess.x - 50.0f);
    specular = saturate(specular);

    float4 finalColor = diffuse + specular;

    return finalColor;
}
```

In another example, the pixel shader takes its own constant buffers that contain light and material information. The input layout in the vertex shader would be expanded to include normal data, and the output from that vertex shader is expected to include transformed vectors for the vertex, the light, and the vertex normal in the view coordinate system.

If you have texture buffers and samplers with assigned registers (**t** and **s**, respectively), you can access them in the pixel shader also.

``` syntax
Texture2D simpleTexture : register(t0);
SamplerState simpleSampler : register(s0);

struct PixelShaderInput
{
    float4 pos : SV_POSITION;
    float3 norm : NORMAL;
    float2 tex : TEXCOORD0;
};

float4 SimplePixelShader(PixelShaderInput input) : SV_TARGET
{
    float3 lightDirection = normalize(float3(1, -1, 0));
    float4 texelColor = simpleTexture.Sample(simpleSampler, input.tex);
    float lightMagnitude = 0.8f * saturate(dot(input.norm, -lightDirection)) + 0.2f;
    return texelColor * lightMagnitude;
}
```

Shaders are very powerful tools that can be used to generate procedural resources like shadow maps or noise textures. In fact, advanced techniques require that you think of textures more abstractly, not as visual elements but as buffers. They hold data like height information, or other data that can be sampled in the final pixel shader pass or in that particular frame as part of a multi-stage effects pass. Multi-sampling is a powerful tool and the backbone of many modern visual effects.

## Next steps

Hopefully, you're comfortable with DirectX 11at this point and are ready to start working on your project. Here are some links to help answer other questions you may have about development with DirectX and C++:

-   [Developing games](/previous-versions/windows/apps/hh452744(v=win.10))
-   [Use Visual Studio tools for DirectX game programming](/previous-versions/windows/apps/dn166877(v=win.10))
-   [DirectX game development and sample walkthroughs](/previous-versions/windows/apps/hh465149(v=win.10))
-   [Additional game programming resources](/previous-versions/windows/apps/dn194515(v=win.10))

## Related topics

<dl> <dt>

[Work with DirectX device resources](work-with-dxgi.md)
</dt> <dt>

[Understand the Direct3D 11 rendering pipeline](understand-the-directx-11-2-graphics-pipeline.md)
</dt> </dl>

 

 