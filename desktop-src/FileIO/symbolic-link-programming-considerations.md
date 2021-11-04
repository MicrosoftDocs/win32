---
description: Programming considerations for working with symbolic links.
ms.assetid: 8966ac3e-a92b-4d68-b40b-e32a4173f869
title: Programming Considerations (Local File Systems)
ms.topic: article
ms.date: 05/31/2018
---

# Programming Considerations (Local File Systems)

Keep the following programming considerations in mind when working with symbolic links:

-   Symbolic links can point to a non-existent target.
-   When creating a symbolic link, the operating system does not check to see if the target exists.
-   If an application tries to open a non-existent target, **ERROR\_FILE\_NOT\_FOUND** is returned.
-   Symbolic links are reparse points. For more information, see [Determining Whether a Directory Is a Mounted Folder](determining-whether-a-directory-is-a-volume-mount-point.md).
-   There is a maximum of 63 reparse points (and therefore symbolic links) allowed in a particular path.

    **Windows Server 2003 and Windows XP:** There is a limit of 31 reparse points on any given path.

## Related topics

<dl> <dt>


</dt> <dt>

[Hard Links and Junctions](hard-links-and-junctions.md)
</dt> </dl>

 

 



