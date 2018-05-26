---
title: IMessengerServices interface
description: Do not use. Manipulates the list of services.
ms.assetid: 26d69dc4-7760-41b2-9276-cca67e8f112e
keywords:
- IMessengerServices interface Windows Messenger
- IMessengerServices interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessengerServices
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessengerServices interface

\[**IMessengerServices** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Manipulates the list of services.

## Members

The **IMessengerServices** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessengerServices** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMessengerServices** interface has these methods.



| Method                                     | Description                                       |
|:-------------------------------------------|:--------------------------------------------------|
| [**Item**](im-imessengerservices-item.md) | Retrieves a specific service by index.<br/> |



 

### Properties

The **IMessengerServices** interface has these properties.



| Property                                                                  | Access type          | Description                                                                                                                   |
|:--------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](im-imessengerservices--newenum.md)<br/>            | Read-only<br/> | Enumerates the [**MessengerService**](im-messengerservice.md) objects in a collection.<br/>                            |
| [**Count**](im-imessengerservices-count.md)<br/>                   | Read-only<br/> | Retrieves the number of [**MessengerServices**](im-messengerservices.md) objects in the collection.<br/>               |
| [**PrimaryService**](im-imessengerservices-primaryservice.md)<br/> | Read-only<br/> | Returns the [**MessengerService**](im-messengerservice.md) object for the primary service for the primary client.<br/> |



 

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



 

 





