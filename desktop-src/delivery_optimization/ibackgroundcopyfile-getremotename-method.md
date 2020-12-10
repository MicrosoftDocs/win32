---
title: IBackgroundCopyFile GetRemoteName method (Deliveryoptimization.h)
description: Retrieves the remote name of the file.
ms.assetid: 518857E0-C16A-400B-8F3D-5264B3CB43FF
keywords:
- GetRemoteName method
- GetRemoteName method, IBackgroundCopyFile interface
- IBackgroundCopyFile interface, GetRemoteName method
topic_type:
- apiref
api_name:
- IBackgroundCopyFile.GetRemoteName
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyFile::GetRemoteName method

Retrieves the remote name of the file.

## Syntax


```C++
HRESULT GetRemoteName(
  [out] LPWSTR *ppName
);
```



## Parameters

<dl> <dt>

*ppName* \[out\]
</dt> <dd>

Null-terminated string that contains the remote name of the file to transfer. The name is fully qualified. Call the [**CoTaskMemFree**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) function to free *ppName* when done.

</dd> </dl>

## Return value

This method returns **S_OK** on success or one of the standard COM **HRESULT** values on error.

## Remarks

To change the remote file name, call the [**IBackgroundCopyFile2::SetRemoteName**](ibackgroundcopyfile2-setremotename-method.md) method.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyFile is defined as 01B7BD23-FB88-4A77-8490-5891D3E4653A<br/>              |



## See also

<dl> <dt>

[**IBackgroundCopyFile**](ibackgroundcopyfile.md)
</dt> <dt>

[**IBackgroundCopyFile::GetLocalName**](ibackgroundcopyfile-getlocalname-method.md)
</dt> </dl>

 

