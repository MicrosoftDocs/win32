---
description: Creates a new Win32\_ClusterShare instance.
ms.assetid: a6fde28d-f19e-4a31-8f0d-35927c75a030
ms.tgt_platform: multiple
title: Create method of the Win32_ClusterShare class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# Create method of the Win32\_ClusterShare class

Creates a new [**Win32\_ClusterShare**](win32-clustershare.md) instance.

## Syntax


```mof
static uint32 Create(
  [in]           string                   Path,
  [in]           string                   Name,
  [in]           uint32                   Type,
  [in, optional] uint32                   MaximumAllowed,
  [in, optional] string                   Description,
  [in, optional] string                   Password,
  [in, optional] Win32_SecurityDescriptor Access
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Local path of the Windows share.

Example, "C:\\Program Files".

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The alias to a path set up as a share on a computer system running Windows.

Example, "public".

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of resource being shared. Types include: disk drives, print queues, interprocess communications (IPC), and general devices.

<dt>

0 (0x0)
</dt> <dd>

Disk Drive

</dd> <dt>

1 (0x1)
</dt> <dd>

Print Queue

</dd> <dt>

2 (0x2)
</dt> <dd>

Device

</dd> <dt>

3 (0x3)
</dt> <dd>

IPC

</dd> <dt>

2147483648 (0x80000000)
</dt> <dd>

Disk Drive Admin

</dd> <dt>

2147483649 (0x80000001)
</dt> <dd>

Print Queue Admin

</dd> <dt>

2147483650 (0x80000002)
</dt> <dd>

Device Admin

</dd> <dt>

2147483651 (0x80000003)
</dt> <dd>

IPC Admin

</dd> </dl> </dd> <dt>

*MaximumAllowed* \[in, optional\]
</dt> <dd>

Limit on the maximum number of users allowed to use this resource concurrently.

</dd> <dt>

*Description* \[in, optional\]
</dt> <dd>

Description of the object.

</dd> <dt>

*Password* \[in, optional\]
</dt> <dd>

TBD

</dd> <dt>

*Access* \[in, optional\]
</dt> <dd>

Optional embedded instance of a [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) class that contains the security descriptor for the new share.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Cimwin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ClusterShare**](win32-clustershare.md)
</dt> </dl>

 

