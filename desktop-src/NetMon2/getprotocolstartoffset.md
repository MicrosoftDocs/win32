---
description: Returns the offset of a specified protocol in the frame.
ms.assetid: bfe5f477-c9de-4bb9-99e5-b8db895b0ae6
title: GetProtocolStartOffset function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetProtocolStartOffset
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetProtocolStartOffset function

The **GetProtocolStartOffset** function returns the offset of a specified protocol in the frame.

## Syntax


```C++
DWORD WINAPI GetProtocolStartOffset(
   HFRAME hFrame,
   LPSTR  ProtocolName
);
```



## Parameters

<dl> <dt>

*hFrame* 
</dt> <dd>

A handle to the frame.

</dd> <dt>

*ProtocolName* 
</dt> <dd>

The Protocol name, such as TCP.

</dd> </dl>

## Return value

If the function is successful, the return value is a **DWORD** offset to the beginning of the protocol being searched for   a return value of zero indicates the protocol is the first protocol in the frame.

If the function is unsuccessful, the protocol is not in the frame, the return value is -1.

## Remarks

When given the handle to a frame, this function returns the offset to a specified protocol in the frame. For example, to determine whether the frame is a DNS frame, the DNS parser requires the port address of the TCP protocol. The DNS parser would call this function with TCP as the *ProtocolName* value. If the frame is recognized by the TCP protocol, the **WORD** offset from the beginning of the frame to the beginning of the TCP frame is returned. If there is no TCP protocol, the return value is zero.

This function finds the beginning of a protocol in a frame.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




