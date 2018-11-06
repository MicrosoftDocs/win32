---
title: Multiple Controls in One DLL
description: Multiple Controls in One DLL
ms.assetid: 76c1c0ef-af24-43e8-b3a7-337841c338ea
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Controls in One DLL

A single .ocx DLL can container any number of ActiveX controls, thus simplifying the distribution and use of a set of related controls.

If you ship multiple controls in a single DLL, be sure to include the vendor name in each control name in the package. Including the vendors' names in each control name will enable users to easily identify controls within a package. For example, if you ship a DLL that implements three controls, Con1, Con2, and Con3, then the control names should be:

-   *Your company name* Con1 Control

-   *Your company name* Con2 Control

-   *Your company name* Con3 Control

 

 




