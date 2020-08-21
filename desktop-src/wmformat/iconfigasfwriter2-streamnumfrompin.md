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
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter2::StreamNumFromPin method

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

 

 