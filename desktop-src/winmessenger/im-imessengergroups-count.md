---
title: IMessengerGroups Count property
description: Retrieves the number of groups.
ms.assetid: d50f5eb0-712c-448c-94bd-3447f7b911e5
keywords:
- Count property Windows Messenger
- Count property Windows Messenger , IMessengerGroups interface
- IMessengerGroups interface Windows Messenger , Count property
topic_type:
- apiref
api_name:
- IMessengerGroups.Count
- IMessengerGroups.get_Count
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

# IMessengerGroups::Count property

\[**Count** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the number of groups.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out, retval] long *pcCount
);
```



## Property value

Pointer to a **LONG** that provides the number of [**MessengerGroup**](im-messengergroup.md) objects in the collection.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                      |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success.<br/>                          |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pcGroups* is a **NULL** pointer.<br/> |



## Remarks

This property does not return any error codes.

This property is available for scripting languages.

> [!Note]  
> This property is available for scripting languages.

 

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

[**IMessengerGroups**](im-imessengergroups.md)
</dt> </dl>

 

 





