---
Description: In Direct3D 9, Direct3D will allow the driver to return error codes such as E\_OUTOFMEMORY, D3DERR\_OUTOFVIDEOMEMORY, and D3DERR\_UNSUPPORTEDCOLORARG so that an application would be able to respond to them.
ms.assetid: 483fdb03-e453-4a1b-bd8e-294e9e9a20c2
title: Driver Internal Errors (Direct3D 9)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Driver Internal Errors (Direct3D 9)

In Direct3D 9, Direct3D will allow the driver to return error codes such as E\_OUTOFMEMORY, D3DERR\_OUTOFVIDEOMEMORY, and D3DERR\_UNSUPPORTEDCOLORARG so that an application would be able to respond to them. However, sometimes the API calls that generated these return types get loaded into a command buffer and are batched up to be sent to the GPU (see [Controlling Runtime and Driver Optimizations](accurately-profiling-direct3d-api-calls.md)). In this case, the errors cannot be relayed to the application when action needs to be taken, so the error code is consumed by the runtime and a note is made on the device object that this happened. Later when the application invokes [**IDirect3DDevice9::Present**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-present?branch=master), **IDirect3DDevice9::Present** will return D3DERR\_DRIVERINTERNALERROR. This is why the best approach for an application to take when receiving a D3DERR\_DRIVERINTERNALERROR from **IDirect3DDevice9::Present** is to destroy and recreate the device.

If you want to try to debug further, here are a couple of suggestions for trying to figure out which API call is generating the error:

-   Because the list of possible return values is not complete, you can try to find which call is failing by surrounding each API call like this:

    ```
    TRACE ( "Calling DrawPrimitive" );
    d3ddev->DrawPrim(...);
    TRACE ( "done\n" );
    ```

    

    The output debug stream should then show the call that is causing the problem.

-   Additionally, for debugging purposes, try calling [**IDirect3DDevice9::ValidateDevice**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-validatedevice?branch=master) immediately before each [**IDirect3DDevice9::DrawPrimitive**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-drawprimitive?branch=master) to see if there is an additional problem with the device driver (unsupported operation, unusable combination of texture formats, etc).

    > [!Note]  
    > [**IDirect3DDevice9::ValidateDevice**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-validatedevice?branch=master) should be used carefully and sparingly because of the amount of validation work the driver needs to perform to return an answer.

     

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 



