---
title: IVMVirtualPC GetVirtualMachineFiles method (VPCCOMInterfaces.h)
description: Retrieves an array of known virtual machine configuration files.
ms.assetid: 38771573-66fa-408a-95db-1281efdf8b73
keywords:
- GetVirtualMachineFiles method Virtual PC
- GetVirtualMachineFiles method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , GetVirtualMachineFiles method
topic_type:
- apiref
api_name:
- IVMVirtualPC.GetVirtualMachineFiles
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::GetVirtualMachineFiles method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves an array of known virtual machine configuration files.

## Syntax


```C++
HRESULT GetVirtualMachineFiles(
  [in]          VARIANT      inAdditionalSearchPaths,
  [in]          VARIANT_BOOL inExcludedRegisteredVMs,
  [out, retval] VARIANT      *outVirtualMachineFileList
);
```



## Parameters

<dl> <dt>

*inAdditionalSearchPaths* \[in\]
</dt> <dd>

These paths will be searched along with the paths set in the [**IVMVirtualPC::SearchPaths**](ivmvirtualpc-searchpaths.md) and [**IVMVirtualPC::DefaultVMConfigurationPath**](ivmvirtualpc-defaultvmconfigurationpath.md) properties.

</dd> <dt>

*inExcludedRegisteredVMs* \[in\]
</dt> <dd>

**TRUE** if registered virtual machines should be excluded from the array return in the *outVirtualMachineFileList* parameter and **FALSE** otherwise.

</dd> <dt>

*outVirtualMachineFileList* \[out, retval\]
</dt> <dd>

An array of path strings for the virtual machine configuration files found in the specified search paths.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                        | Description                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                              | The operation was successful.<br/>                                                        |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                | The *outVirtualMachineFileList* parameter is **NULL**.<br/>                               |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                             | The *inAdditionalSearchPaths* parameter is not an array of strings.<br/>                  |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                        | An unexpected error has occurred.<br/>                                                    |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl> | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/> |



 

## Remarks

The search paths used to retrieve the array of configuration files will include those set previously by [**IVMVirtualPC::SearchPaths**](ivmvirtualpc-searchpaths.md) and [**IVMVirtualPC::DefaultVMConfigurationPath**](ivmvirtualpc-defaultvmconfigurationpath.md) in addition to those specified by the *inAdditionalSearchPaths* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualPC is defined as 236ba0d9-a24a-4292-a132-27c1421dfd01<br/>               |



## See also

<dl> <dt>

[**IVMVirtualPC**](ivmvirtualpc.md)
</dt> </dl>

 

