---
description: Interdependencies Between Properties
ms.assetid: 1c7c7c76-ec27-4ee4-a860-24244843a1e5
title: Interdependencies Between Properties
ms.topic: article
ms.date: 05/31/2018
---

# Interdependencies Between Properties

When you set properties, the COM+ catalog enforces some coherency logic to ensure that you configure elements in a reasonable way. This logic can be implemented in two ways, as follows:

-   **Dependencies.** You might be blocked from making some changes because another property depends on a particular setting for a property you attempt to set. For example, if a component is set with the attribute Transactions Required and if you then attempt to change the Synchronization setting to None, an error is generated when you attempt to call [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges) because transactions depend on synchronization.
-   **Side effects.** Some properties might be changed for you without your explicitly setting them. For example, if you set a component with the attribute Transactions Required, Synchronization will be set to Required as well. This is really the flip side of dependencies—one property takes precedence over another, and its dependency is expressed through first setting the secondary property and then blocking changes to it.

In the list of properties exposed by items in a collection, all listed in [COM+ Administration Collections](com--administration-collections.md), the dependencies and side effects are stated for each property. When you configure COM+ applications and components, you should be aware of what constraints are imposed on configurations.

## Related topics

<dl> <dt>

[Getting and Setting Properties](getting-and-setting-properties.md)
</dt> <dt>

[Querying for Available Properties](querying-for-available-properties.md)
</dt> <dt>

[Saving or Discarding Changes](saving-or-discarding-changes.md)
</dt> </dl>

 

 



