---
description: File associations define how the Shell treats a file type on the system.
ms.assetid: A1C05857-26F8-4d4a-977B-4782E8AFA317
title: How File Associations Work
ms.topic: article
ms.date: 05/31/2018
---

# How File Associations Work

File associations define how the Shell treats a [file type](fa-file-types.md) on the system.

This topic is organized as follows:

- [About File Associations](#about-file-associations)
- [When You Should Implement or Modify File Associations](#when-you-should-implement-or-modify-file-associations)
- [How File Associations Work](#how-file-associations-work)
- [Additional Resources](#additional-resources)
- [Related topics](#related-topics)

## About File Associations

File associations control the following functionality:

- Which application launches when a user double-clicks a file.
- Which icon appears for a file by default.
- How the file type appears when viewed in Windows Explorer.
- Which commands appear in a file's shortcut menu.
- Other UI features, such as tooltips, tile info, and the details pane.

Application developers can use file associations to control how the Shell treats custom file types, or to associate an application with existing file types. For example, when an application is installed, the application can check for the presence of existing file associations, and either create or override those file associations.

Users can control some aspects of file associations to customize how the Shell treats a file type either by using the **Open With** UI, or editing the registry.

In the Windows Explorer window shown in the screen shot below, the Shell displays different icons for each file, based on the icon associated with the file type. If the user double-clicks the file **Sample Bitmap Image**, the Shell launches Paint and uses it to open the file because on this system, Paint is associated with .bmp files. People can control these actions using file associations.

![illustration of how file associations work in practice](images/file-assoc/fileassoc-icons.png)

## When You Should Implement or Modify File Associations

Applications can use files for various purposes: some files are used exclusively by the application, and are not typically accessed by users, while other files are created by the user and are often opened, searched for, and viewed from the Shell.

Unless your custom file type is used exclusively by the application, you should implement file associations for it. As a general rule, implement file associations for your custom file type if you expect the user to interact directly with these files in any way. That includes using the Shell to browse and open the files, searching the content or properties of the files, and previewing the files.

If your application is handling an existing file type, do not modify the file association unless you want to modify the way the Shell handles all files of this type.

## How File Associations Work

Files are exposed in the Shell as Shell items. To control file associations, application developers can register a mapping between the file type and the handlers (COM objects that provide functionality for the file type's Shell items). When the Shell needs to query for the file associations of a file type, it creates an array of registry keys containing the associations for the file type, and checks these keys for the appropriate file associations to use.

## Additional Resources

- For conceptual background on file associations, see [Overview of Verbs and File Associations](fa-verbs.md).

## Related topics

<dl> <dt>

[Application Registration](app-registration.md)
</dt> <dt>

[File Types](fa-file-types.md)
</dt> <dt>

[Content View By File Type or Kind](prophand-content-view.md)
</dt> <dt>

[File Type Verifier](file-type-verifier.md)
</dt> <dt>

[File Type Handlers](fa-file-extensions.md)
</dt> <dt>

[Programmatic Identifiers](fa-progids.md)
</dt> <dt>

[Perceived Types](fa-perceivedtypes.md)
</dt> <dt>

[Association Arrays](fa-associationarray.md)
</dt> </dl>

 

 



