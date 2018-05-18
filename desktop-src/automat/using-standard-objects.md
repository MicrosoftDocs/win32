---
title: Using Standard Objects
description: Describes the standard objects.
ms.assetid: '4e7357bb-f57d-4893-b111-5a1d1a5d5d3d'
---

# Using Standard Objects

The following table lists the Automation standard objects. Although none of these objects are required, user-interactive applications with subordinate objects should include an Application object.



| Object name               | Description                                                                                                                             |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Application<br/>    | Top-level object. Provides a standard way for ActiveX clients to retrieve and navigate an application's subordinate objects.<br/> |
| Document<br/>       | Provides a way to open, print, change, and save an application document.<br/>                                                     |
| Documents<br/>      | Provides a way to iterate over and select open documents in MDI applications.<br/>                                                |
| Font<br/>           | Describes fonts that are used to display or print text.<br/>                                                                      |
| Picture<br/>        | Provides a language-neutral abstraction for bitmaps, icons, and metafiles. <br/>                                                  |
| Property Frame<br/> | The user interface mechanism that displays one or more property pages for a control. <br/>                                        |



 

The following illustration shows how the standard objects fit into the organization of objects provided by an application.

![](images/oa04-01.png)

The following sections describe the standard properties and methods for all objects, all collection objects, and each of the standard objects. These sections list the standard methods and properties for each object, as well as the standard arguments for those properties and methods.

## In this section



| Topic                                                                                                           | Description                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Object Properties](object-properties.md)<br/>                                                           | Describes the properties that must be provided by all objects and collections.<br/>                                                                |
| [Collection Object Properties](collection-object-properties.md)<br/>                                     | A collection provides a set of objects over which iteration can be performed.<br/>                                                                 |
| [Using the Application Object in a Type Library](using-the-application-object-in-a-type-library.md)<br/> | Describes how to use the Application object in a type library.<br/>                                                                                |
| [Document Object Properties](document-object-properties.md)<br/>                                         | If the application is document based, it should provide a Document object named Document.<br/>                                                     |
| [Documents Collection Object](documents-collection-object.md)<br/>                                       | If your application supports a multiple-document interface (MDI), you should provide a Documents collection object.<br/>                           |
| [The Font Object](the-font-object.md)<br/>                                                               | The standard font object supports a number of read-write properties as well as a set of methods through its [**IFont**](https://msdn.microsoft.com/library/windows/desktop/ms680673) interface.<br/> |
| [The Picture Object](the-picture-object.md)<br/>                                                         | Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles.<br/>                                                     |
| [The Property Frame Object](the-property-frame-object.md)<br/>                                           | Property frame objects are the user interface mechanism that displays one or more property pages for a control.<br/>                               |



 

> [!Note]  
> You can define additional application-specific properties and methods for each object. You can also provide additional optional arguments for any of the listed properties or methods; however, the optional arguments should follow the standard arguments in a positional argument list.

 

 

 





