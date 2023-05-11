---
description: The Bindlink API coordinates execution of deferrable tasks, called activities, on a Windows system.
ms.assetid: e80b0855-e843-4b11-ab31-82dbf249fc96
title: Overview of the Bindlink API
ms.topic: article
ms.date: 05/11/2023
---

# Overview of the Bindlink API

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). The earliest version in which these features appear is Windows Insider Preview, version 10.0.25314.0.

The **Bindlink** library allows admin users to bind a filesystem namespace to a local "virtual path" via the Bind Filter (mini filter bindflt.sys). Bind Links provide file system redirection from a local "virtual path" to a local or remote "backing path". They can primarily enable two kinds of scenarios: first, they can make remote files over a network share appear local which improves app compatibility, and second, they enable scenarios where an application wants files from different locations to  appear in a new location, potentially with different names and directory structures, without copying the files. Bind Links are transparent to applications and all existing APIs work without the knowledge of this redirection. No physical file or directory is created for the virtual path and bind links extend the security descriptors and permissions of the files and directories in the backing path to the virtual path.

## Usage

The set of APIs is comprised of 2 related functions:

- **CreateBindLink** – This API allows admins to create a bind link between a virtual path and a backing path.
- **RemoveBindLink** – This API allows a user to remove a link that was previously created by calling **CreateBindLink**.

For sample usage of these functions, see [Bindlink examples](bindlink-examples.md).

## Creating bind links

Bind links are transparent to the applications and whilst these links exist, all operations apply to the backing path. As a result, **DeleteFile** or **RemoveDirectory** will act upon the backing path, effectively deleting the backing path but not the link. This API will fail if the user does not have Administrator privileges, if the user does not have permissions to open the virtual path or the backing path, if the backing path doesn’t exist, if another link exists for the virtual path, or if there is an internal failure while setting up the link. Specifically, the admin user should be able to attach the filter (permissions for **FilterAttach**), connect to the filter port (permissions for **FilterConnectCommunicationPort**) and access the root of the backing path or else the api will fail with **ERROR_ACCESS_DENIED**.

If an app tries to follow the link to a backing path that was deleted after the link was setup, the app will see *ERROR_FILE_NOT_FOUND**. Later if the backing path is created again, the link will now apply to this new backing path. If a file were to be created at the *virtualPath* while the link exists, it would show up at the *virtualPath* if the link exists but is physically created at the backing path. When the link is removed, the file would only appear at the backing path and would no longer show up at the *virtualPath*. This applies to all the kinds of links described below.

Depending on whether the virtual path is present on-disk, the resulting link will either be an anchorless link or a shadow link.

### Anchorless Links

Anchorless links are bind links that are created when the virtual path does not exist on the disk before the link is created. When this sort of link is created, the virtual path is synthesized in-memory and appears like a regular path in the filesystem. Note that to create such a bind link, the parent of the virtual path must exist either as an on-disk directory or as a previously created link. For example, to use C:\\Foo\\Bar as a virtual path, C:\\Foo must be an on-disk directory or previously created as the virtual path for another link. Since there is no parent for a volume, there cannot be an anchorless link to a volume that doesn’t exist. For example, creating a bind link with a virtual path "Z:" would fail if there wasn't already a volume named "Z".

### Shadow Links

A shadow link is one where the virtual path exists on the volume prior to the link being created. When such a virtual path is used to create a link, the contents of the virtual path are hidden while the contents of the backing path become visible at the virtual path. For example:

- C:\\Foo exists on disk with two files Cat.txt and Dog.txt
- C:\\Bar exists on disk with two files Cow.txt and Mouse.txt

When a link is created with C:\\Foo as the virtual path and C:\\Bar as the backing path, the C:\\Foo path will then show Cow.txt and Mouse.txt to all users while Cat.txt and Dog.txt will be hidden, until the link is removed.

Another example in the following diagram helps distinguish between Shadow link and Anchorless link.

:::image type="content" source="images/anchorless-vs-shadow-bind-links.png" alt-text="Anchorless versus shadow bind links diagram":::

A user enumerating c:\\Foo will find the directory and its existing contents even before any of the bind links shown in the diagram are created. After the links are created, enumerating c:\\Foo will show C:\\Foo\\Bar and Cow.txt. Since C:\\Foo exists on the disk with or without the link, the link between C:\\Foo and \\\\Remote\\Target is a shadow link.

A user enumerating c:\\Foo wouldn’t see c:\\Foo\\Bar before the second bind link is created. Since C:\\Foo\\Bar shows up only after the link between c:\\Foo\\Bar and C:\\Target2 is added, It is purely virtual and hence the link between c:\\Foo\\Bar and C:\\Target2 is an Anchorless link.

