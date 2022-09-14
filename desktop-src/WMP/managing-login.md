---
title: Managing Login
description: Managing Login
ms.assetid: 5cafcd3a-e819-4524-b7a9-580ff36fc4f8
keywords:
- Windows Media Player online stores,managing logins
- online stores,managing logins
- type 1 online stores,managing logins
- Windows Media Player online stores,logins
- online stores,logins
- type 1 online stores,logins
- Windows Media Player online stores,standard log-in process
- online stores,standard log-in process
- type 1 online stores,standard log-in process
- Windows Media Player online stores,log-out process
- online stores,log-out process
- type 1 online stores,log-out process
- standard log-in process
- log-out process
- logins
ms.topic: article
ms.date: 05/31/2018
---

# Managing Login

Windows Media Player supports a variety of methods for the user to log in to a type 1 online store. The Player provides a standard log-in dialog box, but the online store can provide a webpage that serves as an alternative to the standard dialog box.

The user can initiate a log-in attempt by interacting with the Windows Media Player user interface or by interacting with a discovery page provided by the online store. If the user initiates a log-in attempt by interacting with a discovery page, script on the discovery page calls the [External.attemptLogin](external-attemptlogin.md) method.

The user's log-in state is maintained by the online store. When the user's log-in state changes, or if a log-in attempt fails, the online store's plug-in notifies Windows Media Player by calling [IWMPContentPartnerCallback::Notify](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-notify), passing wmpcnLoginStateChange in the *type* parameter. The Player passes the notification along to the discovery page by raising the [External.OnLoginChange](external-onloginchange-event.md) event.

A call to **OnLoginChange** does not necessarily mean that the user's log-in state changed; it could mean that an attempt to log in failed. To determine the user's log-in state, the **OnLoginChange** event handler can inspect the [External.userLoggedIn](external-userloggedin.md) property.

The following sections describe the standard log-in process, the alternative log-in process, and the log-out process.

## Standard Log-in

The standard log-in process involves the following steps:

1.  The user initiates a log-in attempt by interacting with the Windows Media Player user interface or by interacting with a discovery page.
2.  Windows Media Player displays a dialog box that prompts the user for a user-name and password.
3.  When the user clicks the **Sign In** button in the dialog box, Windows Media Player calls [IWMPContentPartner::Login](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-login), which is implemented by the online store's plug-in.
4.  The plug-in communicates with the online store and either succeeds or fails to log in the user.
5.  If the log-in attempt succeeds, the plug-in notifies Windows Media Player by calling **IWMPContentPartnerCallback::Notify**, passing VARIANT\_TRUE in the **boolVal** member of the *pContext* parameter. If the log-in attempt fails, the plug-in notifies Windows Media Player by calling **IWMPContentPartnerCallback::Notify**, passing a 32-bit value in the **ulVal** member of the *pContext* parameter. The Player then passes that 32-bit value to [IWMPContentPartner::GetItemInfo](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getiteminfo) to get the URL of a webpage that can handle the failure.

## Alternative Login

If the SUBSCRIPTION\_CAP\_ALTLOGIN flag is set in the **Capabilities** registry entry for the online store's plug-in, Windows Media Player does not use the standard log-in dialog box. Instead, Windows Media Player calls **IWMPContentPartner::GetItemInfo** to retrieve the URL of a webpage that performs the log-in process. For more information about the **Capabilities** registry entry, see [Registry Keys and Entries for a Type 1 Online Store](registry-keys-and-entries-for-a-type-1-online-store.md).

The Player calls **GetItemInfo** twice: once passing g\_szItemInfo\_ALTLoginURL to retrieve the URL of the log-in webpage and once passing g\_szItemInfo\_ALTLoginCaption to retrieve the caption for the window that hosts the webpage. When **GetItemInfo** returns the URL of the log-in webpage, it can specify the size of the log-in window by appending the following parameter string to the URL:

?DlgX=*width*&DlgY=*height*

In the parameter string, *width* and *height* are the width and height of the window in pixels. For example **GetItemInfo** could return the following string to specify that AltLogin.htm should be displayed in a window that has a width of 800 pixels and a height of 400 pixels


```C++
https://proseware.com/AltLogin.htm?DlgX=800&DlgY=400
```



The alternative log-in process involves the following steps:

1.  The user initiates a log-in attempt by interacting with the Windows Media Player user interface or by interacting with a discovery page.
2.  Windows Media Player opens a modal window that displays the log-in webpage provided by the online store.
3.  The webpage communicates with the online store and either succeeds or fails to log in the user.
4.  If the log-in attempt succeeds, the webpage notifies the online store's plug-in by calling [External.sendMessage](external-sendmessage.md), which results in a call to [IWMPContentPartner::SendMessage](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-sendmessage). The online store's plug-in determines that the log-in attempt succeeded by inspecting the parameters passed to **IWMPContentPartner::SendMessage**. Those parameters are not interpreted by Windows Media Player; they have meaning only to the online store. The plug-in calls **IWMPContentPartnerCallback::Notify**, passing VARIANT\_TRUE in the **boolVal** member of the *pContext* parameter. If the log-in fails, the online store must determine how to assist the user. One possibility is to display a new webpage in the modal window that hosts the alternative log-in webpage.

## Log-out

The log-out process involves the following steps.

1.  The user initiates a log-out attempt by interacting with the Windows Media Player user interface or by interacting with a discovery page.
2.  Windows Media Player calls [IWMPContentPartner::Logout](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-logout), which is implemented by the online store's plug-in.
3.  The plug-in communicates with the online store and either succeeds or fails to log out the user.
4.  If the log-out attempt succeeds, the plug-in notifies Windows Media Player by calling **IWMPContentPartnerCallback::Notify**, passing VARIANT\_FALSE in the **boolVal** member of the *pContext* parameter.

When an attempt to log in or out is successful, the online store's plug-in calls **IWMPContentPartnerCallback::Notify**, passing wmpcnLoginStateChange in the *type* parameter. The plug-in uses the *pContext* parameter to specify the user's current log-in state. If the plug-in sets *pContext*->**boolVal** to VARIANT\_TRUE, the user is logged in. If the plug-in sets *pContext*->**boolVal** to VARIANT\_FALSE, the user is logged out. Note that *pContext* does not indicate the success or failure of the attempt; rather, it indicates user's current log-in state.

## Related topics

<dl> <dt>

[**External.attemptLogin**](external-attemptlogin.md)
</dt> <dt>

[**External.OnLoginChange Event**](external-onloginchange-event.md)
</dt> <dt>

[**External.userLoggedIn**](external-userloggedin.md)
</dt> <dt>

[**IWMPContentPartner::Login**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-login)
</dt> <dt>

[**IWMPContentPartner::Logout**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-logout)
</dt> <dt>

[**Programming Guide for Type 1 Online Stores**](programming-guide-for-type-1-online-stores.md)
</dt> </dl>

 

 




