---
title: How to Build Samples
description: To build a COM sample, the computer environment must be set up to build Microsoft Win32 C++ applications.
ms.assetid: c62b8b4d-a9d2-4587-8bb6-7b2c30d1c00d
keywords:
- How to Build Samples
ms.topic: article
ms.date: 05/31/2018
---

# How to Build Samples

To build a COM sample, the computer environment must be set up to build Microsoft Win32 C++ applications.

## Preparing a Computer to Create COM Samples

The computer environment must be set up with a properly installed 32-bit C++ compiler, linker, and resource compiler that are compatible with Microsoft Visual C++ 4.x or later, and a properly installed Windows SDK. It is best to install the Windows SDK last. The Windows SDK provides .h include and .lib library files required for the COM functionality coded in the samples.

To successfully run the Remclien, Freserve, and Freclien samples requires system facilities that are available in the Windows operating systems: Windows Server 2003, Windows XP, Windows 2000, or Windows NT 4.0. The Remclien, Freserve, and Freclien samples will build but will not run on the Windows Me, Windows 98, or Windows 95 operating systems unless Distributed COM (DCOM) and free threaded COM are part of the operating system. This support is available for the Windows Me, Windows 98, and Windows 95 operating systems in the DCOM95 add on.

Each sample directory has the necessary source files to build and run the sample. The parent sample directory has a Makeall.bat file, which you can run from the command prompt to make all the code samples in the branch below. For more information, see the Makeall.bat file. If your environment is set up to build Win32 C++ applications, you can simply run Makeall.bat from the directory where it resides to build all the code samples in the branch below. Makeall ensures the correct order to the build so that all the code sample dependencies are satisfied.

The main directory also has a makefile that builds all the tutorial code samples using options similar to those supported by Makeall.bat. For more information, see this makefile. This makefile assumes that the entire code samples branch is installed as part of the Windows SDK. Currently this location has a path similar to *D:\\MSSDK\\SAMPLES\\COM\\TUTSAMP*, where D: represents the installation drive. If you have extracted the tutorial code sample branch (for example, the COM directory COM and its subdirectories) to another location outside the Windows SDK (or if you obtained the sample set as a separate download from the Microsoft website), then use Makeall.bat to compile all the samples in the branch. In general, Makeall.bat is recommended. A Logmall.bat file is also provided. It does the same as Makeall batch file except that it logs all compilation output to file Errorlog.txt in the main tutorial directory.

Two batch files, Regall.bat and Unregall.bat, are also provided in the main directory to register and unregister all COM servers in the tutorial code sample series. To register all servers, run Regall.bat file from the main directory. To unregister all servers, run Unregall.bat in the same manner. These batch files require a prior build of the REGISTER, MARSHAL, DLLSERVE, LICSERVE, LOCSERVE, APTSERVE, FRESERVE, and CONSERVE code samples. If you perform a normal build of the code samples, the server makefiles will automatically register the servers. In this case, it is not necessary to run the Regall batch file.

Run the Cleanall.bat batch file to perform an exhaustive Cleanall of all the COM Tutorial Samples.

> [!WARNING]
> This batch file deletes all Visual Studio project files and other temporary work files created by Visual C++ in the samples. All of the COM servers built in the tutorial code samples are unregistered from the registry. All executable exe and .dll files are deleted. All debug symbol files are deleted. Files generated in a variety of build environments are also deleted.

 

Run 'Makeall Clean' to perform a faster, but more modest, cleanup of all the code samples. This cleaning operation does not attempt to be as comprehensive as that performed by Cleanall.bat. The .obj files are deleted, but the output binaries are retained. The COM servers are not unregistered from the registry.

This sample series originated as an integral part of the Windows SDK, therefore the tutorial narrative assumes an environment with the Windows SDK properly installed.

However, releases of Microsoft Visual C++ version 4.0 and later may also provide the .h include and .lib library files required for compilation. In such cases, installation of the Windows SDK may not be required to compile the samples.

For more information and complete sample build details, see:

[Environment Setup](environment-setup.md)

[Makefiles](makefiles.md)

[Using Visual Studio](using-visual-studio.md)

[Extracting the Code Samples](extracting-the-code-samples.md)

[Coding Style Conventions](coding-style-conventions.md)

 

 




