---
title: IMessengerGroups interface
description: Do not use. The IMessengerGroups interface provides methods and properties to handle groups of users.
ms.assetid: d5d75ce5-6b54-4d65-a1b9-0065e19aee0a
keywords:
- IMessengerGroups interface Windows Messenger
- IMessengerGroups interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessengerGroups
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IMessengerGroups interface

\[**IMessengerGroups** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **IMessengerGroups** interface provides methods and properties to handle groups of users.

## Members

The **IMessengerGroups** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessengerGroups** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMessengerGroups** interface has these methods.



| Method                                       | Description                                                                                          |
|:---------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**Item**](im-imessengergroups-item.md)     | Retrieves a specific [**MessengerGroup**](im-messengergroup.md) object by numeric index.<br/> |
| [**Remove**](im-imessengergroups-remove.md) | Removes a [**MessengerGroup**](im-messengergroup.md) object from a collection.<br/>           |



 

### Properties

The **IMessengerGroups** interface has these properties.



| Property                                                     | Access type          | Description                                                                                    |
|:-------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------|
| [**\_NewEnum**](im-imessengergroups--newenum.md)<br/> | Read-only<br/> | Enumerates the [**MessengerGroup**](im-messengergroup.md) objects in a collection.<br/> |
| [**Count**](im-imessengergroups-count.md)<br/>        | Read-only<br/> | Retrieves the number of groups.<br/>                                                     |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





