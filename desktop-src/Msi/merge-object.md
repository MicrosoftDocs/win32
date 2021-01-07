---
description: The Merge object provides access to other top-level objects. A Merge object must be created before loading the automation support required by COM to access the functions in Mergemod.dll.
ms.assetid: 3f76ee8a-d195-4a69-99a3-31ef2c1c72d5
title: Merge Object
ms.topic: article
ms.date: 05/31/2018
---

# Merge Object

The **Merge** object provides access to other top-level objects. A **Merge** object must be created before loading the automation support required by COM to access the functions in Mergemod.dll.

Mergemod.dll provides access to the extended functionality at build time through a second version of the existing CLSID. This CLSID supports existing functionality available through the [**IMsmMerge**](/windows/win32/api/mergemod/nn-mergemod-imsmmerge) interface, but the default interface on the object (and the associated dual interface) is the [**IMsmMerge2**](/windows/desktop/api/Mergemod/nn-mergemod-imsmmerge2) interface instead of the **IMsmMerge** interface.

 

 
