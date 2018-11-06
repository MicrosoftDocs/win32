---
title: The Environment
description: Developers working on applications for 64-bit Windows will find the development environment virtually identical to the development environment for 32-bit Windows.
ms.assetid: 49b2b952-f771-4721-a9b0-01eb67a98007
keywords:
- development environment 64-bit Windows Programming
- environment 64-bit Windows Programming
- 64-bit Windows programming guide 64-bit Windows Programming , development environment
ms.topic: article
ms.date: 05/31/2018
---

# The Environment

Developers working on applications for 64-bit Windows will find the development environment virtually identical to the development environment for 32-bit Windows. The existing APIs have been modified where necessary to allow them to reflect the precision of the platform on which they are running. The result is simplicity and a short learning curve for the developer—writing code for 64-bit Windows is just like writing code for 32-bit Windows.

The Windows header files support new data types that allow pointers and pointer-associated variables to reflect the precision of the platform. This means that developers can compile a single source base to run natively on either 32-bit Windows or 64-bit Windows. This strategy reduces the cost of developing applications that leverage 64-bit hardware such as AMD Opteron or Athlon64 processors or Intel Itanium processors.

You will have more time to make your applications 64-bit ready if you adopt the new data-type conventions as soon as possible. If you are changing your code, you should change the data definitions at the same time. Test the application on 32-bit Windows, run it through the 64-bit compiler (described in [The Tools](the-tools.md)), and the application will be ready to test when you have the appropriate 64-bit hardware.

 

 




