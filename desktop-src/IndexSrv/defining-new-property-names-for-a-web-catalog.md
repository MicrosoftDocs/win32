---
Description: Defining New Property Names for a Web Catalog
ms.assetid: 7482fbf4-7c45-46b2-9efe-db07eb07249a
title: Defining New Property Names for a Web Catalog
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Defining New Property Names for a Web Catalog

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

To define properties that are not in the previous list, in the [Default Property Names for a Web Catalog](default-property-names-for-a-web-catalog.md) section, you must list them in a \[Names\] section in the .idq file. To use these properties in a restriction, sort specification, or as a retrieved column, you must define them in the .idq file, using the following format:

\[Names\]

\#Properties that are not in the standard list

*Propertyname* ( *Datatype* ) = *GUID* \["*Name*" \| *propid*\]

In the syntax, "*Name*" is the property name ("Sales" in the following example), and *propid* is the property ID in hexadecimal. Note that you need to surround the friendly name with quotation marks, but that the property ID does not take quotation marks.

For example, suppose you want to define an HTML meta tag as a property name that somebody can search for. The property you want to define is **Sales**.

**To define the Sales property**

-   In the .idq file, under the \[Names\] section, add the following line.

    MetaDescription(DBTYPE\_WSTR) = d1b5d3f0-c0b3-11cf-9a92-00a0c908dbf1 "Sales"

    The GUID number comes from the *MetaTagClsid* parameter in the registry, at the following location:

    ```
    HKEY_LOCAL_MACHINE\SYSTEM
       CurrentControlSet
          Control
             HtmlFilter
                MetaTagClsid
    ```

> [!Note]  
> Starting with Windows 2000, the GUID for a property is hard-coded and is not read from the *MetaTagClsid* parameter in the registry.

 

-   Then, in the HTML files where you want the tag to appear, define the meta description.

    For example, suppose that you want to search for all files that give sales projections for the future:

    In File1.htm:

    &lt;META NAME="Sales" CONTENT="Projections for 1999"&gt;

    In File2.htm:

    &lt;META NAME="Sales" CONTENT="Projections for 2000"&gt;

    In File3.htm:

    &lt;META NAME="Sales" CONTENT="Sales in 1998"&gt;

> [!Note]  
> Be sure to add your META NAME tags between the &lt;head&gt; and &lt;/head&gt; HTML tags at the beginning of the file.

 

You can now search for all files that show sales projections. Send the following query:

@metadescription projections

This query returns all the files with the word *projections* in the **CONTENT** field of the meta tag. In this example, File1.htm and File2.htm are returned.

But suppose you want to search for sales by year, for example a list of sales in 1998. Send the following query:

@metadescription 1998

File3.htm is returned.

For more information about defining columns and properties, see the following topics:

-   DefaultColumnFile
-   DefineColumn
-   SET PROPERTYNAME

 

 



