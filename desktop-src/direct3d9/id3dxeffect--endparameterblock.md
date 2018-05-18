---
Description: 'Stop capturing effect parameter state changes.'
ms.assetid: 'b6ca2917-2df0-4f3a-9ee3-23e9d2501ff4'
title: 'ID3DXEffect::EndParameterBlock method'
---

# ID3DXEffect::EndParameterBlock method

Stop capturing effect parameter state changes.

## Syntax


```C++
D3DXHANDLE EndParameterBlock();
```



## Parameters

This method has no parameters.

## Return value

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Returns a handle to the parameter state block.

## Remarks

All effect parameters that change state (after calling BeginParameterBlock and before calling EndParameterBlock) will be saved in an effect parameter state block. Use ApplyParameterBlock to apply this block of state changes to the effect system. Once you are finished with a state block use DeleteParameterBlock to free the memory.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> <dt>

[**ID3DXEffect::BeginParameterBlock**](id3dxeffect--beginparameterblock.md)
</dt> <dt>

[**ID3DXEffect::ApplyParameterBlock**](id3dxeffect--applyparameterblock.md)
</dt> <dt>

[**ID3DXEffect::DeleteParameterBlock**](id3dxeffect--deleteparameterblock.md)
</dt> </dl>

 

 




