---
title: IMessengerGroup Name property
description: Sets or retrieves the name of the group.
ms.assetid: e68c27b7-b836-4757-9002-aeaed3fc2fa0
keywords:
- Name property Windows Messenger
- Name property Windows Messenger , IMessengerGroup interface
- IMessengerGroup interface Windows Messenger , Name property
topic_type:
- apiref
api_name:
- IMessengerGroup.Name
- IMessengerGroup.get_Name
- IMessengerGroup.put_Name
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMessengerGroup::Name property

\[**Name** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves

the name of the group.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
                BSTR bstrName
);

HRESULT get_Name(
  [out, retval] BSTR *bstrName
);
```



## Property value

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                       |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success.<br/>                           |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pbstrName* is a **NULL** pointer.<br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | String comparison failed.<br/>          |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Local user is not logged on.<br/>       |
| <dl> <dt>MSGR\_E\_NOT\_LOGGED\_ON</dt> </dl>   | Client is offline.<br/>                 |



## Remarks

The following table lists the error codes returned by this property.



| Error Code                       | Meaning                                                             |
|----------------------------------|---------------------------------------------------------------------|
| 0x80004005                       | Local user is not logged on.                                        |
| 0x8007000E                       | String comparison failed.                                           |
| MSGR\_E\_NOT\_LOGGED\_ON         | Client is offline.                                                  |
| MSGR\_E\_GROUPS\_NOT\_ENABLED    | The current service does not support groups.                        |
| MSGR\_E\_GROUP\_DOES\_NOT\_EXIST | The group to be renamed does not exist.                             |
| MSGR\_E\_GROUP\_NAME\_TOO\_LONG  | The new name of the group exceeds the maximum number of characters. |
| MSGR\_E\_BAD\_GROUP\_NAME        | The new name of the group is invalid.                               |
| MSGR\_E\_CANNOT\_RENAME          | The group "Other Contacts" is read-only and cannot be renamed.      |



 

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

[**IMessengerGroup**](im-imessengergroup.md)
</dt> </dl>

 

 





