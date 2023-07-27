---
description: IMpeg2PsiParser::GetPmtVersionNumber method - The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.
ms.assetid: 50113d6b-4e10-4dc9-aaef-f67c6918a2de
title: IMpeg2PsiParser::GetPmtVersionNumber method
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMpeg2PsiParser.GetPmtVersionNumber
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# IMpeg2PsiParser::GetPmtVersionNumber method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




