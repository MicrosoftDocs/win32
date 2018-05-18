---
title: Interaction with WinEvents
description: The Dynamic Annotation run time will not send WinEvents; it is the annotator's responsibility to send appropriate events, when necessary. If you need to send WinEvents, be sure to send them after the annotation has taken place.
ms.assetid: '657a540b-8838-4d2e-ade6-c4fa1ad08e21'
---

# Interaction with WinEvents

The Dynamic Annotation run time will not send [WinEvents](winevents-collision169.md); it is the annotator's responsibility to send appropriate events, when necessary. If you need to send WinEvents, be sure to send them after the annotation has taken place.

For example, if you use [**IAccPropServices::SetPropValue**](iaccpropservices-iaccpropservices--setpropvalue.md) to set the [**Name**](name-property.md) property of an element, send an [**EVENT\_OBJECT\_NAMECHANGE**](event-constants.md#event-object-namechange) event for that object after **SetPropValue** returns.

However, if you use [**IAccPropServices::SetPropValue**](iaccpropservices-iaccpropservices--setpropvalue.md) to set the ValueMap for a slider, no events are required because setting the ValueMap does not change the slider's value.

 

 




