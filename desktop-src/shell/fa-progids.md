---
description: The Shell uses a programmatic identifier (ProgID) registry subkey to associate a file type with an application, and to control the behavior of the association.
ms.assetid: f2b666d6-bf22-47b5-87e1-8de5ff51c152
title: Programmatic Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Programmatic Identifiers

The Shell uses a programmatic identifier (ProgID) registry subkey to associate a file type with an application, and to control the behavior of the association. The ProgID entries used for file associations are located under **HKEY\_CLASSES\_ROOT** in the registry.

This topic is organized as follows:

- [Programmatic Identifier Elements Used by File Associations](#programmatic-identifier-elements-used-by-file-associations)
- [Using Versioned Programmatic Identifiers](#using-versioned-programmatic-identifiers)
- [Related topics](#related-topics)

For additional information, read [How To Register a File Type for a New Application](how-to-register-a-file-type-for-a-new-application.md)

## Programmatic Identifier Elements Used by File Associations

The proper format of a ProgID key name is \[*Vendor or Application*\].\[*Component*\].\[*Version*\], separated by periods and with no spaces, as in Word.Document.6. The *Version* portion is optional but strongly recommended. For more information, see [Using Versioned Programmatic Identifiers](#using-versioned-programmatic-identifiers).

A ProgID subkey should include the following elements. Note that some string data in this key requires specific formatting.




| Element | Description | 
|---------|-------------|
| <strong>(Default)</strong> | Set the default entry of the ProgID subkey to a friendly name for that ProgID, suitable to display to the user. The use of this entry to hold the friendly name is deprecated by the FriendlyTypeName entry on systems running Windows 2000 or later. However, you should set this value for backward compatibility.<br /> | 
| <strong>AllowSilentDefaultTakeOver</strong> (introduced in Windows 8) | Set this optional entry to signal that Windows should ignore this ProgID when determining a default handler for a public file type. Regardless of whether this value is set, the ProgID continues to appear in the OpenWith shortcut menu and dialog. This is a REG_NONE value. | 
| <strong>AppUserModelID</strong> (introduced in Windows 7) | Set this optional entry to the application's explicit Application User Model ID (AppUserModelID) if the application uses an explicit AppUserModelID and uses either the system's automatically generated <strong>Recent</strong> or <strong>Frequent</strong> Jump Lists or provides a custom Jump List. If an application uses an explicit AppUserModelID and does not set this value, items will not appear in that application's Jump Lists. This is a REG_SZ string. For more information, see <a href="appids.md">Application User Model IDs (AppUserModelIDs)</a>.<br /> | 
| <strong>EditFlags</strong> | Set this optional entry using flags from the <a href="/windows/desktop/api/Shlwapi/ne-shlwapi-filetypeattributeflags"><strong>FILETYPEATTRIBUTEFLAGS</strong></a> enumeration. The EditFlags entry controls some aspects of the Shell's handling of the file types linked to this ProgID. You can also use the EditFlags entry to limit how much the user can modify certain aspects of these file types using a file's property sheet. The <strong>FILETYPEATTRIBUTEFLAGS</strong> values used for EditFlags are binary values designed so that you can combine multiple attributes into a single value in a bitwise OR operation. This is a REG_DWORD or REG_BINARY value.<br /> | 
| <strong>FriendlyTypeName</strong> | Set this entry to a friendly name for the ProgID, suitable to display to the user. For consistency, this string should contain the same data as the Default entry for this ProgID key. This entry can be either a REG_SZ or REG_EXPAND_SZ string, but it must be formatted as an indirect string (a fully qualified file name and resource value preceded by the @ symbol), for instance <em>@%SystemRoot%\shell32.dll,-154</em>.<br /> | 
| <strong>InfoTip</strong> | Set this entry to a brief help message that the Shell displays for this ProgID. The InfoTip entry displays in a mouse-over dialog box. This value can be either a REG_SZ or REG_EXPAND_SZ string but, like FriendlyTypeName, it must be formatted as an indirect string.<br /> | 
| <strong>CurVer</strong> | Set the (Default) entry of this subkey to the most current version of this ProgID.<br /><blockquote>[!Note]<br />Unless you have side-by-side application versions, that is, multiple versions installed on the same system, you should avoid using <strong>CurVer</strong>.</blockquote><br /> | 
| <strong>DefaultIcon</strong>. | Set the (Default) entry of this subkey to the default icon that you want to display for file types associated with this ProgID. This value can be either a REG_SZ or REG_EXPAND_SZ string, but it must be provided as a fully qualified file name with its attendant resource value, for instance <em>%SystemRoot%\shell32.dll,-154</em>.<br /> | 




 

The following registry key example illustrates a file association ProgID key node:

```
HKEY_CLASSES_ROOT
   Vendor.App.1
      (Default) = My Friendly Name
      AllowSilentDefaultTakeOver
      AppUserModelID = Vendor.Application
      EditFlags = 0x00000001
      FriendlyTypeName = @%SystemRoot%\shell32.dll,-154
      InfoTip = @%SystemRoot%\shell32.dll,-54
      CurVer
         (Default) = Vendor.App.1
      DefaultIcon
         (Default) = %SystemRoot%\shell32.dll,-1
```

## Using Versioned Programmatic Identifiers

A versioned ProgID is one whose version is indicated in its name. You typically do this by adding a period and the version number to the name. For example:

-   Word.Document.6
-   Word.Document.8

These are versioned ProgIDs, with versions 6 and 8 respectively. If you have a side-by-side application, that is, one that supports multiple versions of your application installed at the same time, then use CurVer and Version Independent ProgIDs. Otherwise, CurVer and Version Independent ProgIDs should be avoided because they will lead to inefficiency.

## Related topics

<dl> <dt>

[How To Register a File Type for a New Application](how-to-register-a-file-type-for-a-new-application.md)
</dt> <dt>

[Application Registration](app-registration.md)
</dt> <dt>

[File Types](fa-file-types.md)
</dt> <dt>

[How File Associations Work](fa-how-work.md)
</dt> <dt>

[Content View By File Type or Kind](prophand-content-view.md)
</dt> <dt>

[File Type Verifier](file-type-verifier.md)
</dt> <dt>

[File Type Handlers](fa-file-extensions.md)
</dt> <dt>

[Perceived Types](fa-perceivedtypes.md)
</dt> <dt>

[Association Arrays](fa-associationarray.md)
</dt> </dl>

 

 




