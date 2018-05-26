---
Description: The QueryInternalConnections method retrieves the pins that are connected internally to this pin (within the filter). This method implements the IPinQueryInternalConnections method.
ms.assetid: 08344fc5-38b2-4dbe-8ef9-30d2fcd64187
title: CBasePin.QueryInternalConnections method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.QueryInternalConnections method

The `QueryInternalConnections` method retrieves the pins that are connected internally to this pin (within the filter). This method implements the [**IPin::QueryInternalConnections**](/windows/win32/Strmif/nf-strmif-ipin-queryinternalconnections?branch=master) method.

## Syntax


```C++
HRESULT QueryInternalConnections(
   IPin  *apPin,
   ULONG *nPin
);
```



## Parameters

<dl> <dt>

*apPin* 
</dt> <dd>

Address of an array of [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) pointers.

</dd> <dt>

*nPin* 
</dt> <dd>

On input, specifies the size of the array. When the method returns, the value is set to the number of pointers returned in the array.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                               | Description                         |
|-------------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>   | Insufficient array size.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                 |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | Failure.<br/>                 |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | Not implemented.<br/>         |



 

## Remarks

On some filters, input pins correspond to particular output pins. For each pin, this method fills an array with pointers to the corresponding pins. If every input pin provides data for every output pin, return E\_NOTIMPL.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




