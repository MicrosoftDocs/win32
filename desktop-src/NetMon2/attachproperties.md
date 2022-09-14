---
description: The AttachProperties export function maps the properties to a location within a piece of recognized data. AttachProperties must be implemented for each parser that the parser DLL supports.
ms.assetid: ef28f571-8364-47d0-841c-580e89333afd
title: AttachProperties callback function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AttachProperties
api_type: 
- UserDefined
api_location: 
- Netmon.h
---

# AttachProperties callback function

The **AttachProperties** export function maps the properties to a location within a piece of recognized data. **AttachProperties** must be implemented for each parser that the parser DLL supports.

## Syntax


```C++
DWORD AttachProperties(
  _In_ HFRAME    hFrame,
  _In_ LPBYTE    lpFrame,
  _In_ LPBYTE    lpProtocol,
  _In_ DWORD     MacType,
  _In_ DWORD     BytesLeft,
  _In_ HPROTOCOL hPreviousProtocol,
  _In_ DWORD     nPreviousProtocolOffset,
  _In_ DWORD     lpInstData
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle of the frame that is being parsed.

</dd> <dt>

*lpFrame* \[in\]
</dt> <dd>

Pointer to the first byte in a frame.

</dd> <dt>

*lpProtocol* \[in\]
</dt> <dd>

Pointer to the start of the recognized data.

</dd> <dt>

*MacType* \[in\]
</dt> <dd>

MAC value of the first protocol in a frame. The *MacType* can be one of the following:



| Value                                                                                                                                                                         | Meaning                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| <span id="MAC_TYPE_ETHERNET"></span><span id="mac_type_ethernet"></span><dl> <dt>**MAC\_TYPE\_ETHERNET**</dt> </dl>    | 802.3 <br/>       |
| <span id="MAC_TYPE_TOKENRING"></span><span id="mac_type_tokenring"></span><dl> <dt>**MAC\_TYPE\_TOKENRING**</dt> </dl> | 802.5 <br/>       |
| <span id="MAC_TYPE_FDDI"></span><span id="mac_type_fddi"></span><dl> <dt>**MAC\_TYPE\_FDDI**</dt> </dl>                | ANSI X3T9.5 <br/> |



 

</dd> <dt>

*BytesLeft* \[in\]
</dt> <dd>

The remaining number of bytes in a frame   starting at the beginning of the recognized data.

</dd> <dt>

*hPreviousProtocol* \[in\]
</dt> <dd>

Handle of the previous protocol.

</dd> <dt>

*nPreviousProtocolOffset* \[in\]
</dt> <dd>

Offset of the previous protocol   starting at the beginning of the frame.

</dd> <dt>

*lpInstData* \[in\]
</dt> <dd>

Pointer to the instance data that the previous protocol provides. Instance data cannot be longer than a DWORD\_PTR in length.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the first byte after the recognized data in a frame or **NULL** if the recognized data is the last piece of data in a frame.

If the function is unsuccessful, the return value is a pointer to the recognized data. The *lpProtocol* parameter passes the pointer to the parser DLL.

## Remarks

Network Monitor calls the **AttachProperties** function for each parser that recognizes a piece of data in a frame. Note that the parser determines which properties exist in the recognized data, and where each property is located.

During the implementation of **AttachProperties**, call [AttachPropertyInstance](attachpropertyinstance.md) to use the data as it exists in the capture. You can also call [AttachPropertyInstanceEx](attachpropertyinstanceex.md) function to modify the property data. However, it is advised that you use the data as it exists in the capture.

The **AttachPropertyInstanceEx** and **AttachPropertyInstance** functions are called only for the properties that exist in the recognized data. Note that Network Monitor has a [*property database*](p.md) for the parser that contains a description of all the properties that the parser supports.

**Instance data**

Instance data is information that is passed from one parser to another. Instance data can be any data that is less than or equal to a DWORD\_PTR in length, or a pointer to data, such as raw frame data, that does not need to be allocated by or freed by the parser. In the *lpInstData* parameter of the **AttachProperties** and [RecognizeFrame](recognizeframe.md) functions, Network Monitor provides a pointer to the instance data of the previous protocol. You can set the instance data for your parser during your implementation of **RecognizeFrame**.



| For information on                                          | See                                                                |
|-------------------------------------------------------------|--------------------------------------------------------------------|
| What parsers are, and how they work with Network Monitor.   | [Parsers](parsers.md)                                             |
| What entry points are included in the parser DLL.           | [Parser DLL Architecture](parser-dll-architecture.md)             |
| How to recognize data.                                      | [Implementing RecognizeFrame](implementing-recognizeframe.md)     |
| How to create a property database.                          | [Implementing Register](implementing-register.md)                 |
| How to implement **AttachProperties**  includes an example. | [Implementing AttachProperties](implementing-attachproperties.md) |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[AttachPropertyInstance](attachpropertyinstance.md)
</dt> <dt>

[AttachPropertyInstanceEx](attachpropertyinstanceex.md)
</dt> <dt>

[RecognizeFrame](recognizeframe.md)
</dt> </dl>

 

 




