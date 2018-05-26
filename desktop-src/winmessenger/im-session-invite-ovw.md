---
title: Messenger Session Invite and Messenger Private APIs
description: This topic provides information about the Messenger Session Invite APIs that provide a way to run peer-to-peer applications for any two Messenger client users.
ms.assetid: 8cf20142-f7fe-49ee-913b-8178d7bb1169
keywords:
- Windows Messenger,Messenger Session Invite
- Messenger client,Messenger Session Invite
- Windows Messenger,Messenger Private
- Messenger client,Messenger Private
- Messenger Session Invite
- Messenger Private
- Microsoft .NET Messenger Service
- unlocking Messenger service
- Messenger service,unlocking
- Messenger Lock and Key,unlocking Messenger service
- Lock and Key,unlocking Messenger service
- Windows Messenger,Lock and Key
- Windows Messenger,unlocking Messenger service
- MsgrSession object
- MsgrSessionManager object
- MessengerPriv object
- Windows Messenger,sending invitations
- Messenger client,sending invitations
- Messenger service,sending invitations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Messenger Session Invite and Messenger Private APIs

This topic provides information about the Messenger Session Invite APIs that provide a way to run peer-to-peer applications for any two Messenger client users.

The Messenger Session Invite and Messenger Private APIs exposed by Windows Messenger enables two client programs to connect programmatically using the Microsoft .NET Messenger Service.

> [!Note]  
> By default, the Messenger Session Invite and Messenger Private APIs are locked only for use with the Microsoft .NET Messenger Service to establish a peer-to-peer connection. They are not locked when used in conjunction with services other than the Microsoft .NET Messenger Service.

 

The topics addressed are:

