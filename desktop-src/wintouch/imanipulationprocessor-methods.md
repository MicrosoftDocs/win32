---
title: Methods
description: This section contains the methods for the IInertiaProcessor interface.
ms.assetid: e4acfcac-06c1-42a5-9722-4534a4492ab8
keywords:
- Windows Touch,IInertiaProcessor interface
- Windows Touch,interface methods
- inertia,IInertiaProcessor interface
- IInertiaProcessor interface,methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Methods

This section contains the methods for the [**IInertiaProcessor**](/windows/win32/manipulations/nn-manipulations-iinertiaprocessor?branch=master) interface.



| Method                                                 | Description                                                                                                                                                                                                                |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Reset**](/windows/win32/manipulations/nf-manipulations-iinertiaprocessor-reset?branch=master)               | Initializes the processor with initial time stamp and restarts inertia.                                                                                                                                                    |
| [**Process**](/windows/win32/manipulations/nf-manipulations-iinertiaprocessor-process?branch=master)           | Performs calculations for the current tick and can raise the **Delta** or **Completed** event depending on whether extrapolation is completed or not. If extrapolation finished at the previous tick, the method is no-op. |
| [**ProcessTime**](/windows/win32/manipulations/nf-manipulations-iinertiaprocessor-processtime?branch=master)   | Performs calculations for the given tick and can raise the **Delta** or **Completed** event depending on whether extrapolation is completed or not.                                                                        |
| [**Complete**](/windows/win32/manipulations/nf-manipulations-iinertiaprocessor-complete?branch=master)         | Finishes the current manipulation and stops inertia on the inertia processor.                                                                                                                                              |
| [**CompleteTime**](/windows/win32/manipulations/nf-manipulations-iinertiaprocessor-completetime?branch=master) | Finishes the current manipulation at the given tick, stops inertia on the inertia processor, and raises the ManipulationCompleted event.                                                                                   |



 

## Related topics

<dl> <dt>

[**IInertiaProcessor**](/windows/win32/manipulations/nn-manipulations-iinertiaprocessor?branch=master)
</dt> </dl>

 

 




