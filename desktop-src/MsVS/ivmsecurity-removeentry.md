---
title: IVMSecurity RemoveEntry method
description: The RemoveEntry method removes an access control entry. This method removes the specified access control entry.
ms.assetid: 9f84efd2-b473-49de-b6f3-4394d91fbb5c
keywords:
- RemoveEntry method Virtual Server
- RemoveEntry method Virtual Server , IVMSecurity interface
- IVMSecurity interface Virtual Server , RemoveEntry method
- RemoveEntry method Virtual Server , VMSecurity interface
- VMSecurity interface Virtual Server , RemoveEntry method
topic_type:
- apiref
api_name:
- IVMSecurity.RemoveEntry
- VMSecurity.RemoveEntry
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

# IVMSecurity::RemoveEntry method

The **RemoveEntry** method removes an access control entry. This method removes the specified access control entry.

## Syntax


```C++
HRESULT RemoveEntry(
  [in] IVMAccessRights *entryToDelete
);
```



## Parameters

<dl> <dt>

*entryToDelete* \[in\]
</dt> <dd>

The entry to delete.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                        | Description                                                                                       |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>              | The operation was successful.<br/>                                                          |
| <dl> <dt> **S\_FALSE**</dt> </dl>           | The specified entry has already been deleted or was not found.<br/>                         |
| <dl> <dt> **E\_POINTER**</dt> </dl>         | The parameter *entryToDelete* was null.<br/>                                                |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl> | An unknown error has occurred. Other **HRESULT** error values may be returned as well.<br/> |



 

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

 

 





