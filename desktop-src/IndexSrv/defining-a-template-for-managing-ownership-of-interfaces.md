---
title: Defining a Template for Managing Ownership of Interfaces
description: Defining a Template for Managing Ownership of Interfaces
ms.assetid: 89d32113-1b42-4e6e-97e7-3f44f7c2b073
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Defining a Template for Managing Ownership of Interfaces

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following code segment defines a template to aid in the management of interface ownership. The sample uses this template with the [ICommand](https://msdn.microsoft.com/windows/desktop/089427ad-5ba3-4613-b89e-8e86420ccc30), [ICommandTree](/previous-versions/windows/desktop/api/cmdtree/nn-cmdtree-icommandtree), [IRowset](https://msdn.microsoft.com/windows/desktop/b14147c4-8b03-49c6-ab5d-00186643a6b4), [IAccessor](https://msdn.microsoft.com/windows/desktop/a39058b6-ecfa-418b-80a3-66eea4a7bf89), and other interfaces.


```C++
template<class T> class XInterface
{
public:
    XInterface( T * p = 0 ) : _p( p ) {}
    ~XInterface() { if ( 0 != _p ) _p->Release(); }
    T * operator->() { return _p; }
    T * GetPointer() const { return _p; }
    IUnknown ** GetIUPointer() { return (IUnknown **) &amp;_p; }
    T ** GetPPointer() { return &amp;_p; }
    void ** GetQIPointer() { return (void **) &amp;_p; }
    T * Acquire() { T * p = _p; _p = 0; return p; }
    BOOL IsNull() { return ( 0 == _p ); }

private:
    T * _p;
};
```



 

 




