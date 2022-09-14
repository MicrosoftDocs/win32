---
description: You can control which feature installation options are available for users and applications to select by authoring the Feature table and Component table.
ms.assetid: 3ce441e0-e709-415c-af64-b1ded7b04f6b
title: Controlling Feature Selection States
ms.topic: article
ms.date: 05/31/2018
---

# Controlling Feature Selection States

You can control which feature installation options are available for users and applications to select by authoring the [Feature table](feature-table.md) and [Component table](component-table.md).

-   To prevent selection of the advertise state for a feature, include **msidbFeatureAttributesDisallowAdvertise** in the feature's Attributes field in the [Feature table](feature-table.md).
-   To prevent selection of the run-from-source or run-from-network states for a feature, include **msidbComponentAttributesLocalOnly** in the Attributes fields in the [Component table](component-table.md) for every component belonging to the feature. If a feature has no components, the feature always has the run-from-source and run-from-my-computer options available.
-   To prevent selection of the run-from-my-computer state for a feature, include **msidbComponentAttributesSourceOnly** in the Attributes fields in the [Component table](component-table.md) for every component belonging to the feature. If a feature has no components, the feature always has the run-from-source and run-from-my-computer options available.
-   New child features can be authored by including **msidbFeatureAttributesFollowParent** and **msidbFeatureAttributesUIDisallowAbsent** in the Attributes field of the [Feature table](feature-table.md).

 

 



