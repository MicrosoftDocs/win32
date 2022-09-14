---
title: Setting Permissions on Virtual Directories
description: For security reasons, Background Intelligent Transfer Service (BITS) does not upload files to a virtual directory that has scripting and execute permissions enabled.
ms.assetid: cf5c8b50-066f-431e-8bdf-ed0692219b20
ms.topic: article
ms.date: 05/31/2018
---

# Setting Permissions on Virtual Directories

For security reasons, Background Intelligent Transfer Service (BITS) does not upload files to a virtual directory that has scripting and execute permissions enabled. If you upload a file to a virtual directory that has these permissions enabled, the job fails with an error code of BG\_E\_SERVER\_EXECUTE\_ENABLED.

BITS does not require the virtual directory to be write enabled, so it is recommended that you turn off write access to the virtual directory.

The authenticated user (or IIS's Anonymous user for anonymous authentication) must have Change permissions on the physical directory to which the virtual directory is mapped; granting Write permissions does not suffice.

## Specifying Permissions for Notifications

The authentication scheme you specify for the virtual directory and notification URL (see the [BITSServerNotificationURL](bits-iis-extension-properties.md) property) must be compatible. BITS uses the authentication scheme specified for the virtual directory to access the notification URL. The upload job fails if BITS is unable to access the notification URL due to authentication failure.

If the notification type (see the [BITSServerNotificationType](bits-iis-extension-properties.md) property) is [by reference](using-bits-notification-request-response-headers.md), the application must ensure the user has access to the referenced file (see the [BITS-Request-DataFile-Name](notification-protocol-for-server-applications.md) header). BITS sets the ACLs on the referenced file to those of the physical directory to which the virtual directory is mapped.

> [!Note]  
> The notified application must be able to map and access the remote file even if the notification URL is serviced by a web server that is on a different computer than the physical upload directory. The [BITS-Request-DataFile-Name](notification-protocol-for-server-applications.md) header always contains a path specification that is relative to the computer hosting the BITS Extensions component. An application running on another computer might need to convert the path to an UNC path before accessing it.

 

BITS supports many combinations of authentication schemes. However, you should use the following authentication scheme for the virtual directory and the matching notification URL.

-   To support by reference notifications, the virtual directory should be configured to use NTLM (negotiate) authentication if the physical upload directory (the directory to which the virtual directory points) uses an authentication scheme other than anonymous. If the physical upload directory allows anonymous requests (no authentication), the virtual directory should enable anonymous (no authentication).

    The ACLs on the physical upload directory must be set such that the authenticated user can read files on the directory to which the notification URL points. BITS uses the ACLs of the physical upload directory to set the ACLs of temporary upload file (the [BITS-Request-DataFile-Name](notification-protocol-for-server-applications.md) header contains the path to the temporary file).

-   Because [by value](using-bits-notification-request-response-headers.md) notifications do not require the notified application to access a temporary file that contains the upload contents, the authentication scheme can be either anonymous or negotiate (NTLM). The only requirement is that the authenticated user for the virtual directory must also be authorized to access the notification URL.

## Specifying Permissions for Remote Shares

A virtual directory can point to a mapped drive on a different machine or a network share. If it points to a mapped network drive, the credentials used to map the drive should have full control on the remote share.

If the virtual directory points to a network share, BITS uses the virtual directory's **Connect As** user credentials to access the remote share. To access a remote share, the **Connect As** account needs to have privileges as described in the documentation for the [**LogonUser**](/windows/desktop/api/winbase/nf-winbase-logonusera) function. BITS logs on using LOGON32\_LOGON\_BATCH or LOGON32\_LOGON\_INTERACTIVE logon types. The **Connect As** user account needs Full-Access permissions to the remote share; granting Write permissions does not suffice.

When the physical upload directory is mapped to a network share, the identity of the caller requesting the notification URL is either the **Connect As** user, or the authenticated user of the physical upload directory (only available in IIS 6.0 and later, when the check box **Always use the authenticated user's credentials when validating access to the network resource** is selected on the **Connect As** dialog box).

 

 