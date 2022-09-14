---
title: SetVirtualIPActive method of the Win32_TSVirtualIP class
description: Sets the VirtualIPActive property value.
ms.assetid: e485aeb1-afdf-4572-bac7-daa80d903edc
ms.tgt_platform: multiple
keywords:
- SetVirtualIPActive method Remote Desktop Services
- SetVirtualIPActive method Remote Desktop Services , Win32_TSVirtualIP class
- Win32_TSVirtualIP class Remote Desktop Services , SetVirtualIPActive method
topic_type:
- apiref
api_name:
- Win32_TSVirtualIP.SetVirtualIPActive
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetVirtualIPActive method of the Win32\_TSVirtualIP class

Sets the **VirtualIPActive** property value.

## Syntax


```mof
uint32 SetVirtualIPActive(
  [in] uint32 VirtualIPActive
);
```



## Parameters

<dl> <dt>

*VirtualIPActive* \[in\]
</dt> <dd>

Type: **uint32**

Specifies if IP virtualization is active on the server. This can be one of the following values.

<dt>

zero
</dt> <dd>

IP virtualization is not active.

</dd> <dt>

nonzero
</dt> <dd>

IP virtualization is active.

</dd> </dl> </dd> </dl>

## Return value

Type: **uint32**

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSVirtualIP**](win32-tsvirtualip.md)
</dt> </dl>

 

 