Note that, for both these types of links, the security descriptors of the backing path apply.

Certain flags can be passed in to change the default behavior to suit the needs of the user.

### CREATE_BIND_LINK_FLAG_MERGED flag

A merged link is like a shadow link, except the existing content in the virtual path is merged with backing path. To create this kind of link, the **CREATE_BIND_LINK_FLAG_MERGED** flag should be used.

Let’s consider the prior example for shadow link once again, with the addition of this flag.

For example:

- C:\\Foo exists on disk with two files Cat.txt and Dog.txt
- C:\\Bar exists on disk with two files Cow.txt and Mouse.txt

When a link is created with C:\\Foo as the virtual path and C:\\Bar as the backing path with the flag **CREATE_BIND_LINK_FLAG_MERGED**, C:\\Foo path will show Cat.txt, Dog.txt, Cow.txt and Mouse.txt.

It is important to remember that merged links only apply when the virtual path is a directory. In the case where a file appears in both the backing path and the virtual path, the file in the backing path takes precedence – i.e., the file in the virtual path is masked. This applies recursively for all directories within the virtual path. Because the merge applies to directories, if the *virtualPath* and the *backingPath* both have a directory with the same name at the same level, the directory will be merged as an outcome of the link. If the link wasn’t a merged link the directory in the *backingPath* will take precedence and override the directory in the *virtualPath*. If a file were created at the merged path when the merged link exists, it will be physically created at the *backingPath* (as is the case with any bind link) and will override a file with the same name at the *virtualPath*.

Let’s consider the following directory structures and the two different links:

- c:\Foo\Sub\Foo_sub.txt
- c:\Bar\Sub\Bar_sub.txt.

If c:\\Foo is linked to c:\\Bar *without* merge, then c:\\Foo\\Sub will only show Bar_sub.txt. However, if c:\\Foo is linked to c:\\Bar *with* merge, then c:\\Foo\\Sub will show both Foo_sub.txt and Bar_sub.txt.

Since bind links are path-based links, if a file is replaced, modified, or deleted/recreated in the backing path after the link is created, the virtual path will point to the file that exists at the time the link is being followed. This happens because the link is resolved at the time a file is opened. Accordingly, if a file from the backing path was masking a file in the virtual path due to the link, and if the file in the backing path was deleted, a subsequent request to open the file will open it in the virtual path.

### CREATE_BIND_LINK_FLAG_READ_ONLY flag

Read-only links are bind links where the users on the system are prevented from making changes to files that reside in the backing path if they are accessed through the virtual path. This means that a user with permission to modify a file on the backing path can still modify that file if they access it through the backing path, but not if they access it through the virtual path. Normally, the permissions of the backing path apply as such when the corresponding virtual path is accessed, however when **CREATE_BIND_LINK_FLAG_READ_ONLY** flag is used the *write* permissions are masked off. This ensures that applications see that the file is **CREATE_BIND_LINK_FLAG_READ_ONLY**.

Note that the read-only restriction only applies to files that reside at the backing path on disk. If the link is merged and files that are originally from the virtual directory path are visible, they will remain modifiable.

For example:

- C:\\Foo exists on disk with a file Cat.txt
- C:\\Bar exists on disk with a file Cow.txt

When a link is created with C:\\Foo as the virtual path and C:\\Bar as the backing path and the link is marked read-only and merged, both Cat.txt and Cow.txt will be visible at C:\\Foo, however, Cat.txt will be modifiable while Cow.txt will not be modifiable.

In addition, this API supports several other link scenarios. These are described in the following sections.

### Nested links

Bind Links can be nested. This means that an ancestor or a descendant component of a virtual path can also be a virtual path for its own link.

Note that there is no restriction on ensuing circular links.

:::image type="content" source="images/nested-bind-links.png" alt-text="Nested bind links diagram":::

Consider the links and the order of the links in the "Nested Bind Links" diagram above.

    If a link is created with virtual path: C:\\Foo\\Bar, another link can be created with C:\\Foo as its virtual path, and yet another link can be created with C:\\Foo\\Bar\\Baz as its virtual path.

    For example:

    - C:\\Target exists on disk with a file Cat.txt
    - C:\\Target2 exists on disk with a file Dog.txt
    - C:\\Foo exists on disk with a directory Bar

    If C:\\Foo\\Bar is linked to C:\\Target (Link1) and then C:\\Foo is linked to C:\\Target2 (Link2), a user enumerating C:\\Foo will see Dog.txt and the directory Bar, since Bar is a virtual path for its own link. Subsequently if C:\\Foo\\Bar\\Baz is linked to C:\\Target2 (Link3), A user enumerating c:\\Foo\\Bar will see Cat.txt and the directory Baz, since Baz is a virtual path for its own link.

### Additional bind link scenarios

