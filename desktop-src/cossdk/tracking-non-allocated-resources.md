---
description: Tracking Non-Allocated Resources
ms.assetid: ebaca876-5249-4b6b-b0d5-08f098e3f5f5
title: Tracking Non-Allocated Resources
ms.topic: article
ms.date: 05/31/2018
---

# Tracking Non-Allocated Resources

The dispenser manager can track a resource that is not inventoried, based on knowledge of the object's lifetime. When a tracked, non-allocated resource is freed, it is destroyed and therefore not returned to inventory. This track-only mode for resources that are inexpensive to create and destroy is more useful than storing them in inventory. This mode is also useful for managing a memory dispenser or for a resource that is difficult to inventory because there are too many different types.

In track-only mode, a resource dispenser directly creates a requested resource instead of asking the dispenser manager to allocate one from inventory. Before returning this resource to the requesting application component, the resource dispenser tells the dispenser manager to track the resource, which ensures that even if the component neglects to free the resource, the dispenser manager will do so when the component's lifetime is over.

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> </dl>

 

 



