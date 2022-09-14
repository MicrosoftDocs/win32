---
title: Automatic Clipping
description: Automatic Clipping
ms.assetid: 9107ee47-52aa-48c8-b141-c821f93fda45
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Clipping

It is strongly recommended that an ActiveX control container supports automatic clipping of its controls. This will result in more efficient operation for most controls. If automatic clipping is supported, the AutoClip ambient property must be supported and have a value of **TRUE**.

Automatic clipping is the ability of a container to ensure that a control's drawn output goes only to the container's current clipping region. In a container that supports automatic clipping, a control can paint without regard to its clipping region, because the container will automatically clip any painting that occurs outside the control's area. If a container does not support automatic clipping, then CDK-generated controls will create an extra parent window if a non-null clipping region is passed.

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

 




