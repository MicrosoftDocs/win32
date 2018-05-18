---
title: IImnAccountManager Unadvise method
description: Removes an advise account object from an array of advise account objects at the specified index.
ms.assetid: '2499e0fa-4278-4982-b7e9-b0ba95591eab'
keywords: ["Unadvise method Windows Mail (formerly Outlook Express)", "Unadvise method Windows Mail (formerly Outlook Express) , IImnAccountManager interface", "IImnAccountManager interface Windows Mail (formerly Outlook Express) , Unadvise method"]
topic_type:
- apiref
api_name:
- IImnAccountManager.Unadvise
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IImnAccountManager::Unadvise method

\[**IImnAccountManager::Unadvise** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes an advise account object from an array of advise account objects at the specified index.

## Syntax


```C++
HRESULT Unadvise(
  [in] DWORD dwConnection
);
```



## Parameters

<dl> <dt>

*dwConnection* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the index of the advise account in the array.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                 |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *dwConnection* is out of bounds. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





