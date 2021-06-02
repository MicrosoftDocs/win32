---
description: The AddFoundLocation method adds a directory to the directory cache.
ms.assetid: 0323c4ea-2e86-433b-87d0-34d1800a5627
title: IMediaLocator::AddFoundLocation method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaLocator.AddFoundLocation
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IMediaLocator::AddFoundLocation method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `AddFoundLocation` method adds a directory to the directory cache.

## Syntax


```C++
HRESULT AddFoundLocation(
   BSTR DirectoryName
);
```



## Parameters

<dl> <dt>

*DirectoryName* 
</dt> <dd>

Directory path to add to the cache.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The media locator keeps a cache of directory paths where it has successfully found files in past searches. When it successfully locates a file, it adds the directory to the cache.

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

[**IMediaLocator Interface**](imedialocator.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




