---
Description: This topic explains how to create and register property handlers to work with the Windows property system.
ms.assetid: E583A00B-F615-41c8-AECF-061F1396DB9A
title: Property Handler Best Practices and FAQ
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Property Handler Best Practices and FAQ

This topic explains how to create and register property handlers to work with the Windows property system.

This topic is organized as follows:

-   [Best Practices](#property-handler-best-practices-and-faq)
    -   [Overriding File System Properties](#overriding-file-system-properties)
    -   [Storing Properties in XML-based File Formats](#storing-properties-in-xml-based-file-formats)
    -   [Computed Properties](#computed-properties)
-   [Frequently Asked Questions](#property-handler-best-practices-and-faq)
-   [Related topics](#related-topics)

## Best Practices

The best practices outlined here provide useful implementation tips.

### Overriding File System Properties

Some properties for files are provided by the file system data source, such as:

-   PKEY\_FileName
-   PKEY\_Extension
-   PKEY\_ModifiedTime

In general, property handlers cannot provide values for these properties. However, in some cases these properties can be overridden based on registration information provided by the property handler. Property handlers populate **HKEY\_CLASSES\_ROOT**\\**CLSID**\\*{handler clsid}*\\**OverrideFileSystemProperties** with the names of properties that they want to override. This is limited to a fixed set of properties shown in the following list of which the system has knowledge.

Overriding is supported for the following property values:

-   [System.Kind](https://www.bing.com/search?q=System.Kind)
-   [System.FileName](https://www.bing.com/search?q=System.FileName)
-   [System.IsPinnedToNameSpaceTree](https://www.bing.com/search?q=System.IsPinnedToNameSpaceTree)
-   [System.ItemNameDisplay](https://www.bing.com/search?q=System.ItemNameDisplay)
-   [System.SFGAOFlags](https://www.bing.com/search?q=System.SFGAOFlags)
-   [System.ItemPathDisplay](https://www.bing.com/search?q=System.ItemPathDisplay)
-   [System.ItemPathDisplayNarrow](https://www.bing.com/search?q=System.ItemPathDisplayNarrow)
-   [System.ItemFolderNameDisplay](https://www.bing.com/search?q=System.ItemFolderNameDisplay)
-   [System.ItemFolderPathDisplay](https://www.bing.com/search?q=System.ItemFolderPathDisplay)
-   [System.ItemFolderPathDisplayNarrow](https://www.bing.com/search?q=System.ItemFolderPathDisplayNarrow)

For a full list of all Shell properties, see [Shell Properties](https://www.bing.com/search?q=Shell Properties).

> \[!Important\]  
> The overridden property values are used only when the files are indexed. Thus, browsing files from the file system data source does not reveal the overridden values.

 

### Storing Properties in XML-based File Formats

There are two basic options available for storing properties in XML-based file formats:

-   Store each property using XML elements and attributes according to the XML schema of the document. This approach is more "XML friendly".
-   Serialize the entire property store into a memory Binary large object (BLOB), convert the BLOB into a base64-encoded string, and then store that string in the XML. This is the simpler of the two approaches and can be used to trivially provide support for open metadata.

Some handlers might combine these approaches, storing some important values in standard XML format and storing the rest in a BLOB, for example.

### Computed Properties

Some properties are derived from specific attributes of a file. For example, the [System.Image.Dimensions](https://www.bing.com/search?q=System.Image.Dimensions) property is determined by the actual dimensions of the image in an image file. Because such property values cannot be changed by the property handler, they are thus marked `isInnate="true"` in the property description. Other properties are computed from a part of a specific property or by aggregating the values of multiple properties. Because updates to these "computed" properties would create ambiguity as to how the "source" values should be changed, computed properties should be marked `isInnate="true"` in the property description or reported as read-only. The latter option is available by instructing the handler to return S\_FALSE from [**IPropertyStoreCapabilities::IsPropertyWritable**](https://www.bing.com/search?q=**IPropertyStoreCapabilities::IsPropertyWritable**).

## Frequently Asked Questions

This section provides answers to frequently asked questions about properties and property handlers, and accompanying answers.

-   **Question:** Why isn't my property handler being loaded by the Windows Search indexer?

    The Windows Search indexer runs as a system service and cannot load DLLs that are stored in the user profile directory. If you are building and debugging using Microsoft Visual Studio, it will place the DLL in your user profile (and therefore it won't be loaded by the indexer). To work around this, copy your DLL outside of your profile folder (for example, into **C:\\Program Files\\YourAppName**) and register it there.

    For more specific guidance on developing property handlers to work with the Windows Search indexer, see [Developing Property Handlers for Windows Search](https://msdn.microsoft.com/windows/desktop/b475329a-1ed7-43a4-8e11-3700889a4ce9).

-   **Question:** Which properties should be discoverable through the [**IPropertyStore::GetCount**](https://www.bing.com/search?q=**IPropertyStore::GetCount**) and [**IPropertyStore::GetAt**](https://www.bing.com/search?q=**IPropertyStore::GetAt**) enumeration methods?

    Not all clients of property store objects use these methods. Some clients are aware of the properties they plan to request directly (by PKEY name), or receive property information through a property description list. The property discovery methods suppport several other scenarios. If a property does not need to participate in these scenarios, it does not need to be enumerated. Hence, a property handler can produce a non-VT\_EMPTY value for properties that are not discovered through the [**IPropertyStore::GetCount**](https://www.bing.com/search?q=**IPropertyStore::GetCount**) and [**IPropertyStore::GetAt**](https://www.bing.com/search?q=**IPropertyStore::GetAt**) methods.

    However, properties should be visible via these methods if any of the following conditions are met:

    -   **If the property is indexed so that it is searchable:** This means it is included in the Windows Search property store (denoted by `isColumn = "true"` in the property description schema) or available for full text searches (`inInvertedIndex = "true"`). In the absence of these flags or the absence of a property description, properties of type "string" will be added automatically to the inverted index to enable searching. Because the list of known properties (those with installed property descriptions) in the property system is very large (more than 800 properties), it would be impractical to ask every property handler for every property registered in the property system. Instead, the indexing process enumerates the relevant properties from the property handler for each item it indexes, and it uses the values of the enumerated properties to build the full text index.
    -   **If the property should be copied when the item's property set is duplicated:** To implement a "copy a property set" function, the source item makes the properties that should be copied visible through the [**IPropertyStore::GetCount**](https://www.bing.com/search?q=**IPropertyStore::GetCount**) and [**IPropertyStore::GetAt**](https://www.bing.com/search?q=**IPropertyStore::GetAt**) methods. Properties that do not need to be copied or do not make sense being copied should not be included.
    -   **If the property value is not empty (VT\_EMPTY):** Property values that are empty are not useful for clients. When clients attempt to return empty property values, a value of VT\_EMPTY is returned. Thus, properties with empty values should not be enumerated.
    -   **If the property should be removed when invoking the "remove properties" function:** This feature exists to protect privacy; it discovers all values from the property handler through enumeration and removes each one selected for removal by the user.
        > [!Note]  
        > Enumerating properties does not communicate the set of properties that a particular property handler supports if the handler supports a fixed schema (and not open metadata). Instead, such handlers should document the set of properties that they support.

         

-   **Question:** How do I know which file formats support open metadata?

    For information about support for open metadata, see "File Types that Support Open Metadata" in [File Types](https://msdn.microsoft.com/windows/desktop/055648cd-46ce-4e61-80b2-bcf1d1823e20).

-   **Question:** Can VT\_NULL values be stored using a property handler?

    No. VT\_NULL values will be converted to VT\_EMPTY on calls to [**IPropertyStore::GetValue**](https://www.bing.com/search?q=**IPropertyStore::GetValue**) and [**IPropertyStore::SetValue**](https://www.bing.com/search?q=**IPropertyStore::SetValue**).

-   **Question:** Which date string formats are supported by the [**PropVariantChangeType**](https://www.bing.com/search?q=**PropVariantChangeType**) function?

    Generally, properties that represent date/time values should be represented using VT\_FILETIME. However, many data sources provide this information in string form. The [**PropVariantChangeType**](https://www.bing.com/search?q=**PropVariantChangeType**) helper API supports coercing some string date formats into [**FILETIME**](https://msdn.microsoft.com/windows/desktop/9baf8a0e-59e3-4fbd-9616-2ec9161520d1) values, as shown in the following table.

    

    | Format                  | Windows Vista, Windows XP, and Microsoft Windows Desktop Search (WDS) | Windows 7 | Notes                                                                                                                                                                                                 |
    |-------------------------|-----------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | yyyy/mm/dd:hh:mm:ss.uuu | Yes                                                                   | Yes       | UTC; y=year, m=month, d=date, h=hours (24-hour clock), m=minutes, s=seconds, u=microseconds                                                                                                           |
    | yyyy-mm-ddThh:mm:ssZ    | No                                                                    | Yes       | **ISO8601 format specification**UTC (denoted by 'Z' time zone indicator); y=year, m=month, d=date, h=hours (24-hour clock), m=minutes, s=seconds; 'T' is a delimiter for the time portion.<br/> |

    

     

-   **Question:** Is it possible to create a read-only property handler?

    Yes. Some property handler implementations do not support writing of property values. These property handlers should return STGM\_E\_ACCESSDENIED on calls to **IInitializeXXX::Initialize** that pass STGM\_READWRITE, or on any call to [**IPropertyStore::SetValue**](https://www.bing.com/search?q=**IPropertyStore::SetValue**).

    All property handlers opened in STGM\_READ mode should return STGM\_E\_ACCESSDENIED on calls to [**IPropertyStore::SetValue**](https://www.bing.com/search?q=**IPropertyStore::SetValue**).

-   **Question:** Can a property handler treat a property as read-only, even if the schema indicates that the property is writeable?

    Yes. In the schema system, properties are annotated as read-only (including those with `isInnate = "true"`) or read/write. Property handlers that do not support writing a particular property that the schema says should be writeable should implement [**IPropertyStoreCapabilities**](https://www.bing.com/search?q=**IPropertyStoreCapabilities**) and return S\_FALSE on calls to [**IPropertyStoreCapabilities::IsPropertyWritable**](https://www.bing.com/search?q=**IPropertyStoreCapabilities::IsPropertyWritable**) for that property. This indicates that in the context of this handler and this file, the property is not writeable.

    > [!Note]  
    > The reverse action is not possible. You cannot enable a property handler to write a property that is marked as read-only in the schema

     

## Related topics

<dl> <dt>

[Understanding Property Handlers](https://www.bing.com/search?q=Understanding Property Handlers)
</dt> <dt>

[Using Kind Names](https://www.bing.com/search?q=Using Kind Names)
</dt> <dt>

[Using Property Lists](https://www.bing.com/search?q=Using Property Lists)
</dt> <dt>

[Initializing Property Handlers](https://www.bing.com/search?q=Initializing Property Handlers)
</dt> <dt>

[Registering and Distributing Property Handlers](https://www.bing.com/search?q=Registering and Distributing Property Handlers)
</dt> </dl>

 

 




