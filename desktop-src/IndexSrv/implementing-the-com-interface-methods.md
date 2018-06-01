---
Description: Implementing the COM Interface Methods
ms.assetid: 7a0cf599-5698-4ff7-8502-6785a0c9ef25
title: Implementing the COM Interface Methods
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the COM Interface Methods

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The filter implements the [IUnknown](https://www.bing.com/search?q=IUnknown) methods for both the filter class and the filter-class factory. The following table lists, in vtable order, the filter-specific interfaces and methods that the filter must also implement. The filter must implement at least one, and can implement several, of the [IPersist](https://www.bing.com/search?q=IPersist) derived interfaces.



| Interface                                          | Method                                                                                                                                                                                                                                                             |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IClassFactory](https://www.bing.com/search?q=IClassFactory)<br/>     | [CreateInstance](https://www.bing.com/search?q=CreateInstance)<br/> [LockServer](https://www.bing.com/search?q=LockServer)<br/>                                                                                                                                              |
| [IFilter](/windows/desktop/api/Filter/nn-filter-ifilter)<br/>                  | [Init](/windows/desktop/api/Filter/nf-filter-ifilter-init)<br/> [GetChunk](/windows/desktop/api/Filter/nf-filter-ifilter-getchunk)<br/> [GetText](/windows/desktop/api/Filter/nf-filter-ifilter-gettext)<br/> [GetValue](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue)<br/> [BindRegion](/windows/desktop/api/Filter/nf-filter-ifilter-bindregion)<br/>                                              |
| [IPersist](https://www.bing.com/search?q=IPersist)<br/>               | [GetClassID](https://www.bing.com/search?q=GetClassID)<br/>                                                                                                                                                                                                                  |
| [IPersistFile](https://www.bing.com/search?q=IPersistFile)<br/>       | [IsDirty](https://www.bing.com/search?q=IsDirty)<br/> [Load](https://www.bing.com/search?q=Load)<br/> [Save](https://www.bing.com/search?q=Save)<br/> [SaveCompleted](https://www.bing.com/search?q=SaveCompleted)<br/> [GetCurFile](https://www.bing.com/search?q=GetCurFile)<br/>              |
| [IPersistStorage](https://www.bing.com/search?q=IPersistStorage)<br/> | [IsDirty](https://www.bing.com/search?q=IsDirty)<br/> [InitNew](https://www.bing.com/search?q=InitNew)<br/> [Load](https://www.bing.com/search?q=Load)<br/> [Save](https://www.bing.com/search?q=Save)<br/> [HandsOffStorage](https://www.bing.com/search?q=HandsOffStorage)<br/> |
| [IPersistStream](https://www.bing.com/search?q=IPersistStream)<br/>   | [IsDirty](https://www.bing.com/search?q=IsDirty)<br/> [Load](https://www.bing.com/search?q=Load)<br/> [Save](https://www.bing.com/search?q=Save)<br/> [GetSizeMax](https://www.bing.com/search?q=GetSizeMax)<br/>                                                                  |



 

The reference page for each method specifies the parameters and functional behavior for that method. Each reference page also gives the result codes to implement for that method. The reference pages for the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) methods give the interface-specific (**FACILITY\_ITF**) result codes to be implemented, and the content-indexing client can also handle any of the generic (**FACILITY\_NULL** and **FACILITY\_WIN32**) result codes.

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 




