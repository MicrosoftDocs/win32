---
title: Getting Started
description: Getting Started
ms.assetid: 92c5bb27-f853-488d-8325-739a3403e37f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

To get started quickly, you can select the most appropriate category and follow the suggestions in the corresponding reference. There is considerable overlap of applicable information in these sections, and eventually you might want to look through more than one.

-   [Power User or Administrator](#power-user-or-administrator)
-   [File System-Oriented Programmer or Script Writer](#file-system-oriented-programmer-or-script-writer)
-   [Web Server-Oriented Programmer or Script Writer](#web-server-oriented-programmer-or-script-writer)
-   [Custom Filter-Component Programmer](#custom-filter-component-programmer)
-   [Custom Language Resources Programmer](#custom-language-resources-programmer)

### Power User or Administrator

The following sections describe how Indexing Service works and how to manage it as a power user or an administrator.



| To Learn About                                                            | See                                                                                                                                                                             |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The structure and operation of Indexing Service<br/>                | [Architecture of Indexing Service](architecture-of-indexing-service.md)<br/>                                                                                             |
| Standard Indexing Service filters available for indexing files<br/> | [Filter DLLs](filter-dlls.md)<br/>                                                                                                                                       |
| Controlling how Indexing Service filters files<br/>                 | [Controlling Filtering](controlling-filtering.md)<br/>                                                                                                                   |
| Managing Indexing Service with scripts<br/>                         | [Programming with Scripts](programming-with-scripts.md)<br/> [IISAdmin Sample](iisadmin-sample.md)<br/>                                                           |
| Managing Indexing Service with applications<br/>                    | [Programming with Applications](programming-with-applications.md)<br/> [ChgState Sample](chgstate-sample.md)<br/> [VBAdmin Sample](vbadmin-sample.md)<br/> |



 

### File System-Oriented Programmer or Script Writer

The following sections describe how Indexing Service interacts with file systems.



| To Learn About                                                                                                | See                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| An overview of programming for Indexing Service<br/>                                                    | [Programming for Indexing Service](programming-for-indexing-service.md)<br/>                                                           |
| How to program Indexing Service for file systems<br/>                                                   | [Using Indexing Service with File Systems](using-indexing-service-with-file-systems.md)<br/>                                           |
| Writing simple query applications using helper functions or ADOs<br/>                                   | [Simple Sample](simple-sample.md)<br/> [VBQuery Sample](vbquery-sample.md)<br/> [VJQuery Sample](vjquery-sample.md)<br/> |
| Writing efficient query applications that directly access the OLE DB Provider for Indexing Service<br/> | [AdvQuery Sample](advquery-sample.md)<br/>                                                                                             |



 

### Web Server-Oriented Programmer or Script Writer

The following sections describe how Indexing Service interacts with web servers and scripts.



| To Learn About                                                                                          | See                                                                                               |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| An overview of programming for Indexing Service.<br/>                                             | [Programming for Indexing Service](programming-for-indexing-service.md)<br/>               |
| How to program Indexing Service for web servers<br/>                                              | [Using Indexing Service with Web Servers](using-indexing-service-with-web-servers.md)<br/> |
| Writing scripts to query Indexing Service using Dynamic HTML (DHTML)<br/>                         | [DHtml Sample](https://www.bing.com/search?q=DHtml Sample)<br/>                                                  |
| Writing queries using an Indexing Service Query Language or the SQL language and an ASP page<br/> | [IISSearch Sample](iissearch-sample.md)<br/>                                               |



 

### Custom Filter-Component Programmer

The following sections describe how standard Indexing Service filters work and how to build a custom one.



| To Learn About                                                                                   | See                                                                                                          |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| The information needed to write an Indexing Service filter for a specific file format<br/> | [Using Custom Filters with Indexing Service](using-custom-filters-with-indexing-service.md)<br/>      |
| Standard Indexing Service filters available for indexing files<br/>                        | [Filter DLLs](filter-dlls.md)<br/>                                                                    |
| Writing a simple filter<br/>                                                               | [Constructing Filters](constructing-filters.md),<br/> [SmpFilt Sample](smpfilt-sample.md)<br/> |
| Writing more complex filters that extract value-type properties<br/>                       | [IFilter Sample](ifilter-sample.md)<br/> [HtmlProp Sample](htmlprop-sample.md)<br/>            |
| Testing a filter implementation<br/>                                                       | [Testing Filters](testing-filters.md)<br/>                                                            |



 

### Custom Language Resources Programmer

The following table lists topics that contain information for programmers who want to develop custom language resource components such as word breakers and stemmers.



| To Learn About                                                                                                            | See                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| The information needed to write an language resource component for a particular language for Indexing Service <br/> | [Extending Language Resources for Indexing Service](extending-language-resources-for-indexing-service.md)<br/> |
| List of language resources available in Indexing Service<br/>                                                       | [Language Resources](language-resources.md)<br/>                                                               |
| Creating a language resource components<br/>                                                                        | [Constructing Language Resource Components](constructing-language-resource-components.md)<br/>                 |
| Troubleshooting language resource components<br/>                                                                   | [Troubleshooting Language Resources](troubleshooting-language-resources.md)<br/>                               |



 

> [!Note]  
> You must install files for East Asian languages in order for Japanese and Korean text in the SDK to appear correctly.

 

You can configure language settings in Windows XP by clicking the Regional and Language Options icon in Control Panel. You can configure language settings in Windows 2000 by clicking the Regional Options icon in Control Panel.

 

 





