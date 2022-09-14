---
title: How To Create a Compute Shader
description: This topic shows how to create a compute shader.
ms.assetid: 6114dd90-626b-4c9e-9da5-7d2d33153e79
ms.topic: article
ms.date: 05/31/2018
---

# How To: Create a Compute Shader

A compute shader is an Microsoft High Level Shader Language (HLSL) programmable shader that uses generalized input and output memory access to support virtually any type of calculation. This topic shows how to create a compute shader. The compute shader technology is also known as the DirectCompute technology.

**To create a compute shader:**

1.  Compile the HLSL shader code by calling [**D3DCompileFromFile**](/windows/desktop/direct3dhlsl/d3dcompilefromfile).
    ```
        UINT flags = D3DCOMPILE_ENABLE_STRICTNESS;
    #if defined( DEBUG ) || defined( _DEBUG )
        flags |= D3DCOMPILE_DEBUG;
    #endif
        // Prefer higher CS shader profile when possible as CS 5.0 provides better performance on 11-class hardware.
        LPCSTR profile = ( device->GetFeatureLevel() >= D3D_FEATURE_LEVEL_11_0 ) ? "cs_5_0" : "cs_4_0";
        const D3D_SHADER_MACRO defines[] = 
        {
            "EXAMPLE_DEFINE", "1",
            NULL, NULL
        };
        ID3DBlob* shaderBlob = nullptr;
        ID3DBlob* errorBlob = nullptr;
        HRESULT hr = D3DCompileFromFile( srcFile, defines, D3D_COMPILE_STANDARD_FILE_INCLUDE,
                                         entryPoint, profile,
                                         flags, 0, &shaderBlob, &errorBlob );
    ```

    

2.  Create a compute shader using [**ID3D11Device::CreateComputeShader**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createcomputeshader).
    ```
    ID3D11ComputeShader* g_pFinalPassCS = NULL;
    pd3dDevice->CreateComputeShader( pBlobFinalPassCS->GetBufferPointer(), 
                                           pBlobFinalPassCS->GetBufferSize(), 
                                           NULL, &g_pFinalPassCS );
    ```

    

The following code example shows how to compile and create a compute shader.

> [!Note]  
> For this example code, you need the Windows SDK 8.0 and the d3dcompiler\_44.dll file from the %PROGRAM\_FILE%\\Windows Kits\\8.0\\Redist\\D3D\\&lt;arch&gt; folder in your path.

 


```cpp
#define _WIN32_WINNT 0x600
#include <stdio.h>

#include <d3d11.h>
#include <d3dcompiler.h>

#pragma comment(lib,"d3d11.lib")
#pragma comment(lib,"d3dcompiler.lib")

HRESULT CompileComputeShader( _In_ LPCWSTR srcFile, _In_ LPCSTR entryPoint,
                              _In_ ID3D11Device* device, _Outptr_ ID3DBlob** blob )
{
    if ( !srcFile || !entryPoint || !device || !blob )
       return E_INVALIDARG;

    *blob = nullptr;

    UINT flags = D3DCOMPILE_ENABLE_STRICTNESS;
#if defined( DEBUG ) || defined( _DEBUG )
    flags |= D3DCOMPILE_DEBUG;
#endif

    // We generally prefer to use the higher CS shader profile when possible as CS 5.0 is better performance on 11-class hardware
    LPCSTR profile = ( device->GetFeatureLevel() >= D3D_FEATURE_LEVEL_11_0 ) ? "cs_5_0" : "cs_4_0";

    const D3D_SHADER_MACRO defines[] = 
    {
        "EXAMPLE_DEFINE", "1",
        NULL, NULL
    };

    ID3DBlob* shaderBlob = nullptr;
    ID3DBlob* errorBlob = nullptr;
    HRESULT hr = D3DCompileFromFile( srcFile, defines, D3D_COMPILE_STANDARD_FILE_INCLUDE,
                                     entryPoint, profile,
                                     flags, 0, &shaderBlob, &errorBlob );
    if ( FAILED(hr) )
    {
        if ( errorBlob )
        {
            OutputDebugStringA( (char*)errorBlob->GetBufferPointer() );
            errorBlob->Release();
        }

        if ( shaderBlob )
           shaderBlob->Release();

        return hr;
    }    

    *blob = shaderBlob;

    return hr;
}

int main()
{
    // Create Device
    const D3D_FEATURE_LEVEL lvl[] = { D3D_FEATURE_LEVEL_11_1, D3D_FEATURE_LEVEL_11_0,
                                      D3D_FEATURE_LEVEL_10_1, D3D_FEATURE_LEVEL_10_0 };

    UINT createDeviceFlags = 0;
#ifdef _DEBUG
    createDeviceFlags |= D3D11_CREATE_DEVICE_DEBUG;
#endif

    ID3D11Device* device = nullptr;
    HRESULT hr = D3D11CreateDevice( nullptr, D3D_DRIVER_TYPE_HARDWARE, nullptr, createDeviceFlags, lvl, _countof(lvl),
                                    D3D11_SDK_VERSION, &device, nullptr, nullptr );
    if ( hr == E_INVALIDARG )
    {
        // DirectX 11.0 Runtime doesn't recognize D3D_FEATURE_LEVEL_11_1 as a valid value
        hr = D3D11CreateDevice( nullptr, D3D_DRIVER_TYPE_HARDWARE, nullptr, 0, &lvl[1], _countof(lvl) - 1,
                                D3D11_SDK_VERSION, &device, nullptr, nullptr );
    }

    if ( FAILED(hr) )
    {
        printf("Failed creating Direct3D 11 device %08X\n", hr );
        return -1;
    }

    // Verify compute shader is supported
    if ( device->GetFeatureLevel() < D3D_FEATURE_LEVEL_11_0 )
    {
        D3D11_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS hwopts = { 0 } ;
        (void)device->CheckFeatureSupport( D3D11_FEATURE_D3D10_X_HARDWARE_OPTIONS, &hwopts, sizeof(hwopts) );
        if ( !hwopts.ComputeShaders_Plus_RawAndStructuredBuffers_Via_Shader_4_x )
        {
            device->Release();
            printf( "DirectCompute is not supported by this device\n" );
            return -1;
        }
    }

    // Compile shader
    ID3DBlob *csBlob = nullptr;
    hr = CompileComputeShader( L"ExampleCompute.hlsl", "CSMain", device, &csBlob );
    if ( FAILED(hr) )
    {
        device->Release();
        printf("Failed compiling shader %08X\n", hr );
        return -1;
    }

    // Create shader
    ID3D11ComputeShader* computeShader = nullptr;
    hr = device->CreateComputeShader( csBlob->GetBufferPointer(), csBlob->GetBufferSize(), nullptr, &computeShader );

    csBlob->Release();

    if ( FAILED(hr) )
    {
        device->Release();
    }

    printf("Success\n");

    // Clean up
    computeShader->Release();

    device->Release();

    return 0;
}

```



