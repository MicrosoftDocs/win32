---
description: IMpeg2PsiParser::GetPmtVersionNumber method - The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.
ms.assetid: 50113d6b-4e10-4dc9-aaef-f67c6918a2de
title: IMpeg2PsiParser::GetPmtVersionNumber method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMpeg2PsiParser.GetPmtVersionNumber
api_type: 
- COM
api_location: 
---

# IMpeg2PsiParser::GetPmtVersionNumber method

The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.

The `GetPmtVersionNumber` method retrieves the version\_number field from a specified PMT. The version number is incremented whenever the definition of the program changes.

## Syntax


```C++
HRESULT GetPmtVersionNumber(
  [in]  WORD wProgramNumber,
  [out] BYTE *pPmtVersion
);
```



## Parameters

<dl> <dt>

*wProgramNumber* \[in\]
</dt> <dd>

Specifies the program\_number field of the program, as given in the PAT.

</dd> <dt>

*pPmtVersion* \[out\]
</dt> <dd>

Pointer to a variable that receives the version\_number field.

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

 

 




