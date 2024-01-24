---
description: The CreateNPPInterface function uses the BLOB returned from the finder to create an NPP that the application can use.
ms.assetid: 41f48c72-3284-4ebc-baff-63553c8971e6
title: CreateNPPInterface function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreateNPPInterface
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# CreateNPPInterface function

The **CreateNPPInterface** function uses the BLOB returned from the finder to create an NPP that the application can use.

## Syntax


```C++
DWORD CreateNPPInterface(
  _In_  HBLOB  hBlob,
  _In_  REFIID iid,
  _Out_ void   **ppvObject
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to the BLOB returned from the finder.

</dd> <dt>

*iid* \[in\]
</dt> <dd>

Identifier of the interface that you call from the NPP (**IRTC** or **IDelaydC**, for example).

</dd> <dt>

*ppvObject* \[out\]
</dt> <dd>

Pointer to the returned pointer to the requested interface.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that describes the error.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



 

 




