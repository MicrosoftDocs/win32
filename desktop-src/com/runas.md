---
title: RunAs
description: Configures a class to run under a specific user account when activated by a remote client without being written as a service application.
ms.assetid: 2325a7da-8acd-41f4-a658-36a02532505a
keywords:
- RunAs registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# RunAs

Configures a class to run under a specific user account when activated by a remote client without being written as a service application.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      RunAs = value
```

## Remarks

The value specifies the user name and must be either of the form *UserName*, *Domain***\\***UserName* or of the string "Interactive User". You can also specify the strings "nt authority\\localservice" (for Local Service) and "nt authority\\networkservice" (for Network Service). You can also specify the string "nt authority\\system" when {*AppID\_GUID*} refers to a COM server that is already started or that has an entry in the class table. However, you cannot use "nt authority\\system" with a COM server that is not already started. The default password for "nt authority\\localservice", "nt authority\\networkservice", and "nt authority\\system" is "" (empty string).

> [!Note]  
> As of Windows Vista, an empty password is no longer required to configure the "nt authority\\localservice", "nt authority\\networkservice" and "nt authority\\system" **RunAs** settings.

 

Classes configured to run as a particular user may not be registered under any other identity, so calls to [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject) with this CLSID fail unless the process was launched by COM on behalf of an actual activation request.

The user-name is taken from the **RunAs** value under the class's **AppID** key. If the user name is "Interactive User", the server is run in the identity of the user currently logged on and is connected to the interactive desktop.

Otherwise, the password is retrieved from a portion of the registry that is available only to administrators of the computer and to the system. The user-name and password are then used to create a logon session in which the server is run. When launched in this way, the user runs with its own desktop and window station and does not share window-handles, the clipboard, or other UI elements with the interactive user or other user running in other user accounts.

To establish a password for a **RunAs** class, you must use the DCOMCNFG administrative tool installed in the system directory.

For **RunAs** identities used by DCOM servers, the user account specified in the value must have the rights to log on as a batch job. This right can be added using Local Security Policy administrative tool. Go to **Local Policies** and open **User Rights Assignment**. Select **Log on as a batch job**, and add the user account.

The **RunAs** value is not used for servers configured to be run as services. COM services that need to run under an identity other than LocalSystem should set the appropriate user name and password using the services control panel applet or the service controller functions. (For more information about these functions, see [Services](/windows/desktop/Services/services).)

> [!Note]  
> As of Microsoft Windows Server 2003, the class AppID is explicitly read from **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\AppID**, which, unlike most registry keys, is not interchangeable with **HKEY\_CLASSES\_ROOT\\AppID**.

 

## Related topics

<dl> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> </dl>

 

 