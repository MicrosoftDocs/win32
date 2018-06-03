---
title: Creating a Registration File
description: Before an application can use OLE and Automation, the OLE objects must be registered with the user's system registration database.
ms.assetid: 84024523-d8a1-480b-a2cb-6f4e0681ea0e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Registration File

Before an application can use OLE and Automation, the OLE objects must be registered with the user's system registration database. OLE provides sample registration files to perform this task for the OLE objects and the sample applications. Registration makes the following possible:

-   ActiveX clients can create instances of the objects through **CoCreateInstance**.

-   Automation tools can find the type libraries that are installed on the user's computer.

-   OLE can find remoting code for the interfaces.

You can use the **DLLRegisterServer** function to register all objects implemented by a dynamic-link library (DLL). This function registers the class identifiers (CLSIDs) for each object, the programmatic identifiers (ProgIDs) for each application, and the type library. For details, refer to the description of **DLLRegisterServer**.

## In this section



| Topic                                                                     | Description                                                                                                                                                      |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Registering the Application](registering-the-application.md)<br/> | Registration maps the ProgID of the application to a unique CLSID, so that you can create instances of the application by name, rather than by CLSID.<br/> |
| [Registering Classes](registering-classes.md)<br/>                 | Objects that can be created with **CoCreateInstance** must also be registered with the system.<br/>                                                        |



 

 

 





