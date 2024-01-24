---
description: Finds the next frame in the current capture context that matches the filter.
ms.assetid: cc99b4a0-b6b0-43b4-8121-0e402d024009
title: FindNextFrame function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FindNextFrame
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# FindNextFrame function

The **FindNextFrame** function finds the next frame in the current capture context that matches the filter.

## Syntax


```C++
HFRAME WINAPI FindNextFrame(
   HFRAME    hCurrentFrame,
   LPSTR     ProtocolName,
   LPADDRESS DestinationAddress,
   LPADDRESS SourceAddress,
   LPWORD    ProtocolOffset,
   DWORD     OriginalFrameNumber,
   DWORD     HighestFrame
);
```



## Parameters

<dl> <dt>

*hCurrentFrame* 
</dt> <dd>

A handle to the frame.

</dd> <dt>

*ProtocolName* 
</dt> <dd>

The protocol name, such as TCP.

</dd> <dt>

*DestinationAddress* 
</dt> <dd>

The destination address.

</dd> <dt>

*SourceAddress* 
</dt> <dd>

The source address.

</dd> <dt>

*ProtocolOffset* 
</dt> <dd>

A pointer to a **WORD** that will receive the protocol offset.

</dd> <dt>

*OriginalFrameNumber* 
</dt> <dd>

The starting point of the search. By default, this function searches forward 1,000 frames from the *OriginalFrameNumber* starting point. To change the search-forward distance, add this line to the Nmapi.ini file, located in the \\Network Monitor directory.

MAXLOOKBACK=\<new lookforward distance\>

</dd> <dt>

*HighestFrame* 
</dt> <dd>

The highest frame number in the capture that is searched.

</dd> </dl>

## Return value

If the function is successful, the return value is a handle to the next frame.

If the function is not successful, the return value is **NULL**.

## Remarks

The capture filter is defined primarily by the *ProtocolName* parameter, which is the only required filter input; you can add *DestinationAddress* and *SourceAddress* data to increase the capture speed.

The *ProtocolOffset* pointer is returned to the calling parser, which adds the **WORD** to the pointer returned by locking the frame (with [ParserTemporaryLockFrame](parsertemporarylockframe.md)) to get the **LPBYTE** of the protocol searched for. On return, the HFRAME that passed the filter is given to the parser. If the parser finds that this frame is not the one sought, the parser can hand the HFRAME back to the **FindNextFrame** function to get the next frame. The source and destination addresses are not required and can be passed as **NULL**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




