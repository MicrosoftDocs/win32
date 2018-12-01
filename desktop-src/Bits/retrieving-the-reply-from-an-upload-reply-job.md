---
title: Retrieving the Reply from an Upload-Reply Job
description: To upload data to a server application and have it return data to the client, specify the job as a BG\_JOB\_TYPE\_UPLOAD\_REPLY job.
ms.assetid: bab28a2c-1e2f-4b76-9dc6-57df26f7efec
ms.topic: article
ms.date: 11/29/2018
---

# Retrieving the Reply from an Upload-Reply Job

A BITS Upload-Reply job, in addition to uploading a file to a server, will also examine a reply URL sent as part of the server reply and then automatically follow the reply URL and download a response from it. See the [Ack for Fragment](/windows/desktop/Bits/ack-for-fragment) documentation for more details about the BITS-Reply-URL header value.

Set the job type as BG\_JOB\_TYPE\_UPLOAD\_REPLY to create an Upload-Reply type job. The reply data is available to the client after the job enters the BG\_JOB\_STATE\_TRANSFERRED state. To retrieve the reply, call one of the following methods:

-   [**IBackgroundCopyJob2::GetReplyData**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-getreplydata)

    Provides an in-memory copy of the reply data. Use this method to read the reply data before or after calling the [**IBackgroundCopyJob::Complete**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-complete) method. If the reply data exceeds 1 MB, the application must call the [**IBackgroundCopyJob2::GetReplyFileName**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-getreplyfilename) method to retrieve the name of the reply file and read its contents directly.

-   [**IBackgroundCopyJob2::GetReplyFileName**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-getreplyfilename)

    Provides the name of the file that contains the reply. You must call the **IBackgroundCopyJob::Complete** method before opening and reading the reply file; the reply file is not available to the client until you call the **Complete** method.

Call these methods in your [**IBackgroundCopyCallback::JobTransferred**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopycallback-jobtransferred) method only if the reply is small and can be processed quickly so as to not block the callback thread. If you use [**command line notification**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setnotifycmdline) instead of the callback, pass the job identifier to the executable file. The executable file uses the job identifier to call the **Complete** method to make the reply file available.

The following examples show how to use each method to retrieve the reply data.

-   [Using GetReplyData](#using-getreplydata)
-   [Using GetReplyFileName](#using-getreplyfilename)

## Using GetReplyData

The following example shows how to retrieve the reply data using the [**IBackgroundCopyJob2::GetReplyData**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-getreplydata) method. The example assumes the [**IBackgroundCopyJob**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) interface pointer is valid, the type of the job is upload-reply, and the state of the job is BG\_JOB\_STATE\_TRANSFERRED.


```C++
HRESULT hr;
IBackgroundCopyJob* pJob;
IBackgroundCopyJob2* pJob2 = NULL;
BYTE* pReply = NULL;
UINT64 ReplySize;

//Need to query the IBackgroundCopyJob interface for an IBackgroundCopyJob2
//interface pointer. The IBackgroundCopyJob2 interface contains the GetReplyData method.
hr = pJob->QueryInterface(__uuidof(IBackgroundCopyJob2), (void**)&pJob2);
if (SUCCEEDED(hr))
{
    hr = pJob2->GetReplyData(&pReply, &ReplySize);
    if (S_OK == hr))
    {
        if (pReply)
        {
            //Do something with the data.
            CoTaskMemFree(pReply);
        }
        else
        {
            //The server application did not return a reply.
        }
    }
    else if (BG_E_TOO_LARGE == hr)
    {
        //The reply exceeds 1 MB. To retrieve the reply, get the reply file name,
        //complete the job, open the reply file, and read the reply.
    }
    else
    {
        //Handle the error
    }

    pJob2->Release(); //When done, release the interface.
}
else
{
    //Handle error. QueryInterface will return E_NOINTERFACE if the version of BITS
    //running on the computer is less than BITS 1.5.
}
```



## Using GetReplyFileName

The following example shows how to retrieve the reply data using the [**IBackgroundCopyJob2::GetReplyFileName**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-getreplyfilename) method. The example assumes the [**IBackgroundCopyJob**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) interface pointer is valid, the type of job is upload-reply, and the state of the job is BG\_JOB\_STATE\_TRANSFERRED.


```C++
HRESULT hr;
IBackgroundCopyJob* pJob;
IBackgroundCopyJob2* pJob2 = NULL;
WCHAR* pszFileName = NULL;

//Need to query the IBackgroundCopyJob interface for an IBackgroundCopyJob2
//interface pointer. The IBackgroundCopyJob2 interface contains the GetReplyFileName method.
hr = pJob->QueryInterface(__uuidof(IBackgroundCopyJob2), (void**)&pJob2);
if (SUCCEEDED(hr))
{
    hr = pJob2->GetReplyFileName(&pszFileName);
    if (SUCCEEDED(hr))
    {
        //Calling the Complete method removes the job from the queue, 
        //so make sure you maintain an interface pointer to this job 
        //or retrieve any job related information that you require 
        //when processing the reply.
        hr = pJob->Complete();

        //Open, read the file, and do something with the data.
        CoTaskMemFree(pszFileName);
    }

    pJob2->Release(); //When done, release the interface.
}
else
{
    //Handle error. QueryInterface will return E_NOINTERFACE if the version of BITS
    //running on the computer is less than BITS 1.5.
}
```



 

 




