---
Description: Examples of Relational Queries
ms.assetid: dd4efc15-c3e9-409a-949b-9c642b967398
title: Examples of Relational Queries
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Examples of Relational Queries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following examples illustrate the use of the relational and bitwise-comparison operators.



| To Search For                                                | Example                                                                              | Results                                                                                                                                       |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Property values in relation to a specified value.<br/> | {prop name = size} &lt; 100<br/> —Or—<br/> @size &lt; 100<br/>     | Documents whose size matches the relational restriction. Any of the five other relational operators can replace the &lt; operator.<br/> |
| Property values with all of a set of bits on. <br/>    | {prop name = attrib} ^a 0x820<br/> —Or—<br/> @attrib ^a 0x820<br/> | Compressed documents with the archive bit on. <br/>                                                                                     |
| Property values with some of a set of bits on.<br/>    | {prop name = attrib} ^s 0x20<br/> —Or—<br/> @attrib ^s 0x20<br/>   | Documents with the archive bit on.<br/>                                                                                                 |



 

 

 




