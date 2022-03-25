---
title: Using Visual Studio
description: For convenience, Microsoft Visual Studio 6.0 provides a project file for each sample.
ms.assetid: 8da6affd-a881-4dc4-a2e6-d35f655c69fe
ms.topic: article
ms.date: 05/31/2018
---

# Using Visual Studio

For convenience, Microsoft Visual Studio 6.0 provides a project file for each sample. This file has the DSP extension. An Allsamp.dsw workspace file is also provided in the main directory so that you can compile all the samples at once from within Visual Studio.

> [!Note]  
> The following instructions are written for Microsoft Visual Studio 6.0. The commands may differ in earlier and later versions of Visual Studio.

 

To load the appropriate project for a sample, you can run Visual Studio at the command prompt in the sample's directory as shown in the following example. You must substitute the sample project name for **\<project name\>**.

**msdev \<project name\>.dsp**

You can also simply double-click the .dsp file in the Windows Explorer to load a sample's workspace into Visual Studio. From within Visual Studio you can then browse the C++ classes of the sample source and generally perform the other edit-compile-debug operations.

As part of the Platform Software Development Kit (SDK), the compilation of these samples from within Visual Studio requires the proper setting of directory paths in Visual Studio. To set the directory paths, perform the following steps:

-   Run Microsoft Visual Studio (Visual C++).
-   Choose **Options...** on the **Tools** menu.
-   Choose the **Directories** tab in the **Options** dialog.
-   In the **Show Directories For** drop-down list, select **Executable files** and enter the BIN directory path for your installed Platform SDK (for example, C:\\Program Files\\Microsoft SDK\\Bin). Click the up arrow button to move this newly entered path so that it is the first entry in the **Directories** list.
-   In the **Show Directories For** drop-down list select **Include files** and enter the INCLUDE directory path for your installed Platform SDK(for example, C:\\Program Files\\Microsoft SDK\\include). Click the up arrow button to move this newly entered path so that it is the first entry in the **Directories** list.
-   In the **Show Directories For** drop-down list select **Library files** and enter the LIB directory path for your installed Platform SDK(for example, C:\\Program Files\\Microsoft SDK\\Lib). Click the up arrow buttons to move this newly entered path so that it is the first entry in the **Directories** list.
-   Click the OK button in the **Options** dialog to complete the settings.

From there you can use the editor, debugger, and project facilities to edit, compile, link, and debug.

Other visual IDEs can also easily generate one of their native project makefiles, given the existing source files of a code sample. If you are using such an IDE, generating such a native project makefile can be very worthwhile because it offers a way to browse the C++ classes of the program. For more information about using external makefiles or creating a native project makefile using a set of existing source files, see your IDE documentation.

Aside from the dependence on the common code in the sibling APPUTIL, INC, and LIB directories, many code samples are self-contained. Build APPUTIL before you build any other code samples. Some samples later in the sequence may work with the compiled results of earlier samples. These code sample interdependencies are as follows:

-   Any: Build of any code sample needs prior build of APPUTIL.
-   DLLUSER: Build or run needs prior build of DLLSKEL.
-   COMUSER: Build or run needs prior build of COMOBJ.
-   DLLSERVE: Build needs prior build of REGISTER.
-   DLLCLIEN: Run needs prior build of DLLSERVE.
-   LICSERVE: Build needs prior build of REGISTER.
-   LICCLIEN: Run needs prior build of LICSERVE and DLLSERVE.
-   MARSHAL: Build needs prior build of REGISTER.
-   LOCSERVE: Build or run needs prior build of REGISTER and MARSHAL.
-   LOCCLIEN: Run needs prior build of LOCSERVE.
-   APTSERVE: Build or run needs prior build of REGISTER and MARSHAL.
-   APTCLIEN: Run needs prior build of APTSERVE.
-   REMCLIEN: Build or run needs prior build of REGISTER and MARSHAL on local (client) computer. Run needs prior build of REGISTER, MARSHAL, and APTSERVE on remote (server) computer.
-   FRESERVE: Build needs prior build of REGISTER.
-   FRECLIEN: Run needs prior build of FRESERVE.
-   CONSERVE: Build needs prior build of REGISTER.
-   CONCLIEN: Run needs prior build of CONSERVE.
-   STOSERVE: Build needs prior build of REGISTER.
-   STOCLIEN: Run needs prior build of STOSERVE.
-   PERSERVE: Build needs prior build of REGISTER.
-   PERTEXT: Build needs prior build of REGISTER.
-   PERDRAW: Build needs prior build of REGISTER.
-   PERCLIEN: Run needs prior build of PERSERVE, PERTEXT, and PERDRAW.
-   DCDMARSH: Build needs prior build of REGISTER.
-   DCDSERVE: Build or run needs prior build of REGISTER and DCDMARSH.
-   DCOMDRAW: Build or run needs prior build of REGISTER and DCDMARSH on local (client) computer. Run needs prior build of REGISTER, DCDMARSH, and DCOMDRAW on remote (server) computer.

 

 




