---
description: An association array is an ordered list of registry locations used to store information about an item type, including handlers, verbs, and other attributes like the icon and display name of the type.
title: Association Arrays
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 9ECD19CA-833E-4565-A0EF-FB16BF7B3F44
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Association Arrays

An association array is an ordered list of registry locations used to store information about an item type, including handlers, verbs, and other attributes like the icon and display name of the type. The Shell uses association arrays to query a predefined set of registry locations that might contain information about a Shell item.

This topic is organized as follows:

- [About Association Arrays](#about-association-arrays)
- [Querying Association Arrays](#querying-association-arrays)
- [Working with Association Arrays for a Particular Shell Data Source](#working-with-association-arrays-for-a-particular-shell-data-source)
    - [Shell Data Source Association Arrays](#shell-data-source-association-arrays)
- [Additional Resources](#additional-resources)
- [Related topics](#related-topics)

## About Association Arrays

An association array is an ordered list of registry locations that contain information about an item type, including handlers, verbs, and other attributes such as the icon and display name of the type. This information about the item type can be registered at varying levels of specificity. For example, you can register a verb that will show up only for a specific file type (such as .jpg), or for all items with the same System.Kind (for example, System.kind = picture), or for all items.

The Shell uses association arrays to query a predefined set of registry locations that might potentially contain information about the item. The association array APIs can be used to retrieve from the registry subkey a single value that contains the requested information, with that value coming from the first entry in the array that provides it. For example, the default icon value is retrieved this way. The association array can also be used to retrieve a set of values that are stored in the registry subkeys. For example, the list of verbs is built from those verbs that are registered under all the subkeys.

After the Shell queries a predefined set of registry locations for information about a Shell item, it puts the registry locations into an array in order from the most specific location to the most general.

Because association arrays are ordered lists, they provide application developers with a mechanism for adding information to the registry that will be returned for a specific type of item. Likewise, association arrays permit application developers to add information to the registry for a specific group of items when those items are registered at a more general location. This logic informs your decision about the most appropriate location in the registry to store information about Shell items.

On a default Windows system a .jpg file has the following association array:

-   **HKEY\_CLASSES\_ROOT**\\**jpgfile**
-   **HKEY\_CLASSES\_ROOT**\\**SystemFileAssociations**\\**.jpg**
-   **HKEY\_CLASSES\_ROOT**\\**image**
-   **HKEY\_CLASSES\_ROOT**\\**\***
-   **HKEY\_CLASSES\_ROOT**\\**AllFilesystemObjects**

For information on registering association arrays, see [Application Registration](app-registration.md).

## Querying Association Arrays

There are Shell APIs to retrieve information from a range of registry subkeys, from the most specific registry subkey to a superset of the information across all registry subkeys.

The most common use of an association array is to query for a single value that the Shell returns from the most specific element in the array that has the requested information. The following code example shows how to do that.


```
IQueryAssociations *pqa;

// pShellItem is assumed to be an existing IShellItem object.
hr = pShellItem->BindToHandler(NULL, BHID_AssociationArray, IID_PPV_ARGS(&pqa));
if (SUCCEEDED(hr))
{
    wchar_t szValue[256];
    DWORD cbValue = sizeof(szValue);      // Count of bytes in the array

    hr = pqa->GetData(0, ASSOCDATA_VALUE, L"InfoTip", szValue, &cbValue);
    if (SUCCEEDED(hr))
    {
        // The "InfoTip" value is used to compute the infotip string from
        // properties of an item.
    }
    pqa->Release();
}
```



The following APIs can be used to query an association array or to construct an association array [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) object that can be queried:

- [**AssocCreate**](/windows/desktop/api/Shlwapi/nf-shlwapi-assoccreate) (prior to Windows Vista)
- [**AssocCreateForClasses**](/windows/desktop/api/Shellapi/nf-shellapi-assoccreateforclasses)
- [**AssocQueryString**](/windows/desktop/api/Shlwapi/nf-shlwapi-assocquerystringa)

## Working with Association Arrays for a Particular Shell Data Source

Each Shell data source defines the association array for its items. Defining an association array is usually a function of the type of item. Shell data source implementers should define and document the association arrays to enable applications to extend the behavior of those types, such as for registering verbs or other information. Applications can extend the behavior of items based on adding data to the association array subkeys, such as adding verbs for items.

The file system data source builds an association array for files based on the following registry subkeys and special ProgIDs:

-   If the file has a registered ProgID, **HKEY\_CLASSES\_ROOT**\\*ProgID* is used. Otherwise **HKEY\_CLASSES\_ROOT**\\**Unknown** is used.
-   The file name extension is registered under **HKEY\_CLASSES\_ROOT**\\**SystemFileAssociations**\\*.fileExtension* subkey.
-   Special ProgIDs are shown in the following table. 

    | Special progID                                    | Description                   |
    |---------------------------------------------------|-------------------------------|
    | **HKEY\_CLASSES\_ROOT**\\**\***                   | All files (non-folders)       |
    | **HKEY\_CLASSES\_ROOT**\\**AllFilesystemObjects** | Files and file system folders |
    | **HKEY\_CLASSES\_ROOT**\\**Directory**            | File system folders           |
    | **HKEY\_CLASSES\_ROOT**\\**Folder**               | Shell containers              |

    

     

### Shell Data Source Association Arrays

The following list represents some of the Shell data store association arrays that can be used for the purposes described in this topic:

-   **HKEY\_CLASSES\_ROOT**\\**\***
-   **HKEY\_CLASSES\_ROOT**\\**AllFilesystemObjects**
-   **HKEY\_CLASSES\_ROOT**\\**Kind.Document**
-   **HKEY\_CLASSES\_ROOT**\\**Results**
-   **HKEY\_CLASSES\_ROOT**\\**SystemFileAssociations**\\**.docx**
-   **HKEY\_CLASSES\_ROOT**\\**Word.Document.12**

Shell data source association arrays that can be used for DBFolder (a Shell data store that represents items in search results and query-based views) are as follows:

-   Drives
-   Network
-   RegItems
-   Examples:
    -   ContentView
    -   Verbs

Other common association arrays include Folder and Printers.

## Additional Resources

-   To create a Shell data store, see [Implementing the Basic Folder Object Interfaces](nse-implement.md).

## Related topics

<dl> <dt>

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

[Programmatic Identifiers](fa-progids.md)
</dt> <dt>

[Perceived Types](fa-perceivedtypes.md)
</dt> </dl>

 

 
