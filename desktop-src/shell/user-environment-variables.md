---
description: Environment variables specify search paths for files, directories for temporary files, application-specific options, and other similar information.
ms.assetid: 6180e54e-4bd9-4692-83fd-f3f7f1d8f8d7
title: User Environment Variables
ms.topic: article
ms.date: 05/31/2018
---

# User Environment Variables

Environment variables specify search paths for files, directories for temporary files, application-specific options, and other similar information. The system maintains an environment block for each user and one for the computer. The system environment block represents environment variables for all users of the particular computer. A user's environment block represents the environment variables the system maintains for that particular user, including the set of system environment variables.

By default, each process receives a copy of the environment block for its parent process. Typically, this is the environment block for the user who is logged on. A process can specify different environment blocks for its child processes using the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) or [**CreateProcessAsUser**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) function.

To add or modify environment variables, the user selects **System** from the **Control Panel**, then selects the **Environment** tab. The user can also add or modify environment variables at a command prompt using the **set** command. Environment variables created with the **set** command apply only to the command window in which they are set, and to its child processes. For more information, type **set /?** at a command prompt.

To retrieve a copy of the environment block for a given user, use the [**CreateEnvironmentBlock**](/windows/desktop/api/Userenv/nf-userenv-createenvironmentblock) function. To free an environment block created by **CreateEnvironmentBlock**, use the [**DestroyEnvironmentBlock**](/windows/desktop/api/Userenv/nf-userenv-destroyenvironmentblock) function. These functions reference a pointer to an environment block. The environment block is an array of null-terminated Unicode strings. The list ends with two nulls (\\0\\0).

To expand a string that contains environment variables by using the environment block for a specified user, use the [**ExpandEnvironmentStringsForUser**](/windows/desktop/api/Userenv/nf-userenv-expandenvironmentstringsforusera) function.
