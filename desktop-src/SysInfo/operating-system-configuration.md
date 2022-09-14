---
description: The Windows directory is the directory that contains Windows-based applications, initialization files, and help files. The GetWindowsDirectory function retrieves the path to this directory.
ms.assetid: c07c6337-2c92-42c5-8283-c95637fcb85a
title: Operating System Configuration
ms.topic: article
ms.date: 05/31/2018
---

# Operating System Configuration

The *Windows directory* is the directory that contains Windows-based applications, initialization files, and help files. The [**GetWindowsDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function retrieves the path to this directory.

The *system directory* is the directory that contains dynamic-link libraries, drivers, and font files. The [**GetSystemDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) function retrieves the path to this directory.

The [**GetUserName**](/windows/desktop/api/Winbase/nf-winbase-getusernamea) function retrieves the name of the user currently logged onto the system. The user name is either the logon name or the user's full name, if the latter is included in the registry.

An *environment variable* is a symbolic variable that represents some element of the system, such as a path, a file name, or other literal data. For example, the environment variable PATH represents the directories in which to search for executable files. When a user logs on, the system initializes environment variables based on the environment section of the registry. The [**ExpandEnvironmentStrings**](/windows/win32/api/processenv/nf-processenv-expandenvironmentstringsa) function retrieves the values of specified environment variables.

Additional information is provided by the [**IADsADSystemInfo**](/windows/desktop/api/iads/nn-iads-iadsadsysteminfo) interface.

 

 
