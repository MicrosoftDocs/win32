---
title: IVMAccessRights \_GetAccessMask method
description: The \_GetAccessMask method retrieves the access rights as a bitmap.
ms.assetid: '4a2723f4-72bd-4fca-981a-66fbb99fd746'
keywords: ["_GetAccessMask method Virtual Server", "_GetAccessMask method Virtual Server , IVMAccessRights interface", "IVMAccessRights interface Virtual Server , _GetAccessMask method"]
topic_type:
- apiref
api_name:
- IVMAccessRights._GetAccessMask
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMAccessRights::\_GetAccessMask method

The **\_GetAccessMask** method retrieves the access rights as a bitmap.

## Syntax


```C++
HRESULT _GetAccessMask(
  [in]  const GENERIC_MAPPING *genericMapping,
  [out]       ACCESS_MASK     *accessMask
);
```



## Parameters

<dl> <dt>

*genericMapping* \[in\]
</dt> <dd>

A **GENERIC\_MAPPING** structure.

</dd> <dt>

*accessMask* \[out\]
</dt> <dd>

The access rights as a bitmap.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                               | Description                              |
|-------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>     | The operation was successful.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl> | A parameter was **NULL**.<br/>     |



 

## Remarks

This method returns the access rights of the object as a bitmap. Generic access rights are mapped to specific rights using the information contained in the *genericMapping* parameter.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccessRights**](ivmaccessrights.md)
</dt> </dl>

 

 





