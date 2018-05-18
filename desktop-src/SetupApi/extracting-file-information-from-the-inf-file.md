---
Description: 'After the INF file is opened, you can gather information from it to build the user interface, or to direct the installation process. The setup functions provide several levels of functionality for gathering information from an INF file.'
ms.assetid: '3ef2768b-8c73-4258-937c-77a40963ffe4'
title: Extracting File Information from the INF file
---

# Extracting File Information from the INF file

After the INF file is opened, you can gather information from it to build the user interface, or to direct the installation process. The setup functions provide several levels of functionality for gathering information from an INF file.



| To gather information…                | Use these functions…                                                        |
|---------------------------------------|-----------------------------------------------------------------------------|
| About the INF file                    | [**SetupGetInfInformation**](setupgetinfinformation.md)                    |
|                                       | [**SetupQueryInfFileInformation**](setupqueryinffileinformation.md)        |
|                                       | [**SetupQueryInfVersionInformation**](setupqueryinfversioninformation.md). |
| About source and target files         | [**SetupGetSourceFileLocation**](setupgetsourcefilelocation.md)            |
|                                       | [**SetupGetSourceFileSize**](setupgetsourcefilesize.md)                    |
|                                       | [**SetupGetTargetPath**](setupgettargetpath.md)                            |
|                                       | [**SetupGetSourceInfo**](setupgetsourceinfo.md)                            |
| From a line of an INF file            | [**SetupGetLineText**](setupgetlinetext.md)                                |
|                                       | [**SetupFindNextLine**](setupfindnextline.md)                              |
|                                       | [**SetupFindNextMatchLine**](setupfindnextmatchline.md)                    |
|                                       | [**SetupGetLineByIndex**](setupgetlinebyindex.md)                          |
|                                       | [**SetupFindFirstLine**](setupfindfirstline.md)                            |
| From a field of a line in an INF file | [**SetupGetStringField**](setupgetstringfield.md)                          |
|                                       | [**SetupGetIntField**](setupgetintfield.md)                                |
|                                       | [**SetupGetBinaryField**](setupgetbinaryfield.md)                          |
|                                       | [**SetupGetMultiSzField**](setupgetmultiszfield.md)                        |



 

The following example uses the [**SetupGetSourceInfo**](setupgetsourceinfo.md) function to retrieve the human-readable description of a source media from an INF file.


```C++
#include <windows.h>
#include <setupapi.h>

BOOL test;  
HINF MyInf;
UINT SourceId;
PTSTR Buffer;
DWORD MaxBufSize;
DWORD BufSize;

int main()  
{ 

test = SetupGetSourceInfo (
     MyInf,   //Handle to the INF file to access                
     SourceId, //Id of the source media                 
     SRCINFO_DESCRIPTION, //which information to retrieve     
     Buffer, //a pointer to the buffer to receive the information                     
     MaxBufSize,  //the size allocated for the buffer 
     &amp;BufSize    //buffer size actually needed
);
  
return 0;
}
```



In the example, MyInf is the handle to the open INF file. SourceId is the identifier for a specific source media. The value SRCINFO\_DESCRIPTION specifies that the [**SetupGetSourceInfo**](setupgetsourceinfo.md) function should retrieve the source media description. Buffer points to a string that will receive the description, MaxBufSize indicates the resources allocated to the buffer, and BufSize indicates the resources necessary to store the buffer.

If BufSize is greater than MaxBufSize, the function will return **FALSE**, and a subsequent call to [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) will return ERROR\_INSUFFICIENT\_BUFFER.

 

 



