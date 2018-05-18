---
title: Methods
description: This section contains the methods for the IInertiaProcessor interface.
ms.assetid: 'e4acfcac-06c1-42a5-9722-4534a4492ab8'
keywords: ["Windows Touch,IInertiaProcessor interface", "Windows Touch,interface methods", "inertia,IInertiaProcessor interface", "IInertiaProcessor interface,methods"]
---

# Methods

This section contains the methods for the [**IInertiaProcessor**](iinertiaprocessor.md) interface.



| Method                                                 | Description                                                                                                                                                                                                                |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Reset**](iinertiaprocessor-reset.md)               | Initializes the processor with initial time stamp and restarts inertia.                                                                                                                                                    |
| [**Process**](iinertiaprocessor-process.md)           | Performs calculations for the current tick and can raise the **Delta** or **Completed** event depending on whether extrapolation is completed or not. If extrapolation finished at the previous tick, the method is no-op. |
| [**ProcessTime**](iinertiaprocessor-processtime.md)   | Performs calculations for the given tick and can raise the **Delta** or **Completed** event depending on whether extrapolation is completed or not.                                                                        |
| [**Complete**](iinertiaprocessor-complete.md)         | Finishes the current manipulation and stops inertia on the inertia processor.                                                                                                                                              |
| [**CompleteTime**](iinertiaprocessor-completetime.md) | Finishes the current manipulation at the given tick, stops inertia on the inertia processor, and raises the ManipulationCompleted event.                                                                                   |



 

## Related topics

<dl> <dt>

[**IInertiaProcessor**](iinertiaprocessor.md)
</dt> </dl>

 

 




