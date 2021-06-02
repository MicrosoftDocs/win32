---
description: The ValidateSourceNames method validates source names in the timeline, using the media locator. Optionally, this method also updates any source object for which it locates a file.
ms.assetid: 8f4b9ff0-f283-4bcb-83f4-92410cead7db
title: IAMTimeline::ValidateSourceNames method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.ValidateSourceNames
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::ValidateSourceNames method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `ValidateSourceNames` method validates source names in the timeline, using the media locator. Optionally, this method also updates any source object for which it locates a file.

## Syntax


```C++
HRESULT ValidateSourceNames(
   long          ValidateFlags,
   IMediaLocator *pOverride,
   long          NotifyEventHandle
);
```



## Parameters

<dl> <dt>

*ValidateFlags* 
</dt> <dd>

Bitwise combination of [**File Name Validation Flags**](file-name-validation-flags.md) specifying the behavior of the media locator. The SFN\_VALIDATEF\_REPLACE and SFN\_VALIDATEF\_CHECK flags must be present, or the method returns E\_INVALIDARG.

</dd> <dt>

*pOverride* 
</dt> <dd>

Optional pointer to the [**IMediaLocator**](imedialocator.md) interface of a media locator to use in place of the default. To use the default media locator, set the value of this parameter to **NULL**. See Remarks for more information.

</dd> <dt>

*NotifyEventHandle* 
</dt> <dd>

Handle to an event. The method signals the event after it has completed the validation.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Using the *pOverride* parameter, you can supply your own custom implementation of the [**IMediaLocator**](imedialocator.md) interface. For example, the default media locator will not notify your application about the files that it finds (or cannot find). To get around this limitation, you could implement a custom media locator, making it a wrapper for the default version. In your custom version, pass [**IMediaLocator::FindMediaFile**](imedialocator-findmediafile.md) calls directly to the default version, and examine the return value.

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

 

 




