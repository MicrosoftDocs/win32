---
Description: This topic describes how to check the access rights of users.
ms.assetid: a3ae7da1-e61d-469f-9158-339e1c12d9d7
title: Checking the Access Rights of Users
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Checking the Access Rights of Users

The fax service is a secure service. The fax service administration application, a Microsoft Management Console (MMC) snap-in component, is available to query and modify the access rights users have for job, port, and global configuration data.

## In the Win32 Environment

Users must have certain access rights to successfully call certain fax service functions. Call the [**FaxAccessCheck**](/windows/previous-versions/Winfax/nc-winfax-pfaxaccesscheck?branch=master) function to query a user's fax access rights.

For more information, see [Fax Client User Access Rights](-mfax-fax-client-user-access-rights.md) and [Fax Port Access Levels](-mfax-fax-port-access-levels.md).

## In the COM Implementation Environment

If you are writing a C/C++ application, you can ensure that the client has access to modify a specified fax port. You can do this by calling the [**IFaxPort::get\_CanModify**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxport-get_canmodify?branch=master) method before calling any method that begins with **IFaxPort::put\_**. For more information, see [**IFaxPort**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxport?branch=master).

If you are writing a Microsoft Visual Basic application, retrieve the [**CanModify**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxport-get_canmodify?branch=master) property of the [FaxPort](-mfax-faxport.md) object to determine if the user has access to modify configuration information for the fax port.

 

 



