---
title: Transition Interfaces
description: This section contains the reference specifications for the Windows Animation Manager interfaces that support transitions.
ms.assetid: '581C853D-F213-4227-AC61-4ED2E5D4EF04'
---

# Transition Interfaces

This section contains the reference specifications for the Windows Animation Manager interfaces that support transitions.

## In this section



| Topic                                                                                                     | Description                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUIAnimationInterpolator**](iuianimationinterpolator.md)<br/>                                   | Defines methods for creating a custom interpolator.<br/>                                                                                                                                                                                                             |
| [**IUIAnimationInterpolator2**](iuianimationinterpolator2.md)<br/>                                 | Extends the [**IUIAnimationInterpolator**](iuianimationinterpolator.md) interface that defines methods for creating a custom interpolator. [**IUIAnimationInterpolator2**](iuianimationinterpolator2.md) supports interpolation in a given dimension. <br/>        |
| [**IUIAnimationPrimitiveInterpolation**](iuianimationprimitiveinterpolation.md)<br/>               | Defines a method that allows a custom interpolator to provide transition information, in the form of a cubic polynomial curve, to the animation manager.<br/>                                                                                                        |
| [**IUIAnimationTransition**](iuianimationtransition.md)<br/>                                       | Defines a transition, which determines how an animation variable changes over time.<br/>                                                                                                                                                                             |
| [**IUIAnimationTransition2**](iuianimationtransition2.md)<br/>                                     | Extends the [**IUIAnimationTransition**](iuianimationtransition.md) interface that defines a transition. An [**IUIAnimationTransition2**](iuianimationtransition2.md) transition determines how an animation variable changes over time in a given dimension.<br/> |
| [**IUIAnimationTransitionFactory**](iuianimationtransitionfactory.md)<br/>                         | Defines a method for creating transitions from custom interpolators.<br/>                                                                                                                                                                                            |
| [**IUIAnimationTransitionFactory2**](iuianimationtransitionfactory2.md)<br/>                       | Defines a method for creating transitions from custom interpolators.<br/>                                                                                                                                                                                            |
| [**IUIAnimationTransitionLibrary**](iuianimationtransitionlibrary.md)<br/>                         | Defines a library of standard transitions. <br/>                                                                                                                                                                                                                     |
| [**IUIAnimationTransitionLibrary2**](iuianimationtransitionlibrary2.md)<br/>                       | Defines a library of standard transitions for a specified dimension.<br/>                                                                                                                                                                                            |
| [**IUIAnimationVariable**](iuianimationvariable.md)<br/>                                           | Defines an animation variable, which represents a visual element that can be animated.<br/>                                                                                                                                                                          |
| [**IUIAnimationVariable2**](iuianimationvariable2.md)<br/>                                         | Defines an animation variable, which represents a visual element that can be animated in multiple dimensions.<br/>                                                                                                                                                   |
| [**IUIAnimationVariableChangeHandler**](iuianimationvariablechangehandler.md)<br/>                 | Defines a method for handling events related to animation variable updates.<br/>                                                                                                                                                                                     |
| [**IUIAnimationVariableChangeHandler2**](iuianimationvariablechangehandler2.md)<br/>               | Defines a method for handling animation variable update events. [**IUIAnimationVariableChangeHandler2**](iuianimationvariablechangehandler2.md) handles events that occur in a specified dimension.<br/>                                                            |
| [**IUIAnimationVariableIntegerChangeHandler**](iuianimationvariableintegerchangehandler.md)<br/>   | Defines a method for handling animation variable update events.<br/>                                                                                                                                                                                                 |
| [**IUIAnimationVariableIntegerChangeHandler2**](iuianimationvariableintegerchangehandler2.md)<br/> | Defines a method for handling animation variable update events. [**IUIAnimationVariableIntegerChangeHandler2**](iuianimationvariableintegerchangehandler2.md) handles events that occur in a specified dimension.<br/>                                              |
| [**IUIAnimationVariableCurveChangeHandler2**](iuianimationvariablecurvechangehandler2.md)<br/>     | Defines a method for handling animation curve update events. <br/>                                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Interfaces](windows-animation-reference.md)
</dt> </dl>

 

 





