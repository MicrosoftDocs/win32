---
description: IMpeg2PsiParser::GetTransportStreamId method - The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.
ms.assetid: 0c35abc0-984f-42df-a2a2-30cd400d4599
title: IMpeg2PsiParser::GetTransportStreamId method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMpeg2PsiParser.GetTransportStreamId
api_type: 
- COM
api_location: 
---

# IMpeg2PsiParser::GetTransportStreamId method

The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.

The `GetTransportStreamId` method retrieves the transport\_stream\_id field from the PAT. This value is defined by the user, and can be used to distinguish a particular transport stream from other streams on the same network. A transport stream contains at most one PAT.

## Syntax


```C++
HRESULT GetTransportStreamId(
  [out] WORD *pStreamId
);
```



## Parameters

<dl> <dt>

*pStreamId* \[out\]
</dt> <dd>

Pointer to a variable that receives the transport\_stream\_id field.

</dd> </dl>

## Return value

The method returns an **HRESULT** value. Possible values include, but are not limited to, the values shown in the following table.



| Return code                                                                          | Description         |
|--------------------------------------------------------------------------------------|---------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Success.<br/> |



 

## See also

<dl> <dt>

[**IMpeg2PsiParser Interface**](impeg2psiparser.md)
</dt> <dt>

[PSI Parser Filter Sample](psi-parser-filter-sample.md)
</dt> </dl>

 

 




