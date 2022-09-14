---
description: Learn about the IAMFilterData::CreateFilterData method, which creates binary registry data for a filter. This interface has been deprecated.
ms.assetid: ab6972ef-7c28-4cd1-b007-eb70f9aeb2cb
title: IAMFilterData::CreateFilterData method (Fil\_data.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMFilterData.CreateFilterData
api_type: 
- COM
api_location: 
- Quartz.dll
---

# IAMFilterData::CreateFilterData method

> [!Note]  
> This interface has been deprecated. New applications should not use it.

 

The `CreateFilterData` method creates binary registry data for a filter. This data can be written to the registry as a REG\_BINARY subkey named FilterData, under the filter's CLSID key.

There is typically no reason for an application to call this method. The [**IFilterMapper2::RegisterFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-registerfilter) method automatically creates the binary data and adds it to the correct location in the registry. For more information, see [How to Register DirectShow Filters](how-to-register-directshow-filters.md).

## Syntax


```C++
HRESULT CreateFilterData(
  [in]  REGFILTER2 *prf2,
  [out] BYTE       **prgbFilterData,
  [out] ULONG      *pcb
);
```



## Parameters

<dl> <dt>

*prf2* \[in\]
</dt> <dd>

Pointer to a [**REGFILTER2**](/windows/desktop/api/strmif/ns-strmif-regfilter2) structure that contains the filter information.

</dd> <dt>

*prgbFilterData* \[out\]
</dt> <dd>

Address of a variable that receives a pointer to the binary data. The method allocates the memory for the data. The caller must release the memory by calling the **CoTaskMemFree** method.

</dd> <dt>

*pcb* \[out\]
</dt> <dd>

Pointer to a variable that receives the size of the binary data, in bytes.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an error code.

## Remarks

> [!Note]  
> The header Fil\_data.h is located in the [Mapper Sample](mapper-sample.md) directory in the Windows SDK.

 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Fil\_data.h</dt> </dl> |
| DLL<br/>    | <dl> <dt>Quartz.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IAMFilterData Interface**](iamfilterdata.md)
</dt> </dl>

 

 




