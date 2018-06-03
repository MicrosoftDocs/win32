---
title: IRangeList RangeToIMAPString method
description: Returns the message range list as an Internet Message Access Protocol (IMAP) message set string for use with IMAP commands.
ms.assetid: 76145413-df05-417f-badf-27dd289f6707
keywords:
- RangeToIMAPString method Windows Mail (formerly Outlook Express)
- RangeToIMAPString method Windows Mail (formerly Outlook Express) , IRangeList interface
- IRangeList interface Windows Mail (formerly Outlook Express) , RangeToIMAPString method
topic_type:
- apiref
api_name:
- IRangeList.RangeToIMAPString
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

# IRangeList::RangeToIMAPString method

\[**IRangeList::RangeToIMAPString** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the message range list as an Internet Message Access Protocol (IMAP) message set string for use with IMAP commands.

## Syntax


```C++
HRESULT RangeToIMAPString(
  [out] LPSTR   *ppszDestination,
  [out] LPDWORD pdwLengthOfDestination
);
```



## Parameters

<dl> <dt>

*ppszDestination* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the IMAP message set string. The client is responsible for freeing this buffer by calling [CoTaskMemFree](http://msdn.microsoft.com/library/com/htm/cmf_a2c_63l1.asp).

</dd> <dt>

*pdwLengthOfDestination* \[out\]
</dt> <dd>

Type: **LPDWORD**

Receives an **LPDWORD** that contains the length of the IMAP message set string (excluding the terminating null character).

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





