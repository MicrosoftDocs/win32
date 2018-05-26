---
Description: Uses the GPU to compute the direct lighting contribution to 3D objects where the source radiance is represented by a spherical harmonic (SH) approximation. Computing the lighting on the GPU will generally be much faster than on the CPU.
ms.assetid: ccea5a5e-23f1-4fdf-bce8-9bfc35d45257
title: ID3DXPRTEngineComputeDirectLightingSHGPU method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTEngine::ComputeDirectLightingSHGPU method

Uses the GPU to compute the direct lighting contribution to 3D objects where the source radiance is represented by a spherical harmonic (SH) approximation. Computing the lighting on the GPU will generally be much faster than on the CPU.

## Syntax


```C++
HRESULT ComputeDirectLightingSHGPU(
  [in]      LPDIRECT3DDEVICE9 pDevice,
  [in]      UINT              Flags,
  [in]      UINT              Order,
  [in]      FLOAT             ZBias,
  [in]      FLOAT             ZAngleBias,
  [in, out] LPD3DXPRTBUFFER   pDataOut
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master)**

Pointer to the [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) device object used to run the simulation on the GPU. The device must support [ps\_2\_0](direct3dhlsl.dx9_graphics_reference_asm_ps_2_0) pixel shaders.

> [!Note]  
> Callback functions should not use the [**IDirect3DDevice9**](/windows/win32/d3d9helper/nn-d3d9-idirect3ddevice9?branch=master) device object used by the GPU simulator.

 

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

GPU simulation parameter that defines the resolution of the shadow z-buffer. Should be set to one of the constant values from [**D3DXSHGPUSIMOPT**](direct3d9.d3dxshgpusimopt). To specifiy higher precision simulation, the D3DXSHGPUSIMOPT\_HIGHQUALITY value may be combined with one of the D3DXSHGPUSIMOPT\_SHADOWRESxxx values.

</dd> <dt>

*Order* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Order of the SH evaluation. Must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The evaluation generates Order² coefficients. The degree of the evaluation is Order - 1.

</dd> <dt>

*ZBias* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Bias in the normal direction.

</dd> <dt>

*ZAngleBias* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Bias in the normal direction, scaled by one minus the cosine of the angle with the light ray.

</dd> <dt>

*pDataOut* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object. This buffer must have the proper number of color channels allocated for the simulation.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

In this method, the albedo is not multiplied by the light signal, and only incoming light is integrated in the simulator. By not multiplying the albedo, you can model albedo variation at a finer scale than the source radiance, thereby yielding more accurate results from compression.

Call [**MultiplyAlbedo**](id3dxprtengine--multiplyalbedo.md) to multiply each precomputed radiance transfer (PRT) vector by the albedo.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 




