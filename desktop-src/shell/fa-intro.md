---
description: 'This section on file types and file associations is organized as follows:'
ms.assetid: 45d8b729-1e9d-40c0-8306-9a475262ac40
title: File Types and File Associations
ms.topic: article
ms.date: 05/31/2018
---

# File Types and File Associations

This section on file types and file associations is organized as follows:

- [Application Registration](app-registration.md)
- [File Types](fa-file-types.md)
- [How to Choose a File Type Extension](how-to-choose-a-file-type-extension.md)
- [How to Define File Type Attributes](how-to-define-file-type-attributes.md)
- [How to Include an Application on the Open with Dialog Box](how-to-include-an-application-on-the-open-with-dialog-box.md)
- [How to Exclude an Application from the Open with Dialog Box for Unassociated File Types](how-to-exclude-an-application-from-the-open-with-dialog-box-for-unassociated-file-types.md)
- [How File Associations Work](fa-how-work.md)
- [Content View By File Type or Kind](prophand-content-view.md)
- [How to Register Custom Properties and Layout for Your File Type](how-to-register-custom-properties-and-layout-for-your-file-type.md)
- [File Type Verifier](file-type-verifier.md)
- [How to Use the File Type Verifier](how-to-use-the-file-type-verifier.md)
- [File Type Handlers](fa-file-extensions.md)
- [Programmatic Identifiers](fa-progids.md)
- [How to Register a File Type for a New Application](how-to-register-a-file-type-for-a-new-application.md)
- [Perceived Types](fa-perceivedtypes.md)
- [Association Arrays](fa-associationarray.md)

## Additional Resources

- Set Program Access and Computer Defaults (SPAD) is a Windows Control Panel which allows users with administrative privilege to set a machine default and hide or show an application. Media, Mail, Browser, Messenger and Java applications are examples of applications registered in SPAD. Set Your Default Programs (SYDP) is a Windows Control Panel, that works with limited privileges, and permits users to set a user default. Any application can register in SYDP. For information about SPAD and SYDP application registration, see [Guidelines for File Associations and Default Programs](appguide-fa-defpro.md), and [Set Program Access and Computer Defaults (SPAD)](cpl-setprogramaccess.md).
- For related conceptual background, see [Overview of Verbs and File Associations](fa-verbs.md).
- To create a Shell data store, see [Implementing the Basic Folder Object Interfaces](nse-implement.md).

For related reference documentation, see the following topics:

- To execute a verb on a Shell item, see the [**InvokeVerb**](folderitem-invokeverb.md) method.
- To retrieve a collection of verbs that can be executed on a Shell item, see the [**Verbs**](folderitem-verbs.md) method.
- For performing an operation on a specified file, see either the [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea) or [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) functions.
- For a list of default perceived types, see the [**PERCEIVED**](/windows/win32/api/shtypes/ne-shtypes-perceived) enumeration.
- To retrieves a file's perceived type based on its extension, see the [**AssocGetPerceivedType**](/windows/desktop/api/Shlwapi/nf-shlwapi-assocgetperceivedtype) function.

 

 



