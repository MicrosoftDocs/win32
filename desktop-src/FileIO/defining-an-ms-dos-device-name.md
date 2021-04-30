---
description: An MS-DOS device name is a junction that points to the path of an MS-DOS device. These junctions make up the MS-DOS device namespace.
ms.assetid: 7d802e9f-dc09-4e3d-b064-e9b57af396e2
title: Defining an MS-DOS Device Name
ms.topic: article
ms.date: 05/31/2018
---

# Defining an MS-DOS Device Name

An MS-DOS device name is a junction that points to the path of an MS-DOS device. These junctions make up the MS-DOS device namespace. Call the [**DefineDosDevice**](/windows/desktop/api/FileAPI/nf-fileapi-definedosdevicew) and [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa) functions to create and modify these junctions. [**DeleteVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-deletevolumemountpointw) deletes a junction created by **SetVolumeMountPoint**, and **DefineDosDevice** deletes junctions it creates.

After an MS-DOS device name is defined, it remains visible to all processes.

-   All MS-DOS devices are identified by Windows through an authentication ID. An authentication ID is the LUID (locally unique identifier) associated with each logon session when created.
-   The visibility of an MS-DOS device name is categorized as either global or local, and is defined as such by its inclusion in the Global MS-DOS Device and Local MS-DOS Device namespaces. The contents of MS-DOS devices in the Global namespace can be accessed by all users, and the contents of MS-DOS devices in the Local namespace can be accessed only by the user whose access token contains the AuthenticationID associated with that Local MS-DOS device namespace.

Multiple Local MS-DOS Device namespaces and only one Global MS-DOS Device namespace may exist at one time and on one machine.

Note that only processes running in the LocalSystem context can call [**DefineDosDevice**](/windows/desktop/api/FileAPI/nf-fileapi-definedosdevicew) to create an MS-DOS device in the Global MS-DOS device namespace. Also, the Local MS-DOS device namespace corresponding to a specific AuthenticationID is deleted when the last reference to that AuthenticationID is removed.

When your code queries an existing MS-DOS device name by calling [**QueryDosDevice**](/windows/desktop/api/FileAPI/nf-fileapi-querydosdevicew), it first searches the Local MS-DOS Device namespace. If it is not found there, the function will then search the Global MS-DOS Device namespace. When your code queries all existing MS-DOS device names through this function, the list of names that are returned is dependent on whether it is running in the LocalSystem context. If so, only the MS-DOS device names included in the Global MS-DOS Device namespace will be returned. If not, a concatenation of the device names in the Global and Local MS-DOS Device namespaces will be returned. If a device name exists in both namespaces, **QueryDosDevice** will return the entry in the Local MS-DOS Device namespace. This also applies to the list of all MS-DOS device names returned by [**GetLogicalDrives**](/windows/desktop/api/FileAPI/nf-fileapi-getlogicaldrives) and [**GetLogicalDriveStrings**](/windows/desktop/api/FileAPI/nf-fileapi-getlogicaldrivestringsw).

Note that the following scenario may occur:

1.  User A, who is not running within the LocalSystem context, creates a device name in the corresponding Local MS-DOS Device namespace, and that device name does not exist in the Global MS-DOS Device namespace.
2.  User B, who is running within the LocalSystem context, creates the same device name in the Global MS-DOS Device namespace.

In this scenario, User A will not have access to the device name in the Global MS-DOS Device namespace until he or she removes or renames the device name in his or her Local MS-DOS Device namespace. To reduce the likelihood of this scenario occurring, MS-DOS drive letters should be allocated in the Global MS-DOS Device namespace starting with C: and ending with Z:. This sequence should be reversed for the allocation of MS-DOS drive letters in the Local MS-DOS Device namespace.

If you are not running within the LocalSystem context, [**DefineDosDevice**](/windows/desktop/api/FileAPI/nf-fileapi-definedosdevicew) will not allow you to define a device name in the Local MS-DOS Device namespace if that device name already exists in your Local or Global MS-DOS Device namespaces. Call [**QueryDosDevice**](/windows/desktop/api/FileAPI/nf-fileapi-querydosdevicew) before calling **DefineDosDevice** to determine whether the device name you intend to define exists in your MS-DOS Device namespaces.

## Related topics

<dl> <dt>

[Naming Files, Paths, and Namespaces](naming-a-file.md)
</dt> </dl>

 

 



