---
title: CloseConformantInstances method of the MSFTSM\_RegisteredProfile class
description: Closes an enumeration session that is opened by the OpenConformantInstances method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ab68194a-9423-4654-8a8d-639ec086d027
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CloseConformantInstances method iSCSI Software Target API
- CloseConformantInstances method iSCSI Software Target API , MSFTSM_RegisteredProfile class
- MSFTSM_RegisteredProfile class iSCSI Software Target API , CloseConformantInstances method
topic_type:
- apiref
api_name:
- MSFTSM_RegisteredProfile.CloseConformantInstances
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CloseConformantInstances method of the MSFTSM\_RegisteredProfile class

Closes an enumeration session that is opened by the [**OpenConformantInstances**](openconformantinstances-msftsm-registeredprofile.md) method.

This method is inherited from the [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375) class.

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

Returns zero on success; otherwise, returns an error.

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

[**MSFTSM\_RegisteredProfile**](msftsm-registeredprofile.md)
</dt> </dl>

 

 





