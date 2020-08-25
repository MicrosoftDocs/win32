---
title: Using StoServe
description: StoServe is a DLL that is intended primarily as a COM server.
ms.assetid: 32cb284a-de78-4953-9d8e-5bb87d6d5a97
ms.topic: article
ms.date: 05/31/2018
---

# Using StoServe

**StoServe** is a DLL that is intended primarily as a COM server. Although it can be implicitly loaded by linking to its associated .LIB file, it is normally used after an explicit LoadLibrary call, usually from within the COM function [**CoGetClassObject**](/windows/win32/api/combaseapi/nf-combaseapi-cogetclassobject). **StoServe** is a self-registering in-process server.

To use **StoServe**, a client program does not need to include STOSERVE.H or link to STOSERVE.LIB. A COM client of **StoServe** obtains access solely through its object's CLSID and COM services. For **StoServe**, that CLSID is CLSID\_DllPaper (defined in file PAPGUIDS.H in the \\INC sibling directory). The [StoClien](structured-storage-client-sample--stoclien-.md) code sample shows how the client obtains this access.

The makefile that builds this sample automatically registers the server in the registry. You can manually initiate its self-registration by issuing the following command at the command prompt in the **StoServe** directory:

**nmake** **register**

This assumes that you have a compilation environment set up. If not, you can also directly invoke the REGISTER.EXE command at the command prompt while in the **StoServe** directory.

**..\\register\\register.exe** **stoserve.dll**

These registration commands require a prior build of the REGISTER sample in this series, as well as a prior build of STOSERVE.DLL.

In this series, the makefiles use the REGISTER.EXE utility from the REGISTER sample. Recent releases of the Platform Software Development Kit (SDK) and Visual C++ include a utility, REGSVR32.EXE, which can be used in a similar fashion to register in-process servers and marshaling DLLs.

**StoServe** uses many of the utility classes and services provided by APPUTIL. For more details on APPUTIL, study the APPUTIL library's source code in the sibling APPUTIL directory and APPUTIL.HTM in the main tutorial directory.

 

 