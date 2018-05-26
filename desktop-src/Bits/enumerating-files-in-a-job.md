---
title: Enumerating Files in a Job
description: To enumerate files in a job, call the IBackgroundCopyJob EnumFiles method. The method returns an IEnumBackgroundCopyFiles interface pointer that you use to enumerate the files.
ms.assetid: 0e1fa024-4576-434c-bc5f-518d246b5faa
keywords:
- transfer job BITS , enumerating files
- enumerating files BITS
- enumerating BITS , files
- file transfer BITS , enumerating
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Files in a Job

To enumerate files in a job, call the [**IBackgroundCopyJob::EnumFiles**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-enumfiles?branch=master) method. The method returns an [**IEnumBackgroundCopyFiles**](/windows/win32/Bits/nn-bits-ienumbackgroundcopyfiles?branch=master) interface pointer that you use to enumerate the files.

Note that the enumerated list is a snapshot of the files in the job at the time you call the [**EnumFiles**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-enumfiles?branch=master) method. However, the property values of those file objects reflect the current values of the file.

The following example shows how to enumerate files in a job and retrieve their properties. The example assumes the [**IBackgroundCopyJob**](/windows/win32/Bits/nn-bits-ibackgroundcopyjob?branch=master) interface pointer is valid.


```C++
HRESULT hr = 0;
IBackgroundCopyJob* pJob;
IEnumBackgroundCopyFiles* pFiles = NULL;
IBackgroundCopyFile* pFile = NULL;
IBackgroundCopyFile3* pFile3 = NULL;
WCHAR* pLocalFileName = NULL;
ULONG cFileCount = 0;
ULONG idx = 0;

hr = pJob->EnumFiles(&amp;pFiles);
if (SUCCEEDED(hr))
{
  //Get the count of files in the job. 
  pFiles->GetCount(&amp;cFileCount);

  //Enumerate the files in the job.
  for (idx=0; idx<cFileCount; idx++)
  {
    hr = pFiles->Next(1, &amp;pFile, NULL);
    if (S_OK == hr)
    {
      // Query for the latest file interface.
      hr = pFile->QueryInterface(__uuidof(IBackgroundCopyFile3), (void**)&amp;pFile3);
      pFile->Release();
      if (FAILED(hr))
      {
        wprintf(L"pFile->QueryInterface failed with 0x%x.\n", hr);
        goto cleanup;
      }

      // You can use the interface to retrieve the local and remote file
      // names, get the ranges to download if only part of the file content
      // is requested, determine the progress of the transfer, change the remote file
      // name, get the name of the temporary file that BITS uses to download
      // the file, determine if the file is downloaded from a peer, and set
      // the validation state of the file so it can be shared with peers.

      //Get the local name of the file.
      hr = pFile3->GetLocalName(&amp;pLocalFileName);
      if (SUCCEEDED(hr))
      {
        //Do something with the file information.
      }

      CoTaskMemFree(pLocalFileName); 
      pFile3->Release();
      pFile3 = NULL;
    }
    else
    {
      //Handle error
      break;
    }
  }

  pFiles->Release();
  pFiles = NULL;
}
```



 

 




