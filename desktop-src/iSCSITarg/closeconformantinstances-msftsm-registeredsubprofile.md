---
title: CloseConformantInstances method of the MSFTSM\_RegisteredSubProfile class
description: Closes an enumeration session that is opened by the OpenConformantInstances method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5a50aa72-8b9d-4b85-b209-3d735c983a90
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CloseConformantInstances method iSCSI Software Target API
- CloseConformantInstances method iSCSI Software Target API , MSFTSM_RegisteredSubProfile class
- MSFTSM_RegisteredSubProfile class iSCSI Software Target API , CloseConformantInstances method
topic_type:
- apiref
api_name:
- MSFTSM_RegisteredSubProfile.CloseConformantInstances
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CloseConformantInstances method of the MSFTSM\_RegisteredSubProfile class

Closes an enumeration session that is opened by the [**OpenConformantInstances**](openconformantinstances-msftsm-registeredsubprofile.md) method.

This method is inherited from the **CIM\_RegisteredSubProfile** class.

## Syntax


```mof
uint32 CloseConformantInstances(
  [in] string EnumerationContext
);
```



## Parameters

<dl> <dt>

*EnumerationContext* \[in\]
</dt> <dd>

Specifies the enumeration context value that identifies the enumeration session to be closed.

</dd> </dl>

## Return value

Returns zero on success; otherwise returns an error.

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\Interop<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFTSM\_RegisteredSubProfile**](msftsm-registeredsubprofile.md)
</dt> </dl>

 

 





