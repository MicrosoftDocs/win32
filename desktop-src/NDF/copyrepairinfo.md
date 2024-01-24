---
title: CopyRepairInfo function (Ndattributils.h)
description: Creates a copy of a RepairInfo structure.
ms.assetid: a1147ce6-9a90-4a46-8fe4-da3353391a13
keywords:
- CopyRepairInfo function NDF
topic_type:
- apiref
api_name:
- CopyRepairInfo
api_location:
- ndattributils.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CopyRepairInfo function

The **CopyRepairInfo** function creates a copy of a [**RepairInfo**](/windows/win32/api/ndattrib/ns-ndattrib-repairinfo) structure.

## Syntax


```C++
HRESULT CopyRepairInfo(
  _Out_       RepairInfo *Dest,
  _In_  const RepairInfo *Source
);
```



## Parameters

<dl> <dt>

*Dest* \[out\]
</dt> <dd>

Type: **[**RepairInfo**](/windows/win32/api/ndattrib/ns-ndattrib-repairinfo)\***

The structure to be updated.

</dd> <dt>

*Source* \[in\]
</dt> <dd>

Type: **const [**RepairInfo**](/windows/win32/api/ndattrib/ns-ndattrib-repairinfo)\***

The existing structure to be copied.

</dd> </dl>

## Return value

Type: **HRESULT**

Possible return values include, but are not limited to, the following.



| Return code                                                                                   | Description                                                                 |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The operation succeeded.<br/>                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One or more parameters has not been provided correctly.<br/>          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | There is not enough memory available to complete this operation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Ndattributils.h</dt> </dl> |



## See also

<dl> <dt>

[**RepairInfo**](/windows/win32/api/ndattrib/ns-ndattrib-repairinfo)
</dt> </dl>

 

 





