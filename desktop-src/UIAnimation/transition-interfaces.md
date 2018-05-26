---
title: Transition Interfaces
description: This section contains the reference specifications for the Windows Animation Manager interfaces that support transitions.
ms.assetid: 581C853D-F213-4227-AC61-4ED2E5D4EF04
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Transition Interfaces

This section contains the reference specifications for the Windows Animation Manager interfaces that support transitions.

## In this section



| Topic                                                                                                     | Description                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUIAnimationInterpolator**](/windows/win32/UIAnimation/nn-uianimation-iuianimationinterpolator?branch=master)<br/>                                   | Defines methods for creating a custom interpolator.<br/>                                                                                                                                                                                                             |
| [**IUIAnimationInterpolator2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationinterpolator2?branch=master)<br/>                                 | Extends the [**IUIAnimationInterpolator**](/windows/win32/UIAnimation/nn-uianimation-iuianimationinterpolator?branch=master) interface that defines methods for creating a custom interpolator. [**IUIAnimationInterpolator2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationinterpolator2?branch=master) supports interpolation in a given dimension. <br/>        |
| [**IUIAnimationPrimitiveInterpolation**](/windows/win32/UIAnimation/nn-uianimation-iuianimationprimitiveinterpolation?branch=master)<br/>               | Defines a method that allows a custom interpolator to provide transition information, in the form of a cubic polynomial curve, to the animation manager.<br/>                                                                                                        |
| [**IUIAnimationTransition**](/windows/win32/UIAnimation/nn-uianimation-iuianimationtransition?branch=master)<br/>                                       | Defines a transition, which determines how an animation variable changes over time.<br/>                                                                                                                                                                             |
| [**IUIAnimationTransition2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationtransition2?branch=master)<br/>                                     | Extends the [**IUIAnimationTransition**](/windows/win32/UIAnimation/nn-uianimation-iuianimationtransition?branch=master) interface that defines a transition. An [**IUIAnimationTransition2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationtransition2?branch=master) transition determines how an animation variable changes over time in a given dimension.<br/> |
| [**IUIAnimationTransitionFactory**](/windows/win32/UIAnimation/nn-uianimation-iuianimationtransitionfactory?branch=master)<br/>                         | Defines a method for creating transitions from custom interpolators.<br/>                                                                                                                                                                                            |
| [**IUIAnimationTransitionFactory2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationtransitionfactory2?branch=master)<br/>                       | Defines a method for creating transitions from custom interpolators.<br/>                                                                                                                                                                                            |
| [**IUIAnimationTransitionLibrary**](/windows/win32/UIAnimation/nn-uianimation-iuianimationtransitionlibrary?branch=master)<br/>                         | Defines a library of standard transitions. <br/>                                                                                                                                                                                                                     |
| [**IUIAnimationTransitionLibrary2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationtransitionlibrary2?branch=master)<br/>                       | Defines a library of standard transitions for a specified dimension.<br/>                                                                                                                                                                                            |
| [**IUIAnimationVariable**](/windows/win32/UIAnimation/nn-uianimation-iuianimationvariable?branch=master)<br/>                                           | Defines an animation variable, which represents a visual element that can be animated.<br/>                                                                                                                                                                          |
| [**IUIAnimationVariable2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationvariable2?branch=master)<br/>                                         | Defines an animation variable, which represents a visual element that can be animated in multiple dimensions.<br/>                                                                                                                                                   |
| [**IUIAnimationVariableChangeHandler**](/windows/win32/UIAnimation/nn-uianimation-iuianimationvariablechangehandler?branch=master)<br/>                 | Defines a method for handling events related to animation variable updates.<br/>                                                                                                                                                                                     |
| [**IUIAnimationVariableChangeHandler2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationvariablechangehandler2?branch=master)<br/>               | Defines a method for handling animation variable update events. [**IUIAnimationVariableChangeHandler2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationvariablechangehandler2?branch=master) handles events that occur in a specified dimension.<br/>                                                            |
| [**IUIAnimationVariableIntegerChangeHandler**](/windows/win32/UIAnimation/nn-uianimation-iuianimationvariableintegerchangehandler?branch=master)<br/>   | Defines a method for handling animation variable update events.<br/>                                                                                                                                                                                                 |
| [**IUIAnimationVariableIntegerChangeHandler2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationvariableintegerchangehandler2?branch=master)<br/> | Defines a method for handling animation variable update events. [**IUIAnimationVariableIntegerChangeHandler2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationvariableintegerchangehandler2?branch=master) handles events that occur in a specified dimension.<br/>                                              |
| [**IUIAnimationVariableCurveChangeHandler2**](/windows/win32/UIAnimation/nn-uianimation-iuianimationvariablecurvechangehandler2?branch=master)<br/>     | Defines a method for handling animation curve update events. <br/>                                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Interfaces](windows-animation-reference.md)
</dt> </dl>

 

 





