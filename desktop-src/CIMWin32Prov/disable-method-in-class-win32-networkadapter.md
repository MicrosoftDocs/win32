---
description: Disables the network adapter.
ms.assetid: 6b328d7c-a9ef-4c9b-bc32-13fa2e0f65eb
ms.tgt_platform: multiple
title: Disable method of the Win32_NetworkAdapter class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_NetworkAdapter.Disable
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Disable method of the Win32\_NetworkAdapter class

The **Disable** method disables the network adapter.

## Syntax


```mof
uint32 Disable();
```



## Parameters

This method has no parameters.

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_NetworkAdapter**](win32-networkadapter.md)
</dt> <dt>

[WMI Tasks: Networking](/windows/desktop/WmiSdk/wmi-tasks--networking)
</dt> <dt>

[IPv6 and IPv4 Support in WMI](/windows/desktop/WmiSdk/ipv6-and-ipv4-support-in-wmi)
</dt> </dl>

 

