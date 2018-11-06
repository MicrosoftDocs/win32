---
title: How to Play Back a Command List
description: This topic shows how to play back a command list.
ms.assetid: 4e6c0a98-85ff-45ca-963b-7d5c55f47195
ms.topic: article
ms.date: 05/31/2018
---

# How to: Play Back a Command List

A [command list](overviews-direct3d-11-render-multi-thread-command-list.md) is a recorded list of rendering commands. Use a command list to pre-record drawing commands and play them back later. This topic shows how to play back a [command list](overviews-direct3d-11-render-multi-thread-command-list.md). A command list can be used to split rendering tasks between threads.

This section describes how to play back a command list. For recording a command list, see [How to: Record a Command List](overviews-direct3d-11-render-multi-thread-command-list-record.md).

**To play back a command list**

-   Call [**ID3D11DeviceContext::ExecuteCommandList**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-executecommandlist) and pass a valid [**ID3D11CommandList**](/windows/desktop/api/D3D11/nn-d3d11-id3d11commandlist) object.
    ```
    if(g_pd3dCommandList)
    {
        g_pImmediateContext->ExecuteCommandList(g_pd3dCommandList, TRUE);
    }
    ```

    

[**ExecuteCommandList**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-executecommandlist) must be executed on the [immediate context](overviews-direct3d-11-devices-intro.md) for recorded commands to be run on the graphics processing unit (GPU). Use the immediate context to feed commands to the GPU for execution, use a deferred context to record commands for playback onto another command list. When you call **ExecuteCommandList** onto another deferred context, you create a ‘merged’ deferred command list. To run the commands on the merged deferred command list, you need to execute them on the immediate context.

## Related topics

<dl> <dt>

[Command List](overviews-direct3d-11-render-multi-thread-command-list.md)
</dt> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> </dl>

 

 




