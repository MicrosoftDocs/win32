---
title: INapComponentInfo ConvertErrorCodeToMessageId method (NapCommon.h)
description: Is used by the NAP System to request the health client convert an HRESULT error code into a message ID.
ms.assetid: 760dd039-5b9c-4227-9939-ad6ea23f5b81
keywords:
- ConvertErrorCodeToMessageId method NAP
- ConvertErrorCodeToMessageId method NAP , INapComponentInfo interface
- INapComponentInfo interface NAP , ConvertErrorCodeToMessageId method
topic_type:
- apiref
api_name:
- INapComponentInfo.ConvertErrorCodeToMessageId
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentInfo::ConvertErrorCodeToMessageId method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapComponentInfo::ConvertErrorCodeToMessageId** callback method is used by the NAP System to request the health client convert an HRESULT error code into a message ID.

## Syntax


```C++
HRESULT ConvertErrorCodeToMessageId(
  [in]  HRESULT   errorCode,
  [out] MessageId *msgId
);
```



## Parameters

<dl> <dt>

*errorCode* \[in\]
</dt> <dd>

The [**error code**](nap-error-constants.md) from the NAP System that is to be converted into a **MessageId**.

</dd> <dt>

*msgId* \[out\]
</dt> <dd>

A pointer to a [**MessageId**](nap-datatypes.md) that contains the resource ID of the corresponding localized string.

</dd> </dl>

## Return value

Return one of these error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

The returned **MessageId** is used by the NAP System to retrieve a localized string.

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

 

 





