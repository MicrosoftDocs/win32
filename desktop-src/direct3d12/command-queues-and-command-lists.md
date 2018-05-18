---
title: Work Submission in Direct3D 12
description: To improve the CPU efficiency of Direct3D apps, Direct3D 12 no longer supports an immediate context associated with a device.
ms.assetid: 'BE2F46EA-D4A9-47F7-A2D1-6A486DD4DC1A'
---

# Work Submission in Direct3D 12

To improve the CPU efficiency of Direct3D apps, Direct3D 12 no longer supports an immediate context associated with a device. Instead, apps record and then submit *command lists*, which contain drawing and resource management calls. These command lists can be submitted from multiple threads to one or more command queues, which manage the execution of the commands. This fundamental change increases single-threaded efficiency by allowing apps to pre-compute rendering work for later re-use, and it takes advantage of multi-core systems by spreading rendering work across multiple threads.

## In this section



| Topic                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Design Philosophy of Command Queues and Command Lists](design-philosophy-of-command-queues-and-command-lists.md)<br/>                                 | The goals of enabling reuse of rendering work and of multi-threaded scaling, required fundamental changes to how Direct3D apps submit rendering work to the GPU.<br/>                                                                                                                                                                             |
| [Creating and Recording Command Lists and Bundles](recording-command-lists-and-bundles.md)<br/>                                                        | This topic describes recording command lists and bundles in Direct3D 12 apps. Command lists and bundles both allow apps to record drawing or state-changing calls for later execution on the graphics processing unit (GPU). <br/>                                                                                                                |
| [Executing and Synchronizing Command Lists](executing-and-synchronizing-command-lists.md)<br/>                                                         | In Microsoft Direct3D 12, the immediate mode of previous versions is no longer present. Instead, apps create command lists and bundles and then record sets of GPU commands. Command queues are used to submit command lists to be executed. This model allows developers to have more control over the efficient usage of both GPU and CPU.<br/> |
| [Managing Graphics Pipeline State in Direct3D 12](managing-graphics-pipeline-state-in-direct3d-12.md)<br/>                                             | This topic describes how graphics pipeline state is set in Direct3D 12. <br/>                                                                                                                                                                                                                                                                     |
| [Using Resource Barriers to Synchronize Resource States in Direct3D 12](using-resource-barriers-to-synchronize-resource-states-in-direct3d-12.md)<br/> | To reduce overall CPU usage and enable driver multi-threading and pre-processing, Direct3D 12 moves the responsibility of per-resource state management from the graphics driver to the application.<br/>                                                                                                                                         |
| [Pipelines and Shaders with Direct3D 12](pipelines-and-shaders-with-directx-12.md)<br/>                                                                | The Direct3D 12 programmable pipeline significantly increases rendering performance compared to previous generation graphics programming interfaces.<br/>                                                                                                                                                                                         |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> </dl>

 

 





