---
title: IIMAPTransport NewIRangeList method
description: Creates a new IRangeList object.
ms.assetid: 3b2cbb23-aa92-4180-ac8c-7e933acf8644
keywords:
- NewIRangeList method Windows Mail (formerly Outlook Express)
- NewIRangeList method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , NewIRangeList method
topic_type:
- apiref
api_name:
- IIMAPTransport.NewIRangeList
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

# IIMAPTransport::NewIRangeList method

\[**IIMAPTransport::NewIRangeList** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a new [**IRangeList**](oe-irangelist.md) object.

## Syntax


```C++
HRESULT NewIRangeList(
  [out] IRangeList **pprlNewRangeList
);
```



## Parameters

<dl> <dt>

*pprlNewRangeList* \[out\]
</dt> <dd>

Type: **[**IRangeList**](oe-irangelist.md)\*\***

Receives the address of a pointer to the new [**IRangeList**](oe-irangelist.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pprlNewRangeList* is **NULL**. <br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





