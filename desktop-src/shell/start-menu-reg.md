---
description: The Start menu in Windows XP and Windows Vista contains reserved slots for the default Internet (browser) and E-mail (mail) clients, together commonly known as Start Menu Internet Applications.
ms.assetid: a3d7416f-0dbd-4af2-ab38-758f9cc8aec5
title: How to Register an Internet Browser or Email Client With the Windows Start Menu
ms.topic: article
ms.date: 05/31/2018
---

# How to Register an Internet Browser or Email Client With the Windows Start Menu

> [!Note]  
> This topic applies to Windows XP, Windows Vista, and Windows 7.

 

The Start menu in Windows XP and Windows Vista contains reserved slots for the default **Internet** (browser) and **E-mail** (mail) clients, together commonly known as *Start Menu Internet Applications*. Applications which register as Start Menu Internet Applications do so across the entire system (per-machine). In Windows Vista, the user may use the **Default Programs** feature to set a per-user default.

When applications register as Start Menu Internet Applications, Windows XP and Windows Vista create **Internet** and **E-mail** icons on the Start menu. Clicking these icons causes the Start menu to check the per-user registry subtree (**HKEY\_CURRENT\_USER**). If no per-user default setting is found, the Start menu looks for the per-machine default subkey in the **HKEY\_LOCAL\_MACHINE** subtree.

> [!Note]  
> The default installation of Windows does not register a per-user default Internet or email program, only a system-wide default. This provides a smooth upgrade path from previous versions of the operating system, in which only the HKEY\_LOCAL\_MACHINE subtree is supported for client registrations.

 

This topic discusses the following items:

