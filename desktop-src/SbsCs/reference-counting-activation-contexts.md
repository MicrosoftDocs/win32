---
Description: 'Activation contexts are reference-counted objects. Your application must have a reference on an activation context in order to use it.'
ms.assetid: '2dc8ffc5-0a65-4227-b93a-30c3cf0d3c2d'
title: Reference Counting Activation Contexts
---

# Reference Counting Activation Contexts

Activation contexts are reference-counted objects. Your application must have a reference on an activation context in order to use it. The functions of the Activation Context API that take an activation context can perform their own reference counting. For example, [**ActivateActCtx**](activateactctx.md) increases and [**DeactivateActCtx**](deactivateactctx.md) decreases the reference count. If however your application passes an activation context without using these functions, the application should provide its own method of reference counting.

When an application calls [**CreateActCtx**](createactctx.md), the handle returned will have a reference count of one. After the application finishes with the activation context, the handle should be released and the reference count decreased by calling [**ReleaseActCtx**](releaseactctx.md). Do not attempt to use [**LocalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366730), [**HeapFree**](https://msdn.microsoft.com/library/windows/desktop/aa366701), or any other memory-management functions on the activation context handle.

The following example shows a method for handling reference counting over the lifetime of an activation context. The function Funct creates an activation context, which it then passes to the object Target, which increments the reference count to 2. Funct then releases its reference on the activation context and decreases the reference count back to 1. Target then owns releasing its own reference when SetActCtx is called again or when the object is destroyed.


```C++
#include <windows.h>

class CMyObject 
{
private:
    HANDLE m_hActCtx;
public:
    CMyObject() : m_hActCtx(INVALID_HANDLE_VALUE) { }
    ~CMyObject() 
    { 
        if (m_hActCtx != INVALID_HANDLE_VALUE) 
        {
            ReleaseActCtx(m_hActCtx);
            m_hActCtx = INVALID_HANDLE_VALUE;
        }
    }
    void SetActCtx(HANDLE hActCtx) 
    {
        if (m_hActCtx != INVALID_HANDLE_VALUE) 
        {
            ReleaseActCtx(m_hActCtx);
        }
        m_hActCtx = hActCtx;
        if (m_hActCtx != INVALID_HANDLE_VALUE) 
        {
            AddRefActCtx(m_hActCtx);
        }
    }
    void DoWorkWithActCtx();
};

void Funct(CMyObject &amp;Target) 
{
    HANDLE hActCtx;
    ACTCTX actctx = { sizeof(ACTCTX) };
    hActCtx = CreateActCtx(&amp;actctx);  //create activation context  
    Target.SetActCtx(hActCtx);    //pass activation context to Target; 
    // actctx now has 1 more reference
    ReleaseActCtx(hActCtx);
}
```



 

 



