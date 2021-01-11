---
description: This topic describes how to use the XPS Print API to print from a Windows application.
ms.assetid: 3d7ab169-412c-434f-a865-4da4af370eaf
title: 'How To: Print with the XPS Print API'
ms.topic: article
ms.date: 05/31/2018
---

# How To: Print with the XPS Print API

This topic describes how to use the [XPS Print API](xpsprint-api.md) to print from a Windows application.

The [XPS Print API](xpsprint-api.md) enables native Windows applications to print XPS documents. An application can create an XPS document by using the [XPS Document API](/previous-versions/windows/desktop/dd316976(v=vs.85)). The [Common XPS Document Programming Tasks](/previous-versions/windows/desktop/dd316968(v=vs.85)) help topic describes how to do this. Once an XPS document has been created, the application can use the XPS Print API to print it.

Using the [XPS Print API](xpsprint-api.md) to print a document from an application involves the following steps.

-   [Initialize COM Interface](#initialize-com-interface)
-   [Create a Completion Event](#create-a-completion-event)
-   [Start an XPS Print Job](#start-an-xps-print-job)
-   [Create an IXpsOMPackageWriter Interface](#create-an-ixpsompackagewriter-interface)
-   [Close the IXpsOMPackageWriter Interface](#close-the-ixpsompackagewriter-interface)
-   [Close the Print Job Stream](#close-the-print-job-stream)
-   [Wait for the Completion Event](#wait-for-the-completion-event)
-   [Release Resources](#release-resources)

The [XPS Print API](xpsprint-api.md) requires an XPS document to print. In the following example, the XPS document is created as it is sent to the printer by the XPS Print API. It is also possible to create an XPS document without sending it to a printer by using the [XPS Document API](/previous-versions/windows/desktop/dd316976(v=vs.85)) and maintaining it as an XPS OM or by saving the XPS OM as an XPS document. For more information about using an XPS OM, see the XPS Document API.

### Initialize COM Interface

Initialize the COM interface, if the application has not already done so.


```C++
    // Initialize the COM interface, if the application has not 
    //  already done so.
    if (FAILED(hr = CoInitializeEx(0, COINIT_MULTITHREADED)))
    {
        fwprintf(stderr, 
            L"ERROR: CoInitializeEx failed with HRESULT 0x%X\n", hr);
        return 1;
    }
```



### Create a Completion Event

Create a completion event, which the [XPS Print API](xpsprint-api.md) uses to notify the application when the print spooler has received the entire document from the application. The XPS Print API also supports a progress event so an application can know about other spooling activity.


```C++
        // Create the completion event
        completionEvent = CreateEvent(NULL, TRUE, FALSE, NULL);
        if (!completionEvent)
        {
            hr = HRESULT_FROM_WIN32(GetLastError());
            fwprintf(stderr, 
                L"ERROR: Could not create completion event: %08X\n", hr);
        }
```



### Start an XPS Print Job

Start an XPS print job by calling [**StartXpsPrintJob**](/windows/desktop/api/XpsPrint/nf-xpsprint-startxpsprintjob). **StartXpsPrintJob** returns a stream into which the application will send the document to be printed.


```C++
        // Start an XPS Print Job
        if (FAILED(hr = StartXpsPrintJob(
                    printerName,
                    NULL,
                    NULL,
                    NULL,
                    completionEvent,
                    NULL,
                    0,
                    &job,
                    &jobStream,
                    NULL
                    )))
        {
            fwprintf(stderr, 
                L"ERROR: Could not start XPS print job: %08X\n", hr);
        }
```



### Create an IXpsOMPackageWriter Interface

Create an [**IXpsOMPackageWriter**](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) interface by calling [**IXpsOMObjectFactory::CreatePackageWriterOnStream**](/windows/win32/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomobjectfactory-createpackagewriteronstream) on the stream returned by [**StartXpsPrintJob**](/windows/desktop/api/XpsPrint/nf-xpsprint-startxpsprintjob).


```C++
    // Create an XPS OM Object Factory. If one has already been 
    //  created by the application, a new one is not necessary.
    if (SUCCEEDED(hr))
    {
        if (FAILED(hr = CoCreateInstance(
                __uuidof(XpsOMObjectFactory), 
                NULL,
                CLSCTX_INPROC_SERVER, 
                IID_PPV_ARGS(&xpsFactory))))
        {
            fwprintf(
                stderr, 
                L"ERROR: Could not create XPS OM Object Factory: %08X\n", 
                hr);
        }
    }
    // Create the Part URI for the Fixed Document Sequence. The
    //  Fixed Document Sequence is the top-level element in the
    //  package hierarchy of objects. There is one Fixed Document
    //  Sequence in an XPS document.
    //
    // The part name is not specified by the XML Paper Specification,
    //  however, the name used in this example is the part name
    //  used by convention.
    //
    if (SUCCEEDED(hr))
    {
        if (FAILED(hr = xpsFactory->CreatePartUri(
                    L"/FixedDocumentSequence.fdseq", 
                    &partUri)))
        {
            fwprintf(stderr, 
                L"ERROR: Could not create part URI: %08X\n", hr);
        }
    }

    // Create the package writer on the print job stream.
    if (SUCCEEDED(hr))
    {
        if (FAILED(hr = xpsFactory->CreatePackageWriterOnStream(
                    jobStream,
                    TRUE,
                    XPS_INTERLEAVING_ON,
                    partUri,
                    NULL,
                    NULL,
                    NULL,
                    NULL,
                    &packageWriter
                    )
                )
           )
        {
            fwprintf(
                stderr, 
                L"ERROR: Could not create package writer: 0x%X\n", 
                hr);
        }
    }

    // Release the part URI interface.
    if (partUri)
    {
        partUri->Release();
        partUri = NULL;
    }
```



For each document in this print job, start a new document and then add pages to that document.

### Start a New Document

Start a new document in the package writer by calling [**IXpsOMPackageWriter::StartNewDocument**](/windows/win32/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-startnewdocument). If a document is open when this method is called, it is closed and a new document is opened.


```C++
    // Create the Part URI for the Fixed Document. The
    //  Fixed Document part contains the pages of the document. 
    //  There can be one or more Fixed Documents in an XPS document.
    //
    // The part name is not specified by the XML Paper Specification,
    //  however, the name format used in this example is the format 
    //  used by convention. The number "1" in this example must be 
    //  changed for each document in the package. For example, 1 
    //  for the first document, 2 for the second, and so on.
    //

    if (SUCCEEDED(hr))
    {
        if (FAILED(hr = xpsFactory->CreatePartUri(
                    L"/Documents/1/FixedDocument.fdoc", 
                    &partUri)))
        {
            fwprintf(
                stderr, 
                L"ERROR: Could not create part URI: %08X\n", 
                hr);
        }
    }

    // Start the new document.
    //
    //  If there was already a document started in this page,
    //  this call will close it and start a new one.
    if (SUCCEEDED(hr))
    {
        if (FAILED(hr = packageWriter->StartNewDocument(
                    partUri, 
                    NULL, 
                    NULL, 
                    NULL,
                    NULL)))
        {
            fwprintf(
                stderr, 
                L"ERROR: Could not start new document: 0x%X\n", 
                hr);
        }
    }
    
    // Release the part URI interface
    if (partUri)
    {
        partUri->Release();
        partUri = NULL;
    }
```



### Add a Page

Call [**IXpsOMPackageWriter::AddPage**](/windows/win32/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-addpage) to write each of the document's pages from the application to the new document in the package writer.

> [!Note]  
> The application is assumed to have created the page prior to this step. For more information about creating document pages and adding content to them, see the [Common XPS Document Programming Tasks](/previous-versions/windows/desktop/dd316968(v=vs.85)).

 


```C++
    if (SUCCEEDED(hr))
    {
        // Add the current page to the document.
        if (FAILED(hr = packageWriter->AddPage(
                    xpsPage,
                    &pageSize,
                    NULL,
                    NULL,
                    NULL,
                    NULL
                    )))
        {
            fwprintf(
                stderr, 
                L"ERROR: Could not add page to document: %08X\n", 
                hr);
        }
    }
```



### Close the IXpsOMPackageWriter Interface

After all the documents have been written for this print job, call [**IXpsOMPackageWriter::Close**](/windows/win32/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-close) to close the package.


```C++
    if (SUCCEEDED(hr))
    {
        if (FAILED(hr = packageWriter->Close()))
        {
            fwprintf(
                stderr, 
                L"ERROR: Could not close package writer: %08X\n", 
                hr);
        }
    }
```



### Close the Print Job Stream

Close the print job stream by calling [**Close**](/windows/desktop/api/XpsPrint/nf-xpsprint-ixpsprintjobstream-close), which tells the print spooler that the entire print job has been sent by the application.


```C++
    if (SUCCEEDED(hr))
    {
        if (FAILED(hr = jobStream->Close()))
        {
            fwprintf(
                stderr,
                L"ERROR: Could not close job stream: %08X\n",
                hr);
        }
    }
    else
    {
        // Only cancel the job if we succeeded in creating a job.
        if (job)
        {
            // Tell the XPS Print API that we're giving up.  
            //  Don't overwrite hr with the return from this function.
            job->Cancel();
        }
    }
```



### Wait for the Completion Event

Wait for the print job's completion event.


```C++
    if (SUCCEEDED(hr))
    {
        wprintf(L"Waiting for job completion...\n");

        if (WaitForSingleObject(completionEvent, INFINITE) != 
                                                    WAIT_OBJECT_0)
        {
            hr = HRESULT_FROM_WIN32(GetLastError());
            fwprintf(
                stderr, 
                L"ERROR: Wait for completion event failed: %08X\n", 
                hr);
        }
    }
```



After the completion event is signaled, call [**GetJobStatus**](/windows/desktop/api/XpsPrint/nf-xpsprint-ixpsprintjob-getjobstatus) to get the job status.


```C++
    if (SUCCEEDED(hr))
    {
        if (FAILED(hr = job->GetJobStatus(&jobStatus)))
        {
            fwprintf(
                stderr, 
                L"ERROR: Could not get job status: %08X\n", 
                hr);
        }
    }

    if (SUCCEEDED(hr))
    {
        switch (jobStatus.completion)
        {
            case XPS_JOB_COMPLETED:
                break;
            case XPS_JOB_CANCELLED:
                fwprintf(stderr, L"ERROR: job was cancelled\n");
                hr = E_FAIL;
                break;
            case XPS_JOB_FAILED:
                fwprintf(
                    stderr, 
                    L"ERROR: Print job failed: %08X\n", 
                    jobStatus.jobStatus);
                hr = E_FAIL;
                break;
            default:
                fwprintf(stderr, L"ERROR: unexpected failure\n");
                hr = E_UNEXPECTED;
                break;
        }
    }
```



### Release Resources

After a job status indicates completion, release the interfaces and resources used for this print job.


```C++
    if (packageWriter)
    {
        packageWriter->Release();
        packageWriter = NULL;
    }

    if (partUri)
    {
        partUri->Release();
        partUri = NULL;
    }

    if (xpsFactory)
    {
        xpsFactory->Release();
        xpsFactory = NULL;
    }

    if (jobStream)
    {
        jobStream->Release();
        jobStream = NULL;
    }

    if (job)
    {
        job->Release();
        job = NULL;
    }

    if (completionEvent)
    {
        CloseHandle(completionEvent);
        completionEvent = NULL;
    }
```



 

 