-   [Introduction](#introduction)
-   [Prerequisites](#prerequisites)
-   [Terminology](#terminology)
-   [Launching Session Invite Within Messenger](#launching-session-invite-within-messenger)
-   [Launching Session Invite Within an Application](#launching-session-invite-within-an-application)
    -   [Create a Session Object](#create-a-session-object)
    -   [Unlock the Messenger APIs](#unlock-the-messenger-apis)
    -   [Send an Invitation](#send-an-invitation)
    -   [Notifications Fired From a Messenger Service](#notifications-fired-from-a-messenger-service)
-   [Additional Information](#additional-information)
    -   [The Local Address of the MsgrSession Object](#the-local-address-of-the-msgrsession-object)
-   [Related topics](#related-topics)

## Introduction

The Messenger Session Invite API provides a way to run peer-to-peer applications for any two Messenger client users. Unlike earlier versions of Messenger client, the messenger session invite mechanism does not depend on Microsoft DirectPlay. It does, however, support DirectPlay invitations from earlier versions of Messenger client.

Users who are already communicating through Messenger client can start both sides of an application from within a Messenger client. Users can also start an application first and then invite a user to join.

The following graphic illustrates the relationship between two Messenger client users who run a peer-to-peer application. Each Messenger user's platform establishes connection with one another, enabling the application to connect on both sides.

![relationship between two applications connected via session invite.](graphics/session-invite-rlnship.gif)

> [!Note]  
> A license and ID/key pair are required in order for an application to access the Microsoft .NET Messenger Service using the Messenger Session Invite and Messenger Private APIs. The license requires an application that uses this API to follow certain guidelines designed to help help protect the integrity of the Messenger service . The ID/key pair is used to unlock the Messenger service   APIs and to authenticate the application. To unlock the Microsoft .NET Messenger Service, see the [Unlock the Messenger APIs](#unlock-the-messenger-apis) section of this topic. For more information, see the [Messenger Lock and Key API](im-lock-and-key-ovw.md).

 

> \[!Important\]  
> ID/key pairs are no longer being issued.

 

## Prerequisites

Users should be familiar with Microsoft Visual C++ or Microsoft Visual Basic and know how to call an API exposed by Component Object Model (COM) objects.

## Terminology

This section defines certain terms that are used throughout the article.



|                                   |                                                                                                                                                                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Messenger client                  | Application that uses the APIs exposed by Windows Messenger to provide client-side functionality for use with Messenger service s.                                                                              |
| Messenger service                 | Service that a Messenger client application uses (for example, the Microsoft .NET Messenger Service.                                                                                                            |
| Messenger Lock and Key            | A friendly name for the mechanism that is used to unlockMessenger service  APIs programmatically. For more information see [Messenger Lock and Key API](im-lock-and-key-ovw.md).                               |
| Messenger Session Invite          | A friendly name for a set of Messenger service  APIs that are locked with the Lock and Key mechanism.                                                                                                           |
| ID                                | An alphanumeric string value that identifies an application used to unlock the Messenger service  APIs.                                                                                                         |
| Key                               | An alphanumeric string value that identifies an application used to access the Messenger service  APIs.                                                                                                         |
| Globally Unique Identifier (GUID) | A text string that represents a Class ID. The valid format of a GUID is {*xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx*} where *x* is a hexadecimal digit (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F). Letters must be uppercase. |
| Internet Protocol (IP)            | TCP/IP.                                                                                                                                                                                                         |
| Session ID                        | A variable used for encryption between peer-to-peer sessions.                                                                                                                                                   |
| DirectPlay                        | The Session Invite mechanism used in earlier versions of Windows Messenger.                                                                                                                                     |



 

## Launching Session Invite Within Messenger

Users who are already communicating through Messenger can start an application with each other from within Messenger by following these steps:

1.  Sign in to Messenger.
2.  Select the application to be used in the invitation.
3.  Choose a recipient, and then click **OK**.

When installing an application, register it so that it belongs to the Messenger Invite menu. By doing this, the user can invite contacts to participate in a peer-to-peer session with this application from the Messenger Invite menu. The user can also accept an invitation to participate in a peer-to-peer session with this application when someone else invites him or her.

During the application registration, specify a location from which a recipient can download the application so that the recipient can run it regardless of whether it has been installed.

To register an application manually, you need a GUID, URL, path, and application name. The GUID is the key identifier for the application and must be unique. The other three values are the strings that identify the key. URL is the download site from which a user can retrieve the application. The path is an absolute or relative path of the application to be run. The application name is used as an identifier for the application. The new key to be created is located at HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MessengerService\\SessionManager\\Apps. After the application is manually registered, it appears in the Messenger Invite menu and can be used in a peer-to-peer session.

## Launching Session Invite Within an Application

You can send an invitation to any running Messenger application using the Microsoft Session Invite API. Although similar to using the Messenger UI, this method is different in two ways. First, the application does not have to be launched on the originating side because it is already running. Second, context data (GUID, IP, sign-in name, and [**SessionID**](im-imsgrsession-sessionid-property.md)) from the application on the originating side can be provided at the beginning of the invitation sequence.

The following describe each step of the invitation process.

-   [Create a Session Object](#create-a-session-object)
-   [Unlock the Messenger APIs](#unlock-the-messenger-apis)
-   [Send an Invitation](#send-an-invitation)
-   [Notifications Fired From a Messenger Service](#notifications-fired-from-a-messenger-service)

### Create a Session Object

Create a [**MsgrSessionManager**](im-msgrsessionmanager-object.md) object using the Messenger Session Invite API. The **MsgrSessionManager** object, when created, is composed of the initial context including both users' sign-in names and the download location (URL) for the application from the registry. After you create the **MsgrSessionManager** object, create a [**MsgrSession**](im-msgrsession-object.md) object.

Upon creating the session, the [**State**](im-imsgrsession-state-property.md) property changes and a [**SessionID**](im-imsgrsession-sessionid-property.md) property is created. The **SessionID** property takes the format of {*xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx*} and the **State** property can be one of eight [**SESSION\_STATE**](im-session-state-enum.md) values.

> [!Note]  
> A new session must be created each time you want to send an invitation.

 

### Unlock the Messenger APIs

To unlock the Messenger service  APIs, you must have a license and valid ID/key pair. The license requires an application that uses the API to follow guidelines designed to help protect the integrity of the Messenger service . The Lock and Key mechanism helps prevent unauthorized applications from using the Messenger service  APIs.

> [!Note]  
> A Messenger client cannot unlock the Messenger service  APIs more than once during a session. Therefore, if an application attempts to re-authenticate during the same session, the **MSGR\_E\_API\_ALREADY\_UNLOCKED** error code is returned and there is no resulting transaction.

 

For more information about the Messenger Lock and Key mechanism used to help control access to the Messenger service  APIs as well as the protocol and service interfaces, see [Messenger Lock and Key API](im-lock-and-key-ovw.md).

### Send an Invitation

The [**Invite**](im-imsgrsession-invite-method.md) method is used to send an invitation to a user. This method creates a session containing all the inviter's session information on the Messenger client server. In addition, the Messenger client server creates a session object on the recipient's Messenger client platform. When this happens, a dialog box is displayed that offers the user the choice to accept, decline, or cancel the invitation. If the recipient declines or cancels the invitation, the result is sent back to the inviter's application and the session is terminated. If the recipient accepts the invitation, the Messenger client platform confirms that the application is installed on the computer.

If the application is not installed, the Messenger client declines the invitation and launches a browser to the site from which the recipient can download it. After the application is successfully installed, the Messenger client sends an acceptance to the inviter's Messenger client switchboard server and the application is launched. The inviter's Messenger client then passes a cookie to the locally launched application with which it creates its own [**MsgrSessionManager**](im-msgrsessionmanager-object.md) object.

At this point, the application is running on both computers and the data is being shared through the session object known to both instances of Messenger client.

The following example shows how to use the [**Invite**](im-imsgrsession-invite-method.md) method. This snippet also includes references to the [MessengerAPI API](http://messenger.microsoft.com). For more information, see [Messenger API SDK Documentation](http://messenger.microsoft.com).


```C++
/******************************************************************************
How to call WM session invite...

    ' 1. Create a context data variable to be used. Context data
         variable is string that contains information specific to   
         the application launching session that needs to be shared   
         across clients
    ' 2. Create and assign a value for the sign-in name to a
         variable.
    ' 3. Create and assign a value for the ServiceID of the user to        
         be invited.
    ' 4. Set the MsgrContact object to the variables created in
         steps 2 and 3
    ' 5. Create a session object using session manager
    ' 6. Set the application id on the session object
    ' 7. Create session using contact ID and context data

CMessengerSessionImpl class has two methods,

1. Initialize : Creates the session manager, messenger client
                objects and gets the interface pointers
2. Invite:      Makes the invite session call.
******************************************************************************/

class CMessengerSessionImpl
{
private:
         // MessengerAPI.Messenger Object
    IMessenger* m_pIMessenger;
    // MessengerPrivate.MsgrSessionManager  
    IMsgrSessionManager* m_pISessionMgr;
public:
    CMessengerSessionImpl()
    {
    // MessengerAPI.Messenger Object
         m_pIMessenger = NULL;
         // MessengerPrivate.MsgrSessionManager
         m_pISessionMgr = NULL;
    }

    ~CMessengerSessionImpl()
    {
        if(m_pIMessenger)
        {
            m_pIMessenger->Release();
        }
        if(m_pISessionMgr)
        {
            m_pISessionMgr->Release();
        }
    }
    
    HRESULT Initialize()
    {
        // Session manager
        hr = CoCreateInstance(CLSID_MsgrSessionManager,NULL,CLSCTX_LOCAL_SERVER,
                        IID_MsgrSessionManager, (LPVOID *)&amp;m_pISessionMgr);

        if(SUCCEEDED(hr))
        {
            // Messenger client api
            hr = CoCreateInstance(CLSID_Messenger,NULL,CLSCTX_LOCAL_SERVER,
                IID_IMessenger, (LPVOID *)&amp;m_pIMessenger);
        }
        return hr;
    }
    HRESULT Invite(BSTR bstrSigninName, BSTR bstrServiceID, BSTR bstrAppGUID, BSTR bstrContextData)
    {
        // Get the Contact
        HRESULT hr=E_POINTER;
        IDispatch** ppContact;
        // Get the Messenger Contact object
        hr = m_pIMessenger->GetContact(bstrSigninName, bstrServiceID, ppContact);
        if(SUCCEEDED(hr))
        {
        IDispatch** ppSession;
        // Create a session object using session manager
        hr = m_pISessionMgr->CreateSession(ppSession);
        if(SUCCEEDED(hr))
        {
            IMsgrSession* pIMsgrSession;
            HRESULT hr = (*ppSession)->QueryInterface(IID_IMsgrSession, (void **) &amp;pIMsgrSession);
            if(SUCCEEDED(hr))
            {
            // Set the application id eg. "{44BBA842-CC51-11CF-AAFA-00AA00B6015C}" for netmeeting
                hr = pIMsgrSession->put_Application(bstrAppGUID);
                if(SUCCEDED(hr))
                {
                    hr = pIMsgrSession->Invite(bstrContextData, *ppContact);
                }
            }
            (*ppSession)->Release();
        }
        if(*ppContact)
        {
            (*ppContact)->Release();
        }
        // Work on session object.
        // Release pIMsgrSession & hence session object when done.
    }
};
```



### Notifications Fired From a Messenger Service

In the preceding example, the MsgrSession, MsgrSessionManager, and MessengerPriv objects are declared with types [**MsgrSession**](im-msgrsession-object.md), [**MsgrSessionManager**](im-msgrsessionmanager-object.md), and [**MessengerPrivate**](im-messengerpriv-object.md), respectively. The following tables show the events that are fired from the three interfaces in C++.

MsgrSession events reference



| C++ Reference                                                    | Description                                                            |
|------------------------------------------------------------------|------------------------------------------------------------------------|
| [**BeforeAppLaunch**](im-dmsgrsessionevents-beforeapplaunch.md) | Fires when the session's application is about to be launched.          |
| [**OnAccepted**](im-dmsgrsessionevents-onaccepted.md)           | Fires when he recipient has accepted the invitation.                   |
| [**OnAppNotPresent**](im-dmsgrsessionevents-onappnotpresent.md) | Fires when the application requested by the invitation is not present. |
| [**OnCancelled**](im-dmsgrsessionevents-oncancelled.md)         | Fires when the session has been cancelled by the inviter.              |
| [**OnContextData**](im-dmsgrsessionevents-oncontextdata.md)     | Fires when new context data has arrived.                               |
| [**OnDeclined**](im-dmsgrsessionevents-ondeclined.md)           | Fires when the recipient has declined the invitation.                  |
| [**OnReadyToLaunch**](im-dmsgrsessionevents-onreadytolaunch.md) | Fires when the session is approved for launch.                         |
| [**OnSendError**](im-dmsgrsessionevents-onsenderror.md)         | Fires when the last operation failed when sending.                     |
| [**OnStateChanged**](im-dmsgrsessionevents-onstatechanged.md)   | Fires when the session state has changed from prevState.               |
| [**OnTermination**](im-dmsgrsessionevents-ontermination.md)     | Fires when the session has ended.                                      |



 

MsgrSessionManager events reference



| C++ Reference                                                               | Description                                                                                                                          |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**OnAppRegistered**](im-dmsgrsessionmanagerevents-onappregistered.md)     | Fires when a new application has been registered.                                                                                    |
| [**OnAppShutdown**](im-dmsgrsessionmanagerevents-onappshutdown.md)         | Fires when a Messenger client application is shutting down.                                                                          |
| [**OnAppUnRegistered**](im-dmsgrsessionmanagerevents-onappunregistered.md) | Fires when an application has been unregistered.                                                                                     |
| [**OnInvitation**](im-dmsgrsessionmanagerevents-oninvitation.md)           | Fires when a new session invitation has been received.                                                                               |
| [**OnLockChallenge**](im-dmsgrsessionmanagerevents-onlockchallenge.md)     | Notifies a Messenger client that an authentication challenge from a Messenger service has been received.                             |
| [**OnLockEnable**](im-dmsgrsessionmanagerevents-onlockenable.md)           | Notifies a Messenger client with the status of the Messenger Lock and Key APIs.                                                      |
| [**OnLockResult**](im-dmsgrsessionmanagerevents-onlockresult.md)           | Returns the result of a Lock and Key authentication transaction between a Messenger client and the Microsoft .NET Messenger Service. |



 

MessengerPriv events reference



| C++ Reference                                                           | Description                                                                                                                          |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**OnAlertReceived**](im-dmessengerprivateevents-onalertreceived.md)   | Fires when an alert notification is sent from a Messenger service to a Messenger client application.                                 |
| [**OnContactListAdd**](im-dmessengerprivateevents-oncontactlistadd.md) | Notifies a Messenger client that a contact has been added to the contact list.                                                       |
| [**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md)   | Notifies a Messenger client that an authentication challenge from a Messenger service has been received.                             |
| [**OnLockEnable**](im-dmessengerprivateevents-onlockenable.md)         | Notifies a Messenger client with the status of the Messenger Lock and Key APIs.                                                      |
| [**OnLockResult**](im-dmessengerprivateevents-onlockresult.md)         | Returns the result of a Lock and Key authentication transaction between a Messenger client and the Microsoft .NET Messenger Service. |



 

## Additional Information

### The Local Address of the MsgrSession Object

The [**LocalAddress**](im-imsgrsession-localaddress-property.md) of a [**MsgrSession**](im-msgrsession-object.md) object can be modified by using the **LocalAddress** property. This property does not change the physical IP address of the computer. It only modifies the data member within the object. Both the inviter and recipient can modify their own **LocalAddress** property by doing the following steps before launching a peer-to-peer application session.

1.  The inviter [creates a session object](#create-a-session-object).
2.  Before sending an invitation, if the inviter wants to send a specific local address, the inviter must set the [**LocalAddress**](im-imsgrsession-localaddress-property.md) property.
3.  Inviter sends an [invitation](#send-an-invitation) to the recipient.
4.  Before the recipient accepts the invitation, the recipient can set the [**LocalAddress**](im-imsgrsession-localaddress-property.md) property.

After the [**LocalAddress**](im-imsgrsession-localaddress-property.md) property of the [**MsgrSession**](im-msgrsession-object.md) object has been set, if the inviter or recipient retrieves the [**RemoteAddress**](im-imsgrsession-remoteaddress-property.md) property, the **LocalAddress** set by either person will be retrieved.

> [!Note]  
> It is not necessary for either the inviter or recipient to set the [**LocalAddress**](im-imsgrsession-localaddress-property.md) property of their respective [**MsgrSession**](im-msgrsession-object.md) objects. By default, the **LocalAddress** property is assigned the local IP of each user's computer.

 

## Related topics

<dl> <dt>

[Windows Messenger](im-messenger-entry.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 




