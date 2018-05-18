---
title: Windows Messenger Service Reference
description: Service reference information for Windows Messenger.
ms.assetid: '44708870-7f52-4538-902d-cbaae3c66b18'
---

# Windows Messenger Service Reference

\[Windows Messenger is no longer available for use as of Windows Vista. For more information, see [Windows Messenger](im-messenger-entry.md).\]

This is the entry page to the reference documentation for the Messenger service  APIs.

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

Applications cannot connect to Microsoft .NET Messenger Service or use any of the Messenger service  APIs until they have successfully authenticated with the Messenger Lock and Key mechanism. After authentication is complete, the Messenger service  APIs are unlocked and can be used as necessary by the application.

The Messenger service  API references are provided for Microsoft Visual C++. Also there is an overview included ([Messenger Lock and Key API](im-lock-and-key-ovw.md)), that provides general guidelines on unlocking and using the Messenger service  APIs.

## Enums



|                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LockError**](im-lockerror-enum.md)Do not use. Provides a list of Lock and Key error status codes.<br/>                               |
| [**LockStatus**](im-lockstatus-enum.md)Do not use. Provides the list of possible status codes for the Messenger Lock and Key API.<br/>  |
| [**SESSION\_STATE**](im-session-state-enum.md)Do not use. Provides the list of possible state codes of the session invitation. <br/>    |
| [**SESSION\_FLAGS**](im-session-flags-enum.md)Do not use. Provides the list of possible flag codes for the session invitation.<br/>     |
| [**SESSION\_RESULT**](im-session-result-enum.md)Do not use. Provides the list of possible result codes of the session invitation. <br/> |



 

## Events



|                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OnAlertReceived**](im-dmessengerprivateevents-onalertreceived.md)Fires when an alert notification is sent from a Messenger service to a Messenger client application. <br/>                             |
| [**OnContactListAdd**](im-dmessengerprivateevents-oncontactlistadd.md)Notifies a Messenger client that a contact has been added to the contact list.<br/>                                                  |
| [**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md)Notifies a Messenger client that an authentication challenge from a Messenger service has been received. <br/>                         |
| [**OnLockEnable**](im-dmessengerprivateevents-onlockenable.md)Notifies a Messenger client with the status of the Messenger Lock and Key APIs.<br/>                                                         |
| [**OnLockResult**](im-dmessengerprivateevents-onlockresult.md)Returns the result of a Lock and Key authentication transaction between a Messenger client and the Microsoft .NET Messenger Service.<br/>    |
| [**BeforeAppLaunch**](im-dmsgrsessionevents-beforeapplaunch.md)Fires when the session's application is about to be launched. <br/>                                                                         |
| [**OnAccepted**](im-dmsgrsessionevents-onaccepted.md)Fires when the recipient has accepted the invitation. <br/>                                                                                           |
| [**OnAppNotPresent**](im-dmsgrsessionevents-onappnotpresent.md)Fires when the application requested by the invitation is not present. <br/>                                                                |
| [**OnCancelled**](im-dmsgrsessionevents-oncancelled.md)Fires when the session has been canceled by the inviter. <br/>                                                                                      |
| [**OnContextData**](im-dmsgrsessionevents-oncontextdata.md)Fires when new context data has arrived.<br/>                                                                                                   |
| [**OnDeclined**](im-dmsgrsessionevents-ondeclined.md)Fires when the recipient has declined the invitation.<br/>                                                                                            |
| [**OnReadyToLaunch**](im-dmsgrsessionevents-onreadytolaunch.md)Fires when the session is approved to start.<br/>                                                                                           |
| [**OnSendError**](im-dmsgrsessionevents-onsenderror.md)Fires when the last operation fails when sending.<br/>                                                                                              |
| [**OnStateChanged**](im-dmsgrsessionevents-onstatechanged.md)Fires when the session state has changed from the previous state.<br/>                                                                        |
| [**OnTermination**](im-dmsgrsessionevents-ontermination.md)Fires when the session has ended.<br/>                                                                                                          |
| [**OnAppRegistered**](im-dmsgrsessionmanagerevents-onappregistered.md)Fires when a new application has been registered.<br/>                                                                               |
| [**OnAppShutdown**](im-dmsgrsessionmanagerevents-onappshutdown.md)Fires when Windows Messenger is shutting down.<br/>                                                                                      |
| [**OnAppUnRegistered**](im-dmsgrsessionmanagerevents-onappunregistered.md)Fires when an application has been unregistered.<br/>                                                                            |
| [**OnInvitation**](im-dmsgrsessionmanagerevents-oninvitation.md)Fires when a new session invitation has been received.<br/>                                                                                |
| [**OnLockChallenge**](im-dmsgrsessionmanagerevents-onlockchallenge.md)Notifies a Messenger client that an authentication challenge from a Messenger service has been received.<br/>                        |
| [**OnLockEnable**](im-dmsgrsessionmanagerevents-onlockenable.md)Notifies a Messenger client with the status of the Messenger Lock and Key APIs. <br/>                                                      |
| [**OnLockResult**](im-dmsgrsessionmanagerevents-onlockresult.md)Returns the result of a Lock and Key authentication transaction between a Messenger client and the Microsoft .NET Messenger Service. <br/> |
| [**OnLockStatusChanged**](im-dmsgrsessionmanagerevents-onlockstatuschanged.md)Fires when the lock status changes. <br/>                                                                                    |



 

