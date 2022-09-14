---
title: Interaction with WinEvents
description: The Dynamic Annotation run time will not send WinEvents; it is the annotator's responsibility to send appropriate events, when necessary. If you need to send WinEvents, be sure to send them after the annotation has taken place.
ms.assetid: 657a540b-8838-4d2e-ade6-c4fa1ad08e21
ms.topic: article
ms.date: 05/31/2018
---

# Interaction with WinEvents

The Dynamic Annotation run time will not send [WinEvents](winevents-infrastructure.md); it is the annotator's responsibility to send appropriate events, when necessary. If you need to send WinEvents, be sure to send them after the annotation has taken place.

For example, if you use [**IAccPropServices::SetPropValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-setpropvalue) to set the [**Name**](name-property.md) property of an element, send an [**EVENT\_OBJECT\_NAMECHANGE**](event-constants.md) event for that object after **SetPropValue** returns.

However, if you use [**IAccPropServices::SetPropValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-setpropvalue) to set the ValueMap for a slider, no events are required because setting the ValueMap does not change the slider's value.

 

 




