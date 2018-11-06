---
title: Create and Run StoServe Sample
description: The client sample and other related samples must be compiled before you can run the client.
ms.assetid: 7d8fe758-0008-495d-89ae-a814cb07ea19
ms.topic: article
ms.date: 05/31/2018
---

# Create and Run StoServe Sample

The client sample and other related samples must be compiled before you can run the client. For more details on building the samples, see [How to Build Samples](how-to-build-samples.md). If you have already built the appropriate samples, STOCLIEN.EXE is the client executable to run for the **StoServe** sample.

## Code Tour

The following table lists the files pertinent to the **StoServe** sample.



| Files        | Description                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------|
| STOSERVE.TXT | Short sample description                                                                                                  |
| MAKEFILE     | The generic makefile for building the STOSERVE.DLL code sample of this lesson.                                            |
| STOSERVE.H   | The include file for declaring as imported or defining as exported the service functions in STOSERVE.DLL.                 |
| STOSERVE.CPP | The main implementation file for STOSERVE.DLL. Has DllMain and the COM server functions (for example, DllGetClassObject). |
| STOSERVE.DEF | The module definition file. Exports server housing functions.                                                             |
| STOSERVE.RC  | The DLL resource definition file for the executable.                                                                      |
| STOSERVE.ICO | The icon resource for the executable.                                                                                     |
| SERVER.H     | The include file for the server control C++ object.                                                                       |
| SERVER.CPP   | The implementation file for the server control C++ object.                                                                |
| FACTORY.H    | The include file for the server's class factory COM objects.                                                              |
| FACTORY.CPP  | The implementation file for the server's class factories.                                                                 |
| CONNECT.H    | The include file for the connection point enumerator, connection point, and connection enumerator classes.                |
| CONNECT.CPP  | The implementation file for the connection point enumerator, connection point, and connection enumerator objects.         |
| PAPER.H      | The include file for the COPaper COM object class.                                                                        |
| PAPER.CPP    | The implementation file for the COPaper COM object class and the connection points.                                       |
| STOSERVE.DSP | Microsoft Visual Studio Project file.                                                                                     |



 

The major topics covered in this code tour are:

-   The [**IPaper**](ipaper-methods.md) interface methods.
-   COPaper's use of the [**IPaperSink**](ipapersink-methods.md) interface for client notifications.
-   [**Structures**](structures---stoserve.md) in StoServe.
-   [Unicode considerations](unicode-considerations.md).

 

 




