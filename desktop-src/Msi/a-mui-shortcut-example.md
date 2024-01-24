---
description: This section describes how to add resource strings to the Windows Installer Shortcut table for use with Multilingual User Interfaces (MUI).
ms.assetid: f521cfb8-32a8-4b62-b258-5b99cc3e0416
title: A MUI Shortcut Example
ms.topic: article
ms.date: 05/31/2018
---

# A MUI Shortcut Example

This section describes how to add resource strings to the Windows Installer [Shortcut](shortcut-table.md) table for use with Multilingual User Interfaces (MUI).

**Windows Installer 2.0 and Windows Installer 3.0:** Not supported. This example requires Windows Installer 4.0.

Refer to the [Multilingual User Interface (MUI)](/windows/desktop/Intl/multilingual-user-interface) documentation for information on how to develop MUI-enabled applications .

To add the resource strings used by Windows Vista Multilingual User Interfaces to a Windows Installer package:

1.  Add the information for all the language-neutral and language files to the [File Table](file-table.md). For example, the files might consist of a language-neutral file (msimsg.dll) and language files for English (msimsgen.dll.mui), Japanese (msimsgja.dll.mui), and Chinese (msimsgcs.dll.mui). Each file can belong to a different component. Each file can have both a long and short file name. In the case of this example, the following information can be added to the [File Table](file-table.md).

    [File Table](file-table.md) (partial)

    

    | File        | Component\_     | FileName                     |
    |-------------|-----------------|------------------------------|
    | msimsgmuija | MSIMSG\_MUI\_JA | msimsgja.dll\|msimsg.dll.mui |
    | msimsgmuics | MSIMSG\_MUI\_CS | msimsgcs.dll\|msimsg.dll.mui |
    | msimsgmuien | MSIMSG\_MUI\_EN | msimsgen.dll\|msimsg.dll.mui |
    | msimsgdll   | MSIMSG          | msimsg.dll                   |

    

     

2.  Add information to the [Component table](component-table.md) for these components. Each component has a unique GUID identifier that should be entered into the ComponentId field of the Component table. The file belonging to the component can serve as the KeyPath for that component. The directory that contains each component can be specified in the Directory\_ field. The following information can be added to the Component table.

    [Component Table](component-table.md) (partial)

    

    | Component       | Directory\_   | KeyPath     |
    |-----------------|---------------|-------------|
    | MSIMSG\_MUI\_JA | MUIFolder\_JA | msimsgmuija |
    | MSIMSG\_MUI\_CS | MUIFolder\_CS | msimsgmuics |
    | MSIMSG\_MUI\_EN | MUIFolder\_EN | msimsgmuien |
    | MSIMSG          | MUIFolder     | msimsgdll   |

    

     

3.  Edit the [Directory](directory-table.md) table so that the components are installed into the correct directories. Be sure to include information about the directory where the shortcut will be installed. For example, the following information might be added to the Directory table of a package that installs the components and a shortcut located in the DesktopFolder directory.

    [Directory Table](directory-table.md) (partial)

    

    | Directory     | Directory\_Parent | DefaultDir |
    |---------------|-------------------|------------|
    | TARGETDIR     |                   | SourceDir  |
    | MsiTest       | TARGETDIR         | MsiTest:.  |
    | MUIFolder     | MsiTest           | MUI        |
    | MUIFolder\_CS | MUIFolder         | cs-CZ      |
    | MUIFolder\_EN | MUIFolder         | en-US      |
    | MUIFolder\_JA | MUIFolder         | ja-JP      |
    | DesktopFolder | TARGETDIR         | .          |

    

     

4.  Add a row to the [Shortcut](shortcut-table.md) table for each shortcut. For example, the [Shortcut](shortcut-table.md) table could contain the following information for two shortcuts, Quick1 and Quick2, installed into the DirectoryFolder directory. Each shortcut belongs to the feature specified in the Target field. The icon associated with the shortcut can be specified in the Icon\_ field and the [Icon](icon-table.md) table.

    [Shortcut Table](shortcut-table.md) (partial)

    

    | Shortcut | Directory\_   | Component\_ | Target               | Icon             |
    |----------|---------------|-------------|----------------------|------------------|
    | Quick1   | DesktopFolder | MSIMSG      | FeatureChild1\_Local | HelpFileIcon.exe |
    | Quick2   | DesktopFolder | MSIMSG      | FeatureChild1\_Local | HelpFileIcon.exe |

    

     

5.  Add information to the [Feature Table](feature-table.md) table for the feature owns shortcut belongs. When the shortcut is activated, the installer verifies that all the components belonging to this feature are installed before launching the key file of the component specified in the Component\_ column of the [Shortcut](shortcut-table.md) table. In the case of this example, the following information can be added to the Feature Table table for the FeatureParent1\_Local feature.

    [Feature Table](feature-table.md) (partial)

    

    | Feature               | Feature\_Parent       | Title                 | Attributes |
    |-----------------------|-----------------------|-----------------------|------------|
    | FeatureParent1\_Local |                       | FeatureParent1\_Local | 16         |
    | FeatureChild1\_Local  | FeatureParent1\_Local | FeatureParent1\_Local | 0          |

    

     

6.  For each new shortcut, add the resource string information to the DisplayResourceDLL, DisplayResourceId, DescriptionResourceDLL, and DescriptionResourceId fields of the [Shortcut table](shortcut-table.md). The DisplayResourceDLL and DescriptionResourceDLL fields contain the resource string in the [Formatted](formatted.md) string format. The formatted string can use the \[\#*filekey*\] convention of the [Formatted](formatted.md) format. Add the display and description indices for the resource strings in the DisplayResourceId and DescriptionResourceId fields.

    [Shortcut Table](shortcut-table.md) (partial)

    

    | Shortcut | DisplayResourceDLL | DisplayResourceId | DescriptionResourceDLL | DescriptionResourceId |
    |----------|--------------------|-------------------|------------------------|-----------------------|
    | Quick1   | \[\#msimsgdll\]    | 36                | \[\#msimsgdll\]        | 37                    |
    | Quick2   | \[\#msimsgdll\]    | 38                | \[\#msimsgdll\]        | 39                    |

    

     

7.  After installing the package, test to ensure that the Multilingual User Interface is working as expected.

 

 
