---
title: IVMVirtualServer GetVirtualNetworkFiles method
description: The GetVirtualNetworkFiles method returns an array of known virtual network configuration files.
ms.assetid: '6e87fd0e-fd72-48cd-94fc-95642e39961b'
keywords: ["GetVirtualNetworkFiles method Virtual Server", "GetVirtualNetworkFiles method Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , GetVirtualNetworkFiles method", "GetVirtualNetworkFiles method Virtual Server , VMVirtualServer class", "VMVirtualServer class Virtual Server , GetVirtualNetworkFiles method"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.GetVirtualNetworkFiles
- VMVirtualServer.GetVirtualNetworkFiles
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::GetVirtualNetworkFiles method

The **GetVirtualNetworkFiles** method returns an array of known virtual network configuration files.

## Syntax


```C++
HRESULT GetVirtualNetworkFiles(
  [in]  VARIANT      inAdditionalSearchPaths,
  [in]  VARIANT_BOOL inExcludedRegisteredVNs,
  [out] VARIANT      *outVirtualNetworkFileList
);
```



## Parameters

<dl> <dt>

*inAdditionalSearchPaths* \[in\]
</dt> <dd>

These paths will be searched along with the paths set in the [**IVMVirtualServer::SearchPaths**](ivmvirtualserver-searchpaths.md) and [**IVMVirtualServer::DefaultVNConfigurationPath**](ivmvirtualserver-defaultvnconfigurationpath.md) properties.

</dd> <dt>

*inExcludedRegisteredVNs* \[in\]
</dt> <dd>

Set to **TRUE** if registered virtual networks should be excluded from the array return in the *outVirtualNetworkFileList* parameter.

</dd> <dt>

*outVirtualNetworkFileList* \[out\]
</dt> <dd>

An array of virtual network configuration files found in the specified search paths.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                       | Description                                                                    |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *outVirtualNetworkFileList* parameter is **NULL**.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>      | The *inAdditionalSearchPaths* parameter is not an array of strings.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>                                   |



 

## Remarks

The search paths used to retrieve the array of configuration files will include those set previously by [**IVMVirtualServer::SearchPaths**](ivmvirtualserver-searchpaths.md) and [**IVMVirtualServer::DefaultVNConfigurationPath**](ivmvirtualserver-defaultvnconfigurationpath.md) in addition to those specified by the *inAdditionalSearchPaths* parameter.

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

 

 





