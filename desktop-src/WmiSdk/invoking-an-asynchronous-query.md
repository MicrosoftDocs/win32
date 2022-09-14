---
description: An asynchronous query, while somewhat more complex to write, is the preferred type of query when system or network performance will be affected by querying a large group of data.
ms.assetid: b382610a-dac9-4d31-b756-aa84d16f0234
ms.tgt_platform: multiple
title: Invoking an Asynchronous Query
ms.topic: article
ms.date: 05/31/2018
---

# Invoking an Asynchronous Query

An asynchronous query, while somewhat more complex to write, is the preferred type of query when system or network performance will be affected by querying a large group of data. In script, creating an [**SWbemSink**](swbemsink.md) object and subroutines to handle the events that the sink could receive are the only additional tasks beyond the basic query.

> [!Note]  
> Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

The following abbreviated script queries for all of the data files on the local machine. This query could take an excessive amount of time if it were executed for all of the machines on a network. An [**SWbemSink**](swbemsink.md) object is set up and the only event that is handled is the OnCompleted event.


```VB
Sub SINK_OnCompleted(iHResult, objErrorObject, objAsyncContext)
    WScript.Echo "Asynchronous operation is done."
End Sub

Set service = GetObject("winmgmts:")
Set sink = WScript.CreateObject("WbemScripting.SWbemSink","SINK_")
service.ExecQueryAsync sink, "SELECT * FROM Win32_DataFile"
WScript.Echo "Waiting for instances."
sink.Cancel()
set sink= Nothing
```



For detailed information about constructing asynchronous method calls in script, see [Calling a Method](calling-a-method.md).

In C++ applications, an asynchronous query spawns a separate process to receive query data. An asynchronous query is more complex than a synchronous query, as you must code a multithreaded application. However, an asynchronous query does not monopolize the main thread of your application.

The following procedure describes how to perform an asynchronous query in C++.

**To perform an asynchronous query in C++**

1.  Implement an **IWbemSink** object.

    An **IWbemSink** object receives information about an asynchronous operation.

2.  Describe your query in a call to [**IWbemServices::ExecQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execqueryasync).

    WMI immediately moves the process that queries the CIM to another thread and frees up the thread that executed the query for another task.

3.  Wait for WMI to call the [**IWbemObjectSink::Indicate**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate) method.

    When finished, WMI calls [**Indicate**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate) to signal your application that the query is complete. WMI also returns results of the query to the sink as a pointer to an [**IEnumWbemClassObject**](/windows/desktop/api/Wbemcli/nn-wbemcli-ienumwbemclassobject) interface pointer. As with a synchronous query, use the pointer to access the objects that make up the result of your query.

The following code example does not compile without an error because the class QuerySink has not been defined. For the definition of the QuerySink class, see [**IWbemObjectSink**](iwbemobjectsink.md). The code example also requires the following reference and \#include statements.


```C++
#include <iostream>
using namespace std;
#include <wbemidl.h>
```



The following code example shows how to make an asynchronous call to issue a query.


```C++
void ExecQuery(IWbemServices *pSvc)
{
    // Create a new sink object.
    QuerySink *pSink = new QuerySink;

    // Initialize the query and query language.
    BSTR strQuery = SysAllocString(L"SELECT * FROM ClassName");
    BSTR strQueryLang = SysAllocString(L"WQL");
    
    // Issue the query.
    HRESULT hRes = pSvc->ExecQueryAsync(strQueryLang, strQuery, 0,
        NULL, pSink);

    // Clean up.
    SysFreeString(strQuery);
    SysFreeString(strQueryLang);
    
    if (hRes)
    {
        printf("ExecQueryAsync failed with = 0x%X\n", hRes);
        return;
    }
    
    printf("Completed.\n");
}
```



For more information, see [Calling a Method](calling-a-method.md).

 

 



