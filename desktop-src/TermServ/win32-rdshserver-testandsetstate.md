---
title: TestAndSetState method of the Win32_RDSHServer class
description: Compares the current state to the specified comparand; if the two match, the state is set to a new value. Regardless of the match, the current state is also returned.
ms.assetid: f1bb0076-251b-4c0d-92f9-1c460e1b26bb
ms.tgt_platform: multiple
keywords:
- TestAndSetState method Remote Desktop Services
- TestAndSetState method Remote Desktop Services , Win32_RDSHServer class
- Win32_RDSHServer class Remote Desktop Services , TestAndSetState method
topic_type:
- apiref
api_name:
- Win32_RDSHServer.TestAndSetState
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TestAndSetState method of the Win32\_RDSHServer class

Compares the current state to the specified comparand; if the two match, the state is set to a new value. Regardless of the match, the current state is also returned.

## Syntax


```mof
uint32 TestAndSetState(
  [in]  uint32 Comparand,
  [in]  uint32 NewState,
  [out] uint32 InitState
);
```



## Parameters

<dl> <dt>

*Comparand* \[in\]
</dt> <dd>

A value to compare to the current state; if the two values match, the state is set to *NewState*.

</dd> <dt>

*NewState* \[in\]
</dt> <dd>

The new value of the state.

</dd> <dt>

*InitState* \[out\]
</dt> <dd>

On success or failure, returns the current state.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDSHServer**](win32-rdshserver.md)
</dt> </dl>

 

 





