---
title: IMessenger MyPhoneNumber property
description: Retrieves the stored phone number of the local client user.
ms.assetid: 5f409553-fe8e-463d-bd12-9e9af096d3aa
keywords:
- MyPhoneNumber property Windows Messenger
- MyPhoneNumber property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , MyPhoneNumber property
topic_type:
- apiref
api_name:
- IMessenger.MyPhoneNumber
- IMessenger.get_MyPhoneNumber
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessenger::MyPhoneNumber property

\[**MyPhoneNumber** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the stored phone number of the local client user.

This property is read-only.

## Syntax


```C++
HRESULT get_MyPhoneNumber(
  [in]          MPHONE_TYPE PhoneType,
  [out, retval] BSTR        *pbstrNumber
);
```



## Property value

A string (not a **numeric** data type) that contains the requested phone number. This number may contain punctuation, depending on how the data was collected.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                                         |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                            |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrNumber* is a **NULL** pointer. <br/>                                                |
| <dl> <dt>MSGR\_E\_NOT\_LOGGED\_ON</dt> </dl>   | Client was not signed in to the primary service at the time this method was called. <br/> |
| <dl> <dt>E\_FAIL</dt> </dl>                    | The requested phone number does not exist. *pbstrNumber* will be a **NULL** string.<br/>  |



## Remarks

> [!Note]  
> This property is not available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**Phone**](im-imessenger-phone.md)
</dt> </dl>

 

 





