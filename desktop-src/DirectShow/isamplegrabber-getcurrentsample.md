---
description: The GetCurrentSample method is not implemented.
ms.assetid: 0c903498-3c1d-4e95-a797-ca8cfded25f2
title: ISampleGrabber::GetCurrentSample method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISampleGrabber.GetCurrentSample
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# ISampleGrabber::GetCurrentSample method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetCurrentSample` method is not implemented.

## Syntax


```C++
HRESULT GetCurrentSample(
   IMediaSample **ppSample
);
```



## Parameters

<dl> <dt>

*ppSample* 
</dt> <dd>

Reserved.

</dd> </dl>

## Return value

Returns E\_NOTIMPL.

## Remarks

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

[Using the Sample Grabber](using-the-sample-grabber.md)
</dt> <dt>

[**ISampleGrabber Interface**](isamplegrabber.md)
</dt> </dl>

 

 




