---
title: Scopes
description: Scopes
ms.assetid: bc46e9d0-f784-49e1-b176-ec21f845c930
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Scopes

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **Scopes** entry is a subkey that contains a list of strings, each containing one scope definition (directory paths to index or to ignore) for the catalog.

### Summary



|       |             |
|-------|-------------|
| Type: | **REG\_SZ** |



 

### Remarks

If IIS is running, the **Scopes** entry does not list directories picked up from IIS when the [**IsIndexingW3SVC**](isindexingw3svc.md) key is set to zero.

For example, the list can be:

``` syntax
c:\MyDocuments
c:\CompanyDocuments\MyDepartment
d:\Favorites
 
```

Each entry under the **Scopes** subkey names the scope to be indexed and specifies a value of *fixup,domain\\user,bitmask*. The *fixup* parameter is a prefix for a path that will be substituted for the scope when a remote client sends a query. The *domain\\user* parameter identifies the remote client when Indexing Service indexes the files in the scope. The *bitmask* parameter specifies characteristics about the scope and can be a logical **OR** operation of the possible values. The following table gives the possible *bitmask* parameter values and their effects.



| Bitmask Value | Scope Characteristic                       |
|---------------|--------------------------------------------|
| 0x0           | Not indexed, not virtual, and not physical |
| 0x1           | Indexed                                    |
| 0x2           | Virtual                                    |
| 0x4           | Physical                                   |



 

### Example

The following example shows a sample registry setting when Indexing Service is running with IIS.

``` syntax
ContentIndex
    GenerateCharacterization   1
    IsIndexingW3Svc   1
    Catalogs
        web
             Location "C:\InetPub"
        correspondence
             GenerateCharacterization  0
             IsIndexingW3Svc   0
             Location "C:\"
             Scopes
                   D:\Memos  "\\Dept05\Memos"
                   \\Corp1\Reports  ",Corp\IISManager"
                   D:\Memos\Confidential  ",,0"
 
```

A remote user queries a website on the computer named Dept05, and the file REPORT1.TXT is returned on the results page. This file is on drive D: of server Dept05, in the Memos directory. The file name and the Uniform Naming Convention (UNC) path is returned on the results page, (for example, \\\\Dept05\\Memos\\Report1.txt). The UNC path allows the user to find the file on the server. However, if a local client makes a query on the server, the physical path on the local drive is returned (D:\\Memos\\Report1.txt).

Because it has a *bitmask* parameter value of zero, the scope D:\\Memos\\Confidential is ignored and is not indexed.

> [!Note]  
> The main registry entries can be overridden for each catalog. For example, the Correspondence catalog in the previous example does not generate abstracts.

 

## Related topics

<dl> <dt>

[Catalog, Property, and Scope Registry Entries](catalog--property--and-scope-registry-entries.md)
</dt> </dl>

 

 




