---
title: IStoreFolder FreeMessageProps method
description: Frees memory associated with a MESSAGEPROPS structure.
ms.assetid: '79235431-059d-4ee0-b433-c7a49dff6616'
keywords: ["FreeMessageProps method Windows Mail (formerly Outlook Express)", "FreeMessageProps method Windows Mail (formerly Outlook Express) , IStoreFolder interface", "IStoreFolder interface Windows Mail (formerly Outlook Express) , FreeMessageProps method"]
topic_type:
- apiref
api_name:
- IStoreFolder.FreeMessageProps
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreFolder::FreeMessageProps method

Frees memory associated with a [**MESSAGEPROPS**](oe-messageprops.md) structure.

## Syntax


```C++
HRESULT FreeMessageProps(
  [in, out] LPMESSAGEPROPS pProps
);
```



## Parameters

<dl> <dt>

*pProps* \[in, out\]
</dt> <dd>

Type: **LPMESSAGEPROPS**

Pointer to a [**MESSAGEPROPS**](oe-messageprops.md) structure that will be freed.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                      | Description                                                                             |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                     | An invalid argument was passed to the method.<br/>                                |
| <dl> <dt>**MSOEAPI\_E\_INVALID\_STRUCT\_SIZE**</dt> </dl> | The structure specified by the *pProps* argument is not the correct version.<br/> |



 

## Remarks

This method should be used instead of the **delete** operator when manipulating [**MESSAGEPROPS**](oe-messageprops.md) structures.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





