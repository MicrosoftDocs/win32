---
Description: The following structures are declared in vspixengine.h.
MS-HAID: vspixengine.vspixengine\_structures
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: Direct3D Diagnostics Capture Interface Structures
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.vspixengine_structures"></span>Direct3D Diagnostics Capture Interface Structures

The following structures are declared in vspixengine.h.

## <span id="in_this_section"></span>In this section

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Topic</th><th>Description</th></tr></thead><tbody><tr class="odd"><td><p>[<strong>ResourcePair</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432855)</p></td><td><p>Represents a shared resource which is encoded as a COM string.</p></td></tr><tr class="even"><td><p>[<strong>DescriptorHeapRecord</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422635)</p></td><td><p>Represents descriptor heap information.</p></td></tr><tr class="odd"><td><p>[<strong>PipeLineStageError</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432835)</p></td><td><p>Represents an error in a pipeline stage.</p></td></tr><tr class="even"><td><p>[<strong>PipeLineStage</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432834)</p></td><td><p>Represents a pipeline stage, including details of the shader used.</p></td></tr><tr class="odd"><td><p>[<strong>ExperimentTrigger</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422642)</p></td><td><p>Represents experiment trigger information.</p></td></tr><tr class="even"><td><p>[<strong>PackedCallPkg</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432833)</p></td><td><p>Represents a package of four calls.</p></td></tr><tr class="odd"><td><p>[<strong>SymbolServerInfo</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432859)</p></td><td><p>Represents information about the debug symbol server.</p></td></tr><tr class="even"><td><p>[<strong>CallStackFrame</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422631)</p></td><td><p>Represents information about a frame on the callstack.</p></td></tr><tr class="odd"><td><p>[<strong>SourceFileInfo</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432857)</p></td><td><p>Represents information about a source code file.</p></td></tr><tr class="even"><td><p>[<strong>SummaryItem</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432858)</p></td><td><p>Represents summary information about an event.</p></td></tr><tr class="odd"><td><p>[<strong>DebugShader</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422633)</p></td><td><p>Represents information about a shader under the debugger.</p></td></tr><tr class="even"><td><p>[<strong>Experiment</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422641)</p></td><td><p>Represents information about an experiment (capture).</p></td></tr><tr class="odd"><td><p>[<strong>Issue</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432806)</p></td><td><p>Represents information about an issue.</p></td></tr><tr class="even"><td><p>[<strong>Point2D</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432850)</p></td><td><p>Represents a 2D point with unsigned integer coordinates.</p></td></tr><tr class="odd"><td><p>[<strong>ThreadData3D</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432860)</p></td><td><p>Represents a 3D index into thread data</p></td></tr><tr class="even"><td><p>[<strong>InputLayoutStruct</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422695)</p></td><td><p>Represents the input layout fields of a vertex buffer, one per field in the vertex buffer.</p></td></tr><tr class="odd"><td><p>[<strong>PixelHistoryOperation</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432839)</p></td><td><p>Represents information about pixel history.</p></td></tr><tr class="even"><td><p>[<strong>PixelHistoryIntersection</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432838)</p></td><td><p>Represents information about a particular</p></td></tr><tr class="odd"><td><p>[<strong>MeshDataBufferLayoutEntry</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432828)</p></td><td><p>Represents information about a single entry in the buffer layout of a mesh.</p></td></tr><tr class="even"><td><p>[<strong>DebugShaderRequestInfo</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422634)</p></td><td><p>Represents information about a shader debugger request.</p></td></tr><tr class="odd"><td><p>[<strong>PixEngineInt4</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432843)</p></td><td><p>Represents a 4D vector with signed integer coordinates.</p></td></tr><tr class="even"><td><p>[<strong>PixEnginePoint4D</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432844)</p></td><td><p>Represents a 4D point with 64-bit floating-point (double) coordinates.</p></td></tr><tr class="odd"><td><p>[<strong>PixEngineChannelDesc</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432841)</p></td><td><p>Represents a description of a color (sample) channel.</p></td></tr><tr class="even"><td><p>[<strong>PixEngineTextureFormatDesc</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432846)</p></td><td><p>Represents a description of a texture format.</p></td></tr><tr class="odd"><td><p>[<strong>PixEngineTextureDescriptor</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432845)</p></td><td><p>Represents a description of a texture resource.</p></td></tr><tr class="even"><td><p>[<strong>PixEngineTextureSliceDescriptor</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432847)</p></td><td><p>Represents a description of a texture slice.</p></td></tr><tr class="odd"><td><p>[<strong>PixEngineTextureSliceIndex</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432848)</p></td><td><p>Represents the index of a texture slice</p></td></tr><tr class="even"><td><p>[<strong>PixEngineHistogram</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432842)</p></td><td><p>Represents a histogram of a texture.</p></td></tr></tbody></table>

 

## <span id="related_topics"></span>Related topics

[Direct3D Diagnostics Capture Interface Reference](vspixengine-reference.md)

 

 



