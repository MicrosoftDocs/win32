---
title: IMimePropertySchema GetPropertyId method
description: Looks up the property ID for the specified property name.
ms.assetid: b0e54de6-5fff-43b4-bfe2-4312a8066dcd
keywords:
- GetPropertyId method Windows Mail (formerly Outlook Express)
- GetPropertyId method Windows Mail (formerly Outlook Express) , IMimePropertySchema interface
- IMimePropertySchema interface Windows Mail (formerly Outlook Express) , GetPropertyId method
topic_type:
- apiref
api_name:
- IMimePropertySchema.GetPropertyId
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

# IMimePropertySchema::GetPropertyId method

Looks up the property ID for the specified property name.

## Syntax


```C++
HRESULT GetPropertyId(
  [in]  LPCSTR  pszName,
  [out] LPDWORD pdwPropId
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name.

</dd> <dt>

*pdwPropId* \[out\]
</dt> <dd>

Type: **LPDWORD**

Receives the property ID.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                                   |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success. <br/>                                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred. <br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pszName* or *pdwPropId* is **NULL**. <br/>                              |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that the property identified by *pszName* does not exist in the schema. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





