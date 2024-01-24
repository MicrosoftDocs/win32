---
title: INapComponentConfig IsUISupported method (NapCommon.h)
description: Specifies whether the component supports a customized user interface.
ms.assetid: 044f8014-f041-4e9c-922a-2691b799ba84
keywords:
- IsUISupported method NAP
- IsUISupported method NAP , INapComponentConfig interface
- INapComponentConfig interface NAP , IsUISupported method
topic_type:
- apiref
api_name:
- INapComponentConfig.IsUISupported
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig::IsUISupported method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **IsUISupported** method specifies whether the component supports a customized user interface.

## Syntax


```C++
HRESULT IsUISupported(
  [out] BOOL *isSupported
) const;
```



## Parameters

<dl> <dt>

*isSupported* \[out\]
</dt> <dd>

A pointer to a BOOL that is set to **TRUE** if the component supports a customized user interface and **FALSE** otherwise.

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

A component's customized user interface should be launched using [**INapComponentConfig::InvokeUI**](inapcomponentconfig-invokeui.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapComponentConfig**](inapcomponentconfig.md)
</dt> <dt>

[**INapComponentConfig::InvokeUI**](inapcomponentconfig-invokeui.md)
</dt> </dl>

 

 





