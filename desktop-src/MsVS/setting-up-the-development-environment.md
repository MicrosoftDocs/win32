---
title: Setting up the Development Environment
description: Developing applications using the Virtual Server COM API requires a minimal amount of setup for the development environment. The Virtual Server's type library is automatically installed when Virtual Server is installed.
ms.assetid: '997bf9d9-8ba2-41cf-845e-dca46a8139a0'
---

# Setting up the Development Environment

Developing applications using the Virtual Server COM API requires a minimal amount of setup for the development environment. The Virtual Server's type library is automatically installed when Virtual Server is installed.

Local Virtual Server applications are developed on a Windows 2003 Server system in which a full Virtual Server installation has been performed. Virtual Server applications which communicate remotely with a Virtual Server system can be developed on a system where either the full or developer installation of Virtual Server has been performed. Using the developer installation to create local Virtual Server applications requires that the Virtual Server service be manually installed and the Virtual Server type or interoperability libraries be manually registered in the development environment before the application program can be compiled or tested.

## Accessing Virtual Server using Visual Basic

To use the Virtual Server object in Visual Basic, select **Project**/**Add Reference** from the menu, select the **COM** tab in the dialog box, then scroll down the list and select **Virtual Server 2005 Type Library**. Once the type library is added as a reference, the VirtualServer object can be referenced and used in the program.

## Accessing Virtual Server using Visual C#

To use the Virtual Server object in Visual C#, select **Project**/**Add Reference** from the menu, select the **COM** tab in the dialog box, then scroll down the list and select **Virtual Server 2005 Type Library**. Once the type library is added as a reference, the VirtualServer object can be referenced in the program.

## Accessing Virtual Server using Visual C++

Accessing the Virtual Server COM object using VC++ requires a few manual steps to set up the development environment properly. Two files are included with Virtual Server: "VSComInterfaces.h" and "VSComInterfaces.lib". These two files are located in the "Program Files\\Microsoft Virtual Server\\Documentation" directory after installation.

"VSComInterfaces.lib" is added to the user's project file and "VSComInterfaces.h" is included in the user's program with: "\#include "VSComInterfaces.h"" In addition, if the user's program is accessing the "Virtual Server" COM object using DCOM, "\_WIN32\_DCOM" is defined globally in the project's **Preprocessor Definitions** property or defined in the user's program with: "\#define \_WIN32\_DCOM"

The initialization and uninitialization routines in the preceding example can easily be wrapped into a class constructor and destructor if the user's program is based on an application object.

 

 