The preceding code example compiles the compute shader code in the ExampleCompute.hlsl file. Here is the code in ExampleCompute.hlsl:


```hlsl
//--------------------------------------------------------------------------------------
// File: BasicCompute11.hlsl
//
// This file contains the Compute Shader to perform array A + array B
// 
// Copyright (c) Microsoft Corporation. All rights reserved.
//--------------------------------------------------------------------------------------

#ifdef USE_STRUCTURED_BUFFERS

struct BufType
{
    int i;
    float f;
#ifdef TEST_DOUBLE
    double d;
#endif    
};

StructuredBuffer<BufType> Buffer0 : register(t0);
StructuredBuffer<BufType> Buffer1 : register(t1);
RWStructuredBuffer<BufType> BufferOut : register(u0);

[numthreads(1, 1, 1)]
void CSMain( uint3 DTid : SV_DispatchThreadID )
{
    BufferOut[DTid.x].i = Buffer0[DTid.x].i + Buffer1[DTid.x].i;
    BufferOut[DTid.x].f = Buffer0[DTid.x].f + Buffer1[DTid.x].f;
#ifdef TEST_DOUBLE
    BufferOut[DTid.x].d = Buffer0[DTid.x].d + Buffer1[DTid.x].d;
#endif 
}

#else // The following code is for raw buffers

ByteAddressBuffer Buffer0 : register(t0);
ByteAddressBuffer Buffer1 : register(t1);
RWByteAddressBuffer BufferOut : register(u0);

[numthreads(1, 1, 1)]
void CSMain( uint3 DTid : SV_DispatchThreadID )
{
#ifdef TEST_DOUBLE
    int i0 = asint( Buffer0.Load( DTid.x*16 ) );
    float f0 = asfloat( Buffer0.Load( DTid.x*16+4 ) );
    double d0 = asdouble( Buffer0.Load( DTid.x*16+8 ), Buffer0.Load( DTid.x*16+12 ) );
    int i1 = asint( Buffer1.Load( DTid.x*16 ) );
    float f1 = asfloat( Buffer1.Load( DTid.x*16+4 ) );
    double d1 = asdouble( Buffer1.Load( DTid.x*16+8 ), Buffer1.Load( DTid.x*16+12 ) );
    
    BufferOut.Store( DTid.x*16, asuint(i0 + i1) );
    BufferOut.Store( DTid.x*16+4, asuint(f0 + f1) );
    
    uint dl, dh;
    asuint( d0 + d1, dl, dh );

    BufferOut.Store( DTid.x*16+8, dl );
    BufferOut.Store( DTid.x*16+12, dh );
#else
    int i0 = asint( Buffer0.Load( DTid.x*8 ) );
    float f0 = asfloat( Buffer0.Load( DTid.x*8+4 ) );
    int i1 = asint( Buffer1.Load( DTid.x*8 ) );
    float f1 = asfloat( Buffer1.Load( DTid.x*8+4 ) );
    
    BufferOut.Store( DTid.x*8, asuint(i0 + i1) );
    BufferOut.Store( DTid.x*8+4, asuint(f0 + f1) );
#endif // TEST_DOUBLE
}

#endif // USE_STRUCTURED_BUFFERS
```



## Related topics

* [Compute Shader Overview](direct3d-11-advanced-stages-compute-shader.md)
* [How to Use Direct3D 11](how-to-use-direct3d-11.md)
* [BasicCompute11 sample application](https://github.com/walbourn/directx-sdk-samples/tree/master/BasicCompute11)
