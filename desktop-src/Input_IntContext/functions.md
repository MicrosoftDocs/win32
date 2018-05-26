---
title: Interaction Context Functions
description: The topics in this section provide the reference specifications for Interaction Context functions.
ms.assetid: 0F34F181-D92C-4B08-9F1D-62379D4A2B15
keywords:
- user interaction
- input
- pointer
- touch
- mouse
- pen
- stylus
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interaction Context Functions

The topics in this section provide the reference specifications for [Interaction Context](interaction-context-portal.md) functions.

## In this section



| Topic                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddPointerInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-addpointerinteractioncontext?branch=master)<br/>                                   | Include the specified pointer in the set of pointers processed by the [Interaction Context](interaction-context-portal.md) object. <br/>                                                                                                                                                                                                                   |
| [**BufferPointerPacketsInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-bufferpointerpacketsinteractioncontext?branch=master)<br/>               | Adds the history for a single input pointer to the buffer of the [Interaction Context](interaction-context-portal.md) object.<br/>                                                                                                                                                                                                                         |
| [**CreateInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-createinteractioncontext?branch=master)<br/>                                           | Creates and initializes an [Interaction Context](interaction-context-portal.md) object.<br/>                                                                                                                                                                                                                                                               |
| [**DestroyInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-destroyinteractioncontext?branch=master)<br/>                                         | Destroys the specified [Interaction Context](interaction-context-portal.md) object.<br/>                                                                                                                                                                                                                                                                   |
| [**GetCrossSlideParameterInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-getcrossslideparameterinteractioncontext?branch=master)<br/>           | Gets the cross-slide interaction behavior. <br/>                                                                                                                                                                                                                                                                                                            |
| [**GetInertiaParameterInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-getinertiaparameterinteractioncontext?branch=master)<br/>                 | Gets the inertia behavior of a manipulation (translation, rotation, scaling). <br/>                                                                                                                                                                                                                                                                         |
| [**GetInteractionConfigurationInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-getinteractionconfigurationinteractioncontext?branch=master)<br/> | Gets interaction configuration state for the [Interaction Context](interaction-context-portal.md) object.<br/>                                                                                                                                                                                                                                             |
| [**GetMouseWheelParameterInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-getmousewheelparameterinteractioncontext?branch=master)<br/>           | Gets the mouse wheel state for the [Interaction Context](interaction-context-portal.md) object. <br/>                                                                                                                                                                                                                                                      |
| [**GetPropertyInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-getpropertyinteractioncontext?branch=master)<br/>                                 | Gets [Interaction Context](interaction-context-portal.md) object properties.<br/>                                                                                                                                                                                                                                                                          |
| [**GetStateInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-getstateinteractioncontext?branch=master)<br/>                                       | Gets current [Interaction Context](interaction-context-portal.md) state and the time when the context will return to idle state. <br/>                                                                                                                                                                                                                     |
| [**ProcessBufferedPacketsInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-processbufferedpacketsinteractioncontext?branch=master)<br/>           | Process buffered packets at the end of a pointer input frame.<br/>                                                                                                                                                                                                                                                                                          |
| [**ProcessInertiaInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-processinertiainteractioncontext?branch=master)<br/>                           | Sends timer input to the [Interaction Context](interaction-context-portal.md) object for inertia processing.<br/>                                                                                                                                                                                                                                          |
| [**ProcessPointerFramesInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-processpointerframesinteractioncontext?branch=master)<br/>               | Processes a set of pointer input frames.<br/>                                                                                                                                                                                                                                                                                                               |
| [**RegisterOutputCallbackInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-registeroutputcallbackinteractioncontext?branch=master)<br/>           | Registers a callback to receive interaction events from an [Interaction Context](interaction-context-portal.md) object.<br/>                                                                                                                                                                                                                               |
| [**RemovePointerInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-removepointerinteractioncontext?branch=master)<br/>                             | Remove the specified pointer from the set of pointers processed by the [Interaction Context](interaction-context-portal.md) object. <br/>                                                                                                                                                                                                                  |
| [**ResetInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-resetinteractioncontext?branch=master)<br/>                                             | Resets the [**interaction state**](/windows/previous-versions/interactioncontext/ne-interactioncontext-interaction_state?branch=master), interaction configuration settings, and all parameters to their initial state. Current interactions are cancelled without notifications. <br/> [Interaction Context](interaction-context-portal.md) must be reconfigured before next use.<br/>                                            |
| [**SetCrossSlideParametersInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-setcrossslideparametersinteractioncontext?branch=master)<br/>         | Configures the cross-slide interaction. <br/>                                                                                                                                                                                                                                                                                                               |
| [**SetInertiaParameterInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-setinertiaparameterinteractioncontext?branch=master)<br/>                 | Configures the inertia behavior of a manipulation (translation, rotation, scaling) after the contact is lifted. <br/>                                                                                                                                                                                                                                       |
| [**SetInteractionConfigurationInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-setinteractionconfigurationinteractioncontext?branch=master)<br/> | Configures the [Interaction Context](interaction-context-portal.md) object to process the specified manipulations.<br/>                                                                                                                                                                                                                                    |
| [**SetMouseWheelParameterInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-setmousewheelparameterinteractioncontext?branch=master)<br/>           | Sets the parameter values for mouse wheel input. <br/>                                                                                                                                                                                                                                                                                                      |
| [**SetPivotInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-setpivotinteractioncontext?branch=master)<br/>                                       | Sets the center point, and the pivot radius from the center point, for a rotation manipulation using a single input pointer. <br/>                                                                                                                                                                                                                          |
| [**SetPropertyInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-setpropertyinteractioncontext?branch=master)<br/>                                 | Sets [Interaction Context](interaction-context-portal.md) object properties.<br/>                                                                                                                                                                                                                                                                          |
| [**StopInteractionContext**](/windows/previous-versions/interactioncontext/nf-interactioncontext-stopinteractioncontext?branch=master)<br/>                                               | Sets the [**interaction state**](/windows/previous-versions/interactioncontext/ne-interactioncontext-interaction_state?branch=master) to INTERACTION\_STATE\_IDLE and leaves all interaction configuration settings and parameters intact. Current interactions are cancelled and notifications sent as required.<br/> [Interaction Context](interaction-context-portal.md) does not have to be reconfigured before next use.<br/> |



 

## Related topics

<dl> <dt>

[Interaction Context Reference](interaction-context-reference.md)
</dt> </dl>

 

 





