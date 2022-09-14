---
description: IMpeg2PsiParser::GetRecordProgramNumber method - The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.
ms.assetid: 3800a0b1-a581-40ed-81ab-3d5f77f442df
title: IMpeg2PsiParser::GetRecordProgramNumber method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMpeg2PsiParser.GetRecordProgramNumber
api_type: 
- COM
api_location: 
---

# IMpeg2PsiParser::GetRecordProgramNumber method

The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.

The `GetRecordProgramNumber` method retrieves the program number for a specified program.

## Syntax


```C++
HRESULT GetRecordProgramNumber(
  [in]  DWORD dwIndex,
  [out] WORD  *pwVal
);
```



## Parameters

<dl> <dt>

*dwIndex* \[in\]
</dt> <dd>

Specifies the entry in the PAT that defines the program, indexed from zero.

</dd> <dt>

*pwVal* \[out\]
</dt> <dd>

Pointer to a variable that receives the program\_number field from the PAT.

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

 

 




