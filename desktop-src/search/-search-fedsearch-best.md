---
description: This topic lists the best practices through which you can build a web-based data store that can be searched using Windows federated search, and integrates your remote data sources with Windows Explorer without having to write or deploy any Windows client-side code.
ms.assetid: d9b62cf5-7236-4252-b88d-18120f50c62c
title: Following Best Practices in Windows Federated Search
ms.topic: article
ms.date: 05/31/2018
---

# Following Best Practices in Windows Federated Search

This topic lists the best practices through which you can build a web-based data store that can be searched using Windows federated search, and integrates your remote data sources with Windows Explorer without having to write or deploy any Windows client-side code.

This topic is organized as follows:

-   [Best Practices for Windows Federated Search](#best-practices-for-windows-federated-search)
-   [Best Practices for Creating RSS Output](#best-practices-for-creating-rss-output)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Best Practices for Windows Federated Search

Best practices for working with [OpenSearch](https://github.com/dewitt/opensearch) in Windows 7 are as follows:

-   Support the *{startIndex}* and *{count}* parameters, and be sure to always return the number of items requested unless you are returning the last of the results.
-   If you know the file name extension, map it to the [System.FileExtension](../properties/props-system-fileextension.md) Windows Shell property. Using file name extensions is a better way to identify a file type than MIME type.
-   Ensure that the MIME type or file name extension that you specify in the RSS matches the file name and MIME type returned in the HTTP header by the web server that hosts the item when the item content is requested.
-   If you are returning file items, return a file size whenever possible. This ensures that the download progress dialog box is accurate.
-   Verify that requests for items beyond the end of the results set return no results.
    > [!Note]  
    > Do not repeat results.

     

-   Do not put HTML tags where they don't belong. Per the RSS specification, they are valid in the description field, but not in the title field.
-   Do not create enclosures for webpage items. For example, if you create an enclosure and map a file name extension of .aspx, the file is downloaded by Windows Explorer to the Internet cache and executed from there. Web browsers do not handle the .aspx file type. The user would get an **Open with** dialog box, or the file might be opened by an application like Microsoft Visual Studio. Avoid this by returning a link element only for webpages.
-   Provide a web roll-over URL in the .osdx file using a URL template with `format="text\html"`.
-   Provide a URL to the parent folder, container, or webpage by mapping a custom element URL value to the [System.ItemFolderPathDisplay](../properties/props-system-itempathdisplay.md) Windows Shell property.

## Best Practices for Creating RSS Output

Best practices for creating RSS output are as follows:

-   Each item MUST return a URL `link` or `enclosure` value (or equivalent, such as `media:content`)
-   Do not include any HTML formatting tags in the **title** attribute, or those tags will appear in the title and be displayed in Windows Explorer.
-   For the **description** element:
    -   Show enough information so that the user knows why this result might be relevant.
    -   Do not include HTML formatting. The [OpenSearch](https://github.com/dewitt/opensearch) provider removes the formatting, which might result in less than desirable results for your description.
    -   Do not include metadata that is already provided in other elements, such as enclosure file name, size, modified date, and so forth, because Windows Explorer already displays the metadata. Displaying it in the **description** element would be redundant.
-   For enclosure or content URLs:
    -   Specify the type attribute as a valid MIME type.
    -   Specify the file size in bytes.
-   If you are implementing RSS output in .NET using `DateTime`, test your feed in Microsoft Internet Explorer to see if it is valid before deploying it to Windows Explorer.

## Additional Resources

For additional information about implementing search federation to remote data stores using OpenSearch technologies in Windows 7 and later, see "Additional Resources" at [Federated Search in Windows](/previous-versions//dd742958(v=vs.85)).

## Related topics

<dl> <dt>

[Federated Search in Windows](-search-federated-search-overview.md)
</dt> <dt>

[Getting Started with Federated Search in Windows](getting-started-with-federated-search-in-windows.md)
</dt> <dt>

[Connecting Your Web Service in Windows Federated Search](-search-federated-search-web-service.md)
</dt> <dt>

[Enabling Your Data Store in Windows Federated Search](-search-federated-search-data-store.md)
</dt> <dt>

[Creating an OpenSearch Description File in Windows Federated Search](-search-federated-search-osdx-file.md)
</dt> <dt>

[Deploying Search Connectors in Windows Federated Search](-search-federated-search-deploying.md)
</dt> <dt>

[Extending the Index](-search-3x-wds-extidx-overview.md)
</dt> </dl>

 

 
