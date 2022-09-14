---
title: Asynchronous Model
description: Most operations in Windows Web Services API can be performed synchronously or asynchronously.
ms.assetid: d0b3f154-2219-4085-a652-e9aeb126598c
keywords:
- Asynchronous Model Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Model

Most operations in Windows Web Services API can be performed synchronously or asynchronously. To call a function synchronously, pass a null value for the [**WS\_ASYNC\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_async_context) structure. To specify that a function may be performed asynchronously, pass a non-null **WS\_ASYNC\_CONTEXT** to the function.

When called asynchronously, a function can nevertheless complete synchronously or asynchronously. If the function completes synchronously, it returns a value that indicates the final success or error, and this value is always something other than **WS\_S\_ASYNC** (See [Windows Web Services Return Values](windows-web-services-return-values.md)). A return value of **WS\_S\_ASYNC**, however, indicates that the function will complete asynchronously. When the function completes asynchronously, a callback is invoked to signal completion of the operation. This callback indicates the final success or error value. The callback is not called if the operation completes synchronously.

To create an asynchronous context, initialize the **callback** and **callbackState** fields of the [**WS\_ASYNC\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_async_context) structure. The **callbackState** field is used to specify a pointer to user-defined data which is passed to the [**WS\_ASYNC\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_async_callback) function.

The following example shows calling a function asynchronously by passing a pointer to a [**WS\_ASYNC\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_async_context) structure that contains the callback and a pointer to the state data.

``` syntax
HRESULT ExampleAsyncFunction(WS_ASYNC_CONTEXT* asyncContext);
void ExampleAsyncFunction()
{
    // Set up the WS_ASYNC_CONTEXT structure.
    MyState* myState = ...;  \\ Declare a pointer to user-defined data.
    WS_ASYNC_CONTEXT asyncContext;
    asyncContext.callback = MyCallback;  \\ Set the callback.
    asyncContext.callbackState = myState; \\ Set the pointer to the user-defined data.

    // Start the asynchronous operation
    HRESULT hr = SomeFunction(&asyncContext);

    if (hr == WS_S_ASYNC)
    {
        // The operation is completing asynchronously.  The callback is called 
        // when the operation is complete.
    }
    else
    {
        // The operation completed synchronously.  The callback is not called.
    }
}
void CALLBACK MyCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState)
{
    MyState* myState = (MyState*)callbackState;

    // The operation completed asynchronously.
}
```

The [**WS\_ASYNC\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_async_context) structure is used by the asynchronous function only for the duration of the function call (not for the duration of the asynchronous operation), so you can safely declare it on the stack.

If any other parameters, besides the [**WS\_ASYNC\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_async_context) structure, are passed to an asynchronous function as pointers and the function completes asynchronously, it is the responsibility of the caller to keep the values pointed to by these parameters alive (not freed) until the asynchronous callback is invoked.

There are limitations on what operations a callback may perform. For more information on possible operations , see the [**WS\_CALLBACK\_MODEL**](/windows/desktop/api/WebServices/ne-webservices-ws_callback_model).

When you implement an asynchronous function, do not invoke the callback on the same thread that called the asynchronous function before the asynchronous function has returned to the caller, as this disrupts the asynchronous model.

When implementing a function that needs to execute a series of asynchronous operations, consider using the [**WsAsyncExecute**](/windows/desktop/api/WebServices/nf-webservices-wsasyncexecute) helper function.

The [Asynchronous Function Example](asyncmodelexample.md) shows how to implement and consume functions that follow the asynchronous model.

Starting an asynchronous IO operation consumes system resources. If enough IO operations are started, the system can become unresponsive. To prevent this, an application needs to limit the number of asynchronous operations that it starts.

The asynchronous model uses the following API elements.

| Callback                                         | Description                                                                                                                           |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_ASYNC\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_async_callback) | The callback function parameter used with the asynchronous model.                                                                     |
| [**WS\_ASYNC\_FUNCTION**](/windows/desktop/api/WebServices/nc-webservices-ws_async_function) | Used with the [**WsAsyncExecute**](/windows/desktop/api/WebServices/nf-webservices-wsasyncexecute) to specify the next function to invoke in a series of asynchronous operations. |



 



| Enumeration                                      | Description                                                                                                       |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [**WS\_CALLBACK\_MODEL**](/windows/desktop/api/WebServices/ne-webservices-ws_callback_model) | Specifies the threading behavior of a callback (for example, a [**WS\_ASYNC\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_async_callback)). |



 



| Function                                 | Description                                                                                                                                                                    |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WsAsyncExecute**](/windows/desktop/api/WebServices/nf-webservices-wsasyncexecute) | Invokes a user-defined callback which can initiate an asynchronous operation and indicate a function that should be called when the asynchronous operation has been completed. |



 



| Structure                                          | Description                                                                                                                           |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**WS\_ASYNC\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_async_context)     | Specifies the asynchronous callback and a pointer to user-defined data, which will be passed to the asynchronous callback.            |
| [**WS\_ASYNC\_OPERATION**](/windows/desktop/api/WebServices/ns-webservices-ws_async_operation) | Used with the [**WsAsyncExecute**](/windows/desktop/api/WebServices/nf-webservices-wsasyncexecute) to specify the next function to invoke in a series of asynchronous operations. |
| [**WS\_ASYNC\_STATE**](/windows/desktop/api/WebServices/ns-webservices-ws_async_state)         | Used by [**WsAsyncExecute**](/windows/desktop/api/WebServices/nf-webservices-wsasyncexecute) to manage the state of an asynchronous operation.                                    |



 

## Related topics

<dl> <dt>

[Asynchronous Function Example](asyncmodelexample.md)
</dt> <dt>

[**WS\_ASYNC\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_async_callback)
</dt> <dt>

[**WS\_ASYNC\_CONTEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_async_context)
</dt> <dt>

[**WS\_CALLBACK\_MODEL**](/windows/desktop/api/WebServices/ne-webservices-ws_callback_model)
</dt> <dt>

[**WsAsyncExecute**](/windows/desktop/api/WebServices/nf-webservices-wsasyncexecute)
</dt> </dl>

 

 




