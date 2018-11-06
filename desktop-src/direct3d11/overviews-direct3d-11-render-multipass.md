---
title: Multiple-Pass Rendering
description: Multiple-pass rendering is a process in which an application traverses its scene graph multiple times in order to produce an output to render to the display.
ms.assetid: 9a11686a-fd99-4d40-8b02-6f8ec18346e8
ms.topic: article
ms.date: 05/31/2018
---

# Multiple-Pass Rendering

Multiple-pass rendering is a process in which an application traverses its scene graph multiple times in order to produce an output to render to the display. Multiple-pass rendering improves performance because it breaks up complex scenes into tasks that can run concurrently.

To perform multiple-pass rendering, you create a deferred context and command list for each additional pass. While the application traverses the scene graph, it records commands (for example, rendering commands such as [**Draw**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-draw)) into a deferred context. After the application finishes the traversal, it calls the [**FinishCommandList**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-finishcommandlist) method on the deferred context. Finally, the application calls the [**ExecuteCommandList**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-executecommandlist) method on the immediate context to execute the commands in each command list.

The following pseudocode shows how to perform multiple-pass rendering:

``` syntax
{
 ImmCtx->SetRenderTarget( pRTViewOfResourceX );
 DefCtx1->SetTexture( pSRView1OfResourceX );
 DefCtx2->SetTexture( pSRView2OfResourceX );

 for () // Traverse the scene graph.
  {
    ImmCtx->Draw(); // Pass 0: immediate context renders primitives into resource X.

    // The following texturing by the deferred contexts occurs after the 
    // immediate context makes calls to ExecuteCommandList. 
    // Resource X is then comletely updated by the immediate context. 
    DefCtx1->Draw(); // Pass 1: deferred context 1 performs texturing from resource X.
    DefCtx2->Draw(); // Pass 2: deferred context 2 performs texturing from resource X.
      }

  // Create command lists and record commands into them.
  DefCtx1->FinishCommandList( &pCL1 ); 
  DefCtx2->FinishCommandList( &pCL2 );

  ImmCtx->ExecuteCommandList( pCL1 ); // Execute pass 1.
  ImmCtx->ExecuteCommandList( pCL2 ); // Exeucte pass 2.
}
```

> [!Note]  
> The immediate context modifies a resource, which is bound to the immediate context as a render target view (RTV); in contrast, each deferred context simply uses the resource, which is bound to the deferred context as a shader resource view (SRV). For more information about immediate and deferred contexts, see [Immediate and Deferred Rendering](overviews-direct3d-11-render-multi-thread-render.md).

 

## Related topics

<dl> <dt>

[Rendering](overviews-direct3d-11-render.md)
</dt> </dl>

 

 




