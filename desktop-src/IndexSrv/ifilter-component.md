---
title: IFilter Component
description: IFilter Component
ms.assetid: 0a0029cb-35cb-4423-a045-bd030866faca
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IFilter Component

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **IFilter** component is an in-process COM server that extracts the text and values for a specific file type. The appropriate **IFilter** component for a file type is called by the [Filtering component](filtering-component.md).

A customized **IFilter** component can be developed for almost any selected file type. The standard **IFilter** components supplied with Indexing Service include the following ones.



| File Name    | Description                                                                                |
|--------------|--------------------------------------------------------------------------------------------|
| mimefilt.dll | Filters Multipurpose Internet Mail Extension (MIME) files.                                 |
| nlhtml.dll   | Filters HTML 3.0 or earlier files.                                                         |
| offfilt.dll  | Filters Microsoft Office files: Microsoft Word, Microsoft Excel, and Microsoft PowerPoint. |
| Query.dll    | Filters plain text files (default filter) and binary files (null filter).                  |



 

 

 




