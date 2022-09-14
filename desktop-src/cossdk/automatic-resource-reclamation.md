---
description: Automatic Resource Reclamation
ms.assetid: c889dd3f-82d1-4bc3-ac2c-6f468d5b2c7f
title: Automatic Resource Reclamation
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Resource Reclamation

COM+ notifies the dispenser manager each time an object's lifetime ends. The dispenser manager then notifies each registered resource dispenser's Holder to see whether it has any resources still held by this object. If so, those resources are freed, preventing the possibility of resource leaks by components that get resources through a resource dispenser.

The auto-reclamation feature is an option that is turned off by default. A resource dispenser can choose to enable this option and, in doing so, guarantees that a reference to any resource dispensed to an object is never returned by the object methods.

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> </dl>

 

 