## DispInterfaces



|                                                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DMessengerPrivateEvents**](im-dmessengerprivateevents.md)Do not use. The [**DMessengerPrivateEvents**](im-dmessengerprivateevents.md) dispinterface fires events in the Messenger client when notifications from [**IMessengerPrivate**](im-imessengerprivate.md) are received. <br/>             |
| [**DMsgrSessionEvents**](im-dmsgrsessionevents.md)Do not use. The [**DMessengerPrivateEvents**](im-dmessengerprivateevents.md) dispinterface fires events in the Messenger client when notifications from [**IMsgrSession**](im-imsgrsession.md) are received.<br/>                                  |
| [**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md)Do not use. The [**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md) dispinterface fires events in the Messenger client when notifications from [**IMsgrSessionManager**](im-imsgrsessionmanager.md) are received. <br/> |



 

## Interfaces



|                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMessengerPrivate**](im-imessengerprivate.md)Do not use. The [**IMessengerPrivate**](im-imessengerprivate.md) interface is a Messenger service  API that provides programmatic access to the [**MessengerPriv**](im-messengerpriv-object.md) object.<br/>                    |
| [**IMsgrLock**](im-imsgrlock.md)Do not use. The [**IMsgrLock**](im-imsgrlock.md) interface implements an API that is used to unlock Licensed Messenger objects.<br/>                                                                                                             |
| [**IMsgrSession**](im-imsgrsession.md)Do not use. The [**IMsgrSession**](im-imsgrsession.md) interface provides programmatic access to the [**MsgrSession**](im-msgrsession-object.md) object. <br/>                                                                            |
| [**IMsgrSessionManager**](im-imsgrsessionmanager.md)Do not use. The [**IMsgrSessionManager**](im-imsgrsessionmanager.md) interface is a Messenger service  API that provides programmatic access to the [**MsgrSessionManager**](im-msgrsessionmanager-object.md) object. <br/> |



 

## Objects



|                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MessengerPriv**](im-messengerpriv-object.md)Do not use. The Messenger service  [**MessengerPriv**](im-messengerpriv-object.md) object.<br/> |
| [**MsgrSession**](im-msgrsession-object.md)Do not use. The Messenger client session object. <br/>                                               |
| [**MsgrSessionManager**](im-msgrsessionmanager-object.md)Do not use. The Messenger client session manager object. <br/>                         |



 

 

 





