---
title: IVMVirtualServer CreateVirtualNetwork method
description: The CreateVirtualNetwork method creates a new virtual network.
ms.assetid: ec8f3026-9d0a-49ee-8dc5-16e886572ce4
keywords:
- CreateVirtualNetwork method Virtual Server
- CreateVirtualNetwork method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , CreateVirtualNetwork method
topic_type:
- apiref
api_name:
- IVMVirtualServer.CreateVirtualNetwork
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::CreateVirtualNetwork method

The **CreateVirtualNetwork** method creates a new virtual network.

## Syntax


```C++
HRESULT CreateVirtualNetwork(
  [in]  BSTR              virtualNetworkName,
  [in]  BSTR              virtualNetworkPath,
  [out] IVMVirtualNetwork **virtualNetwork
);
```



## Parameters

<dl> <dt>

*virtualNetworkName* \[in\]
</dt> <dd>

The name of the new virtual network. The length of the name cannot exceed 256 characters and the combined length of the name and path cannot exceed 260 characters. The file name extension ".vnc" will be appended to the end of the virtual network name when the configuration file is created. If this parameter is **NULL** or an empty string, the *virtualNetworkPath* parameter must specify the full path to the configuration file.

</dd> <dt>

*virtualNetworkPath* \[in\]
</dt> <dd>

The path to the folder that will contain the configuration file. This folder will be created if it does not exist. If the *virtualNetworkName* parameter is **NULL** or an empty string, this must specify the full path the new configuration file.

</dd> <dt>

*virtualNetwork* \[out\]
</dt> <dd>

A pointer to a new [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object which represents this virtual network.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                       | Description                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                              | The operation was successful.<br/>                                                                                                                                                         |
| <dl> <dt>**E\_POINTER**</dt> </dl>                         | The *virtualNetwork* parameter is **NULL**.<br/>                                                                                                                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                      | The *virtualNetworkName* or *virtualNetworkPath* parameter is not valid or is an empty string.<br/>                                                                                        |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl>                | The system cannot find the path specified by the *virtualNetworkName* and *virtualNetworkPath* parameters.<br/>                                                                            |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>                   | The *virtualNetworkPath* parameter contains a character that is not valid (one of "\*?:&lt;&gt;/\|"").<br/>                                                                                |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>                   | The *virtualNetworkPath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                                                                 |
| <dl> <dt>**E\_BUFFER\_OVERFLOW**</dt> </dl>                | The path specified by the *virtualNetworkName* and *virtualNetworkPath* parameters results is a path that is too long. The total length of the path must be less than 260 characters.<br/> |
| <dl> <dt>**E\_ALREADY\_EXISTS**</dt> </dl>                 | A configuration file with this name already exists at this location.<br/>                                                                                                                  |
| <dl> <dt>**VM\_E\_CONFIG\_NAME\_INVALID\_CHAR**</dt> </dl> | The *virtualNetworkName* parameter contains a character that is not valid (one of "\*?:&lt;&gt;/\|\\"").<br/>                                                                              |
| <dl> <dt>**VM\_E\_CONFIG\_DUPLICATE\_NAME**</dt> </dl>     | There is already a virtual network with this name.<br/>                                                                                                                                    |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>                 | An unexpected error occurred.<br/>                                                                                                                                                         |



 

## Remarks

By default, the adapter of the virtual network is set for guest-only networking, which isolates the virtual machine from the network. Use the [**IVMVirtualNetwork::HostAdapter**](ivmvirtualnetwork-hostadapter.md) method to change the adapter for this virtual network. The name must be unique with respect to the names of any existing virtual networks. Virtual network names are case-insensitive, for example, "MyNetwork" and "mynetwork" refer to the same virtual network.

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

 

 





