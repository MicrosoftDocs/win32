---
title: StoServe Overview
description: The StoServe code example shows how to use Structured Storage services as provided in the compound files implementation. The use of the standard IStorage and IStream interfaces is described.
ms.assetid: 41ccd333-15c8-46b2-91c6-3e1929f7198c
ms.topic: article
ms.date: 05/31/2018
---

# StoServe Overview

## Purpose

The primary focus of this code example is the use of Structured Storage services as provided in the compound files implementation. The use of the standard [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) and [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) interfaces is described. **StoServe** works with the [StoClien](structured-storage-client-sample--stoclien-.md) code example to illustrate the joint use of compound file storage by client and server.

## Functionality

The **StoServe** sample introduces the COPaper COM object, which virtually represents a blank sheet of drawing paper.

COPaper objects expose a set of features for free-form drawing on the paper surface using "ink" of specified color and width. The functionality is outwardly similar to the "scribble" tutorial samples in many versions of Microsoft Visual C++. The difference in the **StoServe**/**StoClien** samples is an architecture-based primarily on COM technology. The electronic drawing paper features of COPaper objects are available to clients through a custom [**IPaper**](ipaper-methods.md) interface. COPaper implements the **IPaper** interface. A clear architectural distinction is kept between client and server. No graphical user interface (GUI) is provided by COPaper. The design of the COPaper object relies on the client for all GUI behavior. COPaper encapsulates only the server-based capture and storage of the drawn ink data.

The ink data that is drawn on the COPaper surface can be stored in and loaded from compound files. The [**IPaper**](ipaper-methods.md), [**Save**](ipaper--save.md) and [**Load**](ipaper--load.md) methods accept an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface pointer. COPaper uses this client-provided **IStorage** interface to store the drawing data.

COPaper is housed in an in-process server and is made publicly available as a custom COM component. Similar to other servers in this tutorial series, StoServe is a self-registering COM server. It makes the COPaper object type available to clients as the DllPaper component using a CLSID\_DllPaper registration in the Registry.

As in the previous CONSERVE server, connectable object features are supported in COPaper. The [**IConnectionPointContainer**](/windows/win32/api/ocidl/nn-ocidl-iconnectionpointcontainer) interface is exposed, and an appropriate connection point is implemented. In this context, an outgoing custom IPaperSink interface is declared for use in sending notifications to the client.

The two [**IPaper**](ipaper-methods.md) and [**IPaperSink**](ipapersink-methods.md) custom interfaces are declared in IPAPER.H located in the common sibling \\INC directory. The GUIDs for the interfaces and objects are defined in PAPGUIDS.H located in that same common include directory.

The CThreaded facility in APPUTIL is used by **StoServe** to achieve thread safety, as it was in the FRESERVE sample. COPaper objects are derived from the CThreaded class and inherit its OwnThis and UnOwnThis methods. These methods allow only one thread at a time to have access to the **StoServe** server and to COPaper objects managed by the server.

## COPaper COM Object

The COPaper COM object is the single object type managed by this **StoServe** in-process server. COPaper is constructed as a connectable COM object with an implementation of the standard [**IConnectionPointContainer**](/windows/win32/api/ocidl/nn-ocidl-iconnectionpointcontainer) interface and an implementation of the custom [**IPaper**](ipaper-methods.md) interface. COPaper exposes the **IPaper** interface so clients can perform a small set of electronic paper operations on an instance of COPaper. The essential operations are starting an ink drawing sequence, drawing the ink data on COPaper virtual paper surface, and ending the ink drawing sequence. In this scheme, the client is assumed to be a GUI application driven by a mouse or tablet device. The client is responsible for translating mouse movements into requests to COPaper, which saves these requests as ink data.

There are two levels of ink data saving in COPaper. COPaper saves the ink data in a RAM-based array that represents the current drawing, and COPaper persistently saves an entire drawing into a compound file. Methods in the [**IPaper**](ipaper-methods.md) interface perform both.

Because the client does not manage the drawn paper data, but is responsible for rendering it as an image on the screen, the [**IPaper**](ipaper-methods.md) implementation in COPaper must expose a method that enables the client to obtain the drawing data. The connectable object technology in COPaper is used for this purpose. A CONNPOINT\_PAPERSINK connection point is implemented by COPaper so a client can connect to COPaper to receive the ink data for drawing. The client first calls the [IPaper::Redraw](ipaper--redraw.md) method on the COPaper object to request all the ink data of the current drawing. The COPaper implementation of Redraw then uses the client implementation of [**IPaperSink**](ipapersink-methods.md) to pass the data to the client.

As the user interactively draws in the client, it paints the data immediately to the screen while also sending it to COPaper for saving. When the client requires the screen to be repainted, it calls the COPaper [Redraw](ipaper--redraw.md) method. Such repainting is common in applications. For example, repainting occurs when the client window is overlaid by another application window. The client has a bitmap rendering of the drawn image, but the bitmap is easily lost and must often be repainted. The client relies on COPaper in the server for the ink data required for repainting.

This is a common client/server division of labor. It is especially appropriate when there is a requirement for multiple clients to share the data. COPaper is coded to enable this. It uses the APPUTIL CThreaded facility to achieve thread safety. An application that might exploit this design is a shared whiteboard application, where multiple clients can contribute to a commonly viewed drawing. COM support for Distributed COM (DCOM) supports this type of workgroup application usage across the network. For more information, see the earlier REMCLIEN sample.

A more modest use of the COPaper client/server scheme is to integrate behavior for objects implemented in different applications on the same computer. In this case, the clients might be an ActiveX container in separate applications that share data managed by the same object. This data may not be the ink drawing data that the DllPaper component supports. **StoServe** can be used as a starting framework for programming components that manage other types of shared data.

## Support Information

The **StoServe** makefile registers the **StoServe** DllPaper COM component in the registry. This component must be registered before **StoServe** is available to outside COM clients as a server for that component. This self-registration is done using the Register.exe utility built into the REGISTER sample. To build or run **StoServe**, first build the REGISTER code example.

For more information about setting up your system to build and test the code examples in this COM Tutorial series, see [How to Build Samples](how-to-build-samples.md). The supplied makefile (MAKEFILE) is Microsoft NMAKE-compatible. To create a debug build, issue the NMAKE command in the command prompt window.

For convenient use in Microsoft Visual Studio, a project file is provided for each sample. To load the project for the **StoServe** example, you can run Visual Studio at the command prompt in the samples directory as follows:

MSDEV STOSERVE.DSP

You can also double-click the Stoserve.dsp file in Windows Explorer to load a sample project into Visual Studio. In Visual Studio you can browse the C++ classes of the sample source and generally perform the other edit-compile-debug operations.

> [!Note]  
> As part of the Platform Software Development Kit (SDK), the compilation of these samples from within Visual Studio requires the proper setting of directory paths in Visual Studio. For more information, see [How to Build Samples](how-to-build-samples.md).

 

 

 