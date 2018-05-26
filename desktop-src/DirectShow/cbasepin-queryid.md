---
Description: The QueryId method retrieves the pin identifier. This method implements the IPinQueryId method.
ms.assetid: b365a574-61b4-454c-b062-8826cbe10f03
title: CBasePin.QueryId method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.QueryId method

The `QueryId` method retrieves the pin identifier. This method implements the [**IPin::QueryId**](/windows/win32/Strmif/nf-strmif-ipin-queryid?branch=master) method.

## Syntax


```C++
HRESULT QueryId(
   LPWSTR *Id
);
```



## Parameters

<dl> <dt>

*Id* 
</dt> <dd>

Pointer to the pin identifier.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                   | Description                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/>       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument.<br/> |



 

## Remarks

This method returns a copy of the [**CBasePin::m\_pName**](cbasepin-m-pname.md) member variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




