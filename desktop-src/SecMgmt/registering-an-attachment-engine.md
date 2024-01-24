---
description: Before the Security Configuration Engine can call your attachment engine to process service-specific tasks, you must install your attachment engine and register it with the Security Configuration Engine.
ms.assetid: f7376a79-97cd-4607-9e1b-5b8c7cd76a32
title: Registering an Attachment Engine
ms.topic: article
ms.date: 05/31/2018
---

# Registering an Attachment Engine

Before the Security Configuration Engine can call your attachment engine to process service-specific tasks, you must install your attachment engine and register it with the Security Configuration Engine.

**To install and register the attachment engine DLL**

1.  Copy the attachment engine DLL to a directory on the system. The preferred directory is %windir%\\secedit\\attachments. If this directory does not exist, you should create it.
2.  Create a registry key under the following node. The *service name* is the registered name for the attachment, and must be the same service name used in the Service Control Manager, a module which manages the stopping and starting of services. The name must also be unique so it does not conflict with the names of other attachments.

    ```
    HKEY_LOCAL_MACHINE
       Microsoft
          Windows NT
             CurrentVersion
                SeCEdit
                   Service
                      service name
    ```

3.  Create the following string value in the new registry key. *attachment engine path* is the full path to the attachment engine module.<dl> <dd>**ServiceAttachmentPath** = *attachment engine path*<dl> <dt>

Data type
</dt> <dd>REG_SZ</dd> </dl> </dd> </dl>

 

 



