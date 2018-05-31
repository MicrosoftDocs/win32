---
title: IVMVirtualServer RegisterVirtualMachine method
description: The RegisterVirtualMachine method registers an existing virtual machine configuration and returns the virtual machine object.
ms.assetid: baf10801-75e1-42be-9e79-590d12c16abf
keywords:
- RegisterVirtualMachine method Virtual Server
- RegisterVirtualMachine method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , RegisterVirtualMachine method
topic_type:
- apiref
api_name:
- IVMVirtualServer.RegisterVirtualMachine
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

# IVMVirtualServer::RegisterVirtualMachine method

The **RegisterVirtualMachine** method registers an existing virtual machine configuration and returns the virtual machine object.

## Syntax


```C++
HRESULT RegisterVirtualMachine(
  [in]  BSTR              configurationName,
  [in]  BSTR              configurationPath,
  [out] IVMVirtualMachine **virtualMachine
);
```



## Parameters

<dl> <dt>

*configurationName* \[in\]
</dt> <dd>

The name of the virtual machine to register. The length of the name cannot exceed 256 characters and the combined length of the name and path cannot exceed 260 characters. The specified name may contain the .vmc file extension. If this parameter is **NULL** or an empty string, the *configurationPath* parameter must specify the full path to the configuration file.

</dd> <dt>

*configurationPath* \[in\]
</dt> <dd>

The path to the folder that contains the existing configuration file. If the *configurationName* parameter is **NULL** or an empty string, this must specify the full path to the existing configuration file.

</dd> <dt>

*virtualMachine* \[out\]
</dt> <dd>

A pointer to a new [**IVMVirtualMachine**](ivmvirtualmachine.md) object which represents this virtual machine.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                       | Description                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                              | The operation was successful.<br/>                                                                                                                                                          |
| <dl> <dt>**E\_POINTER**</dt> </dl>                         | *configurationName* or *configurationPath* is invalid, or *virtualMachine* is **NULL**.<br/>                                                                                                |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl>                | The system cannot find the path specified by the *configurationName* and *configurationPath* parameters.<br/>                                                                               |
| <dl> <dt>**E\_FILE\_NOT\_FOUND**</dt> </dl>                | The system cannot find the file specified by the *configurationName* and *configurationPath* parameters.<br/>                                                                               |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>                   | *configurationPath* contains an invalid character (one of "\*?:&lt;&gt;/\|"").<br/>                                                                                                         |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>                   | The parameter *configurationPath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                                                         |
| <dl> <dt>**E\_BUFFER\_OVERFLOW**</dt> </dl>                | The path specified by the *configurationName* and *configurationPath* parameters results in a path that is too long. The combined length of the path must be less than 260 characters.<br/> |
| <dl> <dt>**E\_ALREADY\_EXISTS**</dt> </dl>                 | A configuration file with this name already exists at this location.<br/>                                                                                                                   |
| <dl> <dt>**VM\_E\_CONFIG\_NAME\_INVALID\_CHAR**</dt> </dl> | *configurationName* contains an invalid character (one of "\*?:&lt;&gt;/\|\\"").<br/>                                                                                                       |
| <dl> <dt>**VM\_E\_CONFIG\_DUPLICATE\_NAME**</dt> </dl>     | There is already a virtual machine with this name.<br/>                                                                                                                                     |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>                 | An unexpected error has occurred.<br/>                                                                                                                                                      |



 

## Remarks

Virtual machine names are case-insensitive, for example, "MyVM" and "myvm" refer to the same virtual machine.

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

 

 





