---
description: WMI applications written in C++ can make asynchronous calls by using many of the methods of the IWbemServices COM interface.
ms.assetid: 5179969f-bc7d-4408-84ef-7b003950a59f
ms.tgt_platform: multiple
title: Making an Asynchronous Call with C++
ms.topic: article
ms.date: 05/31/2018
---

# Making an Asynchronous Call with C++

WMI applications written in C++ can make asynchronous calls by using many of the methods of the [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) COM interface. However, the recommended procedure for calling a [*WMI method*](gloss-w.md) or a [*provider method*](gloss-p.md) is by using semisynchronous calls because semisynchronous calls are more secure than asynchronous calls. For more information, see [Making a Semisynchronous Call with C++](making-a-semisynchronous-call-with-c--.md) and [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

The following procedure describes how to make an asynchronous call by using the sink in your process.

**To make an asynchronous call using C++**

1.  Implement the [**IWbemObjectSink**](iwbemobjectsink.md) interface.

    All applications that make asynchronous calls must implement [**IWbemObjectSink**](iwbemobjectsink.md). Temporary event consumers also implement **IWbemObjectSink** to receive notification of events.

2.  Log on to the target WMI namespace.

    Applications always have to call the COM function [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) during the initialization phase. If they do not do so before making an asynchronous call, WMI releases the application sink without completing the asynchronous call. For more information, see [Initializing COM for a WMI Application](initializing-com-for-a-wmi-application.md).

3.  Set the security for your sink.

    Asynchronous calls create a variety of security issues that you may have to deal with, for example, allowing WMI access to your application. For more information, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

4.  Make the asynchronous call.

    The method returns immediately with the **WBEM\_S\_NO\_ERROR** success code. The application can proceed with other tasks while waiting for the operation to complete. WMI reports back to the application by calling methods in the [**IWbemObjectSink**](iwbemobjectsink.md) implementation of your application.

5.  If necessary, check your implementation periodically for updates.

    Applications can receive notification of intermediate status by setting the *lFlags* parameter in the asynchronous call to **WBEM\_FLAG\_SEND\_STATUS**. WMI reports the status of your call by setting the *lFlags* parameter of [**IWbemObjectSink**](iwbemobjectsink.md) to **WBEM\_STATUS\_PROGRESS**.

6.  If necessary, you can cancel the call before WMI finishes processing by calling the [**IWbemServices::CancelCallAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-cancelasynccall) method.

    The [**CancelAsyncCall**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-cancelasynccall) method cancels asynchronous processing by immediately releasing the pointer to the [**IWbemObjectSink**](iwbemobjectsink.md) interface and guarantees that the pointer is released before **CancelAsyncCall** returns.

    If you are using a wrapper object implementing the **IUnsecured** interface to host [**IWbemObjectSink**](iwbemobjectsink.md), you may find some additional complications. Because the application must pass the same pointer to [**CancelAsyncCall**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-cancelasynccall) that was passed in the original asynchronous call, the application must hold on to the wrapper object until it becomes clear that cancellation is not required. For more information, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

7.  When finished, clean up pointers and shut down the application.

    WMI provides the final status call through the [**SetStatus**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemproviderinitsink-setstatus) method.

    > [!Note]  
    > After sending the final status update, WMI releases the object sink by calling the **Release** method for the class that implements the [**IWbemObjectSink**](iwbemobjectsink.md) interface. In the previous example, this is the **QuerySink::Release** method. If you want to have control over the lifetime of the sink object, you can implement the sink with an initial reference count of one (1).

     

    If a client application passes the same sink interface in two different overlapping asynchronous calls, WMI does not guarantee the order of the callback. A client application making overlapping asynchronous calls should either pass different sink objects or serialize the calls.

The following example requires the following reference and \#include statements.


```C++
#include <iostream>
using namespace std;
#pragma comment(lib, "wbemuuid.lib")
#include <wbemidl.h>
```



The following example describes how to make an asynchronous query using the [**ExecQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execqueryasync) method, but does not create security settings or release the [**IWbemObjectSink**](iwbemobjectsink.md) object. For more information, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).


```C++
// Set input parameters to ExecQueryAsync.
BSTR QueryLang = SysAllocString(L"WQL");
BSTR Query = SysAllocString(L"SELECT * FROM MyClass");

// Create IWbemObjectSink object and set pointer.
QuerySink *pSink = new QuerySink;

IWbemServices* pSvc = 0;

// Call ExecQueryAsync.
HRESULT hRes = pSvc->ExecQueryAsync(QueryLang, 
                                    Query, 
                                    0, 
                                    NULL, 
                                    pSink);

// Check for errors.
if (hRes)
{
    printf("ExecQueryAsync failed with = 0x%X\n", hRes);
    SysFreeString(QueryLang);
    SysFreeString(Query);
    delete pSink;    
    return ERROR;
}
```



> [!Note]  
> The code above does not compile without error because the **QuerySink** class has not been defined. For more information about **QuerySink**, see [**IWbemObjectSink**](iwbemobjectsink.md).

 

## Related topics

<dl> <dt>

[Calling a Method](calling-a-method.md)
</dt> </dl>

 

 
