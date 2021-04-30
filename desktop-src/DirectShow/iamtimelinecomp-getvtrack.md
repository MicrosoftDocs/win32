---
description: The GetVTrack method retrieves the virtual track at the specified priority.
ms.assetid: e866064b-a511-4f0c-8cb1-62e4f1c42347
title: IAMTimelineComp::GetVTrack method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineComp.GetVTrack
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineComp::GetVTrack method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetVTrack` method retrieves the virtual track at the specified priority.

## Syntax


```C++
HRESULT GetVTrack(
  [out] IAMTimelineObj **ppVirtualTrack,
        long           Which
);
```



## Parameters

<dl> <dt>

*ppVirtualTrack* \[out\]
</dt> <dd>

Receives the virtual track's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> <dt>

*Which* 
</dt> <dd>

Priority of the virtual track to retrieve.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values:



| Return code                                                                                  | Description                                              |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | No virtual track with the specified priority.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | **NULL** pointer argument.<br/>                    |



 

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

[**IAMTimelineComp Interface**](iamtimelinecomp.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




