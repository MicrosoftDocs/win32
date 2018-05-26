---
title: ActiveX Objects
description: An ActiveX object is an instance of a class that exposes properties, methods, and events to ActiveX clients.
ms.assetid: 973ca2be-7f0e-43db-8790-0aa07c45675d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ActiveX Objects

An ActiveX object is an instance of a class that exposes properties, methods, and events to ActiveX clients. ActiveX objects support the COM. An ActiveX component is an application or library that is capable of creating one or more ActiveX objects. For example, Microsoft Excel exposes many objects that you can use to create new applications and programming tools. Within Microsoft Excel, objects are organized hierarchically, with an object named Application at the top of the hierarchy.

The following figure shows some of the objects in Microsoft Excel.

![](images/oa01-03.png)

Each ActiveX object has its own unique member functions. When the member functions are exposed, it makes the object programmable by ActiveX clients. Three types of members for an object can be exposed:

-   *Methods* are actions that an object can perform. For example, the Worksheet object in Microsoft Excel provides a **Calculate** method that recalculates the values in the worksheet.

-   *Properties* are functions that access information about the state of an object. The Worksheet object's **Visible** property determines whether the worksheet is visible.

-   *Events* are actions recognized by an object, such as clicking the mouse or pressing a key. You can write code to respond to such actions. In Automation, an event is a method that is called, rather than implemented, by an object.

For example, you might expose the following objects in a document-based application by implementing these methods and properties:



| ActiveX object | Methods                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Properties                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Application    | <dl> <dt>**Help**</dt> <dt>**Quit**</dt> <dt>**Save**</dt> <dt>**Repeat**</dt> <dt>**Undo**</dt> </dl>                                                                                                                                                                                                                       | <dl> <dt>**ActiveDocument**</dt> <dt>**Application**</dt> <dt>**Caption**</dt> <dt>**DefaultFilePath**</dt> <dt>**Documents**</dt> <dt>**Height**</dt> <dt>**Name**</dt> <dt>*Parent*</dt> <dt>*Path*</dt> <dt>*Printers*</dt> <dt>*StatusBar*</dt> <dt>*Top*</dt> <dt>*Value*</dt> <dt>**Visible**</dt> <dt>**Width**</dt> </dl> |
| Document       | <dl> <dt>**Activate**</dt> <dt>**Close**</dt> <dt>**NewWindow**</dt> <dt>**Print**</dt> <dt>**PrintPreview**</dt> <dt>**RevertToSaved**</dt> <dt>**Save**</dt> <dt>**SaveAs**</dt> </dl> | <dl> <dt>**Application**</dt> <dt>**Author**</dt> <dt>**Comments**</dt> <dt>**FullName**</dt> <dt>**Keywords**</dt> <dt>**Name**</dt> <dt>**Parent**</dt> <dt>**Path**</dt> <dt>**ReadOnly**</dt> <dt>**Saved**</dt> <dt>**Subject**</dt> <dt>**Title**</dt> <dt>**Value**</dt> </dl>                                                                                                                                     |



 

Often, an application works with several instances of an object which together make up a *collection object*. For example, an ActiveX application based on Microsoft Excel might have multiple workbooks. To provide an easy way to access and program the workbooks, Microsoft Excel exposes an object named Workbooks, which refers to all of the current Workbook objects. Workbooks is a collection object.

In the preceding figure, collection objects in Microsoft Excel are shaded. Collection objects let you work iteratively with the objects they manage. If an application is created with a multiple-document interface (MDI), it might expose a collection object named Documents with the methods and properties in the following table.



| Collection object | Methods                                                                                                                                                                                                                                                                       | Properties                                                                                                                                                                                                                |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Documents         | <dl> <dt>**Add**</dt> <dt>**Close**</dt> <dt>**Item**</dt> <dt>**Open**</dt> </dl> | <dl> <dt>**Application**</dt> <dt>**Count**</dt> <dt>**Parent**</dt> </dl> |



 

 

 




