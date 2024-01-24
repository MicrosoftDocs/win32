---
title: Properties (IInertiaProcessor)
description: This section contains the properties for the IInertiaProcessor interface.
ms.assetid: 47fd1a49-8e14-4076-8ce6-f0c4917e8cf1
keywords:
- Windows Touch,IInertiaProcessor interface
- Windows Touch,interface properties
- inertia,IInertiaProcessor interface
- IInertiaProcessor interface,properties
ms.topic: article
ms.date: 05/31/2018
---

# Properties (IInertiaProcessor)

This section contains the properties for the [**IInertiaProcessor**](/windows/desktop/api/manipulations/nn-manipulations-iinertiaprocessor) interface.



| Property                                                                               | Desription                                                                                               |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**InitialOriginX**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_initialoriginx)                             | Specifies the starting horizontal location for a target with intertia.                                   |
| [**InitialOriginY**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_initialoriginy)                             | Specifies the starting vertical location for a target with intertia.                                     |
| [**InitialVelocityX**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_initialvelocityx)                         | Specifies the initial movement of the target object on the horizontal axis.                              |
| [**InitialVelocityY**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_initialvelocityy)                         | Specifies the initial movement of the target object on the vertical axis.                                |
| [**InitialAngularVelocity**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_initialangularvelocity)             | Specifies the rotational velocity of the target when movement begins.                                    |
| [**InitialExpansionVelocity**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_initialexpansionvelocity)         | Specifies the rate of radius expansion of the target when movement begins.                               |
| [**InitialRadius**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_initialradius)                               | Specifies the distance from the edge of the target to its center before the object was changed.          |
| [**BoundaryLeft**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_boundaryleft)                                 | Limits how far toward the left of the screen the target object can move.                                 |
| [**BoundaryTop**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_boundarytop)                                   | Limits how far toward the top of the screen the target object can move.                                  |
| [**BoundaryRight**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_boundaryright)                               | Limits how far toward the right side of the screen the target object can move.                           |
| [**BoundaryBottom**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_boundarybottom)                             | Limits how far toward the bottom of the screen the target object can move.                               |
| [**ElasticMarginLeft**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_elasticmarginleft)                       | Specifies the leftmost region for bouncing the target object.                                            |
| [**ElasticMarginTop**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_elasticmargintop)                         | Specifies the topmost region for bouncing the target object.                                             |
| [**ElasticMarginRight**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_elasticmarginright)                     | Specifies the rightmost region for bouncing the target object.                                           |
| [**ElasticMarginBottom**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_elasticmarginbottom)                   | Specifies the bottom region for bouncing the target object.                                              |
| [**DesiredAngularDeceleration**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_desiredangulardeceleration)     | Specifies the desired rate that the target object will stop spinning in radians per msec.                |
| [**DesiredRotation**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_desiredrotation)                           | Specifies the desired distance (in radians) that an object will be manipulated by the inertia processor. |
| [**DesiredExpansion**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_desiredexpansion)                         | Specifies the desired change in the average radius of the object.                                        |
| [**DesiredExpansionDeceleration**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_desiredexpansiondeceleration) | Specifies the rate at which the object will stop expanding.                                              |
| [**DesiredDeceleration**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_desireddeceleration)                   | Specifies the desired rate at which translation operations will decelerate.                              |
| [**DesiredDisplacement**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_desireddisplacement)                   | Specifies the desired distance that the object will travel.                                              |
| [**InitialTimestamp**](/windows/desktop/api/manipulations/nf-manipulations-iinertiaprocessor-get_initialtimestamp)                         | Specifies the starting time stamp for a target object that has inertia.                                  |



 

## Related topics

<dl> <dt>

[**IInertiaProcessor**](/windows/desktop/api/manipulations/nn-manipulations-iinertiaprocessor)
</dt> </dl>

 

 




