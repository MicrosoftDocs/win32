---
description: The GetEffect method retrieves the effect at the specified priority level.
ms.assetid: 8606c457-1c4d-4a20-b674-aaf82abeb451
title: IAMTimelineEffectable::GetEffect method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineEffectable.GetEffect
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineEffectable::GetEffect method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **GetEffect** method retrieves the effect at the specified priority level.

## Syntax


```C++
HRESULT GetEffect(
  [out] IAMTimelineObj **ppFX,
        long           Which
);
```



## Parameters

<dl> <dt>

*ppFX* \[out\]
</dt> <dd>

Receives the effect's [**IAMTimelineObj**](iamtimelineobj.md) interface.

</dd> <dt>

*Which* 
</dt> <dd>

Priority level of the effect to retrieve.

</dd> </dl>

## Return value

Returns an HRESULT value. Possible values include the following:



| Return code                                                                               | Description                                     |
|-------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>   | No effect at the specified priority,<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                             |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/>           |



 

## Remarks

If the method returns S\_OK, the **IAMTimelineObj** interface that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

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

[**IAMTimelineEffectable Interface**](iamtimelineeffectable.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




