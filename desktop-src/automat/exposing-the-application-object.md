---
title: Exposing the Application Object
description: The Application object identifies the application and provides a way for ActiveX clients to bind to and navigate the application's exposed objects.
ms.assetid: 2eaf4b6f-300d-4697-aeaf-28078e5cdf75
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Exposing the Application Object

Any document-based, user-interactive applications that expose ActiveX objects should have one top-level object named the Application object. This object is initialized as the active object when an application starts.

The Application object identifies the application and provides a way for ActiveX clients to bind to and navigate the application's exposed objects. All other exposed objects are subordinate to the Application object; it is the root-level object in the object hierarchy.

The names of the Application object's members are part of the global name space, so ActiveX clients do not need to qualify them. For example, if MyApplication is the name of the Application object, a Visual Basic program can refer to a method of MyApplication as MyApplication.MyMethod or simply MyMethod. However, you should be careful not to overload the Application object with too many members because it can cause ambiguity and decrease performance. A large, complicated application with many members should be organized hierarchically, with a few generalized objects at the top, branching out into smaller, more specialized objects.

The following chart shows how applications should expose their Application and Document objects.



| Command line               | Multiple-document interface application                                                                                                                                                                                                     | Single-document interface application                                                                                                                                                                                                                 |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **/Embedding**<br/>  | Expose class factories for document classes, but not for the application.<br/> Call [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) for the Application object.<br/>                                                       | Expose class factories for document class, but not for the application.<br/> Call [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) for the Application object.<br/>                                                                   |
| **/Automation**<br/> | Expose class factories for document classes.<br/> Expose class factory for the application using **RegisterClassObject**.<br/> Call [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) for the Application object.<br/> | Do not expose class factory for document class.<br/> Expose class factory for the Application object using **RegisterClassObject**.<br/> Call [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) for the Application object.<br/> |
| No OLE switches<br/> | Expose class factories for document classes, but not for the application.<br/> Call [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) for the Application object.<br/>                                                       | Call [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) for the Application object. <br/>                                                                                                                                                     |



 

The call to **RegisterActiveObject** enters the Application object in OLE's running object table (ROT), so ActiveX clients can retrieve the active object instead of creating a new instance. Visual Basic applications can use the **GetObject** statement to access an existing object.

 

 





