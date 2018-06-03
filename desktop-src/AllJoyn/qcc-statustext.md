---
title: QCC\_StatusText function
description: Convert a status code to a C string.
ms.assetid: 95A60B76-C624-4175-935D-2AF03C530A7E
keywords:
- QCC_StatusText function AllJoyn API
topic_type:
- apiref
api_name:
- QCC_StatusText
api_location:
- MSAJApi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QCC\_StatusText function

Convert a status code to a C string.

## Syntax


```C++
CONST CHAR* WINAPI QCC_StatusText(
   QStatus status
);
```



## Parameters

<dl> <dt>

*status* 
</dt> <dd>

Status code to be converted.

</dd> </dl>

## Return value

C string representation of the status code.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps \| UWP apps\]<br/>                            |
| Minimum supported phone<br/>  | Windows 10 Mobile<br/>                                                           |
| Header<br/>                   | <dl> <dt>Status.h</dt> </dl>    |
| Library<br/>                  | <dl> <dt>MSAJApi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSAJApi.dll</dt> </dl> |



 

 





