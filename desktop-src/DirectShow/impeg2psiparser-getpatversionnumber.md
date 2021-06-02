---
description: IMpeg2PsiParser::GetPatVersionNumber method - The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.
ms.assetid: 2f5ad9bf-3d70-491a-ab45-15cd922a02d4
title: IMpeg2PsiParser::GetPatVersionNumber method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMpeg2PsiParser.GetPatVersionNumber
api_type: 
- COM
api_location: 
---

# IMpeg2PsiParser::GetPatVersionNumber method

The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.

The `GetPatVersionNumber` method retrieves the version\_number field from the PAT. A transport stream contains at most one PAT. The version number is incremented whenever the information in the table changes.

## Syntax


```C++
HRESULT GetPatVersionNumber(
  [out] BYTE *pPatVersion
);
```



## Parameters

<dl> <dt>

*pPatVersion* \[out\]
</dt> <dd>

Pointer to a variable that receives the version\_number field.

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

 

 




