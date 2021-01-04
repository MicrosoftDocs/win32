---
title: EnableUserVhd method of the Win32_TSSessionDirectory class
description: Enables a user profile VHD on an RDSH server.
ms.assetid: bb39fa19-38eb-4caf-ae81-2bccd901ee2f
ms.tgt_platform: multiple
keywords:
- EnableUserVhd method Remote Desktop Services
- EnableUserVhd method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , EnableUserVhd method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.EnableUserVhd
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EnableUserVhd method of the Win32\_TSSessionDirectory class

Enables a user profile VHD on an RDSH server.

## Syntax


```mof
uint32 EnableUserVhd(
  [in] string UvhdShareUrl,
  [in] string UvhdRoamingPolicyXml
);
```



## Parameters

<dl> <dt>

*UvhdShareUrl* \[in\]
</dt> <dd>

The location of the share where all user profile VHDs are stored.

</dd> <dt>

*UvhdRoamingPolicyXml* \[in\]
</dt> <dd>

The roaming policy for the user profile VHD.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSSessionDirectory**](win32-tssessiondirectory.md)
</dt> </dl>

 

 





