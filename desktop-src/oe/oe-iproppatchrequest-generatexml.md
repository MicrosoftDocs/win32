---
title: IPropPatchRequest GenerateXML method
description: Generates the XML to be sent as part of a PROPPATCH request for setting and removing properties.
ms.assetid: '1a7f4609-d515-4824-ae38-b0e7d733708e'
keywords: ["GenerateXML method Windows Mail (formerly Outlook Express)", "GenerateXML method Windows Mail (formerly Outlook Express) , IPropPatchRequest interface", "IPropPatchRequest interface Windows Mail (formerly Outlook Express) , GenerateXML method"]
topic_type:
- apiref
api_name:
- IPropPatchRequest.GenerateXML
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IPropPatchRequest::GenerateXML method

\[**IPropPatchRequest::GenerateXML** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Generates the XML to be sent as part of a PROPPATCH request for setting and removing properties.

## Syntax


```C++
HRESULT GenerateXML(
  [out] LPSTR *pszXML
);
```



## Parameters

<dl> <dt>

*pszXML* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the generated XML.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszXML* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





