---
title: Security Considerations
description: Security Considerations
ms.assetid: 'fd789539-02a8-4457-8552-81a665d87a38'
---

# Security Considerations

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Be careful when substituting parameters for the [CiTemplate](variables-in-forms-and-in-idq-files.md#-idxs-citemplate-var) parameter because you could unintentionally allow files in scripts directories with only Execute permission to be sent over the network. For example, if an .idq file contained the line

``` syntax
CiTemplate=%CiTemplate%
```

A client could send a Uniform Resource Locator (URL) that contained the following line in the query string:

``` syntax
CiTemplate=/scripts/mysecretfile.pl
```

With this string, an unauthorized user could read the contents of a confidential file.

It is better to switch among different .htx files by just using the base name of the file and adding the script directory and file name extension in the parameter substitution. The following file, Sample.idq, shows how to do this:

``` syntax
[Query]
CiRestriction=%q%
CiTemplate=/scripts/%t%.htx
CiSort=%s%
CiScope=/
```

The query can be executed with a URL like the following:

``` syntax
http://computername/scripts/sample.idq?q=ActiveX&t=form1
```

> [!Note]  
> A URL or a form-based query can send up to 4 kilobytes (KB) of data. If a query larger than 4 KB is sent, the behavior is unpredictable. The query size includes all variables sent from the browser to the .idq file.

 

 

 




