---
title: Asking an Object for an Interface
description: Asking an Object for an Interface
ms.assetid: 04296372-4897-426e-9be3-e6862a530ac6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Asking an Object for an Interface

We saw earlier that an object can implement more than one interface. The Common Item Dialog object is a real-world example of this. To support the most typical uses, the object implements the [**IFileOpenDialog**](https://msdn.microsoft.com/library/windows/desktop/bb775834) interface. This interface defines basic methods for displaying the dialog box and getting information about the selected file. For more advanced use, however, the object also implements an interface named [**IFileDialogCustomize**](https://msdn.microsoft.com/library/windows/desktop/bb775912). A program can use this interface to customize the appearance and behavior of the dialog box, by adding new UI controls.

Recall that every COM interface must inherit, directly or indirectly, from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. The following diagram shows the inheritance of the Common Item Dialog object.

![diagram that shows interfaces exposed by the common item dialog object](images/com06.png)

As you can see from the diagram, the direct ancestor of [**IFileOpenDialog**](https://msdn.microsoft.com/library/windows/desktop/bb775834) is the [**IFileDialog**](https://msdn.microsoft.com/library/windows/desktop/bb775966) interface, which in turn inherits [**IModalWindow**](https://msdn.microsoft.com/library/windows/desktop/bb761686). As you go up the inheritance chain from **IFileOpenDialog** to **IModalWindow**, the interfaces define increasingly generalized window functionality. Finally, the **IModalWindow** interface inherits [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509). The Common Item Dialog object also implements [**IFileDialogCustomize**](https://msdn.microsoft.com/library/windows/desktop/bb775912), which exists in a separate inheritance chain.

Now suppose that you have a pointer to the [**IFileOpenDialog**](https://msdn.microsoft.com/library/windows/desktop/bb775834) interface. How would you get a pointer to the [**IFileDialogCustomize**](https://msdn.microsoft.com/library/windows/desktop/bb775912) interface?

![diagram that shows two interface pointers to interfaces on the same object](images/com07.png)

Simply casting the [**IFileOpenDialog**](https://msdn.microsoft.com/library/windows/desktop/bb775834) pointer to an [**IFileDialogCustomize**](https://msdn.microsoft.com/library/windows/desktop/bb775912) pointer will not work. There is no reliable way to "cross cast" across an inheritance hierarchy, without some form of run-time type information (RTTI), which is a highly language-dependent feature.

The COM approach is to *ask* the object to give you an [**IFileDialogCustomize**](https://msdn.microsoft.com/library/windows/desktop/bb775912) pointer, using the first interface as a conduit into the object. This is done by calling the [**IUnknown::QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) method from the first interface pointer. You can think of **QueryInterface** as a language-independent version of the **dynamic\_cast** keyword in C++.

The [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) method has the following signature:

``` syntax
HRESULT QueryInterface(REFIID riid, void **ppvObject);
```

Based on what you already know about [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615), you might be able to guess how [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) works.

-   The *riid* parameter is the GUID that identifies the interface you are asking for. The data type **REFIID** is a **typedef** for `const GUID&`. Notice that the class identifier (CLSID) is not required, because the object has already been created. Only the interface identifier is necessary.
-   The *ppvObject* parameter receives a pointer to the interface. The data type of this parameter is **void\*\***, for the same reason that [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) uses this data type: [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) can be used to query for any COM interface, so the parameter cannot be strongly typed.

Here is how you would call [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) to get an [**IFileDialogCustomize**](https://msdn.microsoft.com/library/windows/desktop/bb775912) pointer:


```C++
hr = pFileOpen->QueryInterface(IID_IFileDialogCustomize, 
    reinterpret_cast<void**>(&amp;pCustom));
if (SUCCEEDED(hr))
{
    // Use the interface. (Not shown.)
    // ...

    pCustom->Release();
}
else
{
    // Handle the error.
}
```



As always, check the **HRESULT** return value, in case the method fails. If the method succeeds, you must call [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) when you are done using the pointer, as described in [Managing the Lifetime of an Object](managing-the-lifetime-of-an-object.md).

## Next

[Memory Allocation in COM](memory-allocation-in-com.md)

 

 




