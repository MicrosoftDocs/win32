---
description: This topic explains how a user registers a new remote data store with federated search by opening an OpenSearch Description (.osdx) file, how to deploy an .osdx file, and how to track usage of your OpenSearch service.
ms.assetid: 9db0f970-4e17-492b-ab75-a8b0f8011d0a
title: Deploy Search Connectors in Windows Federated Search
ms.topic: article
ms.date: 05/31/2018
---

# Deploying Search Connectors in Windows Federated Search

This topic explains how a user registers a new remote data store with federated search by opening an OpenSearch Description (.osdx) file, how to deploy an .osdx file, and how to track usage of your [OpenSearch](https://github.com/dewitt/opensearch) service.

This topic is organized as follows:

-   [The .searchconnector-ms (Search Connector) File](#the-searchconnector-ms-search-connector-file)
-   [Deployment Methods](#deployment-methods)
    -   [Pull Deployment](#pull-deployment)
    -   [Push Deployment](#push-deployment)
-   [Tracking Usage](#tracking-usage)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## The .searchconnector-ms (Search Connector) File

Merely opening the .osdx file that describes how to connect to the web service and how to map any custom elements in your RSS or Atom XML registers your new remote data store with federated search. A data store that already has an [OpenSearch](https://github.com/dewitt/opensearch) web service that is compatible with federated search can be added to Windows Explorer when a user opens an .osdx file.

After you have given the .osdx to your user and the user opens the .osdx file, the following events occur.

1.  A .searchconnector-ms file is created in the **Windows Searches** folder (%userprofile%/Searches).
2.  A shortcut to the .searchconnector-ms file is created in the **Links** folder (%userprofile%/Links).
3.  A shortcut appears in the Windows Explorer navigation **Favorites** pane, enabling the user to navigate into the new data store and query the web service.

## Deployment Methods

There are two ways to deploy search connectors, pull deployment and push deployment.

### Pull Deployment

Pull deployment describes any type of deployment in which the end user takes the initiative to install the search connectors. Common methods of pull deployment are:

-   Attaching the .osdx file in an email.
-   Posting the file on a webpage.
-   Providing a dynamic link on your intranet site; for example, one that generates custom .osdx files based on user choices or the current scope within the site.

For the file to be downloaded when the user clicks the link in their browser, the web server hosting the web service must be configured to deliver the .osdx as a file. Hence, you must configure the MIME Types on the web server to treat .osdx files as `"application/opensearchdescription+xml"`. Optionally, you can use the icon supplied by Microsoft to identify search connector link.

### Push Deployment

Push deployment describes any type of deployment that does not depend on user initiative to install the search connectors. Common methods of push deployment are:

-   Group Policy Preferences (GPP)
-   Logon script
-   Roaming profiles
-   Imaging

## Tracking Usage

To track the usage of your [OpenSearch](https://github.com/dewitt/opensearch) service by users searching from Windows Explorer, filter your web server log files for this user agent string: `Windows-Search+(Windows+NT+6.1)`.

## Additional Resources

For additional information about implementing search federation to remote data stores using OpenSearch technologies in Windows 7 and later, see "Additional Resources" at [Federated Search in Windows](/previous-versions//dd742958(v=vs.85)).

## Related topics

<dl> <dt>

[Federated Search in Windows](-search-federated-search-overview.md)
</dt> <dt>

[Getting Started with Federated Search in Windows](getting-started-with-federated-search-in-windows.md)
</dt> <dt>

[Connecting Your web Service in Windows Federated Search](-search-federated-search-web-service.md)
</dt> <dt>

[Enabling Your Data Store in Windows Federated Search](-search-federated-search-data-store.md)
</dt> <dt>

[Creating an OpenSearch Description File in Windows Federated Search](-search-federated-search-osdx-file.md)
</dt> <dt>

[Following Best Practices in Windows Federated Search](-search-fedsearch-best.md)
</dt> </dl>

 

 
