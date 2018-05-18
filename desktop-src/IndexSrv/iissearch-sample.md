---
title: IISSearch Sample
description: IISSearch Sample
ms.assetid: 'cd188676-ac93-4ba6-8fe7-e3de670d330c'
---

# IISSearch Sample

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The IISSearch sample is a set of HTML and ASP forms that demonstrates how to use IIS to query Indexing Service. The forms use Indexing Service Query Language queries and the [Query Helper](programming-apis.md#-idxs-query-helper-api) API, use SQL queries and the [ADO](programming-apis.md#-idxs-activex-data-objects-api) and Query Helper APIs, and use IDQ+HTX and the [ISAPI Extensions](programming-apis.md#-idxs-isapi-extensions-api) API.

Source: mssdk\\samples\\winbase\\indexing\\IISSearch\\

**To install the sample files**

1.  Open a command window and change the directory to the source path of the sample.
2.  Determine where your Inetpub directory resides.
    -   If it resides on %SystemDrive%, you can use the install.bat file without modifying it.
    -   If it resides on another drive, modify the dst environment variable in the install.bat file to define the location of your inetpub directory.
3.  At the command prompt, type "install".

> [!Note]  
> The sample files are copied to the directory specified by the dst environment variable, which specifies by default the directory %SystemDrive%\\Inetpub\\IISSamples\\ISSamples.

 

**To use using the sample forms**

1.  Start Internet Explorer.
2.  Type the URL "http://localhost/iissamples/issamples/default.htm".
3.  In the left frame, select the sample query to execute.

### Programming Notes

The sample files include the following.

<dl> <dt>

<span id="advquery.asp"></span><span id="ADVQUERY.ASP"></span>advquery.asp
</dt> <dd>

An advanced Active Server Pages (ASP) example written in VBScript and Microsoft JScript that illustrates server-side scripting to execute Indexing Service Query Language queries using the [Query Helper](programming-apis.md#-idxs-query-helper-api) API.

</dd> <dt>

<span id="advsqlq.asp"></span><span id="ADVSQLQ.ASP"></span>advsqlq.asp
</dt> <dd>

An advanced ASP example written in VBScript and JScript that illustrates server-side scripting to execute SQL queries using the [ADO](programming-apis.md#-idxs-activex-data-objects-api) and Query Helper APIs.

</dd> <dt>

<span id="default.htm"></span><span id="DEFAULT.HTM"></span>default.htm
</dt> <dd>

An HTML page that provides easy access to each sample.

</dd> <dt>

<span id="fastq.htm__fastq.idq__fastq.htx"></span><span id="FASTQ.HTM__FASTQ.IDQ__FASTQ.HTX"></span>fastq.htm, fastq.idq, fastq.htx
</dt> <dd>

An optimized IDQ+HTX example that uses the [ISAPI Extensions](programming-apis.md#-idxs-isapi-extensions-api) API.

</dd> <dt>

<span id="query.asp"></span><span id="QUERY.ASP"></span>query.asp
</dt> <dd>

A simple ASP example written in VBScript and JScript that illustrates server-side scripting to execute Indexing Service Query Language queries using the Query Helper API.

</dd> <dt>

<span id="query.htm__query.idq__query.htx"></span><span id="QUERY.HTM__QUERY.IDQ__QUERY.HTX"></span>query.htm, query.idq, query.htx
</dt> <dd>

A simple IDQ+HTX example that uses the ISAPI Extensions API.

</dd> <dt>

<span id="sqlqhit.asp__sqlqhit.htm"></span><span id="SQLQHIT.ASP__SQLQHIT.HTM"></span>sqlqhit.asp, sqlqhit.htm
</dt> <dd>

A simple ASP example written in VBScript that illustrates the execution of queries using the [OLE DB Provider](programming-apis.md#-idxs-ole-db-provider-api) for Indexing Service API.

</dd> </dl>

 

 




