---
title: Sharing an I/O Procedure with Other Applications
description: Sharing an I/O Procedure with Other Applications
ms.assetid: 56e4804b-fe88-4b3b-93f6-f8e41048780d
keywords:
- multimedia file I/O,shared procedures
- file I/O,shared procedures
- input and output (I/O),shared procedures
- I/O (input and output),shared procedures
- sharing I/O procedures with other applications
- mmioInstallIOProc function
ms.topic: article
ms.date: 05/31/2018
---

# Sharing an I/O Procedure with Other Applications

If you want to share an I/O procedure with other applications, you need to write a dynamic-link library (DLL) for your application. You can share the I/O procedure by doing one of the following:

-   Include the code for the I/O procedure in the DLL.
-   Create a function in the DLL that calls the [**mmioInstallIOProc**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioinstallioproc) function to install the I/O procedure.
-   Export this function in the module-definitions file of the DLL.

To use the shared I/O procedure, an application must first call the function in the DLL to install the I/O procedure.

 

 