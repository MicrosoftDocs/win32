---
description: IMpeg2PsiParser::GetCountOfElementaryStreams method - The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.
ms.assetid: 19ef96a8-3d5b-4da1-8cff-d6a271ad4915
title: IMpeg2PsiParser::GetCountOfElementaryStreams method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMpeg2PsiParser.GetCountOfElementaryStreams
api_type: 
- COM
api_location: 
---

# IMpeg2PsiParser::GetCountOfElementaryStreams method

The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.

The `GetCountOfElementaryStreams` method retrieves the number of elementary streams in a specified program.

## Syntax


```C++
HRESULT GetCountOfElementaryStreams(
  [in]  WORD wProgramNumber,
  [out] WORD *pwVal
);
```



## Parameters

<dl> <dt>

*wProgramNumber* \[in\]
</dt> <dd>

Specifies the program\_number field for the program, as given in the PAT.

</dd> <dt>

*pwVal* \[out\]
</dt> <dd>

Pointer to a variable that receives the number of elementary streams in the program.

</dd> </dl>

## Return value

The method returns an **HRESULT** value. Possible values include, but are not limited to, the values shown in the following table.



| Return code                                                                          | Description         |
|--------------------------------------------------------------------------------------|---------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Success.<br/> |



 

## Remarks

Use the **GetRecordProgramNumber** method to obtain the program number.

## See also

<dl> <dt>

[**IMpeg2PsiParser Interface**](impeg2psiparser.md)
</dt> <dt>

[**IMpeg2PsiParser::GetRecordProgramNumber**](impeg2psiparser-getrecordprogramnumber.md)
</dt> <dt>

[PSI Parser Filter Sample](psi-parser-filter-sample.md)
</dt> </dl>

 

 




