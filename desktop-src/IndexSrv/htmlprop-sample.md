---
title: HtmlProp Sample
description: HtmlProp Sample
ms.assetid: '2f7e6399-eb92-472c-8219-8dffc4b8849a'
---

# HtmlProp Sample

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The HtmlProp sample is an example [**IFilter**](ifilter.md) implementation that specializes the Indexing Service [HTML filter](html-filter.md) to extract value-type properties. It converts HTML meta properties to data types other than strings as specified by a configuration file.

Source: mssdk\\samples\\winbase\\indexing\\htmlprop\\

**To build the sample**

1.  Set the Lib environment variable to "D:\\mssdk\\Lib;%Lib%" and the Include environment variable to "D:\\mssdk\\Include;%Include%", where D: is the drive on which you installed the Platform SDK.
2.  Correctly set the CPU environment variable, for example to "i386".
3.  Open a command window and change directory to the source path of the sample.
4.  Build the filter DLL by entering, at the command-line prompt, "nmake".

**To register the sample**

1.  Copy the filter DLL file HtmlProp.dll to your %windir%\\System32 directory.
2.  Self-register the filter by entering, at the command-line prompt: "regsvr32.exe %windir%\\System32\\HtmlProp.dll".
3.  Enable automatic registration of the filter by adding it to the MULTI\_SZ value of the [DLLsToRegister](dllstoregister.md) entry in the registry under the following key.
    ```
    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ContentIndex.
    ```

    

**To filter files using the sample**

1.  Update htmlprop.ini to specify data types for the HTML meta properties you have defined in your HTML files. Update your HTML files to contain properties that match the definitions. For examples, refer to the sample files htmlprop.ini, dog1,htm, dog2.htm, and dog3.htm.
2.  Copy the file htmlprop.ini to your %windir%\\System32 directory.
3.  Copy the properties you defined in htmlprop.ini to your .idq file and/or update your .asp script to define these properties.
4.  Restart the cisvc service. If the files don't need to be filtered, touch files containing all of the meta properties added to htmlprop.ini and wait for them to be filtered.
5.  Using the Indexing Service MMC snap-in, update the property cache to contain the properties you have defined. Be sure to choose the equivalent data type for each property or queries won't work. For example, DBTYPE\_I4 is the same as VT\_I4.
6.  Force a full re-scan of all files and wait for the index to be updated.

> [!Note]  
> Do not commit properties when scans are in progress. Wait for scans to complete. Index Server 2.0 has a bug that will cause your index to become corrupt. The bug is fixed in Indexing Service 3.0.

 

> [!Note]  
> You need to repeat steps 5 and 6 when your index is corrupt. Index Server 2.0 doesn't retain the list of properties in the property cache when your index becomes corrupt. Indexing Service 3.0 remember the properties.

 

### To query using the sample

Issue queries using the properties and/or retrieve the values in their native types. The following are some sample queries using the sample files.

@breedWeight &gt; 10

@breedOrigin = Australia

@breedFirstBred = 1840

### Programming Notes

The HtmlProp filter loads the default HTML filter (nlhtml.dll) and passes most of the processing to that filter. If the htmlprop.ini configuration file specifies that certain HTML meta properties should be converted into non-string data types, HtmlProp takes the string value from the HTML filter and coerces it into the desired type.

This is useful because if htmlprop.dll is installed and properly configured, the following actions are possible:

-   You can query HTML meta property values using data types other than strings.
-   You can sort meta properties using native data types, rather than just strings.
-   You can retrieve properties in .htx/.asp scripts in their native types, rather than as strings.

HtmlProp supports the following data types:

DBTYPE\_UI1, DBTYPE\_I2, DBTYPE\_UI2, DBTYPE\_I4, DBTYPE\_UI4, DBTYPE\_I8, DBTYPE\_UI8, DBTYPE\_R4, DBTYPE\_R8, and VT\_FILETIME

By modifying htmlprop.cxx, additional data types can be supported, and additional date formats can be added. Currently, only the Indexing Service syntax is supported for date specifications.

VT\_FILETIME values can be in any time zone you like, but the .htx file parser in Indexing Service assume all times are Coordinated Universal Time (UTC) and are displayed as such.

 

 




