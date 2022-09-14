---
description: The SetUserData method sets application-defined persistent data.
ms.assetid: 195d8e92-a25c-40ff-8cc7-c1f05bdd76ab
title: IAMTimelineObj::SetUserData method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.SetUserData
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::SetUserData method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetUserData` method sets application-defined persistent data.

## Syntax


```C++
HRESULT SetUserData(
   BYTE *pData,
   long Size
);
```



## Parameters

<dl> <dt>

*pData* 
</dt> <dd>

Pointer to a buffer containing the data.

</dd> <dt>

*Size* 
</dt> <dd>

Size of the data, in bytes.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




