---
description: Making an asynchronous call to a WMI method or a provider method allows a script to continue executing while objects return to an SWbemSink object, and are handled by methods such as SWbemSink.OnObjectReady.
ms.assetid: 61f401d9-c874-472d-8dd3-7cf9d7f20a12
ms.tgt_platform: multiple
title: Making an Asynchronous Call with VBScript
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Making an Asynchronous Call with VBScript

Making an asynchronous call to a [*WMI method*](gloss-w.md) or a [*provider method*](gloss-p.md) allows a script to continue executing while objects return to an [**SWbemSink**](swbemsink.md) object, and are handled by methods such as [**SWbemSink.OnObjectReady**](swbemsink-onobjectready.md). However, asynchronous calls are not recommended because the data may not be returned at the same level of security as the call is made.

When using asynchronous sink calls like [**SWbemSink.OnObjectReady**](swbemsink-onobjectready.md) to get returned data, you can set the following registry value.

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM**\\**UnsecAppAccessControlDefault**

Setting this registry value ensures authentication of the data objects returned to the sink. If **UnsecAppAccessControlDefault** is set to one (1), then WMI performs access checking of the data return. Access checks verify that the data comes from the correct source. For more information, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

Asynchronous methods with names that end in "Async\_" always return immediately after being called so that a program can continue executing. For example, [**SWbemServices.ExecQuery**](swbemservices-execquery.md) is synchronous and blocks execution until all of the objects are returned. The [**SWbemServices.ExecQueryAsync**](swbemservices-execqueryasync.md) method is the nonblocking asynchronous version. A more secure way to make the call to **SWbemServices.ExecQuery** nonblocking is by making the call [*semisynchronously*](gloss-s.md). For more information, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md) and [Making a Semisynchronous Call with VBScript](making-a-semisynchronous-call-with-vbscript.md).

The *iFlags* parameter for asynchronous calls always defaults to zero (0). Asynchronous methods do not supply an [**SWbemObjectSet**](swbemobjectset.md) collection to the sink subroutine. Instead, the [**SWbemSink.OnObjectReady**](swbemsink-onobjectready.md) event subroutine in your script or application receives each object as it is provided.

When the original asynchronous call is complete, it calls the [**SWbemSink.OnCompleted**](swbemsink-oncompleted.md) event of the object sink, and executes the code you place there to process the result of the call.

> [!Note]  
> An Active Server Page (ASP) as a script host does not support an asynchronous call.

 

The following procedure describes how to make an asynchronous call by using VBScript.

**To make an asynchronous call using VBScript**

1.  Connect to WMI and get an [**SWbemServices**](swbemservices.md) object.

    ```VB
    Set Service = GetObject("Winmgmts:")
    ```

    

2.  Create the object sink using either [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) or (for Windows Script Host 2.0 only) the OBJECT tag with an events attribute set to **TRUE**.

    ```VB
    Set sink = WScript.CreateObject("WbemScripting.SWbemSink","SINK_")
    ```

    

    -or-

    ```VB
    <OBJECT progid="WbemScripting.SWbemSink" ID="SINK" events="true"/>
    ```

    

3.  Create a subroutine for each event an asynchronous event can trigger. These events are defined as methods on [**SWbemObject**](swbemobject.md). For example, WMI makes a callback to [**SWbemSink.OnObjectReady**](swbemsink-onobjectready.md) as each instance returns.

    When you create the subroutine, place code in the subroutine to handle each event when it is received.

    ```VB
    Sub SINK_OnCompleted(
          iHResult, 
          objErrorObject, 
          objAsyncContext
          )
        WScript.Echo "Asynchronous operation is done."
    End Sub

    Sub SINK_OnObjectReady(objObject, objAsyncContext)
        WScript.Echo (objObject.Name)
    End Sub
    ```

    

    Examine the *iHresult* parameter returned by the [**OnCompleted**](swbemsink-oncompleted.md) event to determine whether or not the asynchronous call is successful, or if an error occurred. If successful, the value passed in the *iHresult* parameter is equal to zero (0). Any other value may indicate an error, and you should check the values in the error object that is returned in the *objErrorObject* parameter.

4.  Make an asynchronous call and pass the name of your sink in the *objWbemSink* parameter.

    ```VB
    Service.InstancesOfAsync sink, "Win32_process"
    ```

    

5.  Make a call that prevents the script from ending before all of the events are received. If your script can run with a screen interface, a simple way to do this is to use a Windows Script Host (WSH) `Echo` command, which is shown in the following example.

    ```VB
    WScript.Echo "Waiting for instances."
    ```

    

    When you execute this script you may see the first instance return before the **Waiting for instances** message or you may see it after. This is the nature of asynchronous processing. If you close the **Waiting for instances** message box too soon, you may not see all of the instances.

6.  If you have results from several different asynchronous calls returning to the same sink, store any necessary distinguishing data in the *objWbemAsyncContext* context parameter.

7.  When finished with the sink, cancel your asynchronous call with the [**Cancel**](swbemsink-cancel.md) method.

    ```VB
    objwbemsink.Cancel()
    ```

    

    The [**Cancel**](swbemsink-cancel.md) method instructs WSH to cancel all of the asynchronous calls associated with a given sink object. Thus, you may want to use separate sinks for asynchronous operations that must be independent.

8.  Release the sink object by assigning the sink object to `Nothing`.

    ```VB
    set objwbemsink= Nothing
    ```

    

The following code example shows an asynchronous query for all the instances of [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) on the local machine. For a semisynchronous version of the same method, see [Calling a Method](calling-a-method.md).


```VB
' Create an object sink
set oSink = WScript.CreateObject("wbemscripting.swbemsink","sink_")
' Connect to WMI and the cimv2 namespace, and obtain
' an SWbemServices object
set oSvc = GetObject("winmgmts:root\cimv2")

bdone = false
' Query for all Win32_Process objects
osvc.ExecQueryAsync oSink, "SELECT Name FROM Win32_Process"
' Wait until all instances are returned. 
' The bdone flag prevents the script from exiting until
' the sink.OnCompleted subroutine is executed when
' all the objects are returned.
while not bdone    
    wscript.sleep 1000
wend

' The sink subroutine to handle the OnObjectReady 
' event. This is called as each object returns.
sub sink_OnObjectReady(oInst, octx)
    WScript.Echo "Got Instance: " & oInst.Name
end sub
' The sink subroutine to handle the OnCompleted event.
' This is called when all the objects are returned. 
' The oErr parameter obtains an SWbemLastError object,
' if available from the provider.
sub sink_OnCompleted(HResult, oErr, oCtx)
    WScript.Echo "ExecQueryAsync completed"
    bdone = true
end sub
```



## Related topics

<dl> <dt>

[Calling a Method](calling-a-method.md)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> </dl>

 

 
