---
title: Implementing a Protocol Handler for WDS
description: Creating a protocol handler involves implementing ISearchProtocol to manage UrlAccessor objects, IUrlAccessor to generate metadata about and to identify appropriate filters for items in the data store, IProtocolHandlerSite to instantiate a SearchProtocol object and identify appropriate filters, and IFilterto filter proprietary files or to enumerate and filter hierarchically stored files.
ms.assetid: d4bcf370-4152-4cfd-a92e-eb9196d23ab4
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Protocol Handler for WDS

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

Creating a protocol handler involves implementing [**ISearchProtocol**](/windows/desktop/api/searchapi/nn-searchapi-isearchprotocol) to manage UrlAccessor objects, [**IUrlAccessor**](/windows/desktop/api/searchapi/nn-searchapi-iurlaccessor) to generate metadata about and to identify appropriate filters for items in the data store, IProtocolHandlerSite to instantiate a SearchProtocol object and identify appropriate filters, and [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)to filter proprietary files or to enumerate and filter hierarchically stored files. The protocol handler must be multithreaded.

This sections contains the following topics:

-   [Note on URLs](#note-on-urls)
-   [Protocol Handler Interfaces](#protocol-handler-interfaces)
-   [IFilters for Containers](#ifilters-for-containers)
-   [Adding Protocol Handler Options Functionality](#adding-protocol-handler-options-functionality)
    -   [ISearchProtocolOptions](#isearchprotocoloptions)
-   [Related topics](#related-topics)

## Note on URLs

Microsoft Windows Desktop Search (WDS) uses URLs to uniquely identify items in a file system, inside a database-like store, or on the Web. A URL that defines an entry node is called a start page; WDS begins at that start page and recursively crawls the data store. The typical URL structure is:

`protocol://host/path/name.extension`

> [!Note]
>
> When you want to add a new data store, you'll need to select a name to identify it that does not conflict with current ones. We recommend this naming convention: companyName.scheme.

 

## Protocol Handler Interfaces

**ISearchProtocol**

The [**ISearchProtocol**](/windows/desktop/api/searchapi/nn-searchapi-isearchprotocol) interface invokes, initializes, and manages UrlAccessor objects. For more information on implementing the ISearchProtocol interface, see **ISearchProtocol Interface reference**.

**IUrlAccessor**

For a specified URL, the [**IUrlAccessor**](/windows/desktop/api/searchapi/nn-searchapi-iurlaccessor) interface generates metadata about the location structure as well as contained items, and it binds those items to an filter. The **IUrlAccessor** object is instantiated and initialized by an SearchProtocol object; however, you can also implement an internal initialization method so your **IUrlAccessor** object can perform initialization tasks specific to your protocol handler, such as validating the URL for an item being accessed or checking the last modified time to determine if a file must be processed in the current crawl.

> [!Note]
>
> Modified times for directories are ignored. The [**IUrlAccessor**](/windows/desktop/api/searchapi/nn-searchapi-iurlaccessor) object must enumerate the child objects to determine whether there have been any modifications or deletions.

 

Much of the design of the **UrlAccessor** object is dependent on whether the structure is hierarchical or link-based. For hierarchical data stores, the **UrlAccessor** object must find an filter that can enumerate their contents. Another distinction between hierarchical and link-based protocol handlers is the use of the IsDirectory method. In link-based protocol handlers, this method should return S\_FALSE. Hierarchical protocol handlers must return S\_OK for containers.

For further instructions on implementing an [**IUrlAccessor**](/windows/desktop/api/searchapi/nn-searchapi-iurlaccessor) interface, see the [**IUrlAccessor Interface**](/windows/desktop/api/searchapi/nn-searchapi-iurlaccessor) reference.

**IProtocolHandlerSite**

This interface is used to instantiate a **SearchProtocol** object and also provides the **UrlAccessor** object with an appropriate filter for a specified class ID (CLSID).

## IFilters for Containers

If you are implementing a hierarchical protocol handler, you must implement a container [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)component that enumerates URLs representing containers or folders. The enumeration process is a loop through the **GetChunk** and **GetValue** methods of the IFilter interface that return a list of URLs that represent each item in the container.

First, **GetChunk** returns a FULLPROSPEC with the property set GATHER\_PROPSET and either:

-   PID\_GTHR\_DIRLINK, the URL to the item without the last modified time, or
-   PID\_GTHR\_DIRLINK\_WITH\_TIME, the URL along with the last modified time

The property set GUID for GATHER\_PROPSET is 0B63E343-9CCC-11D0-BCDB-00805FCCCE04. The PROPSPEC Property is either PID\_GTHR\_DIRLINK=2 or PID\_GTHR\_DIRLINK\_WITH\_TIME = 12 decimal.

Returning PID\_GTHR\_DIRLINK\_WITH\_TIME is more efficient because the indexer can immediately determine whether the item needs to be indexed without calling the ISearchProtocol->CreateUrlAccessor() and IUrlAccessor->GetLastModified() methods.

Then **GetValue** returns a PROPVARIANT for the URL (and last modified time if used), as either:

-   VT\_LPWSTR, the URL of the child item, or
-   Vector of the URL followed by a FILETIME

The following sample code demonstrates how to build the proper PID\_GTHR\_DIRLINK\_WITH\_TIME.

> [!Note]
>
> **THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.**
>
> Copyright (C) Microsoft. All rights reserved.

 


```
// params are assumed to be valid

HRESULT GetPropVariantForUrlAndTime(PCWSTR pszUrl, const FILETIME &ftLastModified, PROPVARIANT **ppPropValue)
{
    *ppPropValue = NULL;

    // allocate the propvariant pointer
    *ppPropValue = (PROPVARIANT *)CoTaskMemAlloc(sizeof(*ppPropValue));
    HRESULT hr = *ppPropValue ? S_OK : E_OUTOFMEMORY;

    if (SUCCEEDED(hr))
    {
        PropVariantInit(*ppPropValue);  // zero init the value

        // now allocate enough memory for 2 nested PropVariants.
        // PID_GTHR_DIRLINK_WITH_TIME is an array of 2 PROPVARIANTs
        PROPVARIANT *pVector = (PROPVARIANT *)CoTaskMemAlloc(sizeof(*pVector) * 2);
        hr = pVector ? S_OK : E_OUTOFMEMORY;

        if (SUCCEEDED(hr))
        {
            // set the container PROPVARIANT that it is a vector of 2 PROPVARIANTS
            (*ppPropValue)->vt = VT_VARIANT | VT_VECTOR;
            (*ppPropValue)->capropvar.cElems = 2;
            (*ppPropValue)->capropvar.pElems = pVector;
            PWSTR pszUrlAlloc;
            hr = SHStrDup(pszUrl, &pszUrlAlloc);

            if (SUCCEEDED(hr))
            {
                // now fill the array of PROPVARIANTS
                // put the pointer to the URL into the vector
                (*ppPropValue)->capropvar.pElems[0].vt = VT_LPWSTR; 
                (*ppPropValue)->capropvar.pElems[0].pwszVal = pszUrlAlloc;

                 // put the FILETIME into vector
                (*ppPropValue)->capropvar.pElems[1].vt = VT_FILETIME; 
                (*ppPropValue)->capropvar.pElems[1].filetime = ftLastModified;
            }

            else
            {
                CoTaskMemFree(pVector);
            }
        }
 
        if (FAILED(hr))
        {
            CoTaskMemFree(*ppPropValue);
            *ppPropValue = NULL;
        }
    }
    return S_OK;
}

```



> [!Note]
>
> A container [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)component should always enumerate all child URLs even if the child URLs have not changed, because the Indexer detects deletions through the enumeration process. If the date output in a DIR\_LINKS\_WITH\_TIME indicates that the data has not changed, the indexer does not update the data for that URL.

 

The physical URL is the URL that the **UrlAccessor** object processes. If the filter does not emit a user-friendly DisplayUrl, WDS displays the physical URL to the user as part of the search results. The WDS schema contains two properties to control what is displayed to the end user, as shown in the table below.



| GUID                                 | PROPSPEC      | Description                                         |
|--------------------------------------|---------------|-----------------------------------------------------|
| D5CDD505-2E9C-101B-9397-08002B2CF9AE | DisplayFolder | Folder Path displayed to the user in search results |
| D5CDD505-2E9C-101B-9397-08002B2CF9AE | FolderName    | Display name of the parent folder                   |



 

If your code does not emit a DisplayFolder or FolderName, these values are computed from the DisplayUrl. Forward slashes in the URL denote containers within the store or file system.

## Adding Protocol Handler Options Functionality

For your protocol handler to have a default start page (and entry node URL), you must implement the **ISearchProtocolOptions** interface. In future versions of WDS, this interface will provide hooks to the Options dialog for an enhanced user experience. This interface provides the following functionality:

-   Determines whether the requirements for your protocol handler are met. For example, your protocol handler's store may require access to a given application to properly index the application's data but that application is unavailable.
-   Identifies the minimum requirements your protocol handler needs to process an item. Requirements can be expressed in a user-friendly, localized description, such as "Microsoft Outlook 2000 or greater."
-   Defines the URLs your protocol handler should process by default.

### ISearchProtocolOptions

The following table describes the methods you need to implement for the **ISearchProtocolOptions** interface.



| Method               | Description                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------|
| CheckRequirements    | Determines whether a custom protocol handler's minimum requirements are met                             |
| GetDefaultCrawlScope | Returns a list of default URLs within a specified store for a custom protocol handler                   |
| GetRequirements      | Identifies a user-friendly, localized description of minimum requirements for a custom protocol handler |



 

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Notifying the Index of Changes](-search-2x-wds-notifyingofchanges.md)
</dt> <dt>

[Adding Icons, Previews, and Context Menus with Shell Extensions](-search-2x-wds-ph-ui-extensions.md)
</dt> <dt>

[Installing and Registering Protocol Handlers](-search-2x-wds-ph-install-registration.md)
</dt> </dl>

 

 