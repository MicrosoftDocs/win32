---
title: Methods (IInertiaProcessor)
description: This section contains the methods for the IInertiaProcessor interface.
ms.assetid: e4acfcac-06c1-42a5-9722-4534a4492ab8
keywords:
- Windows Touch,IInertiaProcessor interface
- Windows Touch,interface methods
- inertia,IInertiaProcessor interface
- IInertiaProcessor interface,methods
ms.topic: reference
ms.date: 05/31/2018
---

# Methods (IInertiaProcessor)

This section contains the methods for the [**IInertiaProcessor**](/windows/desktop/api/manipulations/nn-manipulations-iinertiaprocessor) interface.



| Method                                                 | Description                                                                                                                                                                                                                |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Reset**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-reset)               | Initializes the processor with initial time stamp and restarts inertia.                                                                                                                                                    |
| [**Process**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-process)           | Performs calculations for the current tick and can raise the **Delta** or **Completed** event depending on whether extrapolation is completed or not. If extrapolation finished at the previous tick, the method is no-op. |
| [**ProcessTime**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-processtime)   | Performs calculations for the given tick and can raise the **Delta** or **Completed** event depending on whether extrapolation is completed or not.                                                                        |
| [**Complete**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-complete)         | Finishes the current manipulation and stops inertia on the inertia processor.                                                                                                                                              |
| [**CompleteTime**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-completetime) | Finishes the current manipulation at the given tick, stops inertia on the inertia processor, and raises the ManipulationCompleted event.                                                                                   |



 

## Related topics

<dl> <dt>

[**IInertiaProcessor**](/windows/desktop/api/manipulations/nn-manipulations-iinertiaprocessor)
</dt> </dl>

 

 




