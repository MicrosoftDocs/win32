---
description: The FindPreviousFrame function finds the previous frame in the current capture context that matches the filter.
ms.assetid: 16c5b981-a9f4-41e5-bb97-2caa3e9d8512
title: FindPreviousFrame function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FindPreviousFrame
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# FindPreviousFrame function

The **FindPreviousFrame** function finds the previous frame in the current capture context that matches the filter.

## Syntax


```C++
HFRAME WINAPI FindPreviousFrame(
   HFRAME    hCurrentFrame,
   LPSTR     ProtocolName,
   LPADDRESS DestinationAddress,
   LPADDRESS SourceAddress,
   LPWORD    ProtocolOffset,
   DWORD     OriginalFrameNumber,
   DWORD     LowestFrame
);
```



## Parameters

<dl> <dt>

*hCurrentFrame* 
</dt> <dd>

Handle to the frame.

</dd> <dt>

*ProtocolName* 
</dt> <dd>

Protocol name, such as TCP.

</dd> <dt>

*DestinationAddress* 
</dt> <dd>

Destination address of the frame that is searched for.

</dd> <dt>

*SourceAddress* 
</dt> <dd>

Source address of the frame that is searched for.

</dd> <dt>

*ProtocolOffset* 
</dt> <dd>

Pointer to a **WORD** that receives the protocol offset.

</dd> <dt>

*OriginalFrameNumber* 
</dt> <dd>

Starting point of the search. By default, this function searches backward 1,000 frames from *OriginalFrameNumber* starting point. You can change the search-back distance by adding this line to the Nmapi.ini file, which is located in the \\Network Monitor directory.

MAXLOOKBACK=\<new lookback distance\>

</dd> <dt>

*LowestFrame* 
</dt> <dd>

Lowest frame number in the capture that is searched.

</dd> </dl>

## Return value

If the function is successful, the return value is a handle to the previous frame.

If the function is not successful, the return value is **NULL**.

## Remarks

The capture filter is defined primarily by *ProtocolName*, which is the only required filter input; you can add *DestinationAddress* and *SourceAddress* information to increase the capture speed.

*ProtocolOffset* is returned to the calling parser, which adds this **DWORD** to the pointer returned by locking the frame (with [ParserTemporaryLockFrame](parsertemporarylockframe.md)) to get the LPBYTE of the protocol that is being searched for. On return, the HFRAME that passed the filter is given to the parser. If the parser finds that the frame is not the one that is being sought, the parser can hand this HFRAME back to the **FindPreviousFrame** function to retrieve the next frame. The source and destination addresses, which are not required, can be passed in as **NULL**. When used, these addresses can be of type ADDRESS\_TYPE\_IP, and so on, not just MAC types.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




