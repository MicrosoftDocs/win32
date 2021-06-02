---
title: INapComponentInfo GetLocalizedString method (NapCommon.h)
description: Is used by the NAP System to get localized strings.
ms.assetid: ad5be180-6329-4c91-b4d1-871a4d83c323
keywords:
- GetLocalizedString method NAP
- GetLocalizedString method NAP , INapComponentInfo interface
- INapComponentInfo interface NAP , GetLocalizedString method
topic_type:
- apiref
api_name:
- INapComponentInfo.GetLocalizedString
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentInfo::GetLocalizedString method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapComponentInfo::GetLocalizedString** callback method is used by the NAP System to get localized strings.

## Syntax


```C++
HRESULT GetLocalizedString(
  [in]  MessageId     msgId,
  [out] CountedString **string
);
```



## Parameters

<dl> <dt>

*msgId* \[in\]
</dt> <dd>

A [**MessageId**](nap-datatypes.md) that contains the resource ID of the string to localize.

</dd> <dt>

*string* \[out\]
</dt> <dd>

A pointer to a pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) that contains the localized version of the message.

</dd> </dl>

## Return value

Return one of these error codes based on the result of this operation.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | The operation is successful.<br/>                            |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

Strings should be localized according to the calling thread's language-id.

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

 

 





