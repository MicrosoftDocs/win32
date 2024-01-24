---
title: INapComponentConfig2 InvokeUIForMachine method (NapCommon.h)
description: Is implemented by system health validators (SHVs) as needed to manage remote configuration directly on the machine specified. This method launches a configuration management UI.
ms.assetid: 67a6d715-250b-4b8b-9c27-8173926b7bfe
keywords:
- InvokeUIForMachine method NAP
- InvokeUIForMachine method NAP , INapComponentConfig2 interface
- INapComponentConfig2 interface NAP , InvokeUIForMachine method
topic_type:
- apiref
api_name:
- INapComponentConfig2.InvokeUIForMachine
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig2::InvokeUIForMachine method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **InvokeUIForMachine** method is implemented by system health validators (SHVs) as needed to manage remote configuration directly on the machine specified. This method launches a configuration management UI.

## Syntax


```C++
HRESULT InvokeUIForMachine(
  [in] HWND          hwndParent,
  [in] CountedString *machineName
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

A handle to the parent or owner window. A valid window handle must be supplied.

</dd> <dt>

*machineName* \[in\]
</dt> <dd>

A pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) that contains the machine name of the NAP client.

</dd> </dl>

## Return value

Returns S\_OK if successful, or one of the standard Windows error codes.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapComponentConfig2**](inapcomponentconfig2.md)
</dt> </dl>

 

 





