---
title: IVMSecurity \_ToSecurityDescriptor method
description: Creates a self-relative SECURITY\_DESCRIPTOR structure representing the current state of the IVMSecurity instance.
ms.assetid: b109c8dd-4ad9-4851-9b19-b7517e0539f2
keywords:
- _ToSecurityDescriptor method Virtual Server
- _ToSecurityDescriptor method Virtual Server , IVMSecurity interface
- IVMSecurity interface Virtual Server , _ToSecurityDescriptor method
topic_type:
- apiref
api_name:
- IVMSecurity._ToSecurityDescriptor
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

# IVMSecurity::\_ToSecurityDescriptor method

The **\_ToSecurityDescriptor** method creates a self-relative **SECURITY\_DESCRIPTOR** structure representing the current state of the [**IVMSecurity**](ivmsecurity.md) instance.

## Syntax


```C++
HRESULT _ToSecurityDescriptor(
  [in]  GENERIC_MAPPING *genericMapping,
  [out] long            *securityDescriptorLength,
  [out] BYTE            **securityDescriptor
);
```



## Parameters

<dl> <dt>

*genericMapping* \[in\]
</dt> <dd>

Type: **GENERIC\_MAPPING\***

A **GENERIC\_MAPPING** structure.

</dd> <dt>

*securityDescriptorLength* \[out\]
</dt> <dd>

Type: **long\***

The length in bytes of the security descriptor returned by this method.

</dd> <dt>

*securityDescriptor* \[out\]
</dt> <dd>

Type: **BYTE\*\***

A self-relative security descriptor representing the current state of the [**IVMSecurity**](ivmsecurity.md) instance. The caller must release the memory occupied by the security descriptor by calling **CoTaskMemFree** when it is finished.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                         | Description                                                                                       |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>                                                          |
| <dl> <dt> **E\_POINTER** </dt> </dl>         | A null pointer was specified in one of the parameters.<br/>                                 |
| <dl> <dt> **E\_OUTOFMEMORY** </dt> </dl>     | There was not enough memory to create the security descriptor.<br/>                         |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unknown error has occurred. Other **HRESULT** error values may be returned as well.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSecurity**](ivmsecurity.md)
</dt> </dl>

 

 





