---
description: The SetGroupName method sets the application-defined name of the group.
ms.assetid: e1d8a91b-d5b9-42a4-9b98-582e1a57ac51
title: IAMTimelineGroup::SetGroupName method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.SetGroupName
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::SetGroupName method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetGroupName` method sets the application-defined name of the group.

## Syntax


```C++
HRESULT SetGroupName(
   BSTR pGroupName
);
```



## Parameters

<dl> <dt>

*pGroupName* 
</dt> <dd>

**BSTR** that specifies the name of the group. The maximum length of the name is 256 characters, incuding the null terminator.

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

[**IAMTimelineGroup Interface**](iamtimelinegroup.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