-   [Registering for the Start Menu Internet Link](#registering-for-the-start-menu-internet-link)
    -   [How to Register as the Default Internet Client](#how-to-register-as-the-default-internet-client)
-   [Registering for the Start Menu Email Link](#registering-for-the-start-menu-email-link)
    -   [How the Start Menu Displays the Default Email Client](#how-the-start-menu-displays-the-default-email-client)
    -   [How to Register as the Default EMail Client](#how-to-register-as-the-default-email-client)
-   [Customizing the Context Menu](#customizing-the-context-menu)

## Registering for the Start Menu Internet Link

> [!Note]  
> This registration is deprecated as of Windows 7, which no longer provides a Start menu Internet link. Existing registrations are ignored in Windows 7 and later. Being registered as the default Start menu Internet application is not the same as being registered as the default web browser. The default web browser is used for launching arbitrary URLs from anywhere in the system. The Start menu Internet application merely controls the program that is started when the user clicks the Internet icon on the Start menu.

 

Any web browser application can register to appear as an Internet client on the Start menu. This visibility, coupled with proper registration for an application's [file](fa-intro.md) and [protocol](/previous-versions//aa767743(v=vs.85)) types, gives an application default browser status.

Registrations made in the **HKEY\_CURRENT\_USER** subtree have higher precedence for the console user than corresponding registrations made in the **HKEY\_LOCAL\_MACHINE**. For new users on the system, the settings stored in **HKEY\_LOCAL\_MACHINE** are used. As of Windows XP, Start menu Internet settings are kept in the default entries of two registry locations:

-   **HKEY\_CURRENT\_USER**\\**SOFTWARE**\\**Clients**\\**StartMenuInternet**
-   **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Clients**\\**StartMenuInternet**

The subkey **HKEY\_CURRENT\_USER**\\**SOFTWARE**\\**Clients**\\**StartMenuInternet** describes the Internet browser that is started when the user clicks the **Internet** icon on the Start menu. If that subkey is blank or missing, then the **Internet** icon on the Start menu is set to the system default stored in the second location at **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Clients**\\**StartMenuInternet** , which describes all Internet browser applications that are installed on the system.

When a new user logs onto the system, the Start menu uses the default value in the subkey at **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Clients**\\**StartMenuInternet** to display the default Internet client and starts the registered application when that icon is clicked.

### How to Register as the Default Internet Client

Below the subkey **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Clients**\\**StartMenuInternet** there can be zero or more subkeys, one for each registered Internet browser application. For example, a hypothetical system might have this arrangement:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         StartMenuInternet
            IEXPLORE.EXE
            BROWSER2.EXE
            BROWSER3.EXE
```

We will demonstrate registry entries with a hypothetical browser called "Lit View" from a fictional company called Litware Inc. Suppose that the executable name for Lit View is Litview.exe. The registration of Lit View occurs as shown here:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         StartMenuInternet
            LITVIEW.EXE
               LocalizedString = @C:\Program Files\LitwareInc\ResourceDLL.dll,-123
```

The LocalizedString data is of type REG\_SZ, or REG\_EXPAND\_SZ if path variables such as `%programfiles%` are used. LocalizedString provides the path to an executable (.exe) or library (.dll) file. Note that the path string begins with an "at" sign (@) and that no quotation marks are required around the path regardless of spaces within it. The decimal integer is the ID of a string resource, contained within the specified DLL, whose value is to be displayed to the user. This enables the same registration to be used for multiple languages. Each language provides a different ResourceDLL.dll. This enables the system to display the correct string based on the currently selected language.

The following REG\_SZ or REG\_EXPAND\_SZ value informs the Start menu of the default icon to display when the user selects Lit View as the Start menu Internet browser.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         StartMenuInternet
            LITVIEW.EXE
               DefaultIcon
                  (Default) = C:\Program Files\LitwareInc\LitView.exe,1
```

The following registry subkey specifies a command line to run when the user clicks the Internet menu command on the Start menu, assuming that Lit View is the selected Start menu Internet browser. For example, the command might open the browser with the user's home page or the command could launch an introductory user interface that the independent software vendor (ISV) feels is appropriate. The data is of type REG\_SZ or REG\_EXPAND\_SZ, but notice that because there is a space in the command-line path, the executable path is enclosed in quotation marks.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         StartMenuInternet
            LITVIEW.EXE
               shell
                  open
                     (Default) = "C:\Program Files\LitwareInc\LitView.exe" -welcome
```

When the user specifies through [Set Program Access and Computer Defaults (SPAD)](cpl-setprogramaccess.md) that Lit View should be used as the computer-level default web browser, the application should set the following REG\_SZ entry. Note that because SPAD runs with Administrator privileges, access to this subkey is allowed.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         StartMenuInternet
            (Default) = LITVIEW.EXE
```

> [!Note]
> In Windows Vista, the user-level default web browser should be set using the **Default Programs** tool, not [SPAD](cpl-setprogramaccess.md).
> 
> **The following information applies to Windows XP only.**
> 
> If the registration of the computer-level default web browser under HKEY\_LOCAL\_MACHINE as shown above is successful, the application should delete the Default entry under the following subkey:
> 
> ```
> HKEY_CURRENT_USER
>    SOFTWARE
>       Clients
>          StartMenuInternet
> ```
> 
> If the registration of the computer-level default web browser under HKEY\_LOCAL\_MACHINE fails, the application should set the REG\_SZ data as shown in this example for the Lit View application:
> 
> ```
> HKEY_CURRENT_USER
>    SOFTWARE
>       Clients
>          (Default) = LITVIEW.EXE
> ```

 

After updating the appropriate subkeys, the application broadcasts the [**WM\_SETTINGCHANGE**](../winmsg/wm-settingchange.md) message with its *wParam* parameter set to 0 and its *lParam* parameter pointing to the null-terminated string `"Software\Clients\StartMenuInternet"`. This notifies the operating system that the default client has changed.

Setting these subkeys for the default Start menu Internet browser is necessary to preserve backward compatibility with old web browsers that do not support per-user registrations.

## Registering for the Start Menu Email Link

> [!Note]  
> The Start menu Email link has been removed as of Windows 7. However, this registration discussed in this section should still be performed for its effect in assigning the default MAPI client.

 

### How the Start Menu Displays the Default Email Client

Any email application can register to appear as an email client on the Start menu. This visibility, coupled with proper registration for an application's [file](fa-intro.md) and [protocol](/previous-versions//aa767743(v=vs.85)) types, gives an application default mail status.

Registrations made in the **HKEY\_CURRENT\_USER** subtree have higher precedence for the console user than corresponding registrations made in the **HKEY\_LOCAL\_MACHINE**. For new users on the system, the settings stored in **HKEY\_LOCAL\_MACHINE** are used. As of Windows XP, Start menu Email settings are kept in the default entries of two registry locations:

-   **HKEY\_CURRENT\_USER**\\**SOFTWARE**\\**Clients**\\**Mail**
-   **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Clients**\\**Mail**

The subkey **HKEY\_CURRENT\_USER**\\**SOFTWARE**\\**Clients**\\**Mail** describes the email client that is started when the user clicks the **E-mail** icon on the Start menu.

The subkey **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Clients**\\**Mail** describes the email applications that are installed on the system, as well as the default email application.

If the **HKEY\_CURRENT\_USER**\\**SOFTWARE**\\**Clients**\\**Mail** is blank or missing, the default value defined in **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Clients**\\**Mail** is used to select the email application that appears on the Start menu.

When a new user logs onto the system, the Start menu uses the default value in the subkey at **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Clients**\\**Mail** to display the default email client and starts the registered application when that icon is clicked.

### How to Register as the Default EMail Client

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Clients**\\**Mail** can contain zero or more subkeys, one for each registered email application. For example, a hypothetical system might define the following subkeys:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         Mail
            Eudora
            Windows Mail
```

We will demonstrate registry entries with a hypothetical email client called "Lit Mail" from the fictional company called Litware Inc. Litware Inc. decides to register this email client under the internal name "LitMail". As with a browser, the internal name is a unique string used as the subkey name, but it is never shown to the user.

To install the Lit Mail email client as the default, they use the following subkey and its entries:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         Mail
            LitMail
               (Default) = Lit Mail
               LocalizedString = @C:\Program Files\LitwareInc\ResourceDLL.dll,-456
```

The LocalizedString data is of type REG\_SZ, or REG\_EXPAND\_SZ if path variables such as `%programfiles%` are used. LocalizedString provides the path to an executable (.exe) or library (.dll) file. Note that the path string begins with an "at" sign (@) and that no quotation marks are required around the path regardless of spaces within it. The decimal integer is the ID of a string resource, contained within the specified DLL, whose value is to be displayed to the user. This enables the same registration to be used for multiple languages. Each language provides a different ResourceDLL.dll. This enables the system to display the correct string based on the currently selected language.

After updating the appropriate subkeys, the application broadcasts the [**WM\_SETTINGCHANGE**](../winmsg/wm-settingchange.md) message with its *wParam* parameter set to 0 and its *lParam* parameter pointing to the null-terminated string `"Software\Clients\Mail"`. This notifies the operating system that the default client has changed.

For backward compatibility with applications that do not support localized strings, the name of the application in the installed language should also be set as the default value for the subkey.

The following **REG\_SZ** or **REG\_EXPAND\_SZ** value informs the Start menu of the default icon to display when the user selects Lit Mail as the Start menu mail program:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         Mail
            LitMail
               DefaultIcon
                  (Default) = C:\Program Files\LitwareInc\LitMail.exe,1
```

The following entry specifies a command line to run when the user clicks the **E-mail** menu item on the Start menu, assuming that Lit Mail is the selected Start menu email program. This command line is also run if the user selects **Read email** from the Windows Internet Explorer **Tools** menu. The data is of type **REG\_SZ** or **REG\_EXPAND\_SZ**, but notice that because there is a space in the command-line path, the executable path is enclosed in quotation marks.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         Mail
            shell
               open
                  command
                     (Default) = "C:\Program Files\LitwareInc\LitMail.exe" -inbox
```

If (and only if) *the user* specifies Lit Mail to be the default Start menu email application, the Lit Mail application may write its internal name to the following **REG\_SZ** value:

```
HKEY_CURRENT_USER
   SOFTWARE
      Clients
         Mail
            (Default) = LitMail
```

If (and only if) *the user* specifies Lit Mail to be the system-wide default email application, the Lit Mail application may write its internal name to the **REG\_SZ** value specified below. Note that access to this subkey might be restricted. Applications should not assume that all users have permission to change the system-wide default email application.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         Mail
            (Default) = LitMail
```

Registration as the default Start menu email application is not equivalent to registration as the system default email client or the registered *mailto* handler.

-   The system default email client is started when the user clicks **Read email** from the Internet Explorer **Tools** menu.
-   The registered *mailto* handler is started when the user clicks a URL of the form `mailto:someone@example.com`.
-   The Start menu email application is started when the user clicks the **E-mail** icon on the Start menu.

If no default Start menu email application is specified, the Email icon on the Start menu launches the system default email client.

This topic does not cover registration of the application as the default *mailto* protocol handler. Applications that want to register in such a manner should continue to follow existing specifications on this subject.

## Customizing the Context Menu

An application can customize the property pages that are displayed when the user selects **Properties** from the **E-mail** (or **Internet**) icon's shortcut menu. For example, the Litware email application adds the following **REG\_SZ** or **REG\_EXPAND\_SZ** data to display a custom property sheet for the **E-mail** icon rather than its default property sheet.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         Mail
            LitMail
               shell
                  properties
                     MUIVerb = @C:\Program Files\LitwareInc\ResourceDLL.dll,-789
                     command
                        (Default) = "C:\Program Files\LitwareInc\LitMail.exe" -properties
```

The MUIVerb data item is constructed beginning with an "at" sign (@), followed by the full path to the resource DLL, a comma, a minus sign (-), and then the decimal string resource identifier to display. Note that the path to the LitMail.exe program contains spaces, so the path string is placed inside quotation marks.

An application can also add additional commands to the context menu. For example, the Litware email application adds a **find** command with the following **REG\_SZ** data:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Clients
         Mail
            LitMail
               shell
                  find
                     MUIVerb = @C:\Program File\LitwareInc\ResourceDLL.dll,-790
                     command
                        (Default) = "C:\Program Files\LitwareInc\LitMail.exe" -contacts
```

The subkey name below **shell** (in this case, "find") is an arbitrary, nonlocalized name. Once again the MUIVerb data contains an "at" sign (@) as the first element, followed by the path to a resource DLL, a comma separator, and then a minus sign preceding the decimal string resource identifier. For example, that string resource might be "Open Address Book". Finally, note that the command-line string contains spaces, so it is enclosed in quotation marks.

 

 
