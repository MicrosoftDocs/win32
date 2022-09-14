---
description: Authors should run validation on every new, or newly modified, merge module before attempting to merge the module into an installation database for the first time.
ms.assetid: 8d6794af-403a-416e-8ace-1af3f193414b
title: Validating Merge Modules
ms.topic: article
ms.date: 05/31/2018
---

# Validating Merge Modules

Authors should run validation on every new, or newly modified, merge module before attempting to merge the module into an installation database for the first time. Merge module validation works in the same way as [package validation](package-validation.md) but uses a different set of [Internal Consistency Evaluators](internal-consistency-evaluators-ices.md) (ICEs) specific to merge modules. For more information about these merge module ICEs, see [Merge Module ICE Reference](merge-module-ice-reference.md).

Merge module ICEs are stored in the merge module .cub file, Mergemod.cub. The installation of the Orca tool or msival2 also provides the Logo.cub, Darice.cub, and Mergemod.cub files.

For more information, see [Merge Module ICE Reference](merge-module-ice-reference.md).

 

 



