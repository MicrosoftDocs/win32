---
title: Create and Run StoClien Sample
description: StoClien works in cooperation with a COPaper object in a COM server to achieve persistent storage of drawings in COM compound files.
ms.assetid: bf622104-10dd-4649-88f0-e2bfb15289b1
keywords:
- Create and Run StoClien Sample
ms.topic: article
ms.date: 05/31/2018
---

# Create and Run StoClien Sample

**StoClien** works in cooperation with a COPaper object in a COM server to achieve persistent storage of drawings in COM compound files. For more information about COPaper's use of streams in the compound file provided to COPaper by **StoClien**, see [**StoServe**](structured-storage-server-sample--stoserve-.md) sample and STOSERVE.HTM. COPaper's construction and its IPaper interface are also covered in the **StoServe** sample.

## Code Tour

The major topics covered in this code tour are:

-   How **CGuiPaper** encapsulates the GUI behavior of **StoClien**'s electronic drawing paper
-   How **StoClien** captures and displays interactive drawing activity
-   How the **CGuiPaper** object uses COPaper to record drawing data
-   How an IPaperSink connection is used in repainting
-   How the CPapFile **Load** and **Save** methods use the structured storage in compound files

As the **CGuiBall** class used in the FRECLIEN and CONCLIEN samples encapsulated the behavior of a bouncing ball, **StoClien** uses a **CGuiPaper** C++ class to encapsulate the data and GUI behavior of electronic drawing paper.

The following table lists the files pertinent to the **StoClien** sample.



| Files        | Description                                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------------|
| STOCLIEN.TXT | Short sample description.                                                                                                        |
| MAKEFILE     | The generic makefile for building the code sample.                                                                               |
| STOCLIEN.H   | The include file for the **StoClien** application. Contains class declarations, function prototypes, and resource identifiers.   |
| STOCLIEN.CPP | The main implementation file for STOCLIEN.EXE. Has WinMain and CMainWindow implementation, as well as the main menu dispatching. |
| STOCLIEN.RC  | The application resource definition file.                                                                                        |
| STOCLIEN.ICO | The application icon resource.                                                                                                   |
| STOCLIEN.PAP | A default paper drawing file for the application.                                                                                |
| PENCIL.CUR   | A pencil image for the client window cursor.                                                                                     |
| SINK.H       | The class declaration for the COPaperSink COM object class.                                                                      |
| SINK.CPP     | Implementation file for the COPaperSink COM object class.                                                                        |
| PAPFILE.H    | The class declaration for the **CPapFile** C++ class.                                                                            |
| PAPFILE.CPP  | Implementation file for the **CPapFile** C++ class.                                                                              |
| GUIPAPER.H   | The class declaration for the **CGuiPaper** C++ class.                                                                           |
| GUIPAPER.CPP | Implementation file for the **CGuiPaper** C++ class.                                                                             |
| STOCLIEN.DSP | Microsoft Visual Studio Project file.                                                                                            |



 

## Compound Files

**StoClien** relies on COPaper to record drawing data. It also relies on COPaper to store the data in a compound file. However, in a typical division of labor between COM client and server, **StoClien** shares part of the responsibility for file storage. This division of labor is important in COM applications where the client is a container and the server is an embedded object. In this arrangement, the client is responsible for creating or opening a structured storage file, while the server object is responsible for using that storage for its own data storage purposes. This may involve the server object creating substorages in the storage that is given to it. It usually involves the server object creating stream objects in the storage. COPaper's use of storage streams is detailed in the **StoClien** sample.

The [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface is used by both client and server object to perform file operations. The compound files implementation of the Structured Storage architecture is used. Standard service functions are used for operations on compound files. For example, the [**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile) function initially creates a compound file and passes back an **IStorage** pointer that can be used to manipulate the file. This particular function is called in **StoClien**. The **IStorage** interface it obtains is passed as a parameter to COPaper for its use. The COPaper object does not create or open compound files on its own: It uses the **IStorage** and [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) interfaces to work in compound files that are given to it.

These [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) and [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) interfaces are not implemented within **StoClien** or **StoServe**. They are implemented within the COM libraries. When a pointer to one of these interfaces is obtained, their methods are essentially used as a set of services to operate on a compound file.

 

 




