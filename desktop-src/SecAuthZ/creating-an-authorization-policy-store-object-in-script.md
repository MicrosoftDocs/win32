---
description: An authorization policy store contains information about the security policy of an application or group of applications.
ms.assetid: bce85da8-11de-4bc1-b097-d8efdbd28abf
title: Creating an Authorization Policy Store Object in Script
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating an Authorization Policy Store Object in Script

An authorization policy store contains information about the security policy of an application or group of applications. The information includes the applications, operations, tasks, users, and groups of users associated with the store. When an application that uses Authorization Manager initializes, it loads this information from the store. The authorization policy store must be located on a trusted system because administrators on that system have a high degree of access to the store.

Authorization Manager supports storing authorization policy either in the Active Directory directory service or in an XML file as shown in the following examples. In the Authorization Manager API, an authorization policy store is represented by an [**AzAuthorizationStore**](/windows/desktop/api/Azroles/nn-azroles-iazauthorizationstore) object. The examples show how to create an **AzAuthorizationStore** object for an Active Directory store and an XML store.

-   [Creating an Active Directory Store](#creating-an-active-directory-store)
-   [Creating a SQL Server Store](#creating-a-sql-server-store)
-   [Creating an XML Store](#creating-an-xml-store)

## Creating an Active Directory Store

To use Active Directory to store the authorization policy, the domain must be in the **Windows Server 2003** domain functional level. The authorization policy store cannot be located in a **Non-Domain Naming Context** (also called an application partition). It is recommended that the store be located in the **Program Data** container under a new organizational unit created specifically for the authorization policy store. It is also recommended that the store be located within the same local area network as application servers that run applications that use the store.

The following example shows how to create an [**AzAuthorizationStore**](/windows/desktop/api/Azroles/nn-azroles-iazauthorizationstore) object that represents an authorization policy store in Active Directory. The example assumes that there is an existing Active Directory organizational unit named Program Data in a domain named authmanager.com.


```VB
'  Create the store object.
Dim authStore
Set authStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the store object.
authStore.Initialize 1, _
    "msldap://CN=MyStore, CN=Program Data,DC=authmanager,DC=com"

'  Save the information to the store.
authStore.Submit
```



## Creating a SQL Server Store

Authorization Manager supports creating a Microsoft SQL Server–based authorization policy store. To create a SQL Server–based authorization store, use a URL that begins with the prefix **MSSQL://**. The URL must contain a valid SQL connection string, a database name, and the name of the authorization policy store: **MSSQL://***ConnectionString***/***DatabaseName***/***PolicyStoreName*.

If the instance of SQL Server does not contain the specified Authorization Manager database, Authorization Manager creates a new database with that name.

> [!Note]  
> Connections to a SQL Server store are not encrypted unless you explicitly set up SQL encryption for the connection or set up encryption of the network traffic that uses Internet Protocol Security (IPsec).

 

The following example shows how to create an [**AzAuthorizationStore**](/windows/desktop/api/Azroles/nn-azroles-iazauthorizationstore) object that represents an authorization policy store in a SQL Server database.


```VB
'  Create the store object.
Dim authStore
Set authStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the store object.
authStore.Initialize 1, _ 
  "MSSQL://Driver={SQL Server};Server={AzServer};/AzDB/MyStore"

'  Save information to the store.
authStore.Submit
```



## Creating an XML Store

Authorization Manager supports creating an authorization policy store in XML format. The XML store can be located on the same computer where the application runs, or it can be stored remotely. Editing the XML file directly is not supported. Use the Authorization Manager MMC snap-in or the Authorization Manager API to edit the policy store.

Authorization Manager does not support delegating administration of an XML policy store. For information about delegation, see [Delegating the Defining of Permissions in Script](delegating-the-defining-of-permissions-in-script.md).

The following example shows how to create an [**AzAuthorizationStore**](/windows/desktop/api/Azroles/nn-azroles-iazauthorizationstore) object that represents an authorization policy store in an XML file.


```VB
'  Create the store object.
Dim authStore
Set authStore = CreateObject("AzRoles.AzAuthorizationStore")

'  Initialize the store object.
authStore.Initialize 1, "msxml://C:\MyStore.xml"

'  Save information to the store.
authStore.Submit
```



 

 



