---
title: IVMVirtualServer GetHardDiskFiles method
description: The GetHardDiskFiles method returns an array of known virtual hard disk files.
ms.assetid: '0686453a-a531-485c-8ed6-5ceb60ff27bf'
keywords: ["GetHardDiskFiles method Virtual Server", "GetHardDiskFiles method Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , GetHardDiskFiles method"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.GetHardDiskFiles
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::GetHardDiskFiles method

The **GetHardDiskFiles** method returns an array of known virtual hard disk files.

## Syntax


```C++
HRESULT GetHardDiskFiles(
  [in]  VARIANT inAdditionalSearchPaths,
  [out] VARIANT *outHardDiskFileList
);
```



## Parameters

<dl> <dt>

*inAdditionalSearchPaths* \[in\]
</dt> <dd>

These paths will be searched along with the paths set in the [**IVMVirtualServer::SearchPaths**](ivmvirtualserver-searchpaths.md) property.

</dd> <dt>

*outHardDiskFileList* \[out\]
</dt> <dd>

An array of virtual hard disk files found in the specified search paths.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                       | Description                                                                    |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *outHardDiskFileList* parameter is **NULL**.<br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>      | The *inAdditionalSearchPaths* parameter is not an array of strings.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>                                   |



 

## Remarks

The search paths used to retrieve the array of files will include those set previously by [**IVMVirtualServer::SearchPaths**](ivmvirtualserver-searchpaths.md) in addition to those specified by the *inAdditionalSearchPaths* parameter.

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

 

 





