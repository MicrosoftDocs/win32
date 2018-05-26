---
title: Adding Files to a Job
description: A job contains one or more files that you want to transfer.
ms.assetid: fb6e7219-b6ca-4f72-b7a3-60d65e8f3892
keywords:
- transfer job BITS , adding files
- file transfer BITS , adding
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Adding Files to a Job

A job contains one or more files that you want to transfer. Use one of the following methods to add files to a job:

<dl> <dt>

<span id="IBackgroundCopyJob__AddFile"></span><span id="ibackgroundcopyjob__addfile"></span><span id="IBACKGROUNDCOPYJOB__ADDFILE"></span>[**IBackgroundCopyJob::AddFile**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-addfile?branch=master)
</dt> <dd>

Adds a single file to a job.

</dd> <dt>

<span id="IBackgroundCopyJob__AddFileSet"></span><span id="ibackgroundcopyjob__addfileset"></span><span id="IBACKGROUNDCOPYJOB__ADDFILESET"></span>[**IBackgroundCopyJob::AddFileSet**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-addfileset?branch=master)
</dt> <dd>

Adds one or more files to a job. If you are adding multiple files, it is more efficient to call this method than to call the **AddFile** method in a loop.

</dd> <dt>

<span id="IBackgroundCopyJob3__AddFileWithRanges"></span><span id="ibackgroundcopyjob3__addfilewithranges"></span><span id="IBACKGROUNDCOPYJOB3__ADDFILEWITHRANGES"></span>[**IBackgroundCopyJob3::AddFileWithRanges**](/windows/win32/Bits2_0/nf-bits2_0-ibackgroundcopyjob3-addfilewithranges?branch=master)
</dt> <dd>

Adds a single file to a job. Use this method if you want to download ranges of data from a file. You can use this method only for download jobs.

</dd> </dl>

When you add a file to a job, you specify the remote name and the local name of the file. For details on the format of the local and remote file names, see the [**BG\_FILE\_INFO**](/windows/win32/Bits/ns-bits-_bg_file_info?branch=master) structure.

An upload job can contain only one file. The [**IBackgroundCopyJob::AddFile**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-addfile?branch=master) and [**IBackgroundCopyJob::AddFileSet**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-addfileset?branch=master) methods return BG\_E\_TOO\_MANY\_FILES if you try to add more than one file to an upload job. If you need to upload more than one file, consider using a CAB or ZIP file.

For download jobs, BITS limits the number of files that a user can add to a job to 200 files and the number of ranges for a file to 500 ranges. These limits do not apply to administrators or services. To change these default limits, see [Group Policies](group-policies.md).

**Prior to Windows Vista:** There are no limits to the number of files or ranges that you can add to a job.

The owner of the job or a user with administrator privileges can add files to the job anytime prior to calling the [**IBackgroundCopyJob::Complete**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-complete?branch=master) method or the [**IBackgroundCopyJob::Cancel**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-cancel?branch=master) method.

If you need to change the remote name of the file after you add the file to the job, you can call the [**IBackgroundCopyJob3::ReplaceRemotePrefix**](/windows/win32/Bits2_0/nf-bits2_0-ibackgroundcopyjob3-replaceremoteprefix?branch=master) method or the [**IBackgroundCopyFile2::SetRemoteName**](/windows/win32/Bits2_0/nf-bits2_0-ibackgroundcopyfile2-setremotename?branch=master) method. Use the **ReplaceRemotePrefix** method to change the server portion of the remote name when the server is unavailable or to let roaming users connect to the closest server. Use the **SetRemoteName** method to change the protocol used to transfer the file or to change the file name or path.

BITS creates a temporary file in the destination directory and uses the temporary file for the file transfer. To get the temporary file name, call the [**IBackgroundCopyFile3::GetTemporaryName**](/windows/win32/Bits3_0/nf-bits3_0-ibackgroundcopyfile3-gettemporaryname?branch=master) method. BITS changes the temporary file name to the destination file name when you call the [**Complete**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-complete?branch=master) method. BITS does not specify a security descriptor when it [**creates**](https://msdn.microsoft.com/library/windows/desktop/aa363858) the temporary file (the file inherits the ACL information from the destination directory). If the transferred data is sensitive, the application should specify an appropriate ACL on the destination directory to prevent unauthorized access.

To maintain the owner and ACL information with the transferred file, call the [**IBackgroundCopyJob3::SetFileACLFlags**](/windows/win32/Bits2_0/nf-bits2_0-ibackgroundcopyjob3-setfileaclflags?branch=master) method.

The owner of the job (the user who created the job or the administrator who [took ownership](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-takeownership?branch=master) of the job) must have permissions to the file on the server as well as the client. For example, to download a file the user must have read permissions on the server and write permissions to the local directory on the client.

The following example shows how to add a single file to the job. The example assumes the [**IBackgroundCopyJob**](/windows/win32/Bits/nn-bits-ibackgroundcopyjob?branch=master) interface pointer, pJob, is valid.


```C++
HRESULT hr;
IBackgroundCopyJob* pJob;

//Replace parameters with variables that contain valid paths.
hr = pJob->AddFile(L"http://ServerName/Path/File.Ext", L"d:\\Path\\File.Ext");
if (SUCCEEDED(hr))
{
  //Do something.
}
```



The following example shows how to add multiple files to the job. The example assumes the [**IBackgroundCopyJob**](/windows/win32/Bits/nn-bits-ibackgroundcopyjob?branch=master) interface pointer, pJob, is valid and the local and remote names come from a list in the user interface.


```C++
HRESULT hr;
IBackgroundCopyJob* pJob;
BG_FILE_INFO* paFiles = NULL;
ULONG idx = 0;
ULONG nCount = 0;            //Set to the number of files to add to the job.
LPWSTR pszLocalName = NULL;  //Comes from the list in the user interface.
LPWSTR pszRemoteName = NULL; //Comes from the list in the user interface.

//Set nCount to the number of files to transfer.

//Allocate a block of memory to contain the array of BG_FILE_INFO structures.
//The BG_FILE_INFO structure contains the local and remote names of the 
//file being transferred.
paFiles = (BG_FILE_INFO*) malloc(sizeof(BG_FILE_INFO) * nCount);
if (NULL == paFiles)
{
  //Handle error
}
else
{
  //Add local and remote file name pairs to the memory block. 
  for (idx=0; idx<nCount; idx++)
  {
    //Set pszLocalName to point to an LPWSTR that contains the local name or
    //allocate memory for pszLocalName and copy the local name to pszLocalName.
    (paFiles+idx)->LocalName = pszLocalName;

    //Set pszRemoteName to point to an LPWSTR that contains the remote name or
    //allocate memory for pszRemoteName and copy the remote name to pszRemoteName.
    (paFiles+idx)->RemoteName = pszRemoteName;
  }

  //Add the files to the job.
  hr = pJob->AddFileSet(nCount, paFiles);
  if (SUCCEEDED(hr))
  {
     //Do Something.
  }

  //Free the memory block for the array of BG_FILE_INFO structures. If you allocated
  //memory for the local and remote file names, loop through the array and free the
  //memory for the file names before you free paFiles.
  free(paFiles);
}
```



 

 




