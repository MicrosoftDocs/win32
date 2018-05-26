---
title: Registration Functions
description: These functions let you identify a running instance of an object. Because they use the OLE object table (GetRunningObjectTable), they also require Ole32.dll.
ms.assetid: f352c885-8373-413a-bb1f-fb22bd318786
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Registration Functions

These functions let you identify a running instance of an object. Because they use the OLE object table (**GetRunningObjectTable**), they also require Ole32.dll.

When an application is started with the **/Automation** switch, it should initialize its Application object as the active object by calling [**RegisterActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-registeractiveobject?branch=master) after it initializes OLE.

Applications can also register other top-level objects as the active object. For example, an application that exposes a Document object may want to let ActiveX clients retrieve and modify the currently active document.

For more information about registering the active object see [Exposing ActiveX Objects](exposing-activex-objects.md).

## In this section



| Topic                                                           | Description                                                                           |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**GetActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-getactiveobject?branch=master)<br/>           | Retrieves a pointer to a running object that has been registered with OLE.<br/> |
| [**RegisterActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-registeractiveobject?branch=master)<br/> | Registers an object as the active object for its class.<br/>                    |
| [**RevokeActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-revokeactiveobject?branch=master)<br/>     | Ends an object's status as active.<br/>                                         |



 

 

 





