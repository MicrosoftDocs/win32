---
Description: 'Security considerations for the Common Log File System API.'
ms.assetid: '11da0e7c-28b9-4990-bf92-b7e6b06b95fb'
title: Security Considerations
---

# Security Considerations

When you are using the Common Log File System API, you should be aware of the following security considerations:

-   CLFS security is based on the underlying file system security. It takes the most restrictive permission that is set from the underlying access control lists (ACLs). If you do not have write permissions to a single container, you do not have write permissions to the entire log.
-   The application must have write permissions to both the log and to the directory in which a container will be created to add a container. The application must have both write and delete permissions to the log to remove a container.
-   To archive the log, the application must have backup permissions, or read and write permissions to the log.
-   The FILE\_GENERIC\_READ and FILE\_GENERIC\_WRITE permissions allow you to not only read and write data, but also to read and write log policies and log metadata.
-   To move the log archive tail, you must have write permissions to the log.
-   If an application must share a log, it is recommended that those applications that must share the log register as managed clients.

 

 



