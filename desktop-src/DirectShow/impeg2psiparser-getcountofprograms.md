---
description: IMpeg2PsiParser::GetCountOfPrograms method - The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.
ms.assetid: 282dd779-9aca-46e3-a791-cb9ea86f637d
title: IMpeg2PsiParser::GetCountOfPrograms method
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMpeg2PsiParser.GetCountOfPrograms
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# IMpeg2PsiParser::GetCountOfPrograms method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.

The `GetCountOfPrograms` method retrieves the number of programs in the transport stream.

## Syntax


```C++
HRESULT GetCountOfPrograms(
  [out] int *pNumOfPrograms
);
```



## Parameters

<dl> <dt>

*pNumOfPrograms* \[out\]
</dt> <dd>

Pointer to a variable that receives the number of programs.

</dd> </dl>

## Return value

The method returns an HRESULT value. Possible values include, but are not limited to, the values shown in the following table.



| Return code                                                                          | Description         |
|--------------------------------------------------------------------------------------|---------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Success.<br/> |



 

## See also

<dl> <dt>

[**IMpeg2PsiParser Interface**](impeg2psiparser.md)
</dt> <dt>

[PSI Parser Filter Sample](psi-parser-filter-sample.md)
</dt> </dl>

 

 




