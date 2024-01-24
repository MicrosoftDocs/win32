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
ms.topic: article
ms.date: 02/06/2020
---

# Interaction Context Functions

The topics in this section provide the reference specifications for [Interaction Context](interaction-context-portal.md) functions.

## In this section

| Topic | Description |
|---|---|
| [**AddPointerInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-addpointerinteractioncontext)<br/> | Include the specified pointer in the set of pointers processed by the [Interaction Context](interaction-context-portal.md) object. <br/> |
| [**BufferPointerPacketsInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-bufferpointerpacketsinteractioncontext)<br/> | Adds the history for a single input pointer to the buffer of the [Interaction Context](interaction-context-portal.md) object.<br/> |
| [**CreateInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-createinteractioncontext)<br/> | Creates and initializes an [Interaction Context](interaction-context-portal.md) object.<br/> |
| [**DestroyInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-destroyinteractioncontext)<br/> | Destroys the specified [Interaction Context](interaction-context-portal.md) object.<br/> |
| [**GetCrossSlideParameterInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-getcrossslideparameterinteractioncontext)<br/> | Gets the cross-slide interaction behavior. <br/> |
| [**GetInertiaParameterInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-getinertiaparameterinteractioncontext)<br/> | Gets the inertia behavior of a manipulation (translation, rotation, scaling). <br/> |
| [**GetInteractionConfigurationInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-getinteractionconfigurationinteractioncontext)<br/> | Gets interaction configuration state for the [Interaction Context](interaction-context-portal.md) object.<br/> |
| [**GetMouseWheelParameterInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-getmousewheelparameterinteractioncontext)<br/> | Gets the mouse wheel state for the [Interaction Context](interaction-context-portal.md) object. <br/> |
| [**GetPropertyInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-getpropertyinteractioncontext)<br/> | Gets [Interaction Context](interaction-context-portal.md) object properties.<br/> |
| [**GetStateInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-getstateinteractioncontext)<br/> | Gets current [Interaction Context](interaction-context-portal.md) state and the time when the context will return to idle state. <br/> |
| [**ProcessBufferedPacketsInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-processbufferedpacketsinteractioncontext)<br/> | Process buffered packets at the end of a pointer input frame.<br/> |
| [**ProcessInertiaInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-processinertiainteractioncontext)<br/> | Sends timer input to the [Interaction Context](interaction-context-portal.md) object for inertia processing.<br/> |
| [**ProcessPointerFramesInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-processpointerframesinteractioncontext)<br/> | Processes a set of pointer input frames.<br/> |
| [**RegisterOutputCallbackInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-registeroutputcallbackinteractioncontext)<br/> | Registers a callback to receive interaction events from an [Interaction Context](interaction-context-portal.md) object.<br/> |
| [**RemovePointerInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-removepointerinteractioncontext)<br/> | Remove the specified pointer from the set of pointers processed by the [Interaction Context](interaction-context-portal.md) object. <br/> |
| [**ResetInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-resetinteractioncontext)<br/> | Resets the [**interaction state**](/windows/win32/api/interactioncontext/ne-interactioncontext-interaction_state), interaction configuration settings, and all parameters to their initial state. Current interactions are cancelled without notifications. <br/> [Interaction Context](interaction-context-portal.md) must be reconfigured before next use.<br/> |
| [**SetCrossSlideParametersInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-setcrossslideparametersinteractioncontext)<br/> | Configures the cross-slide interaction. <br/> |
| [**SetInertiaParameterInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-setinertiaparameterinteractioncontext)<br/> | Configures the inertia behavior of a manipulation (translation, rotation, scaling) after the contact is lifted. <br/> | 
| [**SetInteractionConfigurationInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-setinteractionconfigurationinteractioncontext)<br/> | Configures the [Interaction Context](interaction-context-portal.md) object to process the specified manipulations.<br/> |
| [**SetMouseWheelParameterInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-setmousewheelparameterinteractioncontext)<br/> | Sets the parameter values for mouse wheel input. <br/> |
| [**SetPivotInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-setpivotinteractioncontext)<br/> | Sets the center point, and the pivot radius from the center point, for a rotation manipulation using a single input pointer. <br/> |
| [**SetPropertyInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-setpropertyinteractioncontext)<br/> | Sets [Interaction Context](interaction-context-portal.md) object properties.<br/> |
| [**StopInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-stopinteractioncontext)<br/> | Sets the [**interaction state**](/windows/win32/api/interactioncontext/ne-interactioncontext-interaction_state) to INTERACTION\_STATE\_IDLE and leaves all interaction configuration settings and parameters intact. Current interactions are cancelled and notifications sent as required.<br/> [Interaction Context](interaction-context-portal.md) does not have to be reconfigured before next use.<br/> |

## Related topics

[Interaction Context Reference](interaction-context-reference.md)
