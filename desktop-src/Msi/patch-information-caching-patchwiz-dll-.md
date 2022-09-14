---
description: Generating a new patch may require significant time.
ms.assetid: 8be9a83a-8c36-43f5-8dda-05fc2f3ce0d2
title: Patch Information Caching (Patchwiz.dll)
ms.topic: article
ms.date: 05/31/2018
---

# Patch Information Caching (Patchwiz.dll)

Generating a new patch may require significant time. After you have generated a patch using [Patchwiz.dll](patchwiz-dll.md), you may need to change the update image again and generate another patch. Patch information caching can reduce the time required to generate subsequent patches by reusing existing patches. For example, the time required to create service packs can be reduced by using the binary patches generated from previous patches. Patchwiz.dll can use PATCH\_CACHE\_DIR to find an existing binary patch and add it to the service pack's cabinet without having to re-create the binary patch.

Patch information caching requires the use of [Patchwiz.dll](patchwiz-dll.md). To activate patch caching, set the PATCH\_CACHE\_ENABLED and PATCH\_CACHE\_DIR properties in the [Properties Table (Patchwiz.dll)](properties-table-patchwiz-dll-.md) of the patch creation properties file (.pcp file). Patchwiz stores all patch creation information in the folder identified by the PATCH\_CACHE\_DIR property and creates this folder if necessary. The next time you attempt to create a patch, Patchwiz checks this folder to see whether the files to be compared match the files in the cache. If the files match, Patchwiz uses the cached information rather than regenerating the binary patch for the file. If the files do not match, or if the information is missing from the cache, Patchwiz generates the patch for the file.

To use patch information caching, the folder specified by PATCH\_CACHE\_DIR must be preserved after creating a .msp file. If the folder is deleted, PatchWiz has to re-generate binary patches for subsequent .msp files. For more information about preserving information in selected regions of a target file see [Patching Selected Regions of a File](patching-selected-regions-of-a-file.md).

 

 



