---
description: This topic explains how to create new file types and how to associate your app with your file type and other well-defined file types.
ms.assetid: 055648cd-46ce-4e61-80b2-bcf1d1823e20
title: File Types
ms.topic: article
ms.date: 05/31/2018
---

# File Types

This topic explains how to create new file types and how to associate your app with your file type and other well-defined file types. Files with a shared common file name extension (.doc, .html, and so on) are of the same *type*. For example, if you create a new text editor, then you can use the existing .txt file type. In other cases, you might need to create a new file type.

This topic is organized as follows:

- [Public and Private File Types](#public-and-private-file-types)
- [Registering a File Type](#registering-a-file-type)
    - [Setting Optional Subkeys and File Type Extension Attributes](#setting-optional-subkeys-and-file-type-extension-attributes)
    - [Deleting Registry Information During Uninstallation](#deleting-registry-information-during-uninstallation)
- [File Types That Support Open Metadata](#file-types-that-support-open-metadata)
- [Related topics](#related-topics)

Additional information can be found on the following topics:

- [How To Choose a File Type Extension](how-to-choose-a-file-type-extension.md)
- [How To Define File Type Attributes](./how-to-define-file-type-attributes.md)
- [How To Include an Application on the Open with Dialog Box](how-to-include-an-application-on-the-open-with-dialog-box.md)
- [How To Exclude an Application from the Open with Dialog Box for Unassociated File Types](how-to-exclude-an-application-from-the-open-with-dialog-box-for-unassociated-file-types.md)

## Public and Private File Types

Public file types are also known as popular or contentious types because competing applications might want to be associated with these file types. Characteristics of public file types include:

- They are typically defined by standards bodies, and/or are promoted by their defining organizations as interchange formats.
- They are often exchanged between computers and users for diverse purposes.
- They need to be supported on many different platforms.
- Applications from multiple vendors are likely to handle them.

Some examples of file types that are considered public are the image file types .png, .gif, .jpg, and .bmp, and the audio types .wav, .mp3, and .au.

Unlike public file types, private or proprietary file types typically have a format that is implemented and understood by only one application or vendor. As a result, private file types are typically not prone to conflicts between applications. Some file types can start as private file types but later become public file types.

> [!Note]  
> Windows does not differentiate between public and private file types. The distinction is relevant only in making decisions about your choice of file type registration.

 

## Registering a File Type

To associate the file type with an existing application, locate the application ProgID in the registry. To associate the file type with a new application, define a ProgID for your application. For information about defining a new ProgID, see [Programmatic Identifiers](fa-progids.md).

File name extension subkeys have the following general form: *extension*=*ProgID*. File name extension subkeys are stored in the **HKEY\_CLASSES\_ROOT** subtree.

It is important to include the leading period (.) when creating file type subkeys in the registry. For example, if you want a file type with the short extension .myp and the long extension .myp-file to be opened with an application called MyProgram, use the following syntax:

```
HKEY_CLASSES_ROOT
   .myp
      (Default) = ApplicationVendor.MyProgram
   .myp-file
      (Default) = ApplicationVendor.MyProgram
   ApplicationVendor.MyProgram
      (Default) = MyProgram Application
```

As demonstrated in the preceding example, if you also register a short file name extension (.myp), you should create a subkey for the long extension (.myp-file) as well. For more information, see [File Type Handlers](fa-file-extensions.md).

### Setting Optional Subkeys and File Type Extension Attributes

File type extension entries in the registry have several optional subkeys and attributes.

The file type extension entries that are used by file associations are described in the following table. All values are of the **REG\_SZ** type.



| Registry entry  | Action                                                                                                                                                                                                                                                                                                                             |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default         | Set the default value of the extension subkey to the ProgID to which it is linked.                                                                                                                                                                                                                                                 |
| Content Type    | Set the Content Type value to the file type's MIME content type.                                                                                                                                                                                                                                                                   |
| OpenWithList    | Do not use. This subkey contains one or more application subkeys for applications that appear in the **Open with** dialog box entry for the file type and is intended only for .exe applications on operating systems prior to Windows XP. Use OpenWithProgIds instead.                                                            |
| OpenWithProgIds | This subkey contains a list of alternate ProgIDs for this file type. The programs for these ProgIDs appear in the **Open with** menu and are available as default Windows Store apps for the file type. Whenever an application takes over this file type by changing the default value, it should also add an entry to this list. |
| PerceivedType   | Set the PerceivedType value to the PerceivedType to which the file belongs, if any. This string is not used by Windows versions prior to Windows Vista. For more information, see [Perceived Types and Application Registration](fa-perceivedtypes.md).                                                                           |



 

The general form of a file name extension subkey is as follows. All entry types are of the **REG\_SZ** type.

```
HKEY_CLASSES_ROOT
   .ext
      (Default) = ProgID.ext.1
      Content Type = MIME content type
      PerceivedType = PerceivedType
      OpenWithProgids
         ProgID2.ext.1
         ProgID3.ext.1
      ProgID.ext.1
         shellnew
```

Important considerations about file types include:

- The **HKEY\_CLASSES\_ROOT** subtree is a view formed by merging **HKEY\_CURRENT\_USER**\\**Software**\\**Classes** and **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Classes**
- In general, **HKEY\_CLASSES\_ROOT** is intended to be read from but not written to. For more information, see the [HKEY\_CLASSES\_ROOT](../sysinfo/hkey-classes-root-key.md) article.
- To register a file type globally on a particular computer, create an entry for the file type in the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Classes** subkey.
- To make a file type registration visible to the current user only, create an entry for the file type in the **HKEY\_CURRENT\_USER**\\**Software**\\**Classes** subkey.
- An application can provide its own implementation of a verb, such as open or play, as shown in the following registry example.

    ```
    HKEY_CLASSES_ROOT
       Applications
          ApplicationName.exe
             shell
                verb
    ```

    Subkeys of the verb subkey include the command line and the drop target method: **command** and **DropTarget**.

- When you create or change a file association, it is important to notify the system that you have made a change. Do so by calling [**SHChangeNotify**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotify) and specifying the **SHCNE\_ASSOCCHANGED** event. If you do not call **SHChangeNotify**, the change may not be recognized until after the system is rebooted.
- To retrieve registry information regarding a file association, use the [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) interface. For a scenario that illustrates this procedure, see [File Association Sample Scenario](fa-sample-scenarios.md).

> [!Note]  
> Both the **App Paths** and **Applications** registry subkeys are used to register and control the behavior of the system on behalf of applications. For more detailed information about this functionality, see [Application Registration](app-registration.md).

 

### Deleting Registry Information During Uninstallation

When uninstalling an application, the ProgIDs and most other registry information associated with that application should be deleted as part of the uninstallation. However, applications that have taken ownership of a file type (by setting the Default value of the file type's **HKEY\_CLASSES\_ROOT**\\*.extension* subkey to the ProgID of the application) should not attempt to remove that value when uninstalling. Leaving the data in place for the Default value avoids the difficulty of determining whether another application has taken ownership of the file type and overwritten the Default value after the original application was installed. Windows respects the Default value only if the ProgID found there is a registered ProgID. If the ProgID is unregistered, it is ignored.

Note that other file-type ownership information is stored in the **HKEY\_CURRENT\_USER** subtree and also is used only when the application that it references is registered. Therefore, this data does not need to be removed when uninstalling an application.

As an example, the following shows the state of the registry before an application is uninstalled:

```
HKEY_CLASSES_ROOT
   .mp3
      (Default) = YourProgID
   YourProgID
      shell
         open
            command
               (Default) = yourapp.exe %1
```

The following shows the state of those same registry entries after the application has been uninstalled.

```
HKEY_CLASSES_ROOT
   .mp3
      (Default) = YourProgID
   YourProgID subkey removed
```

## File Types That Support Open Metadata

In Windows 7 and later, the following file types support open metadata.



| File type                                                               | File name extensions                                          |
|-------------------------------------------------------------------------|---------------------------------------------------------------|
| Office 2007 Documents                                                   | .docx, .xlsx, .pptx                                           |
| Office 97-2003 Documents                                                | .doc, .xls, .ppt                                              |
| Saved Search                                                            | .search-ms                                                    |
| Windows Media-based formats (Advanced Streaming Format (ASF) container) | .wmv, .wma                                                    |
| MP4 (property handler)                                                  | .mp4, .m4a, .m4v, .mp4v, .m4p, .m4b, .3gp, .3gpp, .3gp2, .mov |



 

## Related topics

<dl> <dt>

[Application Registration](app-registration.md)
</dt> <dt>

[How File Associations Work](fa-how-work.md)
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

 

 
