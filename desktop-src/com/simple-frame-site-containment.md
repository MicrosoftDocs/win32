---
title: Simple Frame Site Containment
description: Simple Frame Site Containment
ms.assetid: 85c3565f-f557-43af-8d36-58414d0790cd
ms.topic: article
ms.date: 05/31/2018
---

# Simple Frame Site Containment

A container control is an ActiveX control that is capable of containing other controls. A group box that contains a collection of radio buttons is an example of a container control. Container controls should set the OLEMISC\_SIMPLEFRAME status bit, and should call its container's [**ISimpleFrameSite**](/windows/desktop/api/OCIdl/nn-ocidl-isimpleframesite) implementation. An ActiveX control container that supports container controls must implement **ISimpleFrameSite**.

CATID - {157083E0-2368-11cf-87B9-00AA006C8166} CATID\_SimpleFrameControl

## Related topics

<dl> <dt>

[Component Categories](component-categories.md)
</dt> </dl>

 

 




