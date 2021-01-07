---
description: The following classes are declared and associated with class identifiers (CLSIDs) in wmcodecdsp.h.
ms.assetid: f82d92dc-fbce-4274-a10f-72fa8dd776cc
title: Class Identifiers for Table of Contents Parser (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Class Identifiers for Table of Contents Parser

The following classes are declared and associated with class identifiers (CLSIDs) in wmcodecdsp.h.



| Class name       | Friendly object name |
|------------------|----------------------|
| CTocEntry        | TOC Entry            |
| CTocEntryList    | TOC Entry List       |
| CToc             | TOC                  |
| CTocCollection   | TOC Collection       |
| CTocParser       | TOC Parser           |
| CTocGeneratorDmo | TOC Generator        |



 

The preceding table gives a friendly object name for each class. This documentation uses those friendly names to refer to instances of the classes. For example, the documentation refers to an instance of the CTocEntry class as a TOC Entry object.

In code, you can use **\_\_uuidof** to refer to the CLSIDs. For example, you can use the following code to refer to the CLSID for CTocGeneratorDmo.


```C++
__uuidof(CTocGeneratorDmo)
```



### CLSID Constants Defined in Wmcodecdsp.h

As an alternative to using **\_\_uuidof**, you can use constants to refer to the CLSIDs. The following constants are defined in wmcodecdsp.h



| Class name     | CLSID constant        |
|----------------|-----------------------|
| CTocEntry      | CLSID\_CTocEntry      |
| CTocEntryList  | CLSID\_CTocEntryList  |
| CToc           | CLSID\_CToc           |
| CTocCollection | CLSID\_CTocCollection |
| CTocParser     | CLSID\_CTocParser     |



 

### CLSID Constants Defined in Wmcodecdspuuid.lib

The following CLSID constant is declared, but not defined, in wmcodecdsp.h. To use it in code, you must link against wmcodecdspuuid.lib.



| Class name       | CLSID constant          |
|------------------|-------------------------|
| CTocGeneratorDmo | CLSID\_CTocGeneratorDmo |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmvdspa.dll</dt> </dl>  |



## See also

<dl> <dt>

[Table of Contents Parser Objects](toc-parser-objects.md)
</dt> </dl>

 

 




