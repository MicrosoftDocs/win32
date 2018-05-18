---
title: Create method of the Win32\_ShadowStorage class
description: The Create method creates differential area storage for the specified Volume on the specified DiffVolume with the specified MaxSpace.
ms.assetid: 'a27a55f3-8b4a-4221-93e9-69d2d3afe4cc'
keywords: ["Create method", "Create method, Win32_ShadowStorage class", "Win32_ShadowStorage class, Create method"]
topic_type:
- apiref
api_name:
- Win32_ShadowStorage.Create
api_location:
- Vsswmi.dll
api_type:
- COM
---

# Create method of the Win32\_ShadowStorage class

The **Create** method creates differential area storage for the specified *Volume* on the specified *DiffVolume* with the specified *MaxSpace*.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Create(
  [in] string Volume,
  [in] string DiffVolume,
  [in] uint64 MaxSpace
);
```



## Parameters

<dl> <dt>

*Volume* \[in\]
</dt> <dd>

Volume that is to be shadowed. Can be as a volume drive letter, mount point, or volume GUID name.

</dd> <dt>

*DiffVolume* \[in\]
</dt> <dd>

Volume used to store the shadow differential area. If this parameter is not supplied, the specified *Volume* is used to store the differential area. Can be as a volume drive letter, mount point, or volume GUID name.

</dd> <dt>

*MaxSpace* \[in\]
</dt> <dd>

Initial maximum size of the differential area.

</dd> </dl>

## Return value



| Return code                                                                       | Description                                                |
|-----------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>  | Success.<br/>                                        |
| <dl> <dt>**1**</dt> </dl>  | Access denied.<br/>                                  |
| <dl> <dt>**2**</dt> </dl>  | Invalid argument.<br/>                               |
| <dl> <dt>**3**</dt> </dl>  | Specified volume not found.<br/>                     |
| <dl> <dt>**4**</dt> </dl>  | Specified volume not supported.<br/>                 |
| <dl> <dt>**5**</dt> </dl>  | Shadow copy storage area already exists.<br/>        |
| <dl> <dt>**6**</dt> </dl>  | Maximum number of shadow storage areas reached.<br/> |
| <dl> <dt>**7**</dt> </dl>  | Shadow copy provider veto of the operation.<br/>     |
| <dl> <dt>**8**</dt> </dl>  | Shadow copy provider not registered.<br/>            |
| <dl> <dt>**9**</dt> </dl>  | Shadow copy provider failure.<br/>                   |
| <dl> <dt>**10**</dt> </dl> | Unknown error.<br/>                                  |
| <dl> <dt>**11**</dt> </dl> | Insufficient storage.<br/>                           |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vss.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vsswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ShadowStorage**](win32-shadowstorage.md)
</dt> </dl>

 

 





