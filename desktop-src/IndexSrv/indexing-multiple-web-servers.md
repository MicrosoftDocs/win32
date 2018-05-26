---
title: Indexing Multiple Web Servers
description: Indexing Multiple Web Servers
ms.assetid: f3dbe0a3-c5c3-4e90-9b56-a8a51a610af8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Indexing Multiple Web Servers

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Many sites use Indexing Service to index multiple web servers, especially in a corporate intranet environment. This is done simply by sharing a folder on the remote volume and creating a virtual directory on the indexing server. However, in some cases, especially if the remote system is a web server, links can break because the share was not made at the correct point in the hierarchy. Consider the following example.

Local Computer: Local

Remote Computer: Remote

Remote Web Root: \\\\Remote\\InetPub\\Wwwroot

Remote Web 1 Directory: \\\\Remote\\InetPub\\Wwwroot\\Web1

Remote Share: \\\\Remote\\Web1

Remote Share Mounted Locally: http://local/specs

In the preceding example, the shared directory that is indexed is D:\\InetPub\\Wwwroot\\Web1. In the Indexing Service default .htx file, links are returned as &lt;%server%&gt;&lt;%vpath%&gt;, so on the local computer remote files are returned through the reference http://local/specs. This usually breaks links because the webpages with physical directories ending in Web1 (such as \\Remote\\InetPub\\Wwwroot\\Web1) probably contain links to virtual roots beginning with http://remote (such as http://remote/web1).

To solve this problem you can share out the Web root directories and modify your .htx file as follows.

Local Computer: Local

Remote Computer: Remote

Remote Web Root: \\\\Remote\\InetPub\\Wwwroot

Remote Web 1 Directory: \\\\Remote\\InetPub\\Wwwroot\\Web1

Remote Share: \\\\Remote\\Wwwroot

Remote Share Mounted Locally: /Remote

Note that the remote share is now the Wwwroot directory, and its virtual directory on the indexing computer (local) is /remote. The last step modifies the .htx file to return hyperlinks as “http:/&lt;%vpath%&gt;”. This setting returns the correct hyperlink for all documents stored on the remote computer.

For example, if a document on the remote computer was referenced as http://remote/web1/sample.doc, it would normally be served by the indexing computer (local) as http://local/remote/web1/sample.doc, because its virtual path is /remote/web1/sample.doc. However the .htx modification inserts an http:/ reference before the virtual path, so the URL that is actually returned is now http://remote/web1/sample.doc, which is the correct URL.

This configuration allows the remote servers to do all the file serving, leaving the indexing server free to do all the serving.

 

 




