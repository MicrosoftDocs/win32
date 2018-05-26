---
title: Implementing the COM Interface Methods
description: Implementing the COM Interface Methods
ms.assetid: 7a0cf599-5698-4ff7-8502-6785a0c9ef25
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing the COM Interface Methods

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The filter implements the [IUnknown](_com_iunknown) methods for both the filter class and the filter-class factory. The following table lists, in vtable order, the filter-specific interfaces and methods that the filter must also implement. The filter must implement at least one, and can implement several, of the [IPersist](_com_ipersist) derived interfaces.



| Interface                                          | Method                                                                                                                                                                                                                                                             |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IClassFactory](_com_iclassfactory)<br/>     | [CreateInstance](_com_iclassfactory_createinstance)<br/> [LockServer](_com_iclassfactory_lockserver)<br/>                                                                                                                                              |
| [IFilter](/windows/win32/Filter/nn-filter-ifilter?branch=master)<br/>                  | [Init](/windows/win32/Filter/nf-filter-ifilter-init?branch=master)<br/> [GetChunk](/windows/win32/Filter/nf-filter-ifilter-getchunk?branch=master)<br/> [GetText](/windows/win32/Filter/nf-filter-ifilter-gettext?branch=master)<br/> [GetValue](/windows/win32/Filter/nf-filter-ifilter-getvalue?branch=master)<br/> [BindRegion](/windows/win32/Filter/nf-filter-ifilter-bindregion?branch=master)<br/>                                              |
| [IPersist](_com_ipersist)<br/>               | [GetClassID](_com_ipersist_getclassid)<br/>                                                                                                                                                                                                                  |
| [IPersistFile](_com_ipersistfile)<br/>       | [IsDirty](_com_ipersistfile_isdirty)<br/> [Load](_com_ipersistfile_load)<br/> [Save](_com_ipersistfile_save)<br/> [SaveCompleted](_com_ipersistfile_savecompleted)<br/> [GetCurFile](_com_ipersistfile_getcurfile)<br/>              |
| [IPersistStorage](_com_ipersiststorage)<br/> | [IsDirty](_com_ipersiststorage_isdirty)<br/> [InitNew](_com_ipersiststorage_initnew)<br/> [Load](_com_ipersiststorage_load)<br/> [Save](_com_ipersiststorage_save)<br/> [HandsOffStorage](_com_ipersiststorage_handsoffstorage)<br/> |
| [IPersistStream](_com_ipersiststream)<br/>   | [IsDirty](_com_ipersiststream_isdirty)<br/> [Load](_com_ipersiststream_load)<br/> [Save](_com_ipersiststream_save)<br/> [GetSizeMax](_com_ipersiststream_getsizemax)<br/>                                                                  |



 

The reference page for each method specifies the parameters and functional behavior for that method. Each reference page also gives the result codes to implement for that method. The reference pages for the [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) methods give the interface-specific (**FACILITY\_ITF**) result codes to be implemented, and the content-indexing client can also handle any of the generic (**FACILITY\_NULL** and **FACILITY\_WIN32**) result codes.

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 





