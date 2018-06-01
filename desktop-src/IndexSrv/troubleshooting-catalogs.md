---
Description: Catalogs for removable media, including CD-ROMs, can be created by using the Microsoft Management Console (MMC) snap-in.
ms.assetid: 73c713f2-b8e7-45fc-888c-c9dceb82183e
title: Troubleshooting Catalogs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting Catalogs

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Catalogs for removable media, including CD-ROMs, can be created by using the Microsoft Management Console (MMC) snap-in. The catalogs can reside on the removable medium. When that medium is inserted into a computer running Indexing Service, the catalog is opened in read-only format for queries.

> [!Note]  
> Although Indexing Service is a legacy application, the content in this topic applies to Windows Server 2003 and later.

 

The symptoms are Indexing Service errors when removing a catalog, and the inability to delete the catalog completely. Due to a failure during the catalog removal, the catalog is only partially deleted, and then becomes frozen.

**To fix the problem of a frozen catalog:**

1.  Stop Indexing Service (cisvc).
2.  Manually remove the directory that contains the catalog that is causing errors.
3.  In the Windows Registry, delete the key that matches the name of the catalog that is causing errors. In the following registry example, we call that key Catalog Name.

    ```
    HKEY_LOCAL_MACHINE
       SYSTEM
          Control
             ContentIndex
                Catalogs
                   Catalog Name
    ```

4.  Alternatively, from the command line enter the following command, where Catalog Name is the name of the catalog causing errors.

    `REG DELETE \\HKLM\SYSTEM\CurrentControlSet\Control\ContentIndex\Catalogs /v <Catalog Name>`

    > [!Note]  
    > In Windows Vista and later, and Windows Server 2008 and later, you must have administrator privileges to modify the registry.

     

5.  Start Indexing Service (cisvc).

 

 



