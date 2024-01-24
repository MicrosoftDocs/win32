---
title: SetVirtualIPMode method of the Win32_TSVirtualIP class
description: Sets the VirtualIPMode property value.
ms.assetid: d4b39566-ad2a-493b-8022-c006a857043d
ms.tgt_platform: multiple
keywords:
- SetVirtualIPMode method Remote Desktop Services
- SetVirtualIPMode method Remote Desktop Services , Win32_TSVirtualIP class
- Win32_TSVirtualIP class Remote Desktop Services , SetVirtualIPMode method
topic_type:
- apiref
api_name:
- Win32_TSVirtualIP.SetVirtualIPMode
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetVirtualIPMode method of the Win32\_TSVirtualIP class

Sets the **VirtualIPMode** property value.

## Syntax


```mof
uint32 SetVirtualIPMode(
  [in] uint32 VirtualIPMode
);
```



## Parameters

<dl> <dt>

*VirtualIPMode* \[in\]
</dt> <dd>

Type: **uint32**

Specifies which IP virtualization mode is being used on the server. This can be one of the following values.

<dt>

0
</dt> <dd>

The IP virtualization mode is per-session.

</dd> <dt>

1
</dt> <dd>

The IP virtualization mode is per-user.

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

 

 





