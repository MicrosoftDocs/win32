---
title: The IFiltTst.ini File
description: The IFiltTst.ini File
ms.assetid: '5d0f3744-d824-4141-bcc5-ea2300df15cb'
---

# The IFiltTst.ini File

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

An [**IFilter**](ifilter.md) interface is initialized by calling the [**IFilter::Init**](ifilter-init.md) method. The **Init** method takes four parameters, *grfFlags*, *cAttributes*, *aAttributes* and *pdwFlags*. The user of the ifilttst.exe program of the IFilter Test Suite can specify the values for these parameters in a file called ifilttst.ini. The next section, [Sample ifilttst.ini File](sample-ifilttst-ini-file.md), shows a sample file.

The file is organized in sections, with the section name enclosed in square brackets. In the example, the sections are named Test1, Test2, and so forth. All section names must be unique. The test reads the values from the first section and initializes the filter with those values. Then it runs all its tests using this filter configuration. It then releases the filter and reinitializes it, using parameters from the next section. It repeats the process until all configurations are tested.

The following table gives the parameters for the [**IFilter::Init**](ifilter-init.md) method. Each section contains a complete description of the parameters.



| Entry         | Value of entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Flags*       | The names of the [IFILTER\_INIT](ifilter-init.md) flags that are to be joined by the **OR** operator to form the *grfFlags* parameter. They must be all uppercase, and they must all be on the same line.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *cAttributes* | A decimal integer representing the value of the *cAttributes* parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| *aAttributes* | The name of this entry must start with "aAttributes" and must be different from the other *aAttributes* entries within the section. Legal names for the *aAttributes* entry are: aAttributes, aAttributes1, aAttributes2, and so forth. The first token must be a globally unique identifier (GUID). The GUID must be formatted exactly as shown in the section \[Test3\]. The second token can be either a property identifier (*propid*), consisting of a number in hexadecimal notation, or a pointer to a wide character string (*lpwstr*). A lpwstr can be specified by enclosing the string in double quotes (see section \[Test6\]). |



 

If the *Flags* and *cAttributes* entries are not specified, they default to zero. If you set *cAttributes* equal to 2, you generally specify two *aAttributes* names. In section \[Test5\], *cAttributes* is 1, but no *aAttributes* have been specified. The test then calls the [**IFilter::Init**](ifilter-init.md) method with *cAttributes* equal to 1, and *aAttributes* equal to **NULL**. This is a useful test case, since it is likely to cause an access violation in the **IFilter::Init** method.

There is no entry for the *pdwFlags* parameter since this parameter is used solely to return a value to the caller; it does not need to have any special value prior to the call to the [**IFilter::Init**](ifilter-init.md) method.

If ifilttst.exe cannot find a file named ifilttst.ini in the working directory, it uses a default configuration to initialize the filter object. Below is the default configuration.


```
[default]
grfFlags = IFILTER_INIT_APPLY_INDEX_ATTRIBUTES 
cAttributes = 0
```



 

 




