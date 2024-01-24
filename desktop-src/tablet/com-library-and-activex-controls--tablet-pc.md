---
description: This section describes how to set up your environment to use the Tablet PC platform COM libraries in C++.
ms.assetid: c0d7f703-d4aa-4c26-ae81-a4c888383c1e
title: COM Library and ActiveX Controls
ms.topic: article
ms.date: 05/31/2018
---

# COM Library and ActiveX Controls

This section describes how to set up your environment to use the Tablet PC platform COM libraries in C++.

## Microsoft Visual C++

To build Tablet PC applications in Visual C++, you need to update the system environment variables, set up directory options for Visual Studio, and access the Tablet PC interfaces in your project.

To update the environment variables, follow the instructions provided by the Windows SDK for adding the environment variables to Visual Studio.

### Accessing the Tablet PC Interfaces

To access the Tablet PC interfaces, you must include the Msinkaut.h and Msinkaut\_i.c files in your project.


```C++
#include <msinkaut.h>
#include <msinkaut_i.c>
```



You can also use the following import directive instead of the \#include statements previously listed.


```C++
#import "InkObj.dll" no_namespace exclude("tagXFORM")
```



To access the InkAnalysis interfaces, you must include IACom.h and IACom\_i.c files in your project.


```C++
#include <IACom.h>
#include <IACom_i.c>
```



You can also use the following import directive instead of the \#include statements previously listed.


```C++
#import "IACom.dll" no_namespace exclude("tagXFORM")
```



To access the [**InkDivider**](inkdivider-class.md) interfaces, you must include msinkaut15\_i.c and msinkaut15.h files in your project.

> [!Note]  
> InkDivider has been superseded by the Ink Analysis APIs.

 


```C++
#include <msinkaut15.h>
#include <msinkaut15_i.c>
```



You can also use the following import directive instead of the \# include statements.


```C++
#import "InkDiv.dll" no_namespace exclude("tagXFORM")
```



To access the [**PenInputPanel**](peninputpanel-class.md) interfaces, you must include PenInputPanel\_i.c and PenInputPanel.h files in your project.


```C++
#include <PenInputPanel.h>
#include <PenInputPanel_i.c>
```



You can also use the following import directive instead of the \# include statements.


```C++
#import "PIPanel.dll" no_namespace 
```



> [!Note]  
> The PenInputPanel APIs have been superseded in Windows Vista by the new Text Input Panel interfaces.

 

To access the [InkEdit](inkedit-control-reference.md) Control interfaces, you must include the Inked.h and Inked\_i.c files in your project.


```C++
#include <inked.h>
#include <inked_i.c>
```



Alternatively, you can \#import the InkEd.dll file.


```C++
#import "InkEd.dll" no_namespace exclude("tagXFORM")
```



 

 