The following points are important and should always be considered together when deciding on the outcome of a link or a set of links:

1. The backing path always takes precedence and overrides if an entity with the same names exists in the virtual path or by virtue of a link. This applies to all kinds of Bind Links.

    For example, consider the following link:

    c:\\Foo is linked to c:\\Target, where c:\\Target is a file.

    In that case c:\\Foo will look like a file having contents of c:\\Target for an anchorless link. Even if c:\\Foo is a directory that exists locally (shadow link), the above link will make c:\\Foo look like a file if the link and the backing path exist.

1. In the event of conflicting links, the most recently created link takes precedence. However, the most recent link cannot hide a prior link.

    As another example consider the following links. The second link changes the view of the namespace.

    - Link1: c:\\Foo is linked to c:\\Target, where c:\\Target is a directory. c:\\Target has a file Bar
    - Link2: c:\\Foo\\Bar is linked to c:\\Target2, where Target2 is a directory containing a file Cat.txt

    :::image type="content" source="images/order-of-bind-links.png" alt-text="Order of bind links diagram":::

    In this case, after Link1 is created, c:\\Foo will have a file Bar. However, after Link2, c:\\Foo will show a directory Bar with a file Cat.txt. Similarly, if c:\\Target2 were a file, c:\\Foo\\Bar will be a file with the contents of C:\\Target2

    On the other hand, If the order of the links were reversed as shown below, c:\\Foo\\Bar will continue to appear as a directory showing Cat.txt from c:\\Target2. The backing path takes precedence over items under a virtual path, but they do not take precedence over the virtual path root itself.

    - Link1: c:\\Foo\\Bar is linked to c:\\Target2, where Target2 is a directory containing a file Cat.txt
    - Link2: c:\\Foo is linked to c:\\Target, where c:\\Target is a directory. c:\\Target has a file Bar

1. For a link to be successfully created, the parent of the virtual path should exist either locally or be showing up due from the *backingPath* in a previous link or be a virtual path itself in a link.

    For example, if c:\\Foo is linked to c:\\Target first, and then c:\\Foo\\Bar\\Baz is being linked to a backing path, the link from c:\\Foo\\Bar\\Baz will succeed if c:\\Foo\\Bar exists due to one of the following conditions:

    - c:\\Foo\\Bar exists locally and an exception in the previous link ensures c:\\Foo\\Bar wasn’t shadowed by c:\\Target (please refer to Exceptions in the next Section) *or*
    - c:\\Foo\\Bar exists by virtue of the previous link (i.e., if c:\\Target has a directory Bar) *or*
    - c:\\Foo\\Bar is a virtual path itself in another link (c:\\Foo\\Bar ==> something)

    >[!NOTE]
    >This implies that nested anchorless links must be created with the deepest link being created last. However, shadow links have no such restrictions, as the virtual paths already exist on the disk.

Consider the following links created in the same order:

- C:\\Foo is linked to C:\\Target
- C:\\Foo\\Bar is linked to c:\\Target2

Creating a link has no effect on the behavior of the backing path. Hence the virtual directory Bar shows up in c:\\Foo and not in c:\\Target. The link table will look like this:

- C:\\Foo --> c:\\Target, C:\\Foo\\Bar --> c:\\Target2 *and not*
- C:\\Foo --> c:\\Target, c:\\Target\\Bar --> c:\\Target2

### Exceptions to Bind Links

Optionally, exceptions can be specified to limit the scope of the created link. Exception paths are descendants of the virtual path where the link does not apply. Exception paths can be files or directories but should be a descendant of the virtual path. The APIs require that the exception paths are accessible when the link are being created. The exception applies for all descendants of the exception path. For example:

- C:\\Foo exists on disk and contains a directory Bar and a directory Baz
- C:\\Foo\\Bar contains Cat.txt
- C:\\Foo\\Baz contains Dog.txt
- C:\\Target exists on disk and contains a file Cow.txt

If a link is created from C:\\Foo to C:\\Target with an exception for C:\\Foo\\Baz, the user will see the following:

- C:\\Foo will contain the file Cow.txt from C:\\Target, and the directory Baz with its child Dog.txt. Note that C:\\Foo\\Bar will not be visible since it has been shadowed by the link.

The following diagram represents the scenario described above:

:::image type="content" source="images/bind-link-exceptions.png" alt-text="Bind link exceptions diagram":::

Finally, bind link exceptions do not apply to anchorless links since anchorless virtual paths have no descendants by definition and, therefore, have no paths that qualify. The API will return an error if there is an attempt to pass exceptions to anchorless link.

## See also

[Bindlink functions](bindlink-api-functions.md)

[Bindlink enums](bindlink-api-enums.md)

[Bindlink examples](bindlink-examples.md)
