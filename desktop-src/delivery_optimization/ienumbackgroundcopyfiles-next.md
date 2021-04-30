---
title: IEnumBackgroundCopyFiles Next method (Deliveryoptimization.h)
description: Retrieves a specified number of items in the enumeration sequence. If there are fewer than the requested number of elements left in the sequence, it retrieves the remaining elements.
ms.assetid: 31E603EC-2684-487D-AB37-4C6A6F661298
keywords:
- Next method
- Next method, IEnumBackgroundCopyFiles interface
- IEnumBackgroundCopyFiles interface, Next method
topic_type:
- apiref
api_name:
- IEnumBackgroundCopyFiles.Next
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IEnumBackgroundCopyFiles::Next method

Retrieves a specified number of items in the enumeration sequence. If there are fewer than the requested number of elements left in the sequence, it retrieves the remaining elements.

## Syntax


```C++
HRESULT Next(
  [in]  ULONG               celt,
  [out] IBackgroundCopyFile **rgelt,
  [out] ULONG               *pceltFetched
);
```



## Parameters

<dl> <dt>

*celt* \[in\]
</dt> <dd>

Number of elements requested.

</dd> <dt>

*rgelt* \[out\]
</dt> <dd>

Array of [**IBackgroundCopyFile**](ibackgroundcopyfile.md) objects. You must release each object in *rgelt* when done.

</dd> <dt>

*pceltFetched* \[out\]
</dt> <dd>

Number of elements returned in *rgelt*. You can set *pceltFetched* to **NULL** if *celt* is one. Otherwise, initialize the value of *pceltFetched* to 0 before calling this method.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                                        |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Successfully returned the number of requested elements.<br/> |
| <dl> <dt>**S_FALSE**</dt> </dl>  | Returned less than the number of requested elements.<br/>    |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IEnumBackgroundCopyFiles is defined as CA51E165-C365-424C-8D41-24AAA4FF3C40<br/>         |



## See also

<dl> <dt>

[**IEnumBackgroundCopyFiles**](ienumbackgroundcopyfiles-.md)
</dt> </dl>

 

 





