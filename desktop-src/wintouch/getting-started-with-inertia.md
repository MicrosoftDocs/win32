---
title: Inertia
description: This section explains inertia for Windows Touch.
ms.assetid: c33dda89-c715-4da0-a7af-aa0010dfd88b
keywords:
- Windows Touch,inertia
- inertia,about
ms.topic: article
ms.date: 05/31/2018
---

# Inertia

This section explains inertia for Windows Touch.

The inertia API included in Windows 7 enables consistent object behavior in Windows Touch applications by providing a simple physics model. Inertia is enabled by using the inertia processor, a class that encapsulates functionality. The inertia processor works by processing events that are passed to it when object manipulations finish and by handling object trajectories in a way that is consistent with other applications. Note that the inertia processor is tightly coupled to the manipulation processor to simplify adding inertia support to applications that use manipulations. In fact, the inertia processor raises the same events that the manipulation processor does. The following section explains how to get started with inertia.



| Section                                                                      | Description                                                                                                              |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [Inertia Mechanics](inertia-mechanics.md)                                   | Explains the basics of inertia calculations.                                                                             |
| [Handling Inertia in Unmanaged Code](handling-inertia-in-unmanaged-code.md) | Explains how to use the [**IInertiaProcessor**](/windows/desktop/api/manipulations/nn-manipulations-iinertiaprocessor) interface for handling inertia in unmanaged code. |



 

## Related topics

<dl> <dt>

[Manipulations and Inertia](manipulation-and-inertia.md)
</dt> </dl>

 

 




