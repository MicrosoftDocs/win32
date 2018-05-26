---
title: Getting Started with the Packaging API
description: The Windows 7 Packaging feature is a set of COM-based APIs that provides support for accessing, modifying, and saving packages using C and C++. This topic includes the prerequisites and programming information needed to begin using the APIs.
ms.assetid: ef392c88-49cd-4ffa-b1fb-1501c6448264
keywords:
- packaging,Packaging APIs
- packages,Packaging APIs
- Packaging APIs,prerequisites
- Packaging APIs,about
- Packaging APIs,programming notes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Started with the Packaging API

The Windows 7 Packaging feature is a set of COM-based APIs that provides support for accessing, modifying, and saving packages using C and C++. This topic includes the prerequisites and programming information needed to begin using the APIs.

This topic contains the following sections.

-   [Prerequisites](#prerequisites)
-   [Header and IDL Files](#header-and-idl-files)
-   [Accessing the Packaging APIs: Creating a Factory](#accessing-the-packaging-apis-creating-a-factory)
-   [Packaging API Support for Previous Versions of Windows](#packaging-api-support-for-previous-versions-of-windows)
-   [Packaging API Programming Notes](#packaging-api-programming-notes)
    -   [COM Programming Notes](#com-programming-notes)
    -   [Multithreading Notes](#multithreading-notes)
    -   [Error Handling Notes](#error-handling-notes)
-   [Additional Resources](#additional-resources)
-   [Disclaimer](#disclaimer)
-   [Related topics](#related-topics)

## Prerequisites

For a table of prerequisites, see [Packaging](packaging.md).

## Header and IDL Files

The Packaging APIs are defined in the following header and IDL files:



| File      | Description                                                                            |
|-----------|----------------------------------------------------------------------------------------|
| msopc.h   | Header that defines C and C++ versions of the primary Packaging interfaces and errors. |
| msopc.idl | IDL that defines the primary Packaging interfaces.                                     |



 

## Accessing the Packaging APIs: Creating a Factory

Windows 7 provides a factory implementation of the [**IOpcFactory**](/windows/previous-versions/msopc/nn-msopc-iopcfactory?branch=master) interface, which you instantiate by calling the [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) function. Through this factory, the **IOpcFactory** interface provides a portal to other Packaging interfaces and objects.

To get started with the Packaging APIs, create a Packaging factory instance, as shown in the following code.


```C++
    IOpcFactory * factory = NULL;

    // Create a new factory.
    HRESULT hr = CoCreateInstance(
                    __uuidof(OpcFactory),
                    NULL,
                    CLSCTX_INPROC_SERVER,
                    __uuidof(IOpcFactory),
                    (LPVOID*)&amp;factory
                    );
```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>    if (factory)
    {
        factory-&gt;Release();
        factory = NULL;
    }</code></pre></td>
</tr>
</tbody>
</table>



[**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615), which is used to create a Packaging factory, must be called on a thread that is bound to a COM apartment. If the factory is created in a multithreaded apartment, you must synchronize access to Packaging objects.

Once created, the factory is not tied to any particular package and can be used as long as an application is running; however, you must release the factory by calling the interface's [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) method before calling the [**CoUninitialize**](https://msdn.microsoft.com/library/windows/desktop/ms688715) function and exiting the application.

## Packaging API Support for Previous Versions of Windows

The Platform Update for Windows Vista is a set of run-time libraries that enables developers to target applications to both Windows 7 and previous versions of Windows. The Platform Update for Windows Vista will be available to all Windows Vista customers through Windows Update. Third-party applications that require Platform Update for Windows Vista can have Windows Update detect whether it is installed; if it is not, Windows Update will download and install it in the background.

The Platform Update for Windows Vista provides the following support for the Packaging API.

-   [**IOpcUri**](/windows/previous-versions/msopc/nn-msopc-iopcuri?branch=master)
-   [**IOpcPartUri**](/windows/previous-versions/msopc/nn-msopc-iopcparturi?branch=master)
-   [**IOpcFactory**](/windows/previous-versions/msopc/nn-msopc-iopcfactory?branch=master) (only the following methods are supported)
    -   [**CreatePackageRootUri**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createpackagerooturi?branch=master)
    -   [**CreatePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createparturi?branch=master)
    -   [**CreateStreamOnFile**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createstreamonfile?branch=master)

Supported Packaging APIs can be used to create streams over files as well as to create and interact with package-based URI.

The behavior and performance of supported Packaging interfaces and methods are the same on all supported versions of Windows.

If an application attempts to instantiate or call an unsupported Packaging interface or method, the attempt will fail. If the call is to an unsupported [**IOpcFactory**](/windows/previous-versions/msopc/nn-msopc-iopcfactory?branch=master) method, the E\_NOTIMPL error code will be returned. For more information, see [Platform Update for Windows Vista](win7ip-platform_update_for_windows_vista_portal).

## Packaging API Programming Notes

### COM Programming Notes

When programming with Packaging APIs, remember the following:

-   The ThreadingModel used by the Packaging APIs is "Both", also known as the mixed-model.

    > \[!Caution\]  
    > Packaging objects are not thread-safe; the caller must synchronize access to Packaging objects.

     

-   The Packaging APIs do not support any form of marshaling across apartments; if the caller attempts to implement marshaling for Packaging interfaces the attempt will fail or cause undefined behavior.
-   Passing raw pointers to Packaging objects across apartments may lead to undefined behavior.

### Multithreading Notes

When programming with Packaging APIs in a multithreaded environment, adhere to the following guidelines:

-   If a thread and a Packaging object exist in the same apartment, the thread can call the object.
-   The [**CoInitializeEx**](https://msdn.microsoft.com/library/windows/desktop/ms695279) function must be called before a Packaging object is called by a thread.
-   \[!Caution\]  
    > The caller must synchronize access to Packaging objects.

     

-   If the **OPC\_CACHE\_ON\_ACCESS** value of the [**OPC\_READ\_FLAGS**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0004?branch=master) enumeration is used to load a package, the part content of different parts may be read concurrently by using distinct streams from distinct threads. This applies to the content accessed by calling either the [**IOpcPart::GetContentStream**](/windows/previous-versions/msopc/nf-msopc-iopcpart-getcontentstream?branch=master) or [**IOpcRelationshipSet::GetRelationshipsContentStream**](/windows/previous-versions/msopc/nf-msopc-iopcrelationshipset-getrelationshipscontentstream?branch=master) method. Potential performance improvements that are made possible by concurrent read operations are contingent on the implementation of the data source.
-   Different packages may be serialized concurrently, by calling [**IOpcFactory::WritePackageToStream**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-writepackagetostream?branch=master) and using distinct package objects and distinct streams.
-   Packaging objects that represent package components in different packages may be accessed concurrently by distinct threads.

The following operations will result in undefined behavior; errors that occur as a result of these operations may not be recoverable.

-   Concurrent attempts to modify the same package.
-   Concurrent attempts to read the same Packaging object.
-   Any attempt to access a Packaging object while the parent package is being serialized. The serialization operation will not be affected.
-   Any attempt to serialize a package while another serialization or deserialization operation on the package is already in progress.

### Error Handling Notes

When programming with the Packaging Digital Signature APIs, remember the following:

-   Some package signature related errors may not be exposed until the [**IOpcDigitalSignatureManager::Validate**](/windows/previous-versions/msopc/nf-msopc-iopcdigitalsignaturemanager-validate?branch=master) method is called.
-   Errors that are introduced into a package signature when the caller is using the [**IOpcSigningOptions**](/windows/previous-versions/msopc/nn-msopc-iopcsigningoptions?branch=master) interface to set signature information may not be exposed until [**IOpcDigitalSignatureManager::Sign**](/windows/previous-versions/msopc/nf-msopc-iopcdigitalsignaturemanager-sign?branch=master) is called.

The following Packaging APIs and Packaging objects can still execute or be accessed successfully after an error is encountered.

-   Part content streams that have been cached will be accessible.
-   If the relationships contained in a Relationships part have been parsed successfully and cached, the [**IOpcRelationshipSet::GetRelationshipsContentStream**](/windows/previous-versions/msopc/nf-msopc-iopcrelationshipset-getrelationshipscontentstream?branch=master) method can be called from the [**IOpcRelationshipSet**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipset?branch=master) interface pointer that represents that part. Relationships are cached when they are modified.

## Additional Resources

While not required to use the Packaging API, knowledge of the following technologies will advance your understanding of the Packaging API.



| Technology                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Markup Compatibility requirements in the [ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375) standard | If your application interacts with packages that comply with different editions of the ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC), familiarity with markup compatibility requirements will be helpful in developing your application. For more information, see 1st edition, Part 5: Markup Compatibility in the [ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375) (http://go.microsoft.com/fwlink/p/?linkid=123375).<br/> |



 

## Disclaimer

Code examples are not intended to be complete and working programs. The code examples that are referenced on this page, for example, do not perform parameter checking, error checking, or error handling. Use these examples as a starting point, then add the code necessary to create a robust application. For more information about error handling in COM, see the [Error Handling (COM)](_com_Error_Handling) topic.

## Related topics

<dl> <dt>

[Packaging API Programming Guide](packaging-programming-guide.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Open Packaging Conventions Fundamentals](open-packaging-conventions-overview.md)
</dt> <dt>

[Platform Update for Windows Vista](win7ip-platform_update_for_windows_vista_portal)
</dt> <dt>

[Understanding and Using COM Threading Models](comthreading)
</dt> <dt>

**Reference**
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> </dl>

 

 





