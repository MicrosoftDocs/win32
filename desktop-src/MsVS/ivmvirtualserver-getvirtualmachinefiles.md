---
title: IVMVirtualServer GetVirtualMachineFiles method
description: The GetVirtualMachineFiles method returns an array of known virtual machine configuration files.
ms.assetid: d4cb57e7-7d97-467b-bb56-b6a651746f0c
keywords:
- GetVirtualMachineFiles method Virtual Server
- GetVirtualMachineFiles method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , GetVirtualMachineFiles method
- GetVirtualMachineFiles method Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , GetVirtualMachineFiles method
topic_type:
- apiref
api_name:
- IVMVirtualServer.GetVirtualMachineFiles
- VMVirtualServer.GetVirtualMachineFiles
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualServer::GetVirtualMachineFiles method

The **GetVirtualMachineFiles** method returns an array of known virtual machine configuration files.

## Syntax


```C++
HRESULT GetVirtualMachineFiles(
  [in]  VARIANT      inAdditionalSearchPaths,
  [in]  VARIANT_BOOL inExcludedRegisteredVMs,
  [out] VARIANT      *outVirtualMachineFileList
);
```



## Parameters

<dl> <dt>

*inAdditionalSearchPaths* \[in\]
</dt> <dd>

These paths will be searched along with the paths set in the [**IVMVirtualServer::SearchPaths**](ivmvirtualserver-searchpaths.md) and [**IVMVirtualServer::DefaultVMConfigurationPath**](ivmvirtualserver-defaultvmconfigurationpath.md) properties.

</dd> <dt>

*inExcludedRegisteredVMs* \[in\]
</dt> <dd>

Set to **TRUE** if registered virtual machines should be excluded from the array return in the *outVirtualMachineFileList* parameter.

</dd> <dt>

*outVirtualMachineFileList* \[out\]
</dt> <dd>

An array of virtual machine configuration files found in the specified search paths.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                       | Description                                                                    |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *outVirtualMachineFileList* parameter is **NULL**.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>      | The *inAdditionalSearchPaths* parameter is not an array of strings.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>                                   |



 

## Remarks

The search paths used to retrieve the array of configuration files will include those set previously by [**IVMVirtualServer::SearchPaths**](ivmvirtualserver-searchpaths.md) and [**IVMVirtualServer::DefaultVMConfigurationPath**](ivmvirtualserver-defaultvmconfigurationpath.md) in addition to those specified by the *inAdditionalSearchPaths* parameter.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





