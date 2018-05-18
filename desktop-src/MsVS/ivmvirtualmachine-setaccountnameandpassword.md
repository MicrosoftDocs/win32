---
title: IVMVirtualMachine SetAccountNameAndPassword method
description: The SetAccountNameAndPassword method sets the account name and password for the context in which this virtual machine will run.
ms.assetid: 'e2733ca9-6c56-427b-ba42-4ef86fb5c01f'
keywords: ["SetAccountNameAndPassword method Virtual Server", "SetAccountNameAndPassword method Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , SetAccountNameAndPassword method"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.SetAccountNameAndPassword
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::SetAccountNameAndPassword method

The **SetAccountNameAndPassword** method sets the account name and password for the context in which this virtual machine will run.

## Syntax


```C++
HRESULT SetAccountNameAndPassword(
  [in] BSTR accountName,
  [in] BSTR accountPassword
);
```



## Parameters

<dl> <dt>

*accountName* \[in\]
</dt> <dd>

The account name for the context in which this virtual machine will run.

</dd> <dt>

*accountPassword* \[in\]
</dt> <dd>

The account password for the context in which this virtual machine will run.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                        | Description                                                               |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>              | The operation was successful.<br/>                                  |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>     | The *accountName* or *accountPassword* parameter is not valid.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>  | The virtual machine configuration is not valid.<br/>                |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error has occurred.<br/>                              |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





