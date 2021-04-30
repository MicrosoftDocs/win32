---
description: The GetGroup method retrieves a specified group.
ms.assetid: 4ff651e5-a3aa-4da9-af23-a3a2bdbf7c5b
title: IAMTimeline::GetGroup method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.GetGroup
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::GetGroup method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetGroup` method retrieves a specified group.

## Syntax


```C++
HRESULT GetGroup(
  [out] IAMTimelineObj **ppGroup,
        long           WhichGroup
);
```



## Parameters

<dl> <dt>

*ppGroup* \[out\]
</dt> <dd>

Receives a pointer to the group's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> <dt>

*WhichGroup* 
</dt> <dd>

Index of the group to retrieve, based on the order in which the groups were added to the timeline. The first group added to the timeline has an index of 0.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the method succeeds, the **IAMTimelineObj** interface that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimeline Interface**](iamtimeline.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




