---
title: Running DSML Services for Windows on the Internet
description: In an Internet scenario, clients will usually connect to DSML Services for Windows from a web application across the Internet.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'b8ccd6ab-6eca-4ee8-80bb-1772213aa9b9'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Running DSML Services for Windows on the Internet DSML"]
---

# Running DSML Services for Windows on the Internet

In an Internet scenario, clients will usually connect to DSML Services for Windows from a web application across the Internet. It is recommended that communication between the client and DSML Services for Windows be made across a secure, encrypted channel to prevent sensitive data from being exposed.

![dsml services for windows virtual directory set to basic authentication](images/production-computers-1.png)

In an Internet scenario, the IIS server that hosts DSML Services for Windows will usually have the security settings for the DSML virtual directory set to basic authentication. The IIS server has a valid SSL certificate installed, and the clients pass a user name and password through the SSL connection.

## Accessing DSML Services for Windows

The following Visual Basic code examples show how clients access DSML Services for Windows across the Internet.


```VB
set xmlhttp = CreateObject("Msxml2.XMLHTTP")
xmlhttp.open "POST", "https://fabrikam.com/dsml/adssoap.dsmlx", false, userName, password
```



The following C# code examples show how clients access DSML Services for Windows across the Internet.


```CSharp
Uri site = new Uri("https://fabrikam.com/dsml/adssoap.dsmlx"); 
WebRequest wReq = WebRequest.Create(site);

// Set "Basic" authorization and create user name and password.
NetworkCredential myCred = new NetworkCredential(userName,password);
CredentialCache myCache = new CredentialCache();
myCache.Add(site, "Basic", myCred);

wReq.Credentials = myCache;
```



This scenario assumes that both IIS and Active Directory are running a data center. The communication between IIS, DSML Services for Windows, and Active Directory can be encrypted using SSL. To set a secure connection, install an appropriate certificate in Active Directory and set DSML Services for Windows to communicate at port 636 in the dsmlv2.config configuration file.

The following is a sample configuration file:


```XML
<extensionConfiguration>
   <virtualDirectory url="/dsml/adssoap.dsmlx`">
        <server>fabrikam.com</server>
        <port>636</port>
        <connectTimeout>30</connectTimeout>
        <operationTimeout>30</operationTimeout>
        <maxConnections>10</maxConnections>
   </virtualDirectory>
</extensionConfiguration>
```



> [!Note]  
> In this configuration, DSML Services for Windows and the Active Directory domain controller can be installed on separate computers.

 

## Users running as anonymous

In some Internet scenarios, the data received by a client computer is public and no data is required to be encrypted. The services are free to users, but users cannot modify the data. A white-page/yellow-page lookup is an example of this type of scenario.

![dsml services for windows white-page/yellow-page lookup scenario](images/production-computers-2.png)

**To configure DSML Services for Windows in this scenario**

1.  Create a new user in Active Directory.
2.  Give this user read-only permissions for Active Directory objects. For sensitive data, you might also want to remove the Read permissions at the object and/or attribute levels.
3.  Set the IIS security settings to anonymous access. Set the new user as the **Account used for anonymous Access**.
4.  Optionally, set the **readOnly** setting to **TRUE** for the virtual directory in the dsmlv2.config file. This will cause DSML Services for Windows to accept only **searchRequest** and **compareRequest** operations on that virtual directory.

Clients are not required to specify a user name or password to access this service.

 

 




