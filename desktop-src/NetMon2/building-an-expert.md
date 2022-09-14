---
description: This topic describes how to build a generic expert that ships with the Network Monitor SDK.
ms.assetid: c05b261d-3fac-40bf-b4ff-bd766f8d148f
title: Building an Expert
ms.topic: article
ms.date: 05/31/2018
---

# Building an Expert

This topic describes how to build a generic expert that ships with the Network Monitor SDK.

> [!Note]  
> Before creating the following code examples, install the Network Monitor SDK and initialize the MySetEnv.bat file.

 

**To build a generic expert**

1.  Open a Network Monitor command prompt and navigate to the \\Experts subdirectory; for example, C:\\Program Files\\NetMonSDK2\\Experts.
2.  Type **xcopy /e /s /v Blrplate MyExpert**; then, when prompted, type **D**.
3.  Move to the \\MyExpert subdirectory.
4.  Type **ren Blrplate\*.\* MyExpert\*.\***. Ensure that all files are properly renamed. Verify the file names by comparing the files in the \\Experts\\Blrplate subdirectory.
5.  Edit the Makefile by replacing all occurrences of **Blrplate** with **MyExpert**.
6.  Edit both .cpp files by replacing all occurrences of **Blrplate** with **MyExpert**. Be aware that the dialog box identifier in Config.cpp must be capitalized (for example, **MYEXPERT**).
7.  Edit MyExpert.h by replacing all occurrences of **Blrplate** with **MyExpert**.
8.  Edit Resrc1.h by renaming **BLRPLATE** to **MYEXPERT**. (Remember, **MYEXPERT** must be capitalized).
9.  Edit the MyExpert.rc file by renaming **IDD\_BLRPLATE\_CONFIG\_DIALOG** to **IDD\_MYEXPERT\_CONFIG\_DIALOG**.
10. Type **nmake** to build the DLL file. To verify the build, change directory to the \\Obj subdirectory and verify that the file exists. For more information, see [Viewing Expert DLL Properties](viewing-expert-dll-properties.md).

When the build is complete, you will have an expert DLL that you can test and deploy with Network Monitor. For more information about installing an expert, see [Installing an Expert to Network Monitor 2.1](installing-an-expert-to-network-monitor-2-1.md). For more information about debugging an expert, see [Debugging an Expert](debugging-an-expert.md).

 

 



