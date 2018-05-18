---
title: Configure Azure RMS for ADAL authentication
description: This topic describes the steps for configuring Azure ADAL based authentication.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '37B20BB0-35C9-4F05-82E7-63F59C5FB3E9'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# Configure Azure RMS for ADAL authentication

This topic describes the steps for configuring Azure ADAL based authentication.

## Internal authentication: setup via Azure Portal

You will need the following:

-   A [subscription for Microsoft Azure](https://azure.microsoft.com/) (a free trial is sufficient):
-   A subscription for Microsoft Azure Rights Management (a free [RMS for Individuals](https://technet.microsoft.com/library/dn592127.aspx) account is sufficient).

    > [!Note]  
    > Ask your IT Admin whether or not you have a subscription for Microsoft Azure Rights Management and, have your IT Admin perform the steps below. If your organization does not have a subscription, you should have your IT admin create one. Also, your IT Admin should subscribe with a *Work or school account*, rather than a *Microsoft account* (i.e. Hotmail).

     

After signing up for Microsoft Azure:

-   Login to the [Azure Management Portal](https://manage.windowsazure.com) for your organization using an account with administrative privileges.

    ![azure login](../images/azureportallogin.png)

-   Browse down to the **Active Directory** application on the left side of the portal.

    ![select active directory](../images/azureadpick.png)

-   If you haven’t created a directory already, choose the **New** button located in the bottom left corner of the portal.

    ![select new](../images/azurenewbtn.png)

-   Select the **Rights Management** tab and ensure that the **Rights Management Status** is either **Active**, **Unknown** or **Unauthorized**.

    If the status is **Inactive**, choose the **Activate** button at the bottom, center portion of the portal and confirm your selection.

    ![choose activate](../images/rmtab.png)

-   Now, create a new Native Application in your directory by selecting your directory, choosing Applications.

    ![select applications](../images/createnativeapp.png)

-   Then choose the **Add** button located in the bottom, center portion of the portal.

    ![select add](../images/addappbtn.png)

-   At the prompt choose **Add an application my organization is developing**

    ![select add an application ...](../images/addanapppick.png)

-   Name your application by selecting **NATIVE CLIENT APPLICATION** and choosing the **Next** button.

    ![name your app](../images/tellusinput.png)

-   Add a redirection URI and choose next.

    The redirection URI needs to be a valid URI and unique to your directory. For example, you could use something like `com.mycompany.myapplication://authorize`

    ![add redirect uri](../images/redirecturi.png)

-   Select your application in the directory and choose **CONFIGURE**

    ![choose configure](../images/configyourapp.png)

    > [!Note]  
    > Copy the CLIENT ID and REDIRECT URI and store them for future use when configuring the RMS client.

     

-   Browse to the bottom of your application settings and choose the **Add application** button under **permissions to other applications**.

    > [!Note]  
    > The **Delegated Permissions** that are shown for Windows Azure Active Directory are correct by default – only one option should be selected and that option is **Sign in and read user profile**.

     

    ![select add application](../images/permissionstootherbtn.png)

-   Now, add this GUID (00000012-0000-0000-c000-000000000000) to the **STARTING WITH** edit box and choose the check button:

    ![add guid](../images/addguid.png)

-   Choose the plus button next to Microsoft Rights Management:

    ![select (+) button](../images/chooseplusbtn.png)

-   Now, choose the check located on the bottom left corner of the dialog:

    ![choose check mark](../images/choosecheck.png)

-   You’re now ready to add a dependency to your application for Azure RMS. To add the dependency, select the new **Microsoft Rights Management Services** entry under **permissions to other applications** and choose the **Create and access protected content for users** checkbox under the **Delegated Permissions:** drop box:

    ![setup permissions](../images/adddependency.png)

-   Save your application to persist the changes by choosing the **Save** icon located on the bottom, center of the portal.

    ![select save](../images/saveapplication.png)

 

 




