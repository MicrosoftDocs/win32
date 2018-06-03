---
Description: The QueryVendorInfo method retrieves a string containing vendor information. This method implements the IBaseFilter::QueryVendorInfo method.
ms.assetid: 083c0556-d516-4daf-8621-e158ea78b5a3
title: CBaseFilter.QueryVendorInfo method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseFilter.QueryVendorInfo method

The `QueryVendorInfo` method retrieves a string containing vendor information. This method implements the [**IBaseFilter::QueryVendorInfo**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-queryvendorinfo) method.

## Syntax


```C++
HRESULT QueryVendorInfo(
   LPWSTR *pVendorInfo
);
```



## Parameters

<dl> <dt>

*pVendorInfo* 
</dt> <dd>

Address of a variable that receives a pointer to a wide-character string containing the vendor information.

</dd> </dl>

## Return value

Returns E\_NOTIMPL.

## Remarks

To provide vendor information for a filter, override this method. If you implement this method, use the **CoTaskMemAlloc** function to allocate memory for the string. The caller is responsible for calling the **CoTaskMemFree** function.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




