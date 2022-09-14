---
description: The GetGroupName method retrieves the application-defined name of the group.
ms.assetid: 402e97d9-abb5-4d8e-8735-1b06d60ab225
title: IAMTimelineGroup::GetGroupName method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.GetGroupName
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::GetGroupName method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetGroupName` method retrieves the application-defined name of the group.

## Syntax


```C++
HRESULT GetGroupName(
  [out, retval] BSTR *pGroupName
);
```



## Parameters

<dl> <dt>

*pGroupName* \[out, retval\]
</dt> <dd>

Receives the name of the group.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The method allocates memory for the string. The application must call **SysFreeString** to free the memory.

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

 

 




