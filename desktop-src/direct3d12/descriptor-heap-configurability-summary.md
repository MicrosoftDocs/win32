---
title: Descriptor Heap Configurability Summary
description: The following table summarizes information about Shader and non-Shader visible heap support.
ms.assetid: DF266915-6224-4FFB-BE3E-34A44F7318DD
ms.topic: article
ms.date: 05/31/2018
---

# Descriptor Heap Configurability Summary

The following table summarizes information about Shader and non-Shader visible heap support.



|                               | Shader Visible Descriptor Heap                                                 | Non Shader Visible Descriptor Heap                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Heap Types Supported**          | CBV\_SRV\_UAV, Sampler                                                         | All                                                                                                                                                                                                                                                                                                                                                                 |
| **CPU Page Properties Supported** | NOT\_AVAILABLE, WRITE\_COMBINE                                                 | WRITE\_BACK                                                                                                                                                                                                                                                                                                                                                         |
| **Residency Management By App**   | Yes, app responsible                                                           | Not applicable (not GPU visible).                                                                                                                                                                                                                                                                                                                                   |
| **Descriptor Edit Support**       | Copy destination only, via command list update and/or CPU copy if CPU visible. | CPU read and write only. No direct GPU access. Can be used for immediate CPU copying (as a source and destination). Can be used as an update source on a command list – this will copy the descriptors into command list storage during command list record. On execution, the stored copy will get copied to the destination, which must be a shader visible heap. |



 

## Related topics

<dl> <dt>

[Descriptor Heaps](descriptor-heaps.md)
</dt> </dl>

 

 




