---
title: Importing and Exporting Named Properties Through vCards
description: If the predefined MAPI schema is insufficient to meet the needs of a client application, that application typically extends the schema using named properties.
ms.assetid: 40638b23-e956-4fe8-b132-245c43df6890
keywords:
- address books
- Windows Address Book (WAB),vCards
- WAB (Windows Address Book),vCards
- vCards
- Windows Address Book (WAB),importing named properties
- Windows Address Book (WAB),exporting named properties
- WAB (Windows Address Book),importing named properties
- WAB (Windows Address Book),exporting named properties
- importing WAB named properties
- exporting WAB named properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Importing and Exporting Named Properties Through vCards

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](_wincontacts_entry_point).

 

If the predefined MAPI schema is insufficient to meet the needs of a client application, that application typically extends the schema using named properties. In order to enable the exchange of data stored in named properties, the vCard conversion engine in the WAB can be extended to import and export named-property data through vCards. At present, the engine is limited to handling only named properties of type PT\_TSTRING.

The following topics are discussed in this document.

-   [Named Property Information](#named-property-information)
-   [Importing and Exporting Named Properties](#importing-and-exporting-named-properties)

## Named Property Information

In order to import and export named-property data, the WAB needs three pieces of information for each named property:

1.  The GUID used by the client to identify its named properties.
2.  The 'NAMES' of the named properties.
3.  The non-standard vCard Type (or tag) used by the client application to identify its data in the vCard. (Non-standard tags are tags with the prefix "X-".)

For example, consider an application that uses custom named properties for a person's hometown and college. The identifying GUID used by the application is {25EF2AE0-2E08-11d1-9ABB-00A0C91F9C8B}, and the application uses two names for these properties: a long integer "8032" (for hometown) and the string "COLLEGE\_INFO" (for college). When a vCard is created or interpreted by the WAB, it imports (or exports) the hometown and college information from the corresponding named property.

## Importing and Exporting Named Properties

To import or export named properties, you must do the following:

1.  Define non-standard types to identify the vCard. For example, our hometown and college types could have the following type names:

    ```
    X-MICROSOFT-APP-HOMETOWN
    X-MICROSOFT-APP-COLLEGE
    ```

    

    Begin non-standard types with an "X-". To avoid conflicts with other named types, use the following format:

    ```
    X-<CompanyName>-<Three letter application-specific-prefix>-<Tag Name>
    ```

    

    Names must be 255 characters or fewer in length.

2.  Add the application's identifying GUID as a key under:
    ```
    HKEY_LOCAL_MACHINE\Software\Microsoft\WAB\WAB4\NamedVCardProps
    ```

    

3.  For each named property corresponding to the GUID, add the identifier for the named property under the GUID as a subkey. You can represent named properties as either a **LONG** or a string. See [MAPINAMEID](0099fa14-0929-4443-9dff-a8b10b95b1c0) for more information.

    If your named property is represented by a **LONG**, save it in the registry as a **DWORD** value. If the named property is represented as a string, save it in the registry as a STRING value. Use the type name ("X-...") for the subkey name, and the property name for the data.

If you have more than one GUID value, add them all as subkeys. For example:


```
HKEY_LOCAL_MACHINE\
    Software\
        Microsoft\
            WAB\
                WAB4\
                    NamedVCardProps
                        {GUID1}
                            "X-1.."=dword:0x0000xxxx
                            "X-2.."="descriptive string"
                        {GUID2}
                            "X-3.."=dword:0x0000xxxx
                            "X-4.."=dword:0x0000xxxx
```



For the example using "hometown" and "college", the .reg file for these settings would appear as follows:


```
REGEDIT4

[HKEY_LOCAL_MACHINE\Software\Microsoft\WAB\WAB4\NamedVCardProps\{25EF2AE0-2E08-11d1-9ABB-00A0C91F9C8B}]
"X-MICROSOFT-APP-HOMETOWN"=dword:00008032
"X-MICROSOFT-APP-COLLEGE"="COLLEGE_INFO"
```



The next time the WAB handles a vCard conversion, it will interpret these properties correctly from the registry. On export, data from these properties will be placed in the vCard. On import, these properties will be read from the vCard and the data stored in the correct named properties in the WAB.

Following the Hometown and College example, a vCard containing the properties in the previous sample will appear as follows:


```
BEGIN:VCARD
N:TestContact
X-MICROSOFT-APP-HOMETOWN:Seattle
X-MICROSOFT-APP-COLLEGE:University of Washington
END:VCARD
```



 

 




