---
description: Windows 7 introduces libraries, which provide users with a single, coherent view of their files even when those files are stored in different locations.
title: Windows Libraries
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 19DA68B2-FCB6-443d-A3CD-0BF2F429B149
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Windows Libraries

Windows 7 introduces libraries, which provide users with a single, coherent view of their files even when those files are stored in different locations. Libraries can be configured and organized by a user and a library can contain folders that are found on the user's computer and also folders that have been shared over a network. Libraries present a simpler view of the underlying storage system because, to the user, the files and folders in a library are displayed in single view, no matter where they are physically stored.

Developers writing new programs in Windows 7 are encouraged to use libraries as the means through which the users interact with the files used by the program. Using libraries in your program will provide users with a cleaner, easier, and more consistent experience in Windows 7.

Developers should also review their existing programs, and update them if necessary, to work with libraries. Because libraries are not a part of the file system, file system-based APIs will not have access to any libraries that the user might have configured.

Programs that currently allow users to store their content in different folders or on different computers will benefit most when they add library support. Libraries simplify the management of content in diverse storage locations for the developer and the user.

This guide describes more about what libraries are, how programs can be made to work with libraries, and some of the ways a program can use libraries to improve the user's experience.

## Related topics

<dl> <dt>

[About Libraries](library-leverage-to-manage-folders.md)
</dt> <dt>

[Using Libraries in your Program](library-be-library-aware.md)
</dt> <dt>

[**IShellLibrary**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllibrary)
</dt> <dt>

[Shell Links](./links.md)
</dt> <dt>

[Known Folders](known-folders.md)
</dt> <dt>

[Library Description Schema](library-schema-entry.md)
</dt> </dl>

 

 
