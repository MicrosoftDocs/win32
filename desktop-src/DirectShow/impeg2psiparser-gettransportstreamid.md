---
description: IMpeg2PsiParser::GetTransportStreamId method - The implementation of this method is provided as sample code with the DirectShow SDK. It is not a supported DirectShow API.
ms.assetid: 0c35abc0-984f-42df-a2a2-30cd400d4599
title: IMpeg2PsiParser::GetTransportStreamId method
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMpeg2PsiParser.GetTransportStreamId
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# IMpeg2PsiParser::GetTransportStreamId method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




