---
title: Container-Specific Private Interfaces
description: Container-Specific Private Interfaces
ms.assetid: 429cf71c-9b9d-4d0b-b5de-91fbe1dde3cf
ms.topic: article
ms.date: 05/31/2018
---

# Container-Specific Private Interfaces

Some containers provide container-specific private interfaces for additional functionality or improved performance. Controls that rely on those container-specific interfaces should, if possible, work without those container-specific interfaces present so that the control functions in different containers. For example, Visual Basic implements private interfaces that provide string formatting functionality to controls. If a control makes use of these private formatting interfaces, it should be able to run with default formatting support if these interfaces are not available. If the control can function without the private interfaces, it should take appropriate action (such as warn the user of reduced functionality) but continue to work. If this is not an option, a component category should be registered as required so that only containers supporting this functionality can host these controls.

 

 




