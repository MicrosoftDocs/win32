---
title: StoClien Overview
description: The StoClien sample demonstrates how the client uses structured storage and how it directs a server component to use this storage.
ms.assetid: 1f540e0f-2189-4f45-aad3-9b4b56732907
keywords:
- StoClien Overview
ms.topic: article
ms.date: 05/31/2018
---

# StoClien Overview

## Purpose

The principal focus of the [StoClien](structured-storage-client-sample--stoclien-.md) sample is how the client uses structured storage and how it instructs a server component to use this storage. The StoClien sample demonstrates a programming model of structured storage services.

## Functionality

The [StoClien](structured-storage-client-sample--stoclien-.md) functionality is similar to the "scribble" samples in some versions of Microsoft Visual C++. The difference between the StoClien sample and the [StoServe](structured-storage-server-sample--stoserve-.md) sample is an internal architecture based on COM technology. A clear architectural distinction is kept between COM client and COM server.

[StoClien](structured-storage-client-sample--stoclien-.md) loads and saves its drawings in the structured storage of COM compound files.

The [StoClien](structured-storage-client-sample--stoclien-.md) sample creates and uses the connectable COPaper COM object that is provided as the CLSID\_DllPaper component in the [StoServe](structured-storage-server-sample--stoserve-.md) server. The StoClien client creates a COPaper object and controls it through the IPaper interface that the object exposes. StoClien obtains drawing data from the user and graphically represents it in a window that it manages. StoClien uses the COPaper IPaper interface to save the drawing data in COPaper and to direct file storage operations on this data.

A COPaper COM object encapsulates only the server-based storage of the drawing paper data: No graphical user interface (GUI) behavior is provided on the server side. All GUI behavior is isolated in the client. The data management and storage features of COPaper objects are available only through an COM custom interface, IPaper.

[StoClien](structured-storage-client-sample--stoclien-.md) cooperates with the COPaper to load and save the COPaper drawing data. StoClien obtains an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface for the storage object in a compound file. In its load and save operations, StoClien passes a pointer to the **IStorage** interface to COPaper in the server. COPaper uses the provided **IStorage** to create streams in the storage. COPaper can then use the standard [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) interface for reading and writing the drawing data it manages.

COPaper only manages the drawing data; it performs no GUI actions. [StoClien](structured-storage-client-sample--stoclien-.md) provides the GUI for the drawing application. It encapsulates this in a central CGuiPaper C++ object.

[StoClien](structured-storage-client-sample--stoclien-.md) also implements the custom IPaperSink interface in a COPaperSink COM object and connects this interface to an appropriate connection point in the server COPaper object. COPaper uses the connected IPaperSink interface to send notifications back to StoClien. The normal GUI repainting of the COPaper drawing data is done in StoClien using the COPaper connectable object technology.

[StoClien](structured-storage-client-sample--stoclien-.md) is an application that you can execute directly in the normal manner or from the command prompt window. StoClien accepts an optional file name parameter on the command line.

In the following example, Drawing.pap is a compound file containing DllPaper-compatible structured storage of drawing data. If no command line file name parameter is specified, [StoClien](structured-storage-client-sample--stoclien-.md) uses the default file name Stoclien.pap and attempts to open it in the same directory as the executing Stoclien.exe.

**StoClien c:\\drawings\\drawing.pap**

## Support Information

For more information, functional descriptions and a code tutorial for [StoClien](structured-storage-client-sample--stoclien-.md), see the Code Tour section in Stoclien.htm. For more information about the external user operation of StoClien, see the Usage and Operation sections in Stoclien.htm. To read Stoclient.htm, run Tutorial.exe in the main tutorial directory and click the StoClien lesson in the table of lessons. Alternatively, click Stoclien.htm after locating the main tutorial directory in Windows Explorer. For more information about how [**StoServe**](structured-storage-server-sample--stoserve-.md) works and exposes its services to StoClien, see Stoserve.htm in the main tutorial directory. Be aware that you must build the Stoserve.dll before building StoClien. The makefile for [**StoServe**](structured-storage-server-sample--stoserve-.md) registers that server in the system registry, so you must build [**StoServe**](structured-storage-server-sample--stoserve-.md) before attempting to run StoClien.

For more information about setting up a system to build and test the code samples in this COM Tutorial series, see [How to Build Samples](how-to-build-samples.md). The supplied makefile (MAKEFILE) is Microsoft NMAKE-compatible. To create a debug build, issue the NMAKE command in the command prompt window.

For convenience, a project file is provided for each sample for use in Microsoft Visual Studio. To load the project for the [StoClien](structured-storage-client-sample--stoclien-.md) sample, run Visual Studio at the command prompt in the sample directory as follows:

MSDEV STOCLIEN.DSP

You can also double-click the Stoclient.dsp file in Windows Explorer to load a sample project into Visual Studio. In Visual Studio, you can browse the C++ classes of the sample source and generally perform the other edit-compile-debug operations. Be aware that, as part of the Server SDK, the compilation of these samples from within Visual Studio requires the proper setting of directory paths in Visual Studio. For more information, see [How to Build Samples](how-to-build-samples.md).

## Remarks

The client sample and other related samples must be compiled before you can run the client. For more information about building the samples, see [How to Build Samples](how-to-build-samples.md). If you have built the appropriate samples, Stoclien.exe is the client executable to run for this sample.

The Stoclien.exe application provides the user interface for this tutorial. It exercises the associated, but independent, Stoserve.dll to demonstrate both client and server use of COM structured storage in compound files.

 

 




