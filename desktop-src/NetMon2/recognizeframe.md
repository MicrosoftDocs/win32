---
description: The RecognizeFrame export function indicates whether a piece of data is recognized as the protocol that the parser detects. The RecognizeFrame export function must be implemented for each parser that the parser DLL supports.
ms.assetid: '3f835f58-b011-4329-b9b2-ff865a1f0ae5'
title: RecognizeFrame callback function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RecognizeFrame
api_type: 
- UserDefined
api_location: 
- Netmon.h
---

# RecognizeFrame callback function

The **RecognizeFrame** export function indicates whether a piece of data is recognized as the protocol that the parser detects. The **RecognizeFrame** export function must be implemented for each parser that the parser DLL supports.

## Syntax


```C++
LPBYTE RecognizeFrame(
  _In_    HFRAME      hFrame,
  _In_    LPBYTE      lpFrame,
  _In_    LPBYTE      lpProtocol,
  _In_    DWORD       MacType,
  _In_    DWORD       BytesLeft,
  _In_    HPROTOCOL   hPreviousProtocol,
  _In_    DWORD       nPreviousProtocolOffset,
  _Out_   LPDWORD     ProtocolStatusCode,
  _Out_   LPHPROTOCOL phNextProtocol,
  _Inout_ PDWORD_PTR  lpInstData
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame that contains the data.

</dd> <dt>

*lpFrame* \[in\]
</dt> <dd>

Pointer to the first byte of a frame. The pointer provides a way to view data that other parsers recognize.

</dd> <dt>

*lpProtocol* \[in\]
</dt> <dd>

Pointer to the start of the unclaimed data. Typically, the unclaimed data is located in the middle of a frame because a previous parser has claimed data before this parser. The parser must test the unclaimed data first.

</dd> <dt>

*MacType* \[in\]
</dt> <dd>

MAC value of the first protocol in a frame. Typically, the *MacType* value is used when the parser must identify the first protocol in a frame. The *MacType* value can be one of the following:



| Value                                                                                                                                                                         | Meaning                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| <span id="MAC_TYPE_ETHERNET"></span><span id="mac_type_ethernet"></span><dl> <dt>**MAC\_TYPE\_ETHERNET**</dt> </dl>    | 802.3 <br/>       |
| <span id="MAC_TYPE_TOKENRING"></span><span id="mac_type_tokenring"></span><dl> <dt>**MAC\_TYPE\_TOKENRING**</dt> </dl> | 802.5 <br/>       |
| <span id="MAC_TYPE_FDDI"></span><span id="mac_type_fddi"></span><dl> <dt>**MAC\_TYPE\_FDDI**</dt> </dl>                | ANSI X3T9.5 <br/> |



 

</dd> <dt>

*BytesLeft* \[in\]
</dt> <dd>

The remaining number of bytes from a location in a frame to the end of the frame.

</dd> <dt>

*hPreviousProtocol* \[in\]
</dt> <dd>

Handle of the previous protocol.

</dd> <dt>

*nPreviousProtocolOffset* \[in\]
</dt> <dd>

Offset of the previous protocol   beginning of the frame.

</dd> <dt>

*ProtocolStatusCode* \[out\]
</dt> <dd>

Protocol status indicator. The parser DLL must set one of the following status codes.



| Value                                                                                                                                                                                                              | Meaning                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PROTOCOL_STATUS_RECOGNIZED"></span><span id="protocol_status_recognized"></span><dl> <dt>**PROTOCOL\_STATUS\_RECOGNIZED**</dt> </dl>              | The parser recognizes the data but does not know which protocol follows. After setting the code, return a pointer to the remaining unclaimed data that follow the recognized protocol. Network Monitor uses the [*follow set*](f.md) of the protocol to continue parsing. <br/> |
| <span id="PROTOCOL_STATUS_NOT_RECOGNIZED"></span><span id="protocol_status_not_recognized"></span><dl> <dt>**PROTOCOL\_STATUS\_NOT\_RECOGNIZED**</dt> </dl> | The parser does not recognize the data. After setting this code, return the pointer to the beginning of the data   using the pointer that the *lpProtocol* parameter passes to the parser DLL. Network Monitor uses the *follow set* of the previous protocol to continue parsing. <br/>                |
| <span id="PROTOCOL_STATUS_CLAIMED"></span><span id="protocol_status_claimed"></span><dl> <dt>**PROTOCOL\_STATUS\_CLAIMED**</dt> </dl>                       | The parser recognizes the data and claims the remaining data. After setting the code, return **NULL** for Network Monitor to terminate parsing a frame. <br/>                                                                                                                                           |
| <span id="PROTOCOL_STATUS_NEXT_PROTOCOL"></span><span id="protocol_status_next_protocol"></span><dl> <dt>**PROTOCOL\_STATUS\_NEXT\_PROTOCOL**</dt> </dl>    | The parser recognizes the data and knows which protocol follows. After setting the code, set the *phNextProtocol* parameter, and return a pointer to the remaining unclaimed data that follow the recognized protocol. Network Monitor continues parsing the frame. <br/>                               |



 

</dd> <dt>

*phNextProtocol* \[out\]
</dt> <dd>

Pointer to the handle of the next protocol. This parameter is set when a protocol identifies the protocol that follows a protocol. To obtain the handle of the next protocol, call the [GetProtocolFromTable](getprotocolfromtable.md) function.

</dd> <dt>

*lpInstData* \[in, out\]
</dt> <dd>

On input, a pointer to the instance data from the previous protocol.

On output, a pointer to the instance data for the current protocol. Instance data cannot be longer than a DWORD\_PTR in length.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the first byte after the recognized parser data. If the parser claims all the remaining data, the return value is **NULL**.

If the function is unsuccessful, the return value is an initial pointer that the *lpProtocol* parameter passes-in.

## Remarks

The **RecognizeFrame** function determines whether the parser recognizes the raw data   starting at the *lpProtocol* pointer.

-   If the protocol recognizes the data, the **RecognizeFrame** function returns a pointer to the remaining data, or returns **NULL** if the current protocol is the last protocol in a frame.
-   If the protocol does not recognize the data, the **RecognizeFrame** function returns the pointer passed to the parser DLL in the *lpProtocol* parameter.

> [!Note]  
> *RecognizeFrame* can be called before the [*Register*](register-parser.md) function is called to register the protocol properties. For that reason, the implementation of the *RecognizeFrame* function does not rely on any properties or structures that are created or initialized during the implementation of the protocol **Register** function.

 

**Handoff Set and Follow Set**

A parser can use a handoff set or follow set to identify for Network Monitor the protocol that follows recognized data.

-   If information is available in recognized data, the parser uses its handoff set to obtain a handle to the next protocol, and then passes that handle to Network Monitor.
-   If information is not available, the parser does not pass a handle, and Network Monitor uses the parser follow set to determine which protocol follows.

**Passing information between protocols**

Use the *lpInstData* parameter to pass information between protocols. On input, you can retrieve the information from the previous protocol. On output, you can pass information to the next protocol.

Instance data can be any data that is less than or equal to a DWORD\_PTR in length, or a pointer to data, such as raw frame data, that does not need to be allocated by or freed by the parser.



| For Information on                                        | See                                                                                                                       |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| What parsers are, and how they work with Network Monitor. | [Parsers](parsers.md)                                                                                                    |
| Which entry points are included in the parser DLL.        | [Parser DLL Architecture](parser-dll-architecture.md)                                                                    |
| How to implement **RecognizeFrame**  includes an example. | [Implementing RecognizeFrame](implementing-recognizeframe.md)                                                            |
| How to specify a handoff set and follow set.              | [Specifying a Handoff Set](specifying-a-handoff-set.md)[Specifying a Follow Set](specifying-a-follow-set.md)<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[GetProtocolFromTable](getprotocolfromtable.md)
</dt> </dl>

 

 




