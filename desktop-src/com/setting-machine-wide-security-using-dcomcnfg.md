---
title: Setting System-Wide Security Using DCOMCNFG
description: When you want all of the applications on one computer that do not provide their own security to share the same default security settings, you would set security on a system-wide basis.
ms.assetid: 23d1e222-c00b-497c-adc8-4ae14c5bdd98
ms.topic: article
ms.date: 05/31/2018
---

# Setting System-Wide Security Using DCOMCNFG

Changing the system-wide security settings will affect all COM server applications that do not set their own process-wide security. This may prevent such applications from working properly. If you are changing the system-wide security settings to affect the security settings for a particular COM application, then you should instead change the process-wide security settings for that particular COM application. For more information about setting process-wide security, see [Setting Process-wide Security](setting-processwide-security.md).

When you want all of the applications on one computer that do not provide their own security to share the same default security settings, you would set security on a system-wide basis. Using Dcomcnfg.exe makes it easy to set default values in the registry that apply to all applications on a computer.

It is important to understand that if the client or server explicitly calls [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) to set process-wide security, the default settings in the registry will be ignored and the parameters to **CoInitializeSecurity** will be used instead for the security settings for the process. Also, if you use Dcomcnfg.exe to specify security settings for a particular process, the default computer settings are overridden by the settings for the process.

When enabling system-wide security, you must set the authentication level to a value other than None and you must set launch and access permissions. You have the option of setting the default impersonation level, and you also can enable reference tracking. The following topics provide step-by-step procedures:

