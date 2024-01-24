---
description: This topic describes the steps involved in connecting a web service between your data store and Windows Federated Search, and how to send queries and return search results in RSS or Atom.
ms.assetid: 4c8de310-49e6-4d90-a920-0c715351c86a
title: Connecting Your Web Service in Windows Federated Search
ms.topic: article
ms.date: 05/31/2018
---

# Connecting Your Web Service in Windows Federated Search

This topic describes the steps involved in connecting a web service between your data store and Windows Federated Search, and how to send queries and return search results in RSS or Atom.

This topic is organized as follows:

-   [Connect Your web Service](#connect-your-web-service)
-   [Register an Existing Remote Data Store](#register-an-existing-remote-data-store)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Connect Your web Service

**To connect the web service of your data store to federated search, perform the following steps:**

1.  Create an .osdx file.
2.  Supply the .osdx file to users so that they can add the service on demand by opening the .osdx file.
3.  Generate a search connector and actively deploy it in your enterprise.

## Register an Existing Remote Data Store

A user registers a new remote data store with Windows Federated Search by opening an OpenSearch Description (.osdx) file. When the user does so, the following events occur:

1.  A .searchconnector-ms file (search connector) is created in the Windows Searches folder (%userprofile%/Searches).
2.  A shortcut to the .searchconnector-ms file is created in the Links folder (%userprofile%/Links).
3.  A shortcut appears in the Windows Explorer navigation **Favorites** pane, enabling the user to navigate into the new data store, and query the web service.

> [!Note]  
> A data store that already has an [OpenSearch](https://github.com/dewitt/opensearch) web service that is compatible with Windows Federated Search can be added to Windows Explorer when a user opens an .osdx file.

 

## Additional Resources

For additional information about implementing search federation to remote data stores using OpenSearch technologies in Windows 7 and later, see "Additional Resources" at [Federated Search in Windows](/previous-versions//dd742958(v=vs.85)).

## Related topics

<dl> <dt>

[Federated Search in Windows](-search-federated-search-overview.md)
</dt> <dt>

[Getting Started with Federated Search in Windows](getting-started-with-federated-search-in-windows.md)
</dt> <dt>

[Enabling Your Data Store in Windows Federated Search](-search-federated-search-data-store.md)
</dt> <dt>

[Creating an OpenSearch Description File in Windows Federated Search](-search-federated-search-osdx-file.md)
</dt> <dt>

[Following Best Practices in Windows Federated Search](-search-fedsearch-best.md)
</dt> <dt>

[Deploying Search Connectors in Windows Federated Search](-search-federated-search-deploying.md)
</dt> </dl>

 

 
