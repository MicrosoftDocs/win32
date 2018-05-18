---
title: IMimePropertySchema GetPropertyName method
description: Looks up the property name for the specified property ID.
ms.assetid: '3794abde-0181-4f86-acb0-175675ced730'
keywords: ["GetPropertyName method Windows Mail (formerly Outlook Express)", "GetPropertyName method Windows Mail (formerly Outlook Express) , IMimePropertySchema interface", "IMimePropertySchema interface Windows Mail (formerly Outlook Express) , GetPropertyName method"]
topic_type:
- apiref
api_name:
- IMimePropertySchema.GetPropertyName
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimePropertySchema::GetPropertyName method

Looks up the property name for the specified property ID.

## Syntax


```C++
HRESULT GetPropertyName(
  [in]  DWORD dwPropId,
  [out] LPSTR *ppszName
);
```



## Parameters

<dl> <dt>

*dwPropId* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the property ID.

</dd> <dt>

*ppszName* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to a **LPSTR** that contains the property name.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                                    |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success. <br/>                                                                 |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred. <br/>                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *ppszName* is **NULL**.<br/>                                              |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that the property identified by *dwPropId* does not exist in the schema. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





