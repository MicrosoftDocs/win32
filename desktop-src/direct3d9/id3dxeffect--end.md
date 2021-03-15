---
description: Ends an active technique.
ms.assetid: 7297aa67-5cd4-4557-b5ef-faa6c27eaeb5
title: ID3DXEffect::End method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffect.End
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffect::End method

Ends an active technique.

## Syntax


```C++
HRESULT End();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

This method always returns the value S\_OK.

## Remarks

All rendering in an effect is done within a matching pair of [**ID3DXEffect::Begin**](id3dxeffect--begin.md) and **ID3DXEffect::End** calls. After all passes are rendered, **ID3DXEffect::End** must be called to end the active technique. The effect system responds by using the state block created when **ID3DXEffect::Begin** was called, to automatically restore the pipeline state before **ID3DXEffect::Begin**.

By default, the effect system takes care of saving state prior to a technique, and restoring state after a technique. If you choose to disable this save and restore functionality, see [D3DXFX\_DONOTSAVESAMPLERSTATE](d3dxfx.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> </dl>

 

 




