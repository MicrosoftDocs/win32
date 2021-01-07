---
description: Microsoft Windows Search uses property handlers to extract the values of properties from items and uses the property system schema to determine how a specific property should be indexed.
ms.assetid: b475329a-1ed7-43a4-8e11-3700889a4ce9
title: Developing Property Handlers for Windows Search
ms.topic: article
ms.date: 05/31/2018
---

# Developing Property Handlers for Windows Search

Microsoft Windows Search uses property handlers to extract the values of properties from items and uses the property system schema to determine how a specific property should be indexed. To read and index property values, property handlers are invoked out-of-process by Windows Search to improve security and robustness. In contrast, property handlers are invoked in-process by Windows Explorer to read and write property values.

This topic supplements the [Property System](../properties/building-property-handlers.md) topic with information specific to Windows Search and contains the following sections:

-   [Design Decisions for Property Handlers](#design-decisions-for-property-handlers)
    -   [Property Decisions](#property-decisions)
    -   [Full-Text Support](#full-text-support)
    -   [Operating System Implementatation Considerations](#operating-system-implementatation-considerations)
-   [Writing Property Description Files](#writing-property-description-files)
-   [Implementing Property Handlers](#implementing-property-handlers)
    -   [IInitializeWithStream](#iinitializewithstream)
    -   [IPropertyStore](#ipropertystore)
    -   [IPropertyStoreCapabilities](#ipropertystorecapabilities)
-   [Ensuring Your Items Get Indexed](#ensuring-your-items-get-indexed)
-   [Installing and Registering Property Handlers](#installing-and-registering-property-handlers)
-   [Testing and Troubleshooting Property Handlers](#testing-and-troubleshooting-property-handlers)
    -   [Installation and Setup Tests](#installation-and-setup-tests)
    -   [Troubleshooting Property Handlers](#troubleshooting-property-handlers)
-   [Using System-Supplied Property Handlers](#using-system-supplied-property-handlers)
-   [Related topics](#related-topics)

 

## Design Decisions for Property Handlers

Implementing property handlers involves the following steps:

1.  Making design decisions regarding the properties you want to support.
2.  Creating a Property Description (.propdesc) file for properties not already in the property system.
3.  Implementing and testing the property handler.
4.  Installing and registering the property handler and property description files.
5.  Testing property handler installation and registration.

Before you begin, you need to consider the following design questions:

-   What properties does/should the file format support?
-   Are these properties already in the System schema?
-   Can I use an existing system-supplied property handler?
-   Which properties can be displayed to end users?
-   Which properties can users edit?
-   Should support for full-text search come from a property handler or a filter?
-   Do I need to support legacy applications? If so, what do I implement?

> [!Note]  
> Before continuing, see [Using System-Supplied Property Handlers](#using-system-supplied-property-handlers) to see if you can use a system-supplied property handler, saving you both time and development resources.

 

After you have made these decisions, you can write formal descriptions of your custom properties so that the Windows Search engine can begin indexing your files and properties. These formal descriptions are XML files, described in [Property Description Schema](/previous-versions//cc144127(v=vs.85)).

### Property Decisions

When considering which properties to support, you should identify your users' indexing and searching needs. For example, you may be able to identify one hundred potentially useful properties for your file type, but users may be interested in searching on only a handful. Furthermore, you may want to display a different, larger or smaller, group of those properties to users in Windows Explorer, and allow users to edit only a subset of those properties displayed.

Your file type can support any custom properties you define, as well as a set of system-defined properties. Before you create a custom property, please review [System Properties](https://msdn.microsoft.com/library/bb763010(VS.85).aspx) to see if the property you want to support is already defined by a system property. Always be sure you support the most important system-defined properties.

We recommend using a matrix to help you design your properties:



| Property name | Is indexable? | Is displayable? | Is editable? |
|---------------|---------------|-----------------|--------------|
| property1     | Y             | Y               | N            |
| property...   | Y             | Y               | N            |
| propertyn     | N             | N               | N            |



 

For each of these properties, you need to determine what attributes it should have and then describe them formally in Property Description XML files (.propdesc). Attributes include the property's data type, label, help string and more. For indexable properties, you should pay particular attention to the following property attributes found in the [searchInfo](../properties/propdesc-schema-searchinfo.md)   XML element of the Property Description file.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>inInvertedIndex</td>
<td>Optional. Indicates whether a string property value should be broken into words and each word stored in the inverted index. The inverted index enables efficient searching for words and phrases over the property value using CONTAINS or FREETEXT (for example, SELECT ... WHERE CONTAINS &quot;sometext&quot;). If set to <strong>FALSE</strong>, searches are done against the whole string. Most string properties should have this set to <strong>TRUE</strong>; non-string properties should have this set to <strong>FALSE</strong>. The default is <strong>FALSE</strong>.</td>
</tr>
<tr class="even">
<td>isColumn</td>
<td>Optional. Indicates whether the property should be stored in the Windows Search database as a column. Storing the property as a column enables retrieving, sorting, grouping, and filtering (that is, using any predicate except CONTAINS or FREETEXT) on the whole column value. Properties displayed to the user should have this set to <strong>TRUE</strong> unless it is a very large textual property (like the body of a document) that would be searched in the inverted index. The default is <strong>FALSE</strong>.</td>
</tr>
<tr class="odd">
<td>isColumnSparse</td>
<td>Optional. Indicates whether a property takes no space if the value is <strong>NULL</strong>. A non-sparse property takes space for every item, even if the value is <strong>NULL</strong>. If the property is multi-valued, this attribute is always <strong>TRUE</strong>. This attribute should be <strong>FALSE</strong> only if a value is present for every item. The default is <strong>TRUE</strong>.</td>
</tr>
<tr class="even">
<td>columnIndexType</td>
<td>Optional. To optimize querying, the Windows Search engine can create secondary indices for properties that have isColumn=<strong>TRUE</strong>. This requires more processing and disk space during indexing, but improves performance during querying. If the property tends to be sorted, grouped, or filtered (that is, using =, !=, <, >, LIKE, MATCHES) frequently by users, this attribute should be set to &quot;OnDisk&quot;. The default is &quot;NotIndexed&quot;. The following values are valid:
<ul>
<li>NotIndexed: No secondary index is created.</li>
<li>OnDisk: Create and store a secondary index on disk.</li>
</ul></td>
</tr>
<tr class="odd">
<td>maxSize</td>
<td>Optional. Indicates the maximum size allowed for the property value stored in the Windows search database. This limit applies to the indvidual elements of a vector, not the vector as a whole. Values beyond this size are truncated. The default is &quot;128&quot; (bytes).<br/> Currently, Windows Search does not use the maxSize when calculating the amount of data it accepts from a file. Instead, the limit Windows Search uses is the product of the size of the file and the MaxGrowFactor (file size N * MaxGrowFactor) read from the registry at HKEY_LOCAL_MACHINE->Software->Microsoft->Windows Search->Gathering Manager->MaxGrowFactor. The default MaxGrowFactor is four (4). Consequently, if your file type tends to be small in total size but have larger properties, Windows Search may not accept all the property data you want to emit. However, you can increase the MaxGrowFactor to suit your needs. <br/></td>
</tr>
</tbody>
</table>



 

> [!Note]  
> For the columnIndexType attribute, the benefit of faster queries needs to be weighed against the greater indexing time and space costs that the secondary indices can incur. However, this cost is only paid for items that have a non-**null** value, so for most properties can have this attribute set to "OnDisk".

 

### Full-Text Support

Generally speaking, full-text search is supported by components called [filters](-search-3x-wds-extidx-filters.md); however, for text-based file types with uncomplicated file formats, property handlers may be able to provide this functionality with less development effort. You should review the [Full-Text Contents](../properties/building-property-handlers-property-handlers.md) section for a comparison of filter and property handler functionality to help you decide what is best for your file type. Of particular importance is the fact that filters can handle multiple language code identifiers (LCIDs) per file while property handlers cannot.

> [!Note]  
> Because property handlers cannot chunk content the way filters can, large files (even if they are uncomplicated file formats) must be completely loaded into memory.

 

### Operating System Implementatation Considerations

### Implementation Information for Windows 7

In Windows 7 and later, there is new behavior when registering a property handler, [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter), or new extension. When a new property handler and/or **IFilter** is installed, files with the corresponding extensions are automatically reindexed.

In Windows 7 it is recommended that an [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) is installed in conjunction with its corresponding property handlers, and that the **IFilter** is registered before the property handler. The registration of the property handler initiates immediate re-indexing of previously indexed files without first requiring a reboot, and takes advantage of any previously registered IFilter(s) for the purpose of content indexing.

If only an [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) is installed, without a corresponding property handler, then automatic reindexing occurs either after a restart of the indexing service, or a reboot of the system.

For property description flags specific to Windows 7, see the following reference topics:

-   [GETPROPERTYSTOREFLAGS](/windows/win32/api/propsys/ne-propsys-getpropertystoreflags)
-   [PROPDESC\_COLUMNINDEX\_TYPE](/windows/win32/api/propsys/ne-propsys-propdesc_columnindex_type)
-   [PROPDESC\_SEARCHINFO\_FLAGS](/windows/win32/api/propsys/ne-propsys-propdesc_searchinfo_flags)

### Implementation Information for Windows Vista and Earlier

Prior to Windows Vista, filters provided support for parsing and enumerating file content and properties. With the introduction of the property system, property handlers handle file properties while filters handle file content. For Windows Vista, you need develop only a partial implementation of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter)interface in coordination with a property handler, as described in [Best Practices for Creating Filter Handlers in Windows Search](-search-3x-wds-extidx-filters.md).

While the property system is also included with the Windows Search installation for Windows XP, third-party and legacy applications may require that filters handle both content and properties. Therefore, if you are developing on the Windows XP platform, you should provide a full filter implementation as well as a property handler for your file type or custom property.

 

## Writing Property Description Files

The structure of property description XML files (.propdesc) is described in the [propertyDescription](../properties/propdesc-schema-propertydescription.md) topic. Of particular interest for search are the attributes of the [searchInfo](../properties/propdesc-schema-searchinfo.md) element. Once you've decided which properties to support, you need to create and register property description files for each properties. When you register your .propdesc files, they are included in the schema's property description list and become column names within the Search engine's property store.

You can register your custom property descriptions using the [PSRegisterPropertySchema](/windows/win32/api/propsys/nf-propsys-psregisterpropertyschema) function, a wrapper API that calls the schema subsystem's IPropertySystem::RegisterPropertySchema. This function informs the schema subsystem of the addition of property description schema (.propdesc) files, using file path(s) to the .propdesc file(s) on the local machine, usually the application's install directory under "Program Files". Typically, a setup or application (for example, your property handler installer) will call this method after installing the .propdesc file(s).

 

## Implementing Property Handlers

Developing a property handler involves implementing the following interfaces:

-   IInitialzeWithStream: Provides stream-based initialization of your property handler.
-   IPropertyStore: Enumerates, gets, and sets property values.
-   IPropertyStoreCapabilities: Optional. Identifies whether users can edit a property from a user interface.

### IInitializeWithStream

As described in the [Property System](../properties/building-property-handlers.md) topic, we strongly recommend implementing property handlers with **IInitializeWithStream** to do stream-based initialization. If you chose not to implement IInitializeWithStream, the property handler must opt out of running in the isolation process by setting the DisableProcessIsolation flag on the property handler's registry key. Disabling process isolation is generally intended only for legacy property handlers and should be strenuously avoided by any new code.

### IPropertyStore

To create a property handler, you must implement the [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) interface with the following methods.



| Method   | Description                                                         |
|----------|---------------------------------------------------------------------|
| Commit   | Saves a property change to the file.                                |
| GetAt    | Retrieves a property key from an item's array of properties.        |
| GetCount | Gets the number of properties attached to the file.                 |
| GetValue | Retrieves data for a specific property.                             |
| SetValue | Sets a new property value or replaces or removes an existing value. |



 

 

 

Important considerations for implementing this interface are included in the [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) documentation.

> [!Note]  
> If your property handler emits multiple values for the same property for a given item, only the last value emitted is stored in the catalog.

 

 

### IPropertyStoreCapabilities

Property handlers can optionally implement this interface to disable a user's ability to edit specific properties. These properties are normally editable in the Details page and pane but editing them is not allowed under the implementing property handler. Implementing this interface correctly provides a better user experience than the alternative—a simple run-time error from the Shell.

 

## Ensuring Your Items Get Indexed

Now that you've implemented your property handler, you want to make sure the items your handler is registered for get indexed. You can use the [Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md) to initiate re-indexing, and you can also use the [Crawl Scope Manager](-search-3x-wds-extidx-csm.md) to set up default rules indicating the URLs you want the Indexer to crawl. Another option is to follow the ReIndex code sample in the [Windows Search SDK Samples](https://www.microsoft.com/downloads/details.aspx?FamilyID=645300AE-5E7A-4CE7-95F0-49793F8F76E8).

For further information, refer to [Using the Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md) and [Using the Crawl Scope Manager](-search-3x-wds-extidx-csm.md).

 

## Installing and Registering Property Handlers

With the property handler implemented, it must be registered and its file name extension associated with the handler. The following example shows the registry keys and values required to do this.

```
HKEY_CLASSES_ROOT
   CLSID
      {<CLSID for property handler>}
         (Default) = <Property Handler Name>
         InProcServer32
            (Default) = <full path to property handler dll>
            ThreadingModel = <your threading model>
```

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               PropertySystem
                  PropertyHandlers
                     <.fileextention>
                        (Default) = {<CLSID for property handler>}
```

 

## Testing and Troubleshooting Property Handlers

The following list provides advice on the kinds of tests you should perform:

-   Test getting output from every single property supported by the file type.
-   Use big property values, for example, use a large metatag in HTML documents.
-   Check that the property handler does not leak file handles by editing it after getting output from the property handler, or by using a tool like oh.exe before and after enumerating file properties.
-   Test all file types associated with the property handler. For example, check that the HTML filter works with .htm and .html file types.
-   Test with corrupted files. Property handler should fail gracefully.
-   If an application supports encryption, test that the property handler does not output encrypted text.
-   If your property handler supports full-text search:
    -   Use multiple special Unicode characters in the file contents and test for their output.
    -   Test the handling of very large documents to ensure the property handler works as expected.

### Installation and Setup Tests

Lastly, you need to test your install and uninstall routines.

-   Installation must recover from failed installations (for example, from canceling and then restarting setup).
-   Uninstall must delete all files associated with the property handler.
-   Uninstall must not delete files other than the ones associated with the property handler installation.
-   Registry keys associated with the property handler must be removed when uninstalled.
-   Uninstall must work even if files are deleted from the installation directory.

### Troubleshooting Property Handlers

The following are some common errors made while developing property handlers:

-   Installing .propdesc files or DLLs under a user directory.
-   Registering components using relative paths.
-   Registering components under HKEY\_CURRENT\_USER instead of HKEY\_LOCAL\_MACHINE.
-   Forgetting to set DisableProcessIsolation for non-stream handlers.
-   Placing the test file in an unindexed location.

If you're having trouble getting your property handler working with the indexer, here are some tips to help you troubleshoot:

-   Verify that your property descriptions (.propdesc files) are marked isColumn="**true**", isViewable="**true**", and isQueryable="**true**" as appropriate.
-   Verify that your .propdesc files are in a global location.
-   Verify that you registered your .propdesc files using absolute paths.
-   Verify that the event log did not record any failures from registering your .propdesc file.
-   Verify that your DLLs is in a global location (and not under your user profile).
-   Verify that your DLLs is registered under HKEY\_LOCAL\_MACHINE\\Software\\Classes.
-   Verify that your DLLs is registered using full paths (or REG\_EXPAND\_SZ strings that expand to absolute paths using environment variables known by the System account).
-   Verify that your property handler works under Windows Explorer.
-   While we recommend using IInitializeWithStream, if you must use IInitializeWithFile or IInitializeWithItem, verify that you specify DisableProcessIsolation.
-   Verify that the Indexing Options Control Panel lists your file type as an indexed file type.
-   Verify that the test file is in an indexed location.
-   Verify that the test file has been modified since you installed your property handler.

If your test file is in an indexed location and the indexer has already crawled that location, you need to modify the file in some way in order to trigger a reindexing of the file.

 

## Using System-Supplied Property Handlers

Windows includes a number of system-supplied property handlers that you can use if the format of your file type is compatible. If you define a new file extension that uses one of these formats you can use the system-provided handlers by registering the handler class identifier (CLSID) for your file extension.

You can use the CLSID listed in the following table to register the system-supplied property handlers for your file format type.



| Format          | CLSID                                  |
|-----------------|----------------------------------------|
| OLE DocFile     | {8d80504a-0826-40c5-97e1-ebc68f953792} |
| Save Game XML   | {ECDD6472-2B9B-4b4b-AE36-F316DF3C8D60} |
| XPS/OPC handler | {45670FA8-ED97-4F44-BC93-305082590BFB} |
| XML             | {c73f6f30-97a0-4ad1-a08f-540d4e9bc7b9} |



 

Before creating a custom property, you should be sure there isn't a system-defined property you can use instead. You can enumerate the system-defined properties by calling [**PSEnumeratePropertyDescriptions**](/windows/win32/api/propsys/nf-propsys-psenumeratepropertydescriptions) or using the prop.exe command line tool.

The system schema defines how these properties interact with the indexer, and you cannot change that. Furthermore, the application you use to create, edit and save your file type needs to conform to certain behavior as well. For example, if the application implements safe save (whereby a temporary file is created during editing, and then ReplaceFile() is used to swap the new version for the old), it must transfer all of the properties from the original file to the new file. Failure to do means the file loses properties added by users or other applications.

 

**Example**

The following shows the registration of the system-supplied OLE DocFile handler for a file type with a .OLEDocFile extension.

```
HKEY_CLASSES_ROOT
   SystemFileAssociations
      .OLEDocFile
         shellex
            {BB2E617C-0920-11d1-9A0B-00C04FC2D6C1}
               (Default) = {9DBD2C50-62AD-11d0-B806-00C04FD706EC}
```

The following shows the registration of the property list information so properties of .OLEDocFile files are displayed on the Details tab and pane.

```
HKEY_CLASSES_ROOT
   SystemFileAssociations
      .OLEDocFile
         ExtendedTileInfo = prop:System.ItemType;System.Size;System.DateModified;System.Author;System.OfflineAvailability
         FullDetails = prop:System.PropGroup.Description;System.Title;System.Subject;
System.Keywords;System.Category;System.Comment;System.PropGroup.Origin;
System.Author;System.Document.LastAuthor;System.Document.RevisionNumber;
System.Document.Version;System.ApplicationName;System.Company;System.Document.Manager;
System.Document.DateCreated;System.Document.DateSaved;System.Document.DatePrinted;
System.Document.TotalEditingTime;System.PropGroup.Content;System.ContentStatus;
System.ContentType;System.Document.PageCount;System.Document.WordCount;
System.Document.CharacterCount;System.Document.LineCount;
System.Document.ParagraphCount;System.Document.Template;System.Document.Scale;
System.Document.LinksDirty;System.Language;System.PropGroup.FileSystem;
System.ItemNameDisplay;System.ItemType;System.ItemFolderPathDisplay;
System.DateCreated;System.DateModified;System.Size;System.FileAttributes;
System.OfflineAvailability;System.OfflineStatus;System.SharedWith;
System.FileOwner;System.ComputerName
         InfoTip = prop:System.ItemType;System.Size;System.DateModified;System.Document.PageCoun
         PerceivedType = document
         PreviewDetails = prop:*System.DateModified;System.Author;System.Keywords;
*System.Size;System.Title;System.Comment;System.Category;
*System.Document.PageCount;System.ContentStatus;System.ContentType;
*System.OfflineAvailability;*System.OfflineStatus;System.Subject;
*System.DateCreated;*System.SharedWith
```

 

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Property Mappings](-search-3x-wds-propertymappings.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Best Practices for Creating Filter Handlers in Windows Search](-search-3x-wds-extidx-filters.md)
</dt> <dt>

[The Indexing Process](-search-indexing-process-overview.md)
</dt> <dt>

[Developing Protocol Handlers](-search-3x-wds-phaddins.md)
</dt> <dt>

[System-Defined Properties for Custom File Formats](-shell-systemdefinedpropertiesforfileformats.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[Property System](../properties/building-property-handlers.md)
</dt> <dt>

[System Properties](https://msdn.microsoft.com/library/bb763010(VS.85).aspx)
</dt> <dt>

[Windows Search SDK Samples](https://www.microsoft.com/downloads/details.aspx?FamilyID=645300AE-5E7A-4CE7-95F0-49793F8F76E8)
</dt> </dl>

 

 
