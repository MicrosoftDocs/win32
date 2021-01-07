---
description: Retrieves the source address of a frame.
ms.assetid: 414f9e64-f1b2-46f1-822e-0fffacfad843
title: GetFrameSourceAddress function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameSourceAddress
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameSourceAddress function

The **GetFrameSourceAddress** function retrieves the source address of a frame.

## Syntax


```C++
DWORD WINAPI GetFrameSourceAddress(
   HFRAME    hFrame,
   LPADDRESS lpAddress,
   DWORD     AddressType,
   DWORD     Flags
);
```



## Parameters

<dl> <dt>

*hFrame* 
</dt> <dd>

A handle to the frame for which to get a pointer to.

</dd> <dt>

*lpAddress* 
</dt> <dd>

A return buffer that stores the frame source address.

</dd> <dt>

*AddressType* 
</dt> <dd>

The type of address searched for, such as ADDRESS\_TYPE\_ETHERNET or ADDRESS\_TYPE\_IP.

</dd> <dt>

*Flags* 
</dt> <dd>

The flags used to modify returned source address data.



| Value                                                                                                                                                                                                           | Meaning                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span id="ADDRESSTYPE_FLAGS_NORMALIZE"></span><span id="addresstype_flags_normalize"></span><dl> <dt>**ADDRESSTYPE\_FLAGS\_NORMALIZE**</dt> </dl>        | Cancels the routing and group BITs.<br/>                   |
| <span id="ADDRESSTYPE_FLAGS_BIT_REVERSE"></span><span id="addresstype_flags_bit_reverse"></span><dl> <dt>**ADDRESSTYPE\_FLAGS\_BIT\_REVERSE**</dt> </dl> | Converts token ring network addresses back to normal.<br/> |



 

</dd> </dl>

## Return value

If the function is successful, the *lpAddress* value is valid, and the return value is BHERR\_SUCCESS.

If the function is unsuccessful, the return value is an error code.



| Return code                                                                                                | Description                                                                                |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| <dl> <dt>**BHERR\_PROTOCOL\_NOT\_FOUND**</dt> </dl> | The protocol specified by the *AddressType* parameter is invalid for the frame.<br/> |
| <dl> <dt>**BHERR\_INVALID\_HFRAME**</dt> </dl>      | The *hFrame* parameter value is invalid.<br/>                                        |



 

## Remarks

An address type of **ADDRESS\_TYPE\_FIND\_HIGHEST** is allowed. When this address type is used, the function searches for the IPX, XNS, IP, or VINES IP address before returning the ETHERNET, TOKENRING, or FDDI address. This approach is useful for protocols and environments in which two NICs can be multiplexed under a single server address.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




