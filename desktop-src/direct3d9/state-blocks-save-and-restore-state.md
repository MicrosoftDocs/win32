---
description: A state block is a group of device states.
ms.assetid: 6b1917a8-8685-40c3-983d-6bd2fed95642
title: State Blocks Save and Restore State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# State Blocks Save and Restore State (Direct3D 9)

A state block is a group of device states. Device state is made up of render state, vertex state, pixel state, or all of the above. A state block contains a snapshot of a device's current state, or you can create a state block that records each state change that your application makes.

## Capture a Block of State

Choose the type of state that you want to capture, and create a state block like this:


```
IDirect3DStateBlock9* pStateBlock = NULL;
pd3dDevice->CreateStateBlock( D3DSBT_ALL, &pStateBlock );
```



[**IDirect3DDevice9::CreateStateBlock**](/windows/desktop/api) creates a state block, and automatically captures the device state. The device state is specified by the state block type in the first argument. This state can be one of the following: all device state (see [Saving All Device States with a StateBlock (Direct3D 9)](saving-all-device-states-with-a-stateblock.md)), all pixel state (see [Saving Pixel State With a StateBlock (Direct3D 9)](saving-pixel-states-with-a-stateblock.md)), or all vertex state (see [Saving Vertex States With a StateBlock (Direct3D 9)](saving-vertex-states-with-a-stateblock.md)).

The effect system uses a state block to save state. After [**ID3DXEffect::Begin**](id3dxeffect--begin.md) is called, a state block is created and state is captured. When [**ID3DXEffect::End**](id3dxeffect--end.md) is called, the state block state is reapplied to the device.

## Capture Individual States

To save a custom state sequence, wrap the state that you want to save in a [**IDirect3DDevice9::BeginStateBlock**](/windows/desktop/api) and [**IDirect3DDevice9::EndStateBlock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-endstateblock) pair. BeginStateBlock tells the current device to set up a state block and add to it every state change that occurs until EndStateBlock is called. Here's an example:


```
IDirect3DStateBlock9* pStateBlock = NULL;
pd3dDevice->BeginStateBlock();
pd3dDevice->SetRenderState ( D3DRS_ZENABLE, true );
pd3dDevice->EndStateBlock( &pStateBlock );
```



This will save any number of state changes in any sequence to a custom stateblock. Later, when you want to use the stateblock to reset the device state, call [**IDirect3DStateBlock9::Apply**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dstateblock9-apply). This will overwrite only the device state that has been captured in the state block. Any other device state that was not captured with the custom stateblock will not be changed. Once again, since the stateblock object is an interface, you will need to release it when you are done with it.

## Related topics

<dl> <dt>

[States (Direct3D 9)](states.md)
</dt> </dl>

 

 
