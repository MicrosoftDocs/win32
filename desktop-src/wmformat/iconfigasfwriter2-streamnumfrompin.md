---
title: IConfigAsfWriter2 StreamNumFromPin method
description: The StreamNumFromPin method retrieves the stream number associated with the specified input pin.
ms.assetid: f645a742-e6dc-4041-8a56-3bbb5188a9a9
keywords:
- StreamNumFromPin method windows Media Format
- StreamNumFromPin method windows Media Format , IConfigAsfWriter2 interface
- IConfigAsfWriter2 interface windows Media Format , StreamNumFromPin method
topic_type:
- apiref
api_name:
- IConfigAsfWriter2.StreamNumFromPin
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IConfigAsfWriter2::StreamNumFromPin method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **StreamNumFromPin** method retrieves the stream number associated with the specified input pin.

## Syntax


```C++
HRESULT StreamNumFromPin(
  [in]  IPin *pPin,
  [out] WORD *pwStreamNum
);
```



## Parameters

<dl> <dt>

*pPin* \[in\]
</dt> <dd>

Pointer to the **IPin** interface on the input pin.

</dd> <dt>

*pwStreamNum* \[out\]
</dt> <dd>

Pointer that receives the stream number.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Remarks

Sometimes you may need to use the Windows Media Format SDK interfaces directly to manipulate a stream before running a filter graph. Because you cannot assume that an ASF stream number is the same as the DirectShow pin number, this method is provided.

## See also

<dl> <dt>

[**IConfigAsfWriter2 Interface**](/previous-versions/windows/desktop/legacy/dd743206(v=vs.85))
</dt> </dl>

 

 