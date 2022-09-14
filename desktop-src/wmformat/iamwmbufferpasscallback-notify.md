---
title: IAMWMBufferPassCallback Notify method
description: The Notify method is called by the pin for each buffer that is delivered during streaming.
ms.assetid: 3f252754-c784-4ffd-bcfc-fab73fa02b9a
keywords:
- Notify method windows Media Format
- Notify method windows Media Format , IAMWMBufferPassCallback interface
- IAMWMBufferPassCallback interface windows Media Format , Notify method
topic_type:
- apiref
api_name:
- IAMWMBufferPassCallback.Notify
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IAMWMBufferPassCallback::Notify method

The **Notify** method is called by the pin for each buffer that is delivered during streaming.

## Syntax


```C++
HRESULT Notify(
  [in] INSSBuffer3    *pNSSBuffer3,
  [in] IPin           *pPin,
  [in] REFERENCE_TIME *prtStart,
  [in] REFERENCE_TIME *prtEnd
);
```



## Parameters

<dl> <dt>

*pNSSBuffer3* \[in\]
</dt> <dd>

Pointer to the [**INSSBuffer3**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer3) interface exposed on the media sample.

</dd> <dt>

*pPin* \[in\]
</dt> <dd>

Pointer to the pin associated with the media stream that the sample belongs to.

</dd> <dt>

*prtStart* \[in\]
</dt> <dd>

Start time of the sample.

</dd> <dt>

*prtEnd* \[in\]
</dt> <dd>

End time of the sample.

</dd> </dl>

## Return value

No particular return value is specified. The calling pin ignores the **HRESULT**.

## Remarks

This method enables an application to examine and act on information in the media buffer before the buffer contents are processed. The application is responsible for knowing the media type on the pin. This information can be obtained by first getting the stream information from the profile and then calling [**IConfigAsfWriter2::StreamNumFromPin**](iconfigasfwriter2-streamnumfrompin.md) method to determine which pin is associated with each stream.

## See also

<dl> <dt>

[**DirectShow QASF Reference**](directshow-qasf-reference.md)
</dt> <dt>

[**IAMWMBufferPassCallback Interface**](/previous-versions/windows/desktop/api/dshowasf/nn-dshowasf-iamwmbufferpasscallback)
</dt> <dt>

[**INSSBuffer3 Interface**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer3)
</dt> </dl>

 

 