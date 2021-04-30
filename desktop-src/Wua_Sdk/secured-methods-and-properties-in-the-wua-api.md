---
description: When WUA detects that a caller does not have permission to access an interface, method, or property, the HRESULT E\_ACCESSDENIED is returned.
ms.assetid: 4535ce8d-c329-4335-8b0a-8f63c22f111d
title: Securing Interfaces, Methods, and Properties in the WUA API
ms.topic: article
ms.date: 05/31/2018
---

# Securing Interfaces, Methods, and Properties in the WUA API

Some interfaces, methods, and properties of Windows Update Agent (WUA) are accessible only to callers who belong to the following Windows security groups:

-   Administrator
-   User
-   Power User

When WUA detects that a caller does not have permission to access an interface, method, or property, the **HRESULT** E\_ACCESSDENIED is returned.

The following interfaces are available to the Administrator, User, and Power User security groups:

-   [**IAutomaticUpdates**](/windows/desktop/api/Wuapi/nn-wuapi-iautomaticupdates)
-   [**IAutomaticUpdatesSettings**](/windows/desktop/api/Wuapi/nn-wuapi-iautomaticupdatessettings)
-   [**IAutomaticUpdatesSettings2**](/windows/desktop/api/Wuapi/nn-wuapi-iautomaticupdatessettings2)
-   [**ISystemInformation**](/windows/desktop/api/Wuapi/nn-wuapi-isysteminformation)
-   [**IUpdateSearcher**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatesearcher)
-   [**IUpdateSession**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatesession) and [**IUpdateSession2**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatesession2)

> [!Note]  
> If the following conditions are true, a search fails:
>
> -   A user who is not an administrator sets the [**UserLocale property of the IUpdateSession2**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesession2-get_userlocale) interface to a locale that corresponds to a language that is not installed on the computer.
> -   The search uses an UpdateSearch object created from the UpdateSession object.

 

The following download interfaces and methods are available to the Administrator and Power User groups:

-   [**IUpdateDownloader**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatedownloader)
-   [**IUpdate::CopyFromCache**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-copyfromcache)
-   [**IAutomaticUpdatesSettings2::CheckPermission**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings2-checkpermission)
    > [!Note]  
    > Administrators, users, and power users can call [**IAutomaticUpdatesSettings2::CheckPermission**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings2-checkpermission).

     

The following installation interfaces, methods, and properties are available to the Administrator groups:

-   [**IAutomaticUpdates::Pause**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdates-pause)
-   [**IAutomaticUpdates::Resume**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdates-resume)
-   [**IAutomaticUpdates::EnableService**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdates-enableservice)
-   [**IUpdateInstaller**](/windows/desktop/api/Wuapi/nn-wuapi-iupdateinstaller)
-   [**IsHidden Property of IUpdate**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_ishidden)
    > [!Note]  
    > Administrators, users, and power users can retrieve the values of the [**IsHidden Property of IUpdate**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_ishidden). However, only administrators and power users can set the values.

     

-   [**IUpdate::AcceptEula**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-accepteula)
    > [!Note]  
    > Administrators and power users can call the [**AcceptEula method of IUpdate**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-accepteula).

     

-   [**IAutomaticUpdatesSettings::Save**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-save)
-   [**NotificationLevel Property of IAutomaticUpdatesSettings**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_notificationlevel)
    > [!Note]  
    > Administrators, users, and power users can retrieve the values of the [**NotificationLevel Property of IAutomaticUpdatesSettings**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_notificationlevel). However, only administrators can set the values.

     

-   [**ScheduledInstallationDay Property of IAutomaticUpdatesSettings**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_scheduledinstallationday)
    > [!Note]  
    > Administrators, users, and power users can retrieve the values of the [**ScheduledInstallationDay Property of IAutomaticUpdatesSettings**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_scheduledinstallationday). However, only administrators can set the values.

     

-   [**ScheduledInstallationTime Property of IAutomaticUpdatesSettings**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_scheduledinstallationtime)
    > [!Note]  
    > Administrators, users, and power users can retrieve the values of the [**ScheduledInstallationTime Property of IAutomaticUpdatesSettings**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_scheduledinstallationtime). However, only administrators can set the values.

     

-   [**IncludeRecommendedUpdates Property of IAutomaticUpdatesSettings2**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings2-get_includerecommendedupdates)
    > [!Note]  
    > Administrators, users, and power users can retrieve the values of the [**IncludeRecommendedUpdates Property of IAutomaticUpdatesSettings2**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings2-get_includerecommendedupdates). However, only administrators can set the values.

     

 

 



