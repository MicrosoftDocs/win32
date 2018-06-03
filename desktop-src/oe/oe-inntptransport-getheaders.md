---
title: INNTPTransport GetHeaders method
description: Retrieves an array of headers from the server.
ms.assetid: 3c74af14-759e-494f-a5b3-3f1357fa8e85
keywords:
- GetHeaders method Windows Mail (formerly Outlook Express)
- GetHeaders method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , GetHeaders method
topic_type:
- apiref
api_name:
- INNTPTransport.GetHeaders
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INNTPTransport::GetHeaders method

\[**INNTPTransport::GetHeaders** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves an array of headers from the server. If a `GROUP` command has not been previously sent this command is not valid. This function will first try to retrieve the specified range of headers using the `XOVER` command. If the server doesn't support `XOVER`, then the function tries other methods such as a series of `XHDR` commands.

## Syntax


```C++
HRESULT GetHeaders(
  [in] LPRANGE pRange
);
```



## Parameters

<dl> <dt>

*pRange* \[in\]
</dt> <dd>

Type: **LPRANGE**

The range of headers to request. See the documentation for the [**RANGE**](oe-range.md) structure above to see how to specify a range.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | An invalid parameter was passed in<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An memory allocation failed<br/>        |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