-   [Setting System-Wide Default Authentication Level](#setting-system-wide-default-authentication-level)
-   [Setting System-Wide Launch Permissions](#setting-system-wide-launch-permissions)
-   [Setting System-Wide Access Permissions](#setting-system-wide-access-permissions)
-   [Setting System-Wide Impersonation Level](#setting-system-wide-impersonation-level)
-   [Setting System-Wide Reference Tracking](#setting-system-wide-reference-tracking)
-   [Enabling and Disabling DCOM](#enabling-and-disabling-dcom)
-   [Related topics](#related-topics)

## Setting System-Wide Default Authentication Level

The authentication level is used to tell COM at what level you want the client to be authenticated. These levels offer various levels of protection, from no protection to full encryption. To enable security for a computer, you need to choose an authentication level other than None. You can choose such a setting, using Dcomcnfg.exe, by completing the following steps.

**To set the authentication level on a system-wide basis**

1.  Run Dcomcnfg.exe.

2.  Choose the **Default Properties** tab.

3.  From the **DefaultÂ AuthenticationÂ Level** list box, choose a value other than **(None)**.

4.  If you will be setting more properties for the computer, click the **Apply** button to apply the new authentication level. Otherwise, click **OK** to apply the changes and exit Dcomcnfg.exe.

## Setting System-Wide Launch Permissions

The launch permissions you set with Dcomcnfg.exe determine a list of users, each of which is explicitly granted or denied permission to launch any server that does not provide its own launch-permission settings. When setting launch permissions, you can add or remove one or more users or groups from this list. For each user that you add, you must specify whether the user is being granted or denied launch permission.

**To set launch permissions for a computer**

1.  On the **Default Security** property page in Dcomcnfg.exe, choose the **Edit Default** button in the **Default Launch Permissions** area.

2.  To remove users or groups, select the user or group you want to remove and choose the **Remove** button. The selected user or group will no longer appear in the list box. When you have finished removing users and groups, choose **OK**.

3.  If you want to add a user or group, choose the **Add** button.

4.  If you know the fully qualified user name you want to add, type it in the **Add Names** text box. If you do not know the user name, see **Setting Processwide Security Using DCOMCNFG** to find it. When you have located the user name, select the user or group from the **Names** list box and choose the **Add** button.

5.  From the **Type of Access** list box, select the access type (either **Allow Launch** or **Deny Launch**). To add other users that will also have the selected type of access, repeat step 4. When you have finished adding users for the selected access type, choose the **OK** button.

6.  To add users that will have a different type of access, repeat steps 4 and 5. Otherwise, choose **OK** to apply the changes.

## Setting System-Wide Access Permissions

Dcomcnfg.exe allows you to set access permissions to control the list of users who are granted or denied access to the methods of those servers that do not provide their own access permissions. You can add users or groups to the list, specifying whether access permission is being granted or denied. You can also remove users from the list.

When setting access permissions, you must ensure that SYSTEM is included in the list of users that are granted access. If you have granted access permissions to Everyone, SYSTEM is included implicitly.

The process of setting access permissions for a computer is similar to setting launch permissions. The following steps should be taken.

**To set access permissions for a computer**

1.  On the **Default Security** property page in Dcomcnfg.exe, choose the **Edit Default** button in the **Default Access Permissions** area.

2.  To remove users or groups, select the user or group you want to remove and choose the **Remove** button. The selected user or group will no longer appear in the list box. When you have finished removing user and groups, choose **OK**.

3.  If you want to add a user or a group, choose the **Add** button.

4.  If you know the fully qualified user name you want to add, type it in the **Add Names** text box. If you do not know the user name, see [Setting Process-wide Security Using DCOMCNFG](setting-processwide-security-using-dcomcnfg.md) to find it. When you have located the user name, select the user or group from the **Names** list box and choose the **Add** button.

5.  From the **Type of Access** list box, select the access type (either **Allow Access** or **Deny Access**). To add other users that will have the selected type of access, repeat step 4. When you have finished adding users for the selected access type, choose the **OK** button.

6.  To add users that will have a different type of access, repeat steps 4 and 5. Otherwise, choose **OK** to apply the changes.

## Setting System-Wide Impersonation Level

The impersonation level, set by the client, determines the amount of authority given to the server to act on the client's behalf. For example, when the client has set its impersonation level to delegate, the server can access local and remote resources as the client, and the server can cloak over multiple computer boundaries if the cloaking capability is set. To help determine which impersonation level you should choose, see [Impersonation Levels](impersonation-levels.md) and [Cloaking](cloaking.md).

Setting the default impersonation level for the whole computer tells COM what impersonation level to use when a particular client on the computer does not specify an impersonation level programmatically by using [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) or [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket).

**To set the impersonation level for a computer**

1.  With Dcomcnfg.exe running, choose the **Default Properties** tab.

2.  From the **Default Impersonation Level** list box, choose the impersonation level you want.

3.  If you will be setting more properties for the computer, choose the **Apply** button to apply the new impersonation level. Otherwise, choose **OK** to apply the changes and exit Dcomcnfg.exe.

## Setting System-Wide Reference Tracking

When you enable reference tracking, you are asking COM to do additional security checks and to keep track of information that will keep objects from being released too early. Keep in mind that these additional checks are expensive. For more information about reference tracking, see [Reference Tracking](reference-tracking.md). Use the following steps to enable or disable reference tracking.

**To set reference tracking for a computer**

1.  With Dcomcnfg.exe running, choose the **Default Properties** tab.

2.  To enable (or disable) reference tracking, select (or clear) the **Provide additional security for reference tracking** check box near the bottom of the page.

3.  If you will be setting more properties for the computer, choose the **Apply** button to apply the new setting. Otherwise, choose **OK** to apply the changes and exit Dcomcnfg.exe.

## Enabling and Disabling DCOM

When a computer is part of a network, the DCOM wire protocol enables COM objects on that computer to communicate with COM objects on other computers. You can disable DCOM for a particular computer, but doing so will disable all communication between objects on that computer and objects on other computers.

Disabling DCOM on a computer has no effect on local COM objects. COM still looks for launch permissions that you have specified. If no launch permissions have been specified, default launch permissions are used. Even if you disable DCOM, if a user has physical access to the computer, they could launch a server on the computer unless you set launch permissions not to allow it.

> [!Note]  
> If you disable DCOM on a remote computer, you will not be able to remotely access that computer afterward to re-enable DCOM. To re-enable DCOM, you will need physical access to that computer.

 

**To manually enable (or disable) DCOM for a computer**

1.  Run Dcomcnfg.exe.

2.  Choose the **DefaultÂ Properties** tab.

3.  Select (or clear) the **Enable Distributed COMÂ on this Computer** check box.

4.  If you will be setting more properties for the computer, click the **Apply** button to enable (or disable) DCOM. Otherwise, click **OK** to apply the changes and exit Dcomcnfg.exe.

## Related topics

<dl> <dt>

[Setting Process-wide Security](setting-processwide-security.md)
</dt> </dl>

 

 




