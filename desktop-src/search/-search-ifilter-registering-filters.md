---
description: Your filter handler must be registered. You can also locate an existing filter handler for a given file name extension either through the registry or by using the ILoadFilter interface.
ms.assetid: 3478b948-73c7-4533-974a-d9b5186a651b
title: Registering Filter Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Registering Filter Handlers

Your filter handler must be registered. You can also locate an existing filter handler for a given file name extension either through the registry or by using the [**ILoadFilter**](/windows/desktop/api/filtereg/nn-filtereg-iloadfilter) interface.

This topic is organized as follows:

- [Registering Filters Handlers for Windows Search](#registering-filter-handlers)
  - [Obsolete Approach for Registering Filters Handlers](#obsolete-approach-for-registering-filters-handlers)
- [Replacing Existing Filter Handlers](#replacing-existing-filter-handlers)
- [Finding a Filter Handler for a Given File Extension](#finding-a-filter-handler-for-a-given-file-extension)
- [Additional Resources](#additional-resources)
- [Related topics](#related-topics)

> [!NOTE]  
> A filter handler is an implementation of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface.

## Registering Filters Handlers for Windows Search

The GUIDs you need for registering a new protocol handler or to find an existing protocol handler are listed in the following table.

| GUID                                     | User or application defined | Description                                                                                               |
|------------------------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| **89BCB740-6119-101A-BCB7-00DD010655AF** | Application                 | The [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface GUID is a registry key constant for all filter handlers. |
| **{PersistentHandlerGUID}**              | User                        | This is the GUID for the persistent handler.                                                              |
| **{FilterHandlerCLSID}**                 | User                        | This is the class identifier (CLSID) for the filter handler.                                              |
| **{ApplicationGUID}**                    | User                        | This is an intermediate (aggregated) GUID.                                                                |

Filter handlers must be registered in HKEY\_LOCAL\_MACHINE because SearchFilterHost.exe is running under the SYSTEM account and therefore cannot access registry keys for HKEY\_CURRENT\_USER for the logged-on user. In addition, the Users group must have read-and-execute access to the filter handler .dll itself because SearchFilterHost.exe removes all administrator rights and permits only non-administrator rights. Because the default Visual Studio project location is in the current user's directory, and so does not give read permissions to the Users group, you must either move the .dll or change the ACLs to allow SearchFilterHost.exe access.

When you register a new filter handler, we recommend that you use a descriptive name, for example, HTML IFilter.

**To register your new filter handler:**

1. Specify the extension and persistent handler GUID that will use the filter handler:

```
    HKEY_LOCAL_MACHINE
       Software
          Classes
             .txt
                PersistentHandler
                   (Default) = {PersistentHandlerGUID}
```

```
    HKEY_LOCAL_MACHINE
       Software
          Classes
             .txt
                CLSID
                   {PersistentHandlerGUID}
                      PersistentAddinsRegistered
                         {89BCB740-6119-101A-BCB7-00DD010655AF}l
                            (Default) = {FilterHandlerCLSID}
```

2. Register your filter handler with the following keys and values:

```
    HKEY_LOCAL_MACHINE
       Software
          Classes
             .txt
                CLSID
                   {FilterHandlerCLSID}
                      (Default) = {DescriptiveFilterHandlerName}
                      InprocServer32
                         (Default) = DLL Install Path
                         ThreadingModel = Both
```

### Obsolete Approach for Registering Filters Handlers

This approach is not recommended for use. Filters can be registered for a CLSID that represents a Component Object Model (COM) class, and/or for a file name extension. You could register both filters if you need to register a filter handler for a class, and a different filter handler for a file name extension within the class. Note that a filter handler registered for a file name extension takes precedence over a filter handler for a CLSID.

These entries are standard OLE registry entries up to and including the entry for the class **CLSID\\{ApplicationGUID}**. The DLL sample.dll implements running object behavior for the .txt class. Note the extra entry, PersistentHandler. This entry specifies the class that is responsible for brokering requests to the persistent objects of the sample class. The entry under **PersistentAddinsRegistered** identifies the implementation responsible for the interface named **89BCB740-6119-101A-BCB7-00DD010655AF**(IID\_IFilter). The class implementing **IID\_IFilter** has standard OLE registry entries. The InprocServer32 DLL is loaded through the standard OLE mechanism.

Windows Search observes the threading model specified for the filter handler. When the threading model is set to **Both**, the filter handler must be thread safe; otherwise, if it is not thread safe, specify **Apartment**. Note that filter handlers should always be thread safe.

The following example registry entries are for a filter handler registered for a class and file name extension. **{PersistentHandlerGUID}** and **{FilterHandlerCLSID}** are used as variables indicating values that need to be specified by the creator of the filter handler. The values are of type REG\_SZ.

```
HKEY_LOCAL_MACHINE
   Software
      Classes
         .txt
            (Default) = SampleFile
         SampleFile
            (Default) = Class for Sample Files
            CLSID
               (Default) = {ApplicationGUID}
         CLSID
            {ApplicationGUID}
               (Default) = Sample Files
               InprocServer32
                  (Default) = sample.dll
               PersistentHandler
                  (Default) = {PersistentHandlerGUID}
            {PersistentHandlerGUID}
               (Default) = Sample file persistent handler
               PersistentAddinsRegistered
                  {89BCB740-6119-101A-BCB7-00DD010655AF}l
                     (Default) = {FilterHandlerCLSID}
            {FilterHandlerCLSID}
               (Default) = Sample Files
               InprocServer32
                  (Default) = sampfilt.dll
                  ThreadingModel = Both
```

## Replacing Existing Filter Handlers

We recommend that you do not replace the built-in filter handlers for common file types such as .txt, .doc, .html, .url, and so forth, because doing so can have undesired effects on other system components. Indexing email message bodies depends on the .txt, .html, and .rtf filter handlers, for example.

If a new filter handler for a file type is being installed as a replacement for an existing filter registration, the installer should save the current registration and restore it if the new filter handler is uninstalled. There is no mechanism to chain filters. Hence, the new filter handler is responsible for replicating any necessary functionality of the old filter.

## Finding a Filter Handler for a Given File Extension

You can use the [**ILoadFilter**](/windows/desktop/api/filtereg/nn-filtereg-iloadfilter) interface to find a filter handler for a given file name extension. The following example registry entries illustrate how to do so for HTML files. In this example, the filter handler for HTML documents is nlhtml.dll. The values are of type REG\_SZ.

**To find the filter handler for a given file name extension:**

1. Check whether the extension for the type of files that are filtered has a persistent handler registered under the registry entry \\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes.extension. If so, let this key be {PersistentHandlerGUID}.

```
    HKEY_LOCAL_MACHINE
       SOFTWARE
          Classes
             .htm
                PersistentHandler
                   {PersistentHandlerGUID}
```

2. If there is not a persistent handler registered for the extension, find the CLSID associated with the document type under the registry entry \\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes. Let this key be {ApplicationGUID}. Then determine whether a persistent handler is registered for the CLSID: using {ApplicationGUID} locate the persistent handler for the \\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\CLSID\\{ApplicationGUID} entry. Let this key be {PersistentHandlerGUID}.

```
    HKEY_LOCAL_MACHINE
       SOFTWARE
          Classes
             htmlfile
                (Default) = Class for WWW HTML files
                CLSID
                   (Default) = {25336920-03F9-11CF-8FD0-00AA00686F13}
             CLSID
                {25336920-03F9-11CF-8FD0-00AA00686F13}
                   PersistentHandler
                      (Default) = {PersistentHandlerGUID}
```

3. Determine the GUID of the persistent handler: using {PersistentHandlerGUID} find the persistent handler GUID for the document type. The value under the registry entry HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\CLSID\\{PersistentHandlerGUID}\\PersistentAddinsRegistered\\ 89BCB740-6119-101A-BCB7-00DD010655AF yields the persistent handler GUID for this document type. Let this key be {FilterHandlerCLSID}.

```
    HKEY_LOCAL_MACHINE
       SOFTWARE
          Classes
             {PersistentHandlerGUID}
                (Default) = HTML File Persistent Handler<dl>
                    REG_SZ     {89BCB740-6119-101A-BCB7-00DD010655AF}
                    REG_SZ     (Default) = {EEC97550-47A9-11CF-B952-00AA0051FE20}
```

4. Determine the filter handler: using {FilterHandlerCLSID} that was determined in the previous step locate the filter handler under the entry \\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\CLSID\\{FilterHandlerCLSID}\\InprocServer32. In this example the descriptive filter handler name used is HTML IFilter.

```
    HKEY_LOCAL_MACHINE
       SOFTWARE
          Classes
             CLSID
                {EEC97550-47A9-11CF-B952-00AA0051FE20}
                   (Default) = HTML IFilter
                    Data type  REG_SZ
                    InprocServer32
                    nlhtml.dll
```

## Additional Resources

- The [IFilterSample](-search-sample-ifiltersample.md) code sample, available on [GitHub](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/IFilterSample), demonstrates how to create an [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) base class for implementing the **IFilter** interface.
- For an overview of the indexing process, see [The Indexing Process](-search-indexing-process-overview.md).
- For an overview of file types, see [File Types](../shell/fa-file-types.md).
- To query file association attributes for a file type, see [PerceivedTypes, SystemFileAssociations, and Application Registration](/previous-versions/windows/desktop/legacy/cc144150(v=vs.85)).

## Related topics

[Developing Filter Handlers](-search-ifilter-conceptual.md)

[About Filter Handlers in Windows Search](-search-ifilter-about.md)

[Best Practices for Creating Filter Handlers in Windows Search](-search-3x-wds-extidx-filters.md)

[Returning Properties from a Filter Handler](-search-ifilter-property-filtering.md)

[Filter Handlers that Ship with Windows](-search-ifilter-implementations.md)

[Implementing Filter Handlers in Windows Search](-search-ifilter-constructing-filters.md)

[Testing Filter Handlers](-search-ifilter-testing-filters.md)
