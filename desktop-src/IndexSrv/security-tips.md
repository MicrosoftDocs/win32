---
title: Security Tips
description: Security Tips
ms.assetid: 11d8856a-7054-48b9-bf6a-50908eb096a4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Security Tips

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following are tips that will help ensure the security of your Indexing Service configuration.

-   Indexing Service fully respects NTFS security. As long as the catalog is on an NTFS drive, users will not see documents in the results list if they do not have the appropriate permission. Note that this is only true for local NTFS volumes.
-   If you index a universal naming convention share, users will be able to see documents on that share in the results list, whether they have permission or not. They might be able to open the documents, depending on their permissions, essentially bypassing security.
-   Indexing Service must run in the local system account. For various architectural and implementation reasons it cannot be configured to run in any other context.
-   If you put a catalog on a FAT drive, users will be able to see the catalog, regardless of their permissions.
-   Indexing Service needs permission to access the documents to be indexed. On the local computer, Indexing Service uses the System account to operate. If the System account does not have access to documents or directories, Indexing Service will not be able to index them.
-   Indexing Service never indexes encrypted documents. Encrypting a document causes Indexing Service to remove that document from the catalog.
-   If your web server is flooded with queries, go to the Microsoft Management Console (MMC), Manage My Computer, and check which files are affected. Repeated and prolonged hits over the same set of files may indicate a possible third party denial of service attack.
-   If you use Hit-Highlighting, ensure that you provide a default .htw. The existence of the .htw file disables the null.htw feature. This enables you to configure Internet Information Services (IIS) to enforce the existence of the .htw file.
-   When Hit-Highlighting a document from a remote computer, the access control lists (ACLs) that are enforced are those for the userid for the vroot on the remote system.
-   Indexing Service creates catalogs with secure ACLs. If you create your own catalog location and pre-create the catalog.wci directory, ensure that you have applied the appropriate file protection.
-   Script that uses the IXSSO object must be on the local computer or the query execution will fail with an access denied error. This feature is designed to protect against malicious execution of queries.
-   Any authenticated local or remote user can issue Indexing Service queries. Indexing Service trims the results based on ACLs for files in the result set. Some versions of Windows before Windows 2000, such as Windows 95 and Windows 98, did not support file system and registry security. Others, such as Windows NT, shipped with lax default security settings. For example, unless a user explicitly restricted access to their file, the file was readable to users in the Everyone security identifier. On computers running Windows XP, Everyone includes Authenticated Users and Guest. On computers running earlier versions of Windows, Everyone includes Authenticated Users and Guest plus Anonymous Logon. If Indexing Service enabled on machines with lax default file permissions, remote users can issue queries to Indexing Service and retrieve result paths since, even though there is no network share that enables the user to open the files. Authenticated remote users can see file paths, abstracts, authors, and other properties on files using this mechanism. Therefore, you should always apply proper ACLs to files that are indexed by Indexing Service, and not rely on the lack of network shares as a security mechanism.

## Other Security Related Topics for Indexing Service

-   [Supporting Multiple Security Domains](supporting-multiple-security-domains.md) describes how to set up Indexing Service to crawl computers in different system domains for inclusion in an index.
-   [Putting Security Features to Work](putting-security-features-to-work.md) describes how Indexing Service uses ACLs.
-   [Security Summary](security-summary.md) described security trimming in Indexing Service queries.
-   [Security Considerations](security-considerations.md) describes security considerations for .idq files.

 

 




