---
title: IScopeAdm interface
description: Manages a scope definition for a catalog within Indexing Service.
ms.assetid: '6958c7b7-642d-41a6-a84a-fa09df4ce1bb'
keywords: ["IScopeAdm interface Indexing Service", "IScopeAdm interface Indexing Service , described"]
topic_type:
- apiref
api_name:
- IScopeAdm
api_type:
- COM
---

# IScopeAdm interface

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Manages a scope definition for a catalog within Indexing Service. Use scope objects to force rescans and modify logon information for remote scopes. A scope defines a path to a local, remote, or virtual directory. You can create scope objects through the [**AddScope**](icatadm-addscope.md), [**GetScopeByPath**](icatadm-getscopebypath.md), or [**GetScopeByAlias**](icatadm-getscopebyalias.md) methods of [**ICatAdm**](icatadm.md).

## Members

The **IScopeAdm** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IScopeAdm** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IScopeAdm** interface has these methods.



| Method                                         | Description                                       |
|:-----------------------------------------------|:--------------------------------------------------|
| [**Rescan**](iscopeadm-rescan.md)             | Triggers a full or incremental rescan.<br/> |
| [**SetLogonInfo**](iscopeadm-setlogoninfo.md) | Sets name, password pair.<br/>              |



 

### Properties

The **IScopeAdm** interface has these properties.



| Property                                                  | Access type           | Description                                                                |
|:----------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------|
| [**Alias**](iscopeadm-alias.md)<br/>               | Read/write<br/> | The friendly name for the scope object.<br/>                         |
| [**ExcludeScope**](iscopeadm-excludescope.md)<br/> | Read/write<br/> | Indicates whether to index this scope.<br/>                          |
| [**Logon**](iscopeadm-logon.md)<br/>               | Read-only<br/>  | The logon name. <br/>                                                |
| [**Path**](iscopeadm-path.md)<br/>                 | Read/write<br/> | The case-insensitive scope path to the directory to be indexed.<br/> |
| [**VirtualScope**](iscopeadm-virtualscope.md)<br/> | Read-only<br/>  | Indicates whether this scope is a virtual path.<br/>                 |



 

## Remarks

Scope objects can be created only through the defined methods of [**ICatAdm**](icatadm.md).

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |
| End of client support<br/>    | Windows 7<br/>                                       |
| End of server support<br/>    | Windows Server 2008 R2<br/>                          |



 

 





