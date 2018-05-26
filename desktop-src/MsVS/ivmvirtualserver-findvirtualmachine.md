---
title: IVMVirtualServer FindVirtualMachine method
description: The FindVirtualMachine method returns a virtual machine object matching the requested configuration.
ms.assetid: 47c47041-15b0-4ae5-a1cf-4d8ce6ca34ff
keywords:
- FindVirtualMachine method Virtual Server
- FindVirtualMachine method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , FindVirtualMachine method
topic_type:
- apiref
api_name:
- IVMVirtualServer.FindVirtualMachine
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualServer::FindVirtualMachine method

The **FindVirtualMachine** method returns a virtual machine object matching the requested configuration.

## Syntax


```C++
HRESULT FindVirtualMachine(
  [in]  BSTR              configurationName,
  [out] IVMVirtualMachine **virtualMachine
);
```



## Parameters

<dl> <dt>

*configurationName* \[in\]
</dt> <dd>

The name of the virtual machine to find.

</dd> <dt>

*virtualMachine* \[out\]
</dt> <dd>

A pointer to a new [**IVMVirtualMachine**](ivmvirtualmachine.md) object which represents this virtual machine.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                       | Description                                                                 |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                                    |
| <dl> <dt>**S\_FALSE**</dt> </dl>           | The specified configuration could not be found.<br/>                  |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | *configurationName* is invalid, or *virtualMachine* is **NULL**.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>                                |



 

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

 

 





