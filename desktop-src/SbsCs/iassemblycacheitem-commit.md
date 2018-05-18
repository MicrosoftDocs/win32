---
Description: 'The Commit method copies information into the side-by-side store. When this method returns, the assembly is visible in the side-by-side store.'
ms.assetid: 'd8f8b6b3-72b4-400b-a780-fc25d1f4b9d0'
title: 'IAssemblyCacheItem::Commit method'
---

# IAssemblyCacheItem::Commit method

The **Commit** method copies information into the side-by-side store. When this method returns, the assembly is visible in the side-by-side store.

## Syntax


```C++
HRESULT Commit(
  [in]            DWORD dwFlags,
  [out, optional] ULONG *pulDisposition
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter specifies how existing information in the side-by-side store is to be replaced by information for the assembly being installed.



| Value                                                                                                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="IASSEMBLYCACHEITEM_COMMIT_FLAG_REFRESH"></span><span id="iassemblycacheitem_commit_flag_refresh"></span><dl> <dt>**IASSEMBLYCACHEITEM\_COMMIT\_FLAG\_REFRESH**</dt> </dl>                    | Replace existing information in the side-by-side store with the information in the assembly being installed if the version in the assembly is greater than or equal to the version of the existing information. This is the default option.<br/> |
| <span id="IASSEMBLYCACHEITEM_COMMIT_FLAG_FORCE_REFRESH"></span><span id="iassemblycacheitem_commit_flag_force_refresh"></span><dl> <dt>**IASSEMBLYCACHEITEM\_COMMIT\_FLAG\_FORCE\_REFRESH**</dt> </dl> | Replace existing information in the side-by-side store with the information for the assembly being installed.<br/>                                                                                                                               |



 

</dd> <dt>*pulDisposition* \[out, optional\]</dt> <dd> 

| Value                                                                                                                                                                                                                                                                                          | Meaning                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <span id="IASSEMBLYCACHEITEM_COMMIT_DISPOSITION_INSTALLED"></span><span id="iassemblycacheitem_commit_disposition_installed"></span><dl> <dt>**IASSEMBLYCACHEITEM\_COMMIT\_DISPOSITION\_INSTALLED**</dt> </dl>                          | The assembly is installed for the first time.<br/>                         |
| <span id="IASSEMBLYCACHEITEM_COMMIT_DISPOSITION_REFRESHED"></span><span id="iassemblycacheitem_commit_disposition_refreshed"></span><dl> <dt>**IASSEMBLYCACHEITEM\_COMMIT\_DISPOSITION\_REFRESHED**</dt> </dl>                          | The assembly replaces an existing assembly.<br/>                           |
| <span id="IASSEMBLYCACHEITEM_COMMIT_DISPOSITION_ALREADY_INSTALLED"></span><span id="iassemblycacheitem_commit_disposition_already_installed"></span><dl> <dt>**IASSEMBLYCACHEITEM\_COMMIT\_DISPOSITION\_ALREADY\_INSTALLED**</dt> </dl> | The assembly is already installed in the side-by-side assembly store.<br/> |



 

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                        | Description                            |
|-------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>    | The method succeeded.<br/>       |
| <dl> <dt>S\_FALSE</dt> </dl> | The method did not succeed.<br/> |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| DLL<br/>                      | <dl> <dt>Sxs.dll</dt> </dl> |



## See also

<dl> <dt>

[**IAssemblyCacheItem**](iassemblycacheitem.md)
</dt> </dl>

 

 




