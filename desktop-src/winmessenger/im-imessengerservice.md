---
title: IMessengerService interface
description: Do not use. The primary interface for an individual MessengerService object.
ms.assetid: 7f20ec7e-a379-4545-80b8-c818f0999aaf
keywords:
- IMessengerService interface Windows Messenger
- IMessengerService interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessengerService
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

# IMessengerService interface

\[**IMessengerService** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The primary interface for an individual [**MessengerService**](im-messengerservice.md) object.

## Members

The **IMessengerService** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessengerService** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMessengerService** interface has these properties.



| Property                                                                 | Access type          | Description                                                                                                                       |
|:-------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**MyFriendlyName**](im-imessengerservice-myfriendlyname.md)<br/> | Read-only<br/> | Retrieves the local user's friendly name that corresponds to the selected service. <br/>                                    |
| [**MySigninName**](im-imessengerservice-mysigninname.md)<br/>     | Read-only<br/> | Retrieves the local user's sign-in name that corresponds to the selected service.<br/>                                      |
| [**MyStatus**](im-imessengerservice-mystatus.md)<br/>             | Read-only<br/> | Retrieves the status of the local user in a service.<br/>                                                                   |
| [**Property**](im-imessengerservice-property.md)<br/>             |                      | Retrieves a specific property of the service.<br/>                                                                          |
| [**ServiceID**](im-imessengerservice-serviceid.md)<br/>           | Read-only<br/> | Retrieves the service ID of the contact associated with the selected service.<br/>                                          |
| [**ServiceName**](im-imessengerservice-servicename.md)<br/>       | Read-only<br/> | Retrieves the service name of the contact associated with this [**MessengerContact**](im-messengercontact.md) object.<br/> |



 

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



 

 





