---
title: SendMessage method of the Win32_VirtualDesktopSession class
description: Send a message to the user through the virtual desktop session.
ms.assetid: 4bb9183e-c016-48f2-8e8c-0d5fb395c435
ms.tgt_platform: multiple
keywords:
- SendMessage method Remote Desktop Services
- SendMessage method Remote Desktop Services , Win32_VirtualDesktopSession class
- Win32_VirtualDesktopSession class Remote Desktop Services , SendMessage method
topic_type:
- apiref
api_name:
- Win32_VirtualDesktopSession.SendMessage
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SendMessage method of the Win32\_VirtualDesktopSession class

Send a message to the user through the virtual desktop session.

## Syntax


```mof
uint32 SendMessage(
  [in] string Title,
  [in] string Message
);
```



## Parameters

<dl> <dt>

*Title* \[in\]
</dt> <dd>

The title of the messge.

</dd> <dt>

*Message* \[in\]
</dt> <dd>

The content of the message.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_VirtualDesktopSession**](win32-virtualdesktopsession.md)
</dt> </dl>

 

 





