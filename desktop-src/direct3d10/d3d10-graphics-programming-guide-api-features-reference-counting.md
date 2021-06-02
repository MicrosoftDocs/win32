---
description: Direct3D 10 set functions do not hold a reference to a device-child object.
ms.assetid: 4f4e1af8-5830-4b2d-ba2e-dc2ec4e74a19
title: Reference Counting (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Reference Counting (Direct3D 10)

Direct3D 10 set functions do not hold a reference to a device-child object. This means that each application must hold a reference to a device-child object for as long as the object needs to be bound to the pipeline. When the reference count of an object drops to zero, the object will be unbound from the pipeline and destroyed. This style of reference holding is also known as weak-reference holding because each pipeline binding location holds a weak reference to the interface/object that is bound to it.

For example:


```
pDevice->CreateRasterizerState( ..., &pRasterizerState );
pDevice->RSSetState( pRasterizerState );
 
pDevice->RSGetState( &pCurRasterizerState );
// pCurRasterizerState will be equal to pRasterizerState.
pCurRasterizerState->Release();
 
pRasterizerState->Release();
// Following the final release, the object is unbound.
pDevice->RSGetState( &pCurRasterizerState );
// pCurRasterizerState will be equal to NULL.
```





Differences between Direct3D 9 and Direct3D 10:

- In Direct3D 9, set functions hold a reference to the device objects; in Direct3D 10 set functions do not hold a reference to the device-child objects.



 

## Related topics

<dl> <dt>

[API Features (Direct3D 10)](d3d10-graphics-programming-guide-api-features.md)
</dt> </dl>

 

 




