---
description: Used to set and query effects, and to choose techniques. An effect object can contain multiple techniques to render the same effect.
ms.assetid: bffc64ab-12e7-44e9-b296-262b0459a68a
title: ID3DXEffect interface (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffect
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXEffect interface

Used to set and query effects, and to choose techniques. An effect object can contain multiple techniques to render the same effect.

## Members

The **ID3DXEffect** interface inherits from [**ID3DXBaseEffect**](id3dxbaseeffect.md). **ID3DXEffect** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXEffect** interface has these methods.



| Method                                                                | Description                                                                                                                                                                                      |
|:----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ApplyParameterBlock**](id3dxeffect--applyparameterblock.md)       | Apply the values in a state block to the current effect system state.<br/>                                                                                                                 |
| [**Begin**](id3dxeffect--begin.md)                                   | Starts an active technique.<br/>                                                                                                                                                           |
| [**BeginParameterBlock**](id3dxeffect--beginparameterblock.md)       | Start capturing state changes in a parameter block.<br/>                                                                                                                                   |
| [**BeginPass**](id3dxeffect--beginpass.md)                           | Begins a pass, within the active technique.<br/>                                                                                                                                           |
| [**CloneEffect**](id3dxeffect--cloneeffect.md)                       | Creates a copy of an effect.<br/>                                                                                                                                                          |
| [**CommitChanges**](id3dxeffect--commitchanges.md)                   | Propagate state changes that occur inside of an active pass to the device before rendering.<br/>                                                                                           |
| [**DeleteParameterBlock**](id3dxeffect--deleteparameterblock.md)     | Delete a parameter block.<br/>                                                                                                                                                             |
| [**End**](id3dxeffect--end.md)                                       | Ends an active technique.<br/>                                                                                                                                                             |
| [**EndParameterBlock**](id3dxeffect--endparameterblock.md)           | Stop capturing effect parameter state changes.<br/>                                                                                                                                        |
| [**EndPass**](id3dxeffect--endpass.md)                               | End an active pass.<br/>                                                                                                                                                                   |
| [**FindNextValidTechnique**](id3dxeffect--findnextvalidtechnique.md) | Searches for the next valid technique, starting at the technique after the specified technique.<br/>                                                                                       |
| [**GetCurrentTechnique**](id3dxeffect--getcurrenttechnique.md)       | Gets the current technique.<br/>                                                                                                                                                           |
| [**GetDevice**](id3dxeffect--getdevice.md)                           | Retrieves the device associated with the effect.<br/>                                                                                                                                      |
| [**GetPool**](id3dxeffect--getpool.md)                               | Gets a pointer to the pool of shared parameters.<br/>                                                                                                                                      |
| [**GetStateManager**](id3dxeffect--getstatemanager.md)               | Get the effect state manager.<br/>                                                                                                                                                         |
| [**IsParameterUsed**](id3dxeffect--isparameterused.md)               | Determines if a parameter is used by the technique.<br/>                                                                                                                                   |
| [**OnLostDevice**](id3dxeffect--onlostdevice.md)                     | Use this method to release all references to video memory resources and delete all stateblocks. This method should be called whenever a device is lost, or before resetting a device.<br/> |
| [**OnResetDevice**](id3dxeffect--onresetdevice.md)                   | Use this method to re-acquire resources and save initial state.<br/>                                                                                                                       |
| [**SetRawValue**](id3dxeffect--setrawvalue.md)                       | Set a contiguous range of shader constants with a memory copy.<br/>                                                                                                                        |
| [**SetStateManager**](id3dxeffect--setstatemanager.md)               | Set the effect state manager.<br/>                                                                                                                                                         |
| [**SetTechnique**](id3dxeffect--settechnique.md)                     | Sets the active technique.<br/>                                                                                                                                                            |
| [**ValidateTechnique**](id3dxeffect--validatetechnique.md)           | Validate a technique.<br/>                                                                                                                                                                 |



 

## Remarks

The ID3DXEffect interface is obtained by calling [**D3DXCreateEffect**](d3dxcreateeffect.md), [**D3DXCreateEffectFromFile**](d3dxcreateeffectfromfile.md), or [**D3DXCreateEffectFromResource**](d3dxcreateeffectfromresource.md).

The LPD3DXEFFECT type is defined as a pointer to this interface.


```
typedef interface ID3DXEffect ID3DXEffect;
typedef interface ID3DXEffect *LPD3DXEFFECT;
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[**ID3DXBaseEffect**](id3dxbaseeffect.md)
</dt> <dt>

[Effect Interfaces](dx9-graphics-reference-effects-interfaces.md)
</dt> <dt>

[**D3DXCreateEffect**](d3dxcreateeffect.md)
</dt> <dt>

[**D3DXCreateEffectFromFile**](d3dxcreateeffectfromfile.md)
</dt> <dt>

[**D3DXCreateEffectFromResource**](d3dxcreateeffectfromresource.md)
</dt> </dl>

 

 




