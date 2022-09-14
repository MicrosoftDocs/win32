---
title: Windows Animation Tasks
description: The topics contained in this section describe the basic tasks required of applications that use Windows Animation Manager.
ms.assetid: 28103e5e-f00a-4ff5-820b-ece24a7ef21a
keywords:
- Windows Animation Windows Animation ,tasks
ms.topic: article
ms.date: 05/31/2018
---

# Windows Animation Tasks

The topics contained in this section describe the basic tasks required of applications that use Windows Animation Manager.

These tasks, in order, include:

## In this section



| Topic                                                                                                | Description                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Create the Main Animation Objects](adding-animation-to-an-application.md)<br/>               | To use Windows Animation in your application, the first step is to create a small set of main animation objects.<br/>                                                                                                                                                                           |
| [Create Animation Variables](create-animation-variables.md)<br/>                              | An application must create an animation variable for each visual characteristic that is to be animated using Windows Animation.<br/>                                                                                                                                                            |
| [Update the Animation Manager and Draw Frames](introducing-windows-animation-manager.md)<br/> | Each time an application schedules a storyboard, the application must supply the current time to the animation manager. The current time is also required when directing the animation manager to update its state and set all animation variables to the appropriate interpolated values.<br/> |
| [Read the Animation Variable Values](updating---application-driven-animation.md)<br/>         | Each time your application paints, it should read the current values of the animation variables that represent the visual characteristics to be animated.<br/>                                                                                                                                  |
| [Create a Storyboard and Add Transitions](updating---timer-driven-animation.md)<br/>          | To create an animation, an application must construct a storyboard.<br/>                                                                                                                                                                                                                        |
| [Schedule a Storyboard](scheduling-a-storyboard.md)<br/>                                      | After a storyboard is created, it is scheduled by the animation manager.<br/>                                                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Windows Animation Overview](scenic-animation-api-overview.md)
</dt> <dt>

[Windows Animation Reference](windows-animation-reference.md)
</dt> <dt>

[Windows Animation Samples](windows-animation-samples.md)
</dt> </dl>

 

 





