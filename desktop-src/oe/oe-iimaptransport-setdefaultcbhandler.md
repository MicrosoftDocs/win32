---
title: IIMAPTransport SetDefaultCBHandler method
description: Changes the current default IIMAPCallback object to the specified one.
ms.assetid: c10840a2-09e2-4bb9-b06b-81c379a606dd
keywords:
- SetDefaultCBHandler method Windows Mail (formerly Outlook Express)
- SetDefaultCBHandler method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , SetDefaultCBHandler method
topic_type:
- apiref
api_name:
- IIMAPTransport.SetDefaultCBHandler
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IIMAPTransport::SetDefaultCBHandler method

\[**IIMAPTransport::SetDefaultCBHandler** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Changes the current default [**IIMAPCallback**](oe-iimapcallback.md) object to the specified one.

## Syntax


```C++
HRESULT SetDefaultCBHandler(
  [in] IIMAPCallback *pCBHandler
);
```



## Parameters

<dl> <dt>

*pCBHandler* \[in\]
</dt> <dd>

Type: **[**IIMAPCallback**](oe-iimapcallback.md)\***

Specifies a pointer to the new [**IIMAPCallback**](oe-iimapcallback.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pCBHandler* is **NULL**.<br/> |



 

## Remarks

This method releases the old callback object and adds the *pCBHandler* to the reference count.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





