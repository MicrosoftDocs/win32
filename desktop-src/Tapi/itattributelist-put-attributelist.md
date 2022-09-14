---
description: The put\_AttributeList method sets the list of attributes.
ms.assetid: f7d57c0c-9114-42a4-b2bc-c812334d8136
title: ITAttributeList::put_AttributeList method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITAttributeList::put\_AttributeList method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **put\_AttributeList** method sets the list of attributes.

## Syntax


```C++
HRESULT put_AttributeList(
  [in] VARIANT newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

Array of attributes to set.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *newVal* parameter is not valid.<br/>                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITAttributeList**](itattributelist.md)
</dt> <dt>

[**ITAttributeList::get\_AttributeList**](itattributelist-get-attributelist.md)
</dt> </dl>

 

 




