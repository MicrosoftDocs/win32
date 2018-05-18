---
title: IStoreNamespace Initialize method
description: Initializes the namespace object and, if necessary, Windows Mail (formerly Outlook Express).
ms.assetid: '2af0172d-f143-4246-bfee-b86df0680e13'
keywords: ["Initialize method Windows Mail (formerly Outlook Express)", "Initialize method Windows Mail (formerly Outlook Express) , IStoreNamespace interface", "IStoreNamespace interface Windows Mail (formerly Outlook Express) , Initialize method"]
topic_type:
- apiref
api_name:
- IStoreNamespace.Initialize
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreNamespace::Initialize method

Initializes the namespace object and, if necessary, Windows Mail (formerly Outlook Express).

## Syntax


```C++
HRESULT Initialize(
  [in] HWND  hwndOwner,
  [in] DWORD dwReserved
);
```



## Parameters

<dl> <dt>

*hwndOwner* \[in\]
</dt> <dd>

Type: **HWND**

Handle to a window with which this namespace will be associated.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies how the namespace will be initialized. Must be 0 or 1.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the value of *dwReserved* is 0, the namespace will initialize using data associated with the default user identity. If the value of *dwReserved* is 1, the user will be asked to select a user identity to initialize.

Certain methods of the [**IStoreNamespace**](oe-istorenamespace.md) interface may be responsible for displaying dialogs to the user. Providing a valid **HWND** value in the *hwndOwner* argument will ensure proper ordering.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





