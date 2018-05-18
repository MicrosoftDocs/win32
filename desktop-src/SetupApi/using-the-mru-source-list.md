---
Description: 'The SetupSetSourceList function will open or create a source list on the user's system.'
ms.assetid: 'cda632cf-6c92-48fb-aef1-25b320affd3e'
title: Using the MRU Source List
---

# Using the MRU Source List

The [**SetupSetSourceList**](setupsetsourcelist.md) function will open or create a source list on the user's system. You can specify to set the user list, the system list, a combination of the user and system lists, or a temporary list as the MRU source list. If a temporary list is used, it will be the only list available to the setup application until [**SetupCancelTemporarySourceList**](setupcanceltemporarysourcelist.md) is called, or **SetupSetSourceList** is called a second time.

After a list is set, you can query the source list by using [**SetupQuerySourceList**](setupquerysourcelist.md) to obtain an array of the source paths. When the source list array is no longer needed, you must call the [**SetupFreeSourceList**](setupfreesourcelist.md) function to free the resources allocated by [**SetupQuerySourceList**](setupquerysourcelist.md).

To add a path to a source list, either one that is resident on the user's system, or a temporary list, call [**SetupAddToSourceList**](setupaddtosourcelist.md). If the source list specified is not temporary, that source will remain on the user's system and is accessible to subsequent installations.

To remove a path from the source path, call the [**SetupRemoveFromSourceList**](setupremovefromsourcelist.md) function.

 

 



