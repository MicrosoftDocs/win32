---
description: The BuildINIPath function returns a fully qualified path to an INI file that corresponds to information you enter.
ms.assetid: 214ce89c-8bb2-4e1a-872a-026743a3e3a6
title: BuildINIPath function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BuildINIPath
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# BuildINIPath function

The **BuildINIPath** function returns a fully qualified path to an INI file that corresponds to information you enter.

## Syntax


```C++
LPSTR BuildINIPath(
   char *FullPath,
   char *IniFileName
);
```



## Parameters

<dl> <dt>

*FullPath* 
</dt> <dd>

Buffer that receives the fully qualified INI file name.

</dd> <dt>

*IniFileName* 
</dt> <dd>

Name of the INI file (the full file name minus the filename extension).

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the fully qualified INI file name.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

The path that this function returns is a fully qualified path to an INI file that corresponds to information you enter. For example, if you enter XNS or TCP, the function generates a path to Xns.ini or Tcp.ini, respectively.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Parser.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl>  |



 

 




