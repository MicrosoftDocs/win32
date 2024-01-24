---
title: INapComponentInfo GetIcon method (NapCommon.h)
description: Is used by the NAP System to get the icon of a health client.
ms.assetid: 6501fe12-1ec0-43a1-b672-b6cfd9a08d85
keywords:
- GetIcon method NAP
- GetIcon method NAP , INapComponentInfo interface
- INapComponentInfo interface NAP , GetIcon method
topic_type:
- apiref
api_name:
- INapComponentInfo.GetIcon
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentInfo::GetIcon method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapComponentInfo::GetIcon** callback method is used by the NAP System to get the icon of a health client.

## Syntax


```C++
HRESULT GetIcon(
  [out] CountedString **dllFilePath,
  [out] UINT32        *iconResourceId
);
```



## Parameters

<dl> <dt>

*dllFilePath* \[out\]
</dt> <dd>

A pointer to a pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) used to return the file path of the DLL that contains the icon.

</dd> <dt>

*iconResourceId* \[out\]
</dt> <dd>

A pointer to value used to return the resource ID of the icon to be used.

</dd> </dl>

## Return value

Return one of these error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

Icons should be localized according to the calling thread's language-id.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>


</dt> <dt>

[**INapComponentInfo**](inapcomponentinfo.md)
</dt> </dl>

 

 





