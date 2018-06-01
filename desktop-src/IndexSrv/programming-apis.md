---
Description: Each programming language has several APIs that communicate with Indexing Service, and you can choose the API most suitable for a task.
ms.assetid: ede1c59d-bf95-4a8d-9190-947b5a8a630f
title: Programming APIs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Programming APIs

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Each programming language has several APIs that communicate with Indexing Service, and you can choose the API most suitable for a task. When you choose an API, you can balance programming complexity with application performance. In general, the OLE DB Provider API is the most difficult API to program, but it is the most flexible and executes fastest. APIs that encapsulate the OLE DB Provider (such as Admin Helper or Query Helper) are easier to program, but they are less flexible and slower in execution. If you have a choice, consider this tradeoff when selecting an API.

The following table lists the APIs available for performing Indexing Service tasks and gives a brief description of each.



| API                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="_idxs_ole_db_provider_api"></span><span id="_IDXS_OLE_DB_PROVIDER_API"></span>OLE DB Provider                                | The lowest-level API for querying with Indexing Service. It specializes the COM interfaces of standard [Microsoft OLE DB](https://msdn.microsoft.com/windows/desktop/cbf78f34-597e-4abf-874b-d123b424f43b) to access Indexing Service data. It's the highest performance, but most complex, API and is usually used with C++ programs.                                                                                                        |
| <span id="_idxs_ole_db_helper_api"></span><span id="_IDXS_OLE_DB_HELPER_API"></span>OLE DB Helper                                      | A high-level API for querying and filtering with Indexing Service. It provides a [functional interface](functions.md) for accessing Indexing Service data, primarily from C++ language programs.                                                                                                                                                                                                  |
| <span id="_idxs_activex_data_objects_api"></span><span id="_IDXS_ACTIVEX_DATA_OBJECTS_API"></span>Microsoft ActiveX Data Objects (ADO) | An intermediate-level API for querying Indexing Service. It provides an [automation layer](https://www.bing.com/search?q=automation layer) between the OLE DB Provider and automation languages for accessing Indexing Service data.                                                                                                                                                                                             |
| <span id="_idxs_admin_helper_api"></span><span id="_IDXS_ADMIN_HELPER_API"></span>Admin Helper                                         | A high-level API for managing Indexing Service. It provides an [object-based interface](objects.md) to Indexing Service from automation languages.                                                                                                                                                                                                                                                |
| <span id="_idxs_query_helper_api"></span><span id="_IDXS_QUERY_HELPER_API"></span>Query Helper                                         | A high-level API for querying Indexing Service. It provides an [object-based interface](objects.md) for accessing Indexing Service data from automation languages.                                                                                                                                                                                                                                |
| <span id="_idxs_isapi_extensions_api"></span><span id="_IDXS_ISAPI_EXTENSIONS_API"></span>ISAPI Extensions                             | An intermediate-level, high-performance API extension to the Internet Server Applications Programming Interface (ISAPI). It provides access for managing and querying Indexing Service from Internet Information Services (IIS) applications. For information about ISAPI extensions, see the Programmer's Guide in the [Internet Information Services SDK](https://msdn.microsoft.com/windows/desktop/b1073d67-0cfd-42cb-b62b-97e670a4eafb). |
| <span id="_idxs_ifilter_component_api"></span><span id="_IDXS_IFILTER_COMPONENT_API"></span>IFilter Component                          | A low-level, customizable [COM interface](/windows/desktop/api/Filter/nn-filter-ifilter), usually written in C++, for extracting text and values from documents.                                                                                                                                                                                                                                                                     |
| Language Resources                                                                                                                     | [IWordBreaker](https://www.bing.com/search?q=IWordBreaker) and [IStemmer](https://www.bing.com/search?q=IStemmer) implementations that allow the Index and Querying components of Indexing Service to access documents in their native languages and locales.                                                                                                                                                                                |



 

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 



