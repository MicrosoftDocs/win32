---
title: Message Reflection
description: Message Reflection
ms.assetid: 26a124d7-6499-4e8f-9001-d2782c1cc290
ms.topic: article
ms.date: 05/31/2018
---

# Message Reflection

It is strongly recommended that an ActiveX control container supports message reflection. This will result in more efficient operation for subclassed controls. If message reflection is supported, the MessageReflect ambient property must be supported and have a value of **TRUE**. If a container does not implement message reflection, then the OLE CDK creates two windows for every subclassed control, to provide message reflection on behalf on the control container.

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

 




