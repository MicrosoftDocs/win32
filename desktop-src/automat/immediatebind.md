---
title: immediatebind
description: Allows individual bindable properties on a form to specify this behavior. When this bit is set, all changes will be notified.
ms.assetid: 304b3c85-d477-410d-829f-fe6a4f3cb1b0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# immediatebind

Allows individual bindable properties on a form to specify this behavior. When this bit is set, all changes will be notified.

## Flags

<dl> VARFLAG\_FIMMEDIATEBIND  
FUNCFLAG\_FIMMEDIATEBIND  
</dl>

## Remarks

Allows controls to differentiate two different types of bindable properties. One type of bindable property needs to notify every change to the database (for example, with a check box control where every change needs to be sent through to the underlying database, even though the control has not lost the focus). However, controls such as a list box need to have the change of a property communicated to the database when the control loses focus, because the user may have changed the selection with the arrow keys before finding the desired setting. If the change notification was sent to the database every time the user pressed an arrow key, it would give an unacceptable performance.

The [bindable](bindable.md) and [requestedit](requestedit.md) attribute bits need to be set for this new bit to have an effect.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




