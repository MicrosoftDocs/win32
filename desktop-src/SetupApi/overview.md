---
description: The Setup application programming interface (API) provides a set of functions that your setup application can call to perform installation operations. These setup functions work with Windows INF files to provide the following setup functionality.
ms.assetid: 58201596-cb8c-480a-abef-896c1f9ef098
title: Overview
ms.topic: article
ms.date: 05/31/2018
---

# Overview

The Setup application programming interface (API) provides a set of functions that your setup application can call to perform installation operations. These setup functions work with Windows INF files to provide the following setup functionality.



| For information about                       | See                                                                                                                                                                         |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Queuing files                               | [File Queues](file-queues.md)                                                                                                                                              |
| Installing files                            | [File Queues](file-queues.md)<br/> [Setup Applications](setup-applications.md)<br/> [Creating Setup Applications](creating-setup-applications.md)<br/> |
| Handling errors and prompting for media     | [Disk Prompting and Error Handling](disk-prompting-and-error-handling.md)                                                                                                  |
| Updating registry entries                   | [Setup Applications](setup-applications.md)                                                                                                                                |
| Logging installed files                     | [File Log](file-log.md)                                                                                                                                                    |
| Storing the most recently used source paths | [MRU Source List](mru-source-list.md)                                                                                                                                      |



 

Unicode and ANSI versions are available for most setup functions. Unicode text files should contain the standard 0xFEFF byte-order mark to enable setup functions to identify the file as Unicode text.

Although the Setup API supports prompting for new media and basic error-handling dialog boxes, the setup functions do not provide wizard functionality or a generic user interface.

Developers should consider whether they can use [Windows Installer](/windows/desktop/Msi/windows-installer-portal) to install their applications rather than the Setup API. Windows Installer reduces the total cost of ownership (TCO) for your customers by enabling them to efficiently install and configure your products and applications. The installer can also provide your product with new capabilities to advertise features without installing them, to install products on-demand, and to add user customizations.

 

