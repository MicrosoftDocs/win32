---
title: Setting Process-Wide Security Using DCOMCNFG
description: You might want to enable security for a particular application if an application has security needs that are different from those required by other applications on the computer.
ms.assetid: 04a7f688-78a3-490a-bcfa-862824a05422
ms.topic: article
ms.date: 05/31/2018
---

# Setting Process-Wide Security Using DCOMCNFG

You might want to enable security for a particular application if an application has security needs that are different from those required by other applications on the computer. For instance, you might decide to use system-wide settings for your applications that require a low level of security while setting a higher level of security for a particular application.

However, security settings in the registry that apply to a particular application are sometimes not used. For example, the process-wide settings that you set in the registry using Dcomcnfg.exe will be overridden if a client calls [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket) to set security for a particular interface proxy. Similarly, if a client or server (or both) call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) to set security for a process, the settings in the registry will be ignored and the parameters specified to **CoInitializeSecurity** will be used instead.

When enabling security for an application, several settings may need to be modified. These include authentication level, location, launch permissions, access permissions, and identity. For step-by-step procedures, see the following:

-   [Setting the Authentication Level for an Application](#setting-the-authentication-level-for-an-application)
-   [Setting the Location for an Application](#setting-the-location-for-an-application)
-   [Setting Launch Permissions for an Application](#setting-launch-permissions-for-an-application)
-   [Setting Access Permissions for an Application](#setting-access-permissions-for-an-application)
-   [Setting the Identity for an Application](#setting-the-identity-for-an-application)
-   [Browsing the User Database](#browsing-the-user-database)
-   [Dcomcnfg.exe and 64-bit Applications](#dcomcnfgexe-and-64-bit-applications)
-   [Related topics](#related-topics)

## Setting the Authentication Level for an Application

To enable security for an application, you must set an authentication level other than None. The authentication level tells COM how much authentication protection is required, and it can range from authenticating the client at the first method call to encrypting parameter states fully.

**To set an application's authentication level**

1.  On the **Applications** property page in Dcomcnfg.exe, select the application and click the **Properties** button (or double-click the selected application).

2.  On the **General** page, select an authentication level other than **(None)** from the **Authentication Level** list box.

3.  If you will be setting other properties for this application, choose the **Apply** button to apply the new authentication level. Click **OK** if you are finished setting properties for this application and you wish to apply the changes.

## Setting the Location for an Application

The location you set for your application determines the computer on which the application will run. You can choose to run your application on the computer where the data is located, on the computer you use to set the location, or on a specified computer.

**To set an application's location**

1.  With Dcomcnfg.exe running, select the application from the **Applications** page and choose the **Properties** button (or double-click the selected application).

2.  On the **Location** page, select one or more check boxes that correspond to locations where you want the application to run. If you select more than one check box, COM uses the first one that applies. If Dcomcnfg.exe is being run on the server computer, always select **Run Application On This Computer**.

3.  If you will be setting other properties for this application, choose the **Apply** button to apply the new location. Choose **OK** if you are finished setting properties for this application and you wish to apply the changes.

## Setting Launch Permissions for an Application

With Dcomcnfg.exe, you can set launch permissions to control the list of users who are granted or denied permission to launch a particular server. You can add users or groups to the list, specifying whether access permission is being granted or denied. You can also remove users from the list.

**To set launch permissions for an application**

1.  With Dcomcnfg.exe running, select the application from the **Applications** page and choose the **Properties** button (or double-click the selected application).

2.  On the **Security** property page, select the **Use custom launch permissions** option button and choose the **Edit** button in the same area.

3.  To remove users or groups, select the user or group you want to remove and choose the **Remove** button. The selected user or group will no longer appear in the list box. When you have finished removing user and groups, choose **OK**.

4.  If you want to add users or groups, choose the **Add** button.

5.  If you know the fully qualified user name you want to add, type it in the **Add Names** text box. If you do not know the user name, you can browse the user database to find it (see Browsing the User Database below). When you have located the user name, select the user or group from the **Names** list box and choose the **Add** button.

6.  From the **Type of Access** list box, select the access type (either **Allow Launch** or **Deny Launch**). To add other users that will have the selected type of access, repeat step 5. When you have finished adding users for the selected access type, choose the **OK** button.

7.  To add users that will have a different type of access, repeat steps 5 and 6. Otherwise, choose **OK** to apply the changes.

## Setting Access Permissions for an Application

With Dcomcnfg.exe, you can manage the list of users who are granted or denied access to the methods of a particular server by setting access permissions. You can add users or groups to the list, specifying whether access permission is being granted or denied. You can also remove users from the list.

When setting access permissions, you must ensure that SYSTEM is included in the list of users that are granted access. If you have granted access permissions to Everyone, SYSTEM is included implicitly.

The process of setting access permissions for an application is similar to setting launch permissions. The steps are as follows.

**To set access permissions for an application**

1.  With Dcomcnfg.exe running, select the application from the **Applications** page and choose the **Properties** button (or double-click the selected application).

2.  On the **Security** property page, select the **Use custom access permissions** option button and choose the **Edit** button in the same area.

3.  To remove users or groups, select the user or group you want to remove and choose the **Remove** button. The selected user or group will no longer appear in the list box. When you have finished removing user and groups, choose **OK**.

4.  If you want to add a user or a group, choose the **Add** button.

5.  If you know the fully qualified user name you want to add, type it in the **Add Names** text box. If you do not know the user name, you can browse the user database to find it. When you have located the user name, select the user or group from the **Names** list box and choose the **Add** button.

6.  From the **Type of Access** list box, select the access type (either **Allow Access** or **Deny Access**). To add other users that will have the selected type of access, repeat step 5. When you have finished adding users for the selected access type, choose the **OK** button.

7.  To add users that will have a different type of access, repeat steps 5 and 6. Otherwise, choose **OK** to apply the changes.

## Setting the Identity for an Application

An application's identity is the account that is used to run the application. The identity can be that of the user that is currently logged on (the interactive user), the user account of the client process that launched the server, a specified user, or a service. You can use Dcomcnfg.exe to choose one of these identities for the application. For help with deciding which identity to set for your application, see [Application Identity](application-identity.md).

**To set identity for an application**

1.  With Dcomcnfg.exe running, select the application from the **Applications** page and choose the **Properties** button (or double-click the selected application).

2.  On the **Identity** property page, select the option button for the identity you want. If you choose **This User**, you must type in the user name, the password, and the confirmed password.

3.  If you will be setting other properties for this application, choose the **Apply** button to apply the new identity. Choose **OK** if you are finished setting properties for this application and you wish to apply the changes.

## Browsing the User Database

You would browse the user database in Dcomcnfg.exe when you need to find the fully qualified user name for a particular user. For instance, you can browse the user database to locate a user that you want to add for access or launch permissions.

**To browse the user database**

1.  In the **List Names From** list box, select the domain containing the user or group you want to add.

2.  To see the users that belong to the selected domain, choose the **Show Users** button.

3.  To see the members of a particular group, select the group in the **Names** list box and choose the **Show Members** button.

4.  If you cannot locate the user or group you want to add, choose the **Search** button, which brings up the **Find Account** dialog box. Select the domain you want to search (or select **Search All**), type the user name you want to look for, and choose the **Search** button.

## Dcomcnfg.exe and 64-bit Applications

On x64 operating systems from Windows XP to Windows Server 2008, the 64-bit version of DCOMCNFG.EXE does not correctly configure 32-bit DCOM applications for remote activation. This behavior causes components that are meant to be activated remotely instead being activated locally. This behavior does not occur in Windows 7 and Windows Server 2008 R2 and higher versions.

The workaround is to use the 32-bit version of DCOMCNFG. Run the 32-bit version of mmc.exe and load the 32-bit version of the Component Services snap-in by using the following command line.

C:\\WINDOWS\\SysWOW64>**mmc comexp.msc /32**

The 32-bit version of Component Services correctly registers 32-bit DCOM applications for remote activation.

## Related topics

<dl> <dt>

[Setting Process-Wide Security](setting-processwide-security.md)
</dt> </dl>

 

 




