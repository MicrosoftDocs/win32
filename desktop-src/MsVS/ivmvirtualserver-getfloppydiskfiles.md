---
title: IVMVirtualServer GetFloppyDiskFiles method
description: The GetFloppyDiskFiles method returns an array of known virtual floppy disk files.
ms.assetid: 'ef6e5574-909b-4df2-a88c-fc9181370bb3'
keywords: ["GetFloppyDiskFiles method Virtual Server", "GetFloppyDiskFiles method Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , GetFloppyDiskFiles method"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.GetFloppyDiskFiles
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::GetFloppyDiskFiles method

The **GetFloppyDiskFiles** method returns an array of known virtual floppy disk files.

## Syntax


```C++
HRESULT GetFloppyDiskFiles(
  [in]  VARIANT inAdditionalSearchPaths,
  [out] VARIANT *outFloppyDiskFileList
);
```



## Parameters

<dl> <dt>

*inAdditionalSearchPaths* \[in\]
</dt> <dd>

These paths will be searched along with the paths set in the [**IVMVirtualServer::SearchPaths**](ivmvirtualserver-searchpaths.md) property.

</dd> <dt>

*outFloppyDiskFileList* \[out\]
</dt> <dd>

An array of virtual floppy disk files found in the specified search paths.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                       | Description                                                                    |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *outFloppyDiskFileList* parameter is **NULL**.<br/>                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>      | The *inAdditionalSearchPaths* parameter is not an array of strings.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>                                   |



 

## Remarks

The search paths used to retrieve the array of files will include those set previously by [**IVMVirtualServer::SearchPaths**](ivmvirtualserver-searchpaths.md) in addition to those specified by the *inAdditionalSearchPaths* parameter and the installer location for the Virtual Machine Additions module.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





