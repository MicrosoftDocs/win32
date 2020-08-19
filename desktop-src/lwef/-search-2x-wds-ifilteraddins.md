---
title: Developing IFilter Add-ins
description: You can extend Microsoft Windows Desktop Search (WDS) with filter add-ins, components that implement the IFilterinterface, to include new file types.
ms.assetid: 71dd515d-a73e-4e0a-b0da-c8a6209d09fe
ms.topic: article
ms.date: 05/31/2018
---

# Developing IFilter Add-ins

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

You can extend Microsoft Windows Desktop Search (WDS) with filter add-ins, components that implement the [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)interface, to include new file types. Filters are responsible for accessing and parsing data in files and for returning pairs of properties and values as well as chunks of text for indexing. During the indexing process, WDS calls the appropriate filter with the URL for each file or item. The filter first extracts metadata that corresponds to properties that are marked retrievable in the WDS schema, such as title, file size, and last modified date. Then it breaks the item content into chunks of text. WDS adds the properties and text returned by the filter to the catalog. WDS can index any file type for which it has a registered filter.

In some circumstances, you do not need to write a new filter. WDS 2.x contains filters for over 200 types of items (including plaintext items such as HTML, XML, and source code files) and uses the same [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)technology as SharePoint Services. If you already have filters installed for your file types, WDS can use those existing filters to index this data. Furthermore, WDS includes a general filter for file types that are plaintext-based. If you have a file type that can be processed by either an existing SharePoint Services filter or the plaintext filter, you can add the file name extension and filter GUID to the Registry so WDS can locate and use it (see [To Register a Filter Add-in](#to-register-a-filter-add-in) for more information).

If, however, you have a non-plaintext and proprietary data or file format, writing a custom filter implementation is the only way to ensure WDS can index the file format in the catalog. You can have only one filter add-in for a file type, so it is possible to override an existing filter or to have another filter override yours for a specific file type.

This section contains the following topics:

-   [Required Filter Interfaces](#required-filter-interfaces)
    -   [IFilter Interface](#ifilter-interface)
    -   [IPersistStream](#ipersiststream)
    -   [IPersistFile](#ipersistfile)
    -   [IPersistStorage](#ipersiststorage)
-   [Outputting Properties with Filters](#outputting-properties-with-filters)
    -   [Property Values](#property-values)
-   [Filter Add-in Installation](#filter-add-in-installation)
    -   [CLSIDs Required for Registration](#clsids-required-for-registration)
    -   [Registration Model](#registration-model)
    -   [To Register a Filter Add-in](#to-register-a-filter-add-in)
-   [Related topics](#related-topics)

## Required Filter Interfaces

A filter add-in must implement the [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)interface and one of the following interfaces:

-   [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream) - To load data from a stream. This is more secure than using files because nothing is written to disk. The IPersistStream interface is the preferred method for forward compatibility with Windows Vista.
-   [IPersistFile Interface](/windows/win32/api/objidl/nn-objidl-ipersistfile) - To load data from a file. This interface is not supported in Windows Vista.
-   [IPersistStorage Interface](/windows/win32/api/objidl/nn-objidl-ipersiststorage) - To load data from an OLE COM Structured Storage.

A filter add-in uses these interfaces to get the contents of the item and return them iteratively to the index until the end of the file is reached. A filter add-in should be as robust as possible to handle corrupt files and those that do not meet expected input formats.

### IFilter Interface

This is a required interface for a filter implementation. For more information, see the [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)interface reference.



| Method       | Description                                                                            |
|--------------|----------------------------------------------------------------------------------------|
| Init()       | Initializes a filtering session.                                                       |
| GetChunk()   | Positions the filter at the beginning of first or next chunk and returns a descriptor. |
| GetText()    | Retrieves text from the current chunk.                                                 |
| GetValue()   | Retrieves property values from the current chunk.                                      |
| BindRegion() | Currently reserved for internal use; do not implement. This method returns E\_NOTIMPL. |



 

### IPersistStream

This interface loads a file from a stream for more secure processing than [IPersistFile Interface](/windows/win32/api/objidl/nn-objidl-ipersistfile) because the context in which a [IPersistStream](/windows/win32/api/objidl/nn-objidl-ipersiststream) filter runs does not need the rights to open any files on the disk or over the network. Of the two methods for accessing a single file, this is the preferred method for forward compatibility with Windows.



| Method       | Description                                                                                                                                        |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| IsDirty()    | Checks if there has been a change. This method returns E\_NOTIMPL in filters.                                                                      |
| InitNew()    | Creates a new storage. This method returns E\_NOTIMPL in filters.                                                                                  |
| Load()       | Initializes an object from the stream where it was previously saved.                                                                               |
| Save()       | Saves an object into the specified stream and indicates whether the object should reset its dirty flag. This method returns E\_NOTIMPL in filters. |
| GetSizeMax() | Returns the size in bytes of the stream needed to save the object. This method returns E\_NOTIMPL in filters.                                      |



 

### IPersistFile

This interface loads a file by absolute path and is not supported in Windows Vista.



| Method          | Description                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------------------|
| GetCurFile()    | Gets the current name of the file associated with the object. Returns the path specified in Load().                          |
| Load()          | Opens the specified file and initializes an object from the file contents. You can delay opening the file until you need it. |
| GetClassID()    | Returns the class identifier (CLSID) for the new file type. You should use uuidgen.exe to generate a unique CLSID.           |
| IsDirty()       | Need only return E\_NOTIMPL in filters                                                                                       |
| Save()          | Need only return E\_NOTIMPL in filters                                                                                       |
| SaveCompleted() | Need only return E\_NOTIMPL in filters                                                                                       |



 

### IPersistStorage

This interface supports the structured storage model, in which each contained object has its own storage that is nested within the container's storage. Like [IPersistFile Interface](/windows/win32/api/objidl/nn-objidl-ipersistfile), this interface loads by absolute path and is not supported in Windows Vista.



| Method            | Description                                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------------------|
| IsDirty()         | Checks if there has been a change. This method returns E\_NOTIMPL in filters.                                 |
| InitNew()         | Creates a new storage. This method returns E\_NOTIMPL in filters.                                             |
| Load()            | Saves the storage. This method returns E\_NOTIMPL in filters.                                                 |
| Save()            | Returns the size in bytes of the stream needed to save the object. This method returns E\_NOTIMPL in filters. |
| SaveCompleted()   | Reserved for internal use. This method returns E\_NOTIMPL in filters.                                         |
| HandsOffStorage() | Reserved for internal use. This method returns E\_NOTIMPL in filters.                                         |



 

## Outputting Properties with Filters

The purpose of a filter is to extract the content and properties of files for inclusion in the full-text index. WDS first calls the Load method on either the IPersistFile, IPersistStream, or IPersistStorage implementations and then invokes the Init method of the IFilter implementation. **GetChunk** is called to retrieve chunks of text or property value data, and then either **GetText** or **GetValue** is called as many times as needed to retrieve all of the text or property values associated with the chunk. This process repeats until **GetChunk** reports that there are no more chunks in the document.

The **GetChunk** method retrieves information about the first or next logical block of information from the file being filtered and returns that information in a STAT\_CHUNK structure, including a monotonically increasing chunk ID, status information about how the current chunk relates to the previous chunk, a flag indicating whether the chunk contains text or a value, the chunk's locale, and the chunk's property specification. The property specification is a [**FULLPROPSPEC**](/windows/desktop/api/filter/ns-filter-fullpropspec) consisting of a CLSID and either an integer or string property identifier (for example, D5CDD505-2E9C-101B-9397-08002B2CF9AE/PerceivedType). It identifies the type of property rather than the property value itself.

The chunk locale identifier is used to choose an appropriate word breaker, and it is very important that you correctly identify it. If the filter cannot determine the locale of the text, it should assume the default system locale, available by using **GetSystemDefaultLCID**. If you control the file format and it currently does not contain locale information, you should add a user feature to enable proper locale identification. Using a mismatched word breaker can lead to a bad query experience for the user.

**GetChunk** only manages accessing chunks and does not return the text or property value itself. Rather, subsequent calls to **GetText** and **GetValue** retrieve the body of the chunk. **GetText** returns text chunks, which are Unicode strings, from the current CHUNK\_TEXT chunk. If the current chunk is too large, more than one call to the **GetText** method can be required. Each call to the **GetText** method retrieves text that immediately follows the text from the last call to the **GetText** method. For example, the last character from one call can be in the middle of a word, and the first character in the next call would continue that word. Search engines must handle this situation.

**GetValue** returns property values for the current CHUNK\_VALUE chunk in PROPVARIANT structures, which can hold a wide variety of data types. **GetValue** must allocate the PROPVARIANT structure itself using CoTaskMemAlloc. The caller of **GetValue** is responsible for freeing memory pointed to by the PROPVARIANT using PropVariantClear, and for freeing the structure itself with CoTaskMemFree. For more information on PROPVARIANTs, see the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) reference.

### Property Values

Filters should output at a minimum the following properties which are the default columns in the WDS results view.



| GUID                                 | PROPSPEC      | Friendly Name  | Description                                                                                                                                     |
|--------------------------------------|---------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| F29F85E0-4FF9-1068-AB91-08002B27B3D9 | 2             | PrimaryTitle   | Title that displays for this item.                                                                                                              |
| F29F85E0-4FF9-1068-AB91-08002B27B3D9 | 4             | PrimaryAuthors | Person most associated with this item.                                                                                                          |
| D5CDD505-2E9C-101B-9397-08002B2CF9AE | PrimaryDate   | PrimaryDate    | Most important date for item, like date received for email or modified for files.                                                               |
| D5CDD505-2E9C-101B-9397-08002B2CF9AE | PerceivedType | PerceivedType  | Type of file being parsed. Must match one of the Windows Desktop Search types listed in WDS [Perceived Type](-search-2x-wds-perceivedtype.md). |



 

For plaintext items, WDS extracts all text and system-defined properties such as file size or extension on including new plaintext file types to the index). Other types of properties that can be returned to the index include:

-   For files: author, title, status, keywords
-   For media: album, genre, camera make, date taken
-   For communications: from, to, cc, importance
-   For contacts: job title, business phone, company

The list above groups properties common to a specified Perceived Type; however, any property can be used regardless of the type. For example, company could be used for a contact's employer name and could also be used to refer to the name of a client the file relates to. Many of these properties are used to display search results in the WDS results view. For example, a file's Title property is shown as the main column in the default results view. IFilter objects should output all the properties related to the item type they are parsing. Custom properties cannot be added in WDS 2.x. For a full list of properties available, see the [WDS Schema](-search-2x-wds-schematable.md).

## Filter Add-in Installation

Installing the filter involves copying the DLL to an appropriate location in the Program Files directory and registering it. Filters should implement self-registration for installation and should follow these guidelines:

-   The installer must use either EXE or MSI installer.
-   Release notes must be provided.
-   An **Add/Remove Programs** entry must be created for each add-in installed.
-   The installer must take over all registry settings for the particular file type or store that the current add-in understands.
-   If a previous add-in is being overwritten, the installer should notify the user.
-   If a newer add-in has overwritten the previous add-in, there should be the ability to restore the previous add-in's functionality and make it the default add-in for that file type or store again.

### CLSIDs Required for Registration

There are three class identifiers, or CLSIDs, associated with every filter. You'll need to generate one or more of these (use uuidgen.exe) to register your filter add-in.

-   The first identifies all filters' persistent handler, IID\_IFilter, which is {89BCB740-6119-101A-BCB7-00DD010655AF}. This CLSID is constant for all filters that implement IFilter.
-   The second (the value of the IID\_IFilter key) identifies the IFilter implementation for your file type. This key contains an InprocServer32 value that specifies the DLL name by path and the threading model. If the filter is in the system path, like the system32 directory, a file name is sufficient. Otherwise, this value should have a full path specification.
-   The third identifies the file type the filter processes and is returned by the GetClassID method on your IPersist interface.

> [!Note]
>
> In future versions of Microsoft operating systems, installing files in the system32 directory may get more difficult, so we recommend you install them under Program Files and include a full path to the filter in the registry. For security reasons, it is also prudent to specify a full path to your DLL in the registry. Otherwise, a "Trojan horse" version of your DLL could be loaded if it happens to be in the process path before your version.

 

### Registration Model

When WDS is ready to filter a file, it looks in the registry under the file's extension to determine which filter to load. It then follows a series of registry links to find the name of the filter DLL, in this order:

1.  From CLSIDs located at:

    **HKEY\_CURRENT\_USER\\SOFTWARE\\Microsoft\\RSSearch\\ContentIndexCommon\\Filters\\Override\\RSApp**

    **HKEY\_CURRENT\_USER\\SOFTWARE\\Microsoft\\RSSearch\\ContentIndexCommon\\Filters**

2.  From the file content type at:

    **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\MIME\\Database\\Content Type**

3.  From the file name extension (same as Win32 LoadIFilter API) at:

    **HKEY\_CURRENT\_USER\\SOFTWARE\\Microsoft\\RSSearch\\ContentIndexCommon\\Filters\\Override\\RSApp**

    **HKEY\_CURRENT\_USER\\SOFTWARE\\Microsoft\\RSSearch\\ContentIndexCommon\\Filters**

    **HKEY\_CLASSES\_ROOT\\extpersistentHandler->CLSID->IID\_IFilter->CLSID**

4.  From Default at:

    **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\RSSearch\\ContentIndexCommon\\Filters**

### To Register a Filter Add-in

You need to make a total of eight entries in the registry to register your filter add-in, where:

-   **.ext** is the new file name extension
-   **GUID\_1** can be any new GUID generated for this extension
-   **89BCB740-6119-101A-BCB7-00DD010655AF** is the IFilter interface GUID, which is a constant for all IFilter implementations.

1.  Register the persistent handler for the file name extension with the following keys and values:

    ```
    HKEY_CLASSES_ROOT\<.ext>\PersistentHandler
       (Default) = {GUID_1}
    ```

    ```
    HKEY_CLASSES_ROOT\CLSID\{GUID_1}
       (Default) = <Persistent Handler Description>
    ```

    ```
    HKEY_CLASSES_ROOT\CLSID\{GUID_1}\PersistentAddinsRegistered
       (Default) = (Value Not Set)
    ```

    ```
    HKEY_CLASSES_ROOT\CLSID\{GUID_1}\PersistentAddinsRegistered\{89BCB740-6119-101A-BCB7-00DD010655AF}
       (Default) = {CLSID of IFilter implementation}
    ```

    ```
    HKEY_CLASSES_ROOT\CLSID\{GUID_1}\PersistentHandler
       (Default) = {GUID_1}
    ```

2.  Register the IFilter implementation with the following keys and values:

    ```
    HKEY_CLASSES_ROOT\CLSID\{CLSID of IFilter implementation}
       (Default) = Extension IFilter Description">
    ```

    ```
    HKEY_CLASSES_ROOT\CLSID\{CLSID of IFilter implementation}\InprocServer32
       (Default) = <DLL Install Path>
       ThreadingModel = Both
    ```

3.  Register the IFilter implementation with Windows Desktop Search with the following key and value:

    ```
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\RSSearch\ContentIndexCommon\Filters\Extension\<.ext>
       (Default) = {CLSID of IFilter implementation}"
    ```

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[SchemaTable](-search-2x-wds-schematable.md)
</dt> <dt>

[Perceived Types](-search-2x-wds-perceivedtype.md)
</dt> <dt>

[Developing Protocol Handlers](-search-2x-wds-phaddins.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)
</dt> </dl>

 

 