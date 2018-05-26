---
Description: Unlike Microsoft Visual Basic or Microsoft Visual C++, scripting languages such as Microsoft Visual Basic Scripting Edition (VBScript) or Microsoft JScript do not support the use of enumerated values.
ms.assetid: 814d04b1-324e-4972-abd8-5699530c26dd
title: Using Enumerations in Scripts
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Enumerations in Scripts

Unlike Microsoft Visual Basic or Microsoft Visual C++, scripting languages such as Microsoft Visual Basic Scripting Edition (VBScript) or Microsoft JScript do not support the use of enumerated values. For this reason, you must define as constants the enumeration members that you use in your scripts, or use the member value rather than the name in the code.

For example, you can use the following statement in Visual Basic:


```
objFaxDocument.CoverPageType = fcptLOCAL
```



However, the preceding code will not be understood in VBScript unless you place this line of code at the beginning of the script:


```
const fcptLOCAL = 1
```



Alternatively, use the member value in the code:


```
objFaxDocument.CoverPageType = 1
```



The reference page for each enumeration provides the constant values that you need. For more information, see [Fax Service Enumerations](-mfax-fax-service-enumerations.md).

 

 



