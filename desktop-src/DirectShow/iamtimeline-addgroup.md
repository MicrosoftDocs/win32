---
description: The AddGroup method adds a group to the timeline.
ms.assetid: c7fc3b59-5852-4a3c-b9bf-f87e659819b5
title: IAMTimeline::AddGroup method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.AddGroup
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::AddGroup method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `AddGroup` method adds a group to the timeline.

## Syntax


```C++
HRESULT AddGroup(
   IAMTimelineObj *pGroup
);
```



## Parameters

<dl> <dt>

*pGroup* 
</dt> <dd>

Pointer to the [**IAMTimelineObj**](iamtimelineobj.md) interface of the group.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Maximum number of groups exceeded.<br/> |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | The object is not a group.<br/>         |



 

## Remarks

Currently, timelines support a maximum of 32 groups.

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

 

 




