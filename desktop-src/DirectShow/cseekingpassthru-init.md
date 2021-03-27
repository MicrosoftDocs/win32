---
description: The Init method initializes the object.
ms.assetid: a919adfa-0ffb-4241-b709-ad0e8d55476a
title: CSeekingPassThru.Init method (Seekpt.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSeekingPassThru.Init
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSeekingPassThru.Init method

The `Init` method initializes the object.

## Syntax


```C++
HRESULT Init(
  [in] BOOL bSupportRendering,
       IPin *pPin
);
```



## Parameters

<dl> <dt>

*bSupportRendering* \[in\]
</dt> <dd>

Boolean value that specifies whether the filter is a renderer. Use the value **TRUE** if the filter is a renderer, or **FALSE** otherwise.

</dd> <dt>

*pPin* 
</dt> <dd>

Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface on the filter's input pin.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                   | Description                                        |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Object was already initialized.<br/>         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Not enough memory to create the object.<br/> |



 

## Remarks

If the value of *bSupportRendering* is **TRUE**, this method creates an instance of the [**CRendererPosPassThru**](crendererpospassthru.md) class. Otherwise, it creates an instance of the [**CPosPassThru**](cpospassthru.md) class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Seekpt.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSeekingPassThru Class**](cseekingpassthru.md)
</dt> </dl>

 

 




