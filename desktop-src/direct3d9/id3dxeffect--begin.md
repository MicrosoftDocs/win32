---
description: Starts an active technique.
ms.assetid: 6598d77b-8b53-4f2d-aa43-adf358ad486d
title: ID3DXEffect::Begin method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffect.Begin
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffect::Begin method

Starts an active technique.

## Syntax


```C++
HRESULT Begin(
  [out] UINT  *pPasses,
  [in]  DWORD Flags
);
```



## Parameters

<dl> <dt>

*pPasses* \[out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Pointer to a value returned that indicates the number of passes needed to render the current technique.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

DWORD that determines if state modified by an effect is saved and restored. The default value 0 specifies that **ID3DXEffect::Begin** and [**ID3DXEffect::End**](id3dxeffect--end.md) will save and restore all state modified by the effect (including pixel and vertex shader constants). Valid flags can be seen at [Effect State Save and Restore Flags](d3dxfx.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

An application sets one active technique in the effect system by calling **ID3DXEffect::Begin**. The effect system responds by capturing all the pipeline state that can be changed by the technique in a state block. An application signals the end of a technique by calling [**ID3DXEffect::End**](id3dxeffect--end.md), which uses the state block to restore the original state. The effect system, therefore, takes care of saving state when a technique becomes active and restoring state when a technique ends. If you choose to disable this save and restore functionality, see [D3DXFX\_DONOTSAVESAMPLERSTATE](d3dxfx.md).

Within the **ID3DXEffect::Begin** and [**ID3DXEffect::End**](id3dxeffect--end.md) pair, an application uses [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md) to set the active pass, [**ID3DXEffect::CommitChanges**](id3dxeffect--commitchanges.md) if any state changes occurred after the pass was activated, and [**ID3DXEffect::EndPass**](id3dxeffect--endpass.md) to end the active pass.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> </dl>

 

 
