---
Description: 'The GetDefaultTransition method retrieves the default transition. If the render engine cannot render a transition, it substitutes the default transition.'
ms.assetid: '3fe5d984-480b-4b35-970f-2f571e0fde7d'
title: 'IAMTimeline::GetDefaultTransition method'
---

# IAMTimeline::GetDefaultTransition method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetDefaultTransition` method retrieves the default transition. If the render engine cannot render a transition, it substitutes the default transition.

## Syntax


```C++
HRESULT GetDefaultTransition(
   GUID *pGuid
);
```



## Parameters

<dl> <dt>

*pGuid* 
</dt> <dd>

Receives the GUID of the default transition.

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

[**IAMTimeline Interface**](iamtimeline.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




