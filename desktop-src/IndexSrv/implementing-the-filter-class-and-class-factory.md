---
Description: Implementing the Filter Class and Class Factory
ms.assetid: b9dcc4d2-08d2-4550-a23e-2aeaef0e55f6
title: Implementing the Filter Class and Class Factory
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Filter Class and Class Factory

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

At least two classes, such as **CFilter** and **CFilterCF**, are typically implemented by each filter DLL.

The **CFilter** class produces the filter object that implements the content-filtering functionality. Its member functions implement the interface methods of the filter. Each filter class requires a unique class identifier (CLSID), which the filter implementer generates.

The **CFilterCF** class produces the class-factory object for the filter. The class factory is called, through its [**IClassFactory**](https://www.bing.com/search?q=**IClassFactory**) interface, by the [DllGetClassObject](https://www.bing.com/search?q=DllGetClassObject) entry point of the DLL. The **CFilterCF** class creates the **CFilter** object and returns a pointer to its [**IUnknown**](https://www.bing.com/search?q=**IUnknown**) interface.

In complex cases, a filter can implement a class hierarchy in place of the single **CFilter** class.

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 



