---
title: Direct3D 12 Raytracing HLSL Intrinsics
description: The following HLSL shaders support the Direct3D 12 raytracing pipeline.
ms.assetid: 
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Raytracing HLSL Intrinsics

The following HLSL intrinisc functions support the Direct3D 12 raytracing pipeline. 

## In this section



| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AcceptHitAndEndSearch function**](accepthitandendsearch-function.md)<br/>                              | Used in an any hit shader to commit the current hit and then stop searching for more hits for the ray.<br/>                                                                                                                                                                                                                                              |
| [**CallShader function**](callshader-function.md)<br/>                              | Invokes another shader from within a shader.<br/>                                                                                                                                                                                                                                              |
| [**IgnoreHit function**](ignorehit-function.md)<br/>                              |  Called from an any hit shader to reject the hit and end the shader.<br/>                                                                                                                                                                                                                                              |
| [**ReportHit function**](reporthit-function.md)<br/>                              | Called by an intersection shader to report a ray intersection.<br/>                                                                                                                                                                                                                                              |
| [**TraceRay function**](traceray-function.md)<br/>                              | Sends a ray into a search for hits in an acceleration structure.<br/>                                                                                                                                                                                                                                              |


## Related topics

<dl> <dt>

[Core Reference](direct3d-12-core-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





