---
title: Visual Basic Private Interfaces
description: Visual Basic Private Interfaces
ms.assetid: 782e5d87-680e-4d0c-b1e6-cf97d1a37ce5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Visual Basic Private Interfaces

Two interfaces that are implemented by Visual Basic are identified here for component categories. It is not expected that controls should require these categories because it is possible for controls to offer alternative functionality when these are not available.

The [**IVBFormat**](/windows/win32/VbInterf/nn-vbinterf-ivbformat?branch=master) interface allows controls to better integrate into the Visual Basic environment when formatting data.

CATID - {02496840-3AC4-11cf-87B9-00AA006C8166} CATID\_VBFormat

The [**IVBGetControl**](/windows/win32/VbInterf/nn-vbinterf-ivbgetcontrol?branch=master) interface allows a control to enumerate other controls on the VB form.

CATID - {02496841-3AC4-11cf-87B9-00AA006C8166} CATID\_VBGetControl

Two additional private interfaces, [**IGetVBAObject**](/windows/win32/VbInterf/nn-vbinterf-igetvbaobject?branch=master) and [**IGetOleObject**](/windows/win32/VbInterf/nn-vbinterf-igetoleobject?branch=master), are described here even though they do not define component categories. Use of these four interfaces is not recommended because they are not supported by containers other than Visual Basic.

## Related topics

<dl> <dt>

[Component Categories](component-categories.md)
</dt> </dl>

 

 




