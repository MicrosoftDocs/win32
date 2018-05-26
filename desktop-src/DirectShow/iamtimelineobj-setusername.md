---
Description: The SetUserName method sets an application-defined name for the object.
ms.assetid: 6f071884-519a-465f-8273-ab1be58dda8b
title: IAMTimelineObjSetUserName method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IAMTimelineObj::SetUserName method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetUserName` method sets an application-defined name for the object.

## Syntax


```C++
HRESULT SetUserName(
   BSTR newVal
);
```



## Parameters

<dl> <dt>

*newVal* 
</dt> <dd>

Wide-character string that contains the name. Strings longer than 256 characters might be truncated.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




