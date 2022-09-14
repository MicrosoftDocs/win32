---
description: Compositor Transition
ms.assetid: 7903ecd7-88fb-4277-82ee-a7f71cae0412
title: Compositor Transition
ms.topic: article
ms.date: 05/31/2018
---

# Compositor Transition

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Compositor transition composites a subrectangle from the foreground into a designated rectangle on the background, without altering the rest of the background. Use this transition to create split-screen or picture-in-picture effects.

The following image shows the compositor transition:

![compositor transition](images/trans-compositor.png)

Class ID (CLSID): {BB44391D-6ABD-422f-9E2E-385C9DFF51FC}

CLSID Variable Name: CLSID\_DxtCompositor

Friendly Name: "DxtCompositor"

Properties



| Property   | Type | Default | Description                                                    |
|------------|------|---------|----------------------------------------------------------------|
| Height     | long | 0       | Height of the target rectangle, in pixels.                     |
| OffsetX    | long | 0       | Horizontal offset of the target rectangle, in pixels.          |
| OffsetY    | long | 0       | Vertical offset of the target rectangle, in pixels.            |
| SrcHeight  | long | 0       | The height of the subrectangle on the source, in pixels.       |
| SrcOffsetX | long | 0       | The x-coordinate of the subrectangle on the source, in pixels. |
| SrcOffsetY | long | 0       | The y-coordinate of the subrectangle on the source, in pixels. |
| SrcWidth   | long | 0       | The width of the subrectangle on the source, in pixels.        |
| Width      | long | 0       | Width of the target rectangle, in pixels.                      |



 

The following diagram illustrates these properties:

![compositor properties](images/compmeasure.png)

## Related topics

<dl> <dt>

[Transitions and Effects](transitions-and-effects.md)
</dt> </dl>

 

 



