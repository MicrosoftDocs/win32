---
title: Security Summary
description: Security Summary
ms.assetid: '730e4506-f84d-4957-ad8d-39b634e33d96'
---

# Security Summary

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Note that the standard security system is used, so IIS and Windows must be configured for secure access. Also, the documents themselves must be protected with ACLs.

Indexing Service checks ACLs before returning query results to the browser. A user must have Read privilege on a document for Indexing Service to return a hit. The query is first executed in the system security context so all hits are returned. Then documents the user cannot see are removed from the result set, and the remaining documents are returned to the user.

Indexing Service by default always checks security; therefore, all queries are performed with ACL checking activated. Any authenticated local or remote user can issue Indexing Service queries. Indexing Service trims the results based on ACLs for files in the result set. If Indexing Service enabled on machines with lax default file permissions, remote users can issue queries to Indexing Service and retrieve result paths since, even though there is no network share that enables the user to open the files. Authenticated remote users can see file paths, abstracts, authors, and other properties on files using this mechanism. Therefore, you should always apply proper ACLs to files that are indexed by Indexing Service and not rely on the lack of network shares as a security mechanism.

If a file has restrictive ACLs and a user is not allowed to read a document, Indexing Service gives that user no reference to the document; he or she does not even know that the document exists. Many other systems will return a reference to the document and then prohibit actual access to the document. Removing prohibited documents from the result set is important because Indexing Service can generate document abstracts derived from the content of a document. To return a reference and abstract for a secure document would violate security because some of the contents would be displayed. Even if abstracts are not generated, returning hits to a prohibited document allows an intruder to find documents with sensitive words and phrases, and determine the location of these documents. This information could easily breach security.

 

 




