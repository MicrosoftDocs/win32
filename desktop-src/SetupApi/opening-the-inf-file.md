---
Description: You must use the SetupOpenInfFile function to open the INF file before you can retrieve information from it, or append other INF files to it.
ms.assetid: ba4d511a-ad19-4619-a10a-cafef789821b
title: Opening the INF File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Opening the INF File

You must use the [**SetupOpenInfFile**](/windows/win32/Setupapi/nf-setupapi-setupopeninffilea?branch=master) function to open the INF file before you can retrieve information from it, or append other INF files to it.

The following opens an INF file using [**SetupOpenInfFile**](/windows/win32/Setupapi/nf-setupapi-setupopeninffilea?branch=master) and returns a handle, MyInf, to the opened INF file. The *InfClass* parameter of **SetupOpenInfFile** is specified as **NULL** to indicate that the Class of the INF file should be ignored.


```C++
HINF MyInf;                //variable to hold the INF handle
UINT ErrorLine;            //variable to hold errors returned
BOOL test=0;                 //variable to receive function success
 
MyInf = SetupOpenInfFile (
      szInfFileName,       //the filename of the inf file to open
      NULL,                //optional class information
      INF_STYLE_WIN4,      //the inf style
      &amp;ErrorLine           //line number of the syntax error
);
```



After an INF file is opened, you can call the [**SetupOpenAppendInfFile**](/windows/win32/Setupapi/nf-setupapi-setupopenappendinffilea?branch=master) function to append a file to the open INF file. To append several files, repeat this process. If you call the **SetupOpenAppendInfFile** function and the filename passed to it is **NULL**, then the function will search the Version section of the open INF file (and any appended INF files) for a LayoutFile key. If the function finds a key, it will append the file specified by that key (usually LAYOUT.INF). When multiple INF files have been combined, **SetupOpenAppendInfFile** starts with the last appended INF file when it searches for a Version section.

 

 



