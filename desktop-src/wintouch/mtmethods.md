---
title: Methods
description: This section contains the methods for the IManipulationProcessor interface.
ms.assetid: 33736f79-cb61-449c-80b9-1358db2621e9
keywords:
- Windows Touch,IManipulationProcessor interface
- Windows Touch,interface methods
- manipulations,IManipulationProcessor interface
- IManipulationProcessor interface,methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Methods

This section contains the methods for the [**IManipulationProcessor**](/windows/win32/manipulations/nn-manipulations-imanipulationprocessor?branch=master) interface.

The following methods are exposed by the [**IManipulationProcessor**](/windows/win32/manipulations/nn-manipulations-imanipulationprocessor?branch=master) interface.



| Method                                                                      | Description                                                                              |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**CompleteManipulation**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-completemanipulation?branch=master) | This method is called when the developer chooses to end the manipulation.                |
| [**GetAngularVelocity**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-getangularvelocity?branch=master)     | Calculates the rotational velocity that the target object is moving at.                  |
| [**GetExpansionVelocity**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-getexpansionvelocity?branch=master) | Calculates the rate that the target object is expanding at.                              |
| [**GetVelocityX**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-getvelocityx?branch=master)                 | Calculates and returns the horizontal velocity for the target object.                    |
| [**GetVelocityY**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-getvelocityy?branch=master)                 | Calculates and returns the vertical velocity.                                            |
| [**ProcessDown**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-processdown?branch=master)                   | Feeds data to the manipulation processor associated with a target.                       |
| [**ProcessMove**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-processmove?branch=master)                   | Feeds data to the manipulation processor associated with a target.                       |
| [**ProcessUp**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-processup?branch=master)                       | Feeds data to the manipulation processor associated with a target.                       |
| [**ProcessDownWithTime**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-processdownwithtime?branch=master)   | Feeds data including a timestamp to the manipulation processor associated with a target. |
| [**ProcessMoveWithTime**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-processmovewithtime?branch=master)   | Feeds data including a timestamp to the manipulation processor associated with a target. |
| [**ProcessUpWithTime**](/windows/win32/manipulations/nf-manipulations-imanipulationprocessor-processupwithtime?branch=master)       | Feeds data including a timestamp to the manipulation processor associated with a target. |



 

## Related topics

<dl> <dt>

[**IManipulationProcessor**](/windows/win32/manipulations/nn-manipulations-imanipulationprocessor?branch=master)
</dt> </dl>

 

 




