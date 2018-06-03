---
title: IMimeSecurity2 DeleteAttribute method
description: Deletes the specified attribute data for the specified signer.
ms.assetid: c2107af6-459d-49c7-a1b8-d32dce36db0d
keywords:
- DeleteAttribute method Windows Mail (formerly Outlook Express)
- DeleteAttribute method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface
- IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , DeleteAttribute method
topic_type:
- apiref
api_name:
- IMimeSecurity2.DeleteAttribute
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

# IMimeSecurity2::DeleteAttribute method

Deletes the specified attribute data for the specified signer.

## Syntax


```C++
HRESULT DeleteAttribute(
  [in] DWORD  dwFlags,
  [in] DWORD  iSigner,
  [in] DWORD  iAttributeSet,
  [in] DWORD  iInstance,
  [in] LPCSTR pszObjId
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the value SMIME\_RECIPIENT\_REPLACE\_ALL.

</dd> <dt>

*iSigner* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the index of the signer for which to delete the attributes.

</dd> <dt>

*iAttributeSet* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the attribute set type.

<dl> <dt>

<span id="SMIME_ATTRIBUTE_SET_SIGNED"></span><span id="smime_attribute_set_signed"></span>**SMIME\_ATTRIBUTE\_SET\_SIGNED** (0)
</dt> <dt>

<span id="SMIME_ATTRIBUTE_SET_UNSIGNED"></span><span id="smime_attribute_set_unsigned"></span>**SMIME\_ATTRIBUTE\_SET\_UNSIGNED** (1)
</dt> <dt>

<span id="SMIME_ATTRIBUTE_SET_UNPROTECTED"></span><span id="smime_attribute_set_unprotected"></span>**SMIME\_ATTRIBUTE\_SET\_UNPROTECTED** (2)
</dt> </dl> </dd> <dt>

*iInstance* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the instance to delete for attributes with the same ID. A value of zero indicates the first instance in the attribute set.

</dd> <dt>

*pszObjId* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the ID of the attribute.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                  | Description                                                                                                                                                         |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                                                                                                                      |
| <dl> <dt>**S\_FALSE**</dt> </dl>      | Indicates that the specified attribute doesn't exist. <br/>                                                                                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *dwFlags* or *iAttributeSet* is invalid, that *iSigner* is zero or out of bounds, or that the message does not support S/MIME version 3. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





