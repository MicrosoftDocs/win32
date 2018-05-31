---
title: Getting the Query Results for Display
description: Getting the Query Results for Display
ms.assetid: a3729d4d-acf4-4071-9727-4f51dcca6078
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting the Query Results for Display

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following code segments from the **IssueQuery** function of the sample get the results of the query for subsequent display. The function first declares an [**IAccessor**](a39058b6-ecfa-418b-80a3-66eea4a7bf89) interface and uses the [**QueryInterface**](_com_iunknown_queryinterface) method of the [**IRowset**](b14147c4-8b03-49c6-ab5d-00186643a6b4) interface to get a pointer to an **IAccessor** interface for the query's rowset.


```C++
...
    XInterface<IAccessor> xIAccessor;
    hr = xIRowset->QueryInterface( IID_IAccessor,
                                   xIAccessor.GetQIPointer() );
...
```



After determining the number of columns in the result and binding each column with the appropriate buffer information, the function declares a handle to an accessor and uses the [**CreateAccessor**](b08e24a3-e732-431d-8972-ec37961ca5d2) method of the [**IAccessor**](a39058b6-ecfa-418b-80a3-66eea4a7bf89) interface to create the accessor from the bindings.


```C++
...
    HACCESSOR hAccessor;
    hr = xIAccessor->CreateAccessor( DBACCESSOR_ROWDATA, // rowdata accessor
                                     cColumns,           // # of columns
                                     xBindings.Get(),    // columns
                                     0,                  // ignored
                                     &amp;hAccessor,         // result
                                     0 );                // no status
...
```



The function finally uses the [**GetData**](896745d0-52c4-4b27-a929-408787cca005) method of the [**IRowset**](b14147c4-8b03-49c6-ab5d-00186643a6b4) interface to get the data for subsequent display.


```C++
...
            for ( DBCOUNTITEM iRow = 0; iRow < cRowsReturned; iRow++ )
            {
                HRESULT hr2 = xIRowset->GetData( aHRow[iRow],   // hrow being accessed
                                                 hAccessor,     // accessor to use
                                                 xData.Get() ); // resulting data
...
            }
...
```



 

 




